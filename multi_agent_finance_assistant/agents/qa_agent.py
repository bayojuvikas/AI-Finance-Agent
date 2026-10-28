import json
import os
import re
import math
from collections import Counter

import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

CORPUS_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "qa_corpus.json")


def _tokenize(text: str):
    return re.findall(r"\w+", text.lower())


class QAAgent:
    def __init__(self, corpus_path=CORPUS_PATH):
        with open(corpus_path, "r", encoding="utf-8") as f:
            self.docs = json.load(f)

        self.texts = [d["content"] for d in self.docs]
        self.titles = [d["title"] for d in self.docs]
        self.categories = [d["category"] for d in self.docs]
        self.ids = [d["id"] for d in self.docs]

        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self._build_semantic_index()
        self._build_keyword_index()

    def _build_semantic_index(self):
        embeddings = self.model.encode(self.texts, convert_to_numpy=True)
        dim = embeddings.shape[1]
        self.semantic_index = faiss.IndexFlatL2(dim)
        self.semantic_index.add(embeddings)

    def _build_keyword_index(self):
        self.doc_tokens = [_tokenize(t) for t in self.texts]
        self.doc_freqs = Counter()
        for tokens in self.doc_tokens:
            self.doc_freqs.update(set(tokens))
        self.n_docs = len(self.docs)

    def _keyword_scores(self, query: str):
        q_tokens = _tokenize(query)
        if not q_tokens:
            return [0.0] * self.n_docs
        scores = []
        for i, tokens in enumerate(self.doc_tokens):
            doc_len = len(tokens) or 1
            tf = Counter(tokens)
            score = 0.0
            for q in q_tokens:
                if q in tf:
                    tf_score = tf[q] / doc_len
                    idf = math.log(self.n_docs / (self.doc_freqs.get(q, 1) + 1)) + 1.0
                    score += tf_score * idf
            scores.append(score)
        max_score = max(scores) if scores else 0.0
        if max_score > 0:
            scores = [s / max_score for s in scores]
        return scores

    def _semantic_scores(self, query: str, top_k: int = 5):
        q_vec = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.semantic_index.search(q_vec, min(top_k, self.n_docs))
        scores = [0.0] * self.n_docs
        if len(distances) > 0:
            max_dist = float(distances[0].max()) if distances[0].max() > 0 else 1.0
            for d, idx in zip(distances[0], indices[0]):
                scores[idx] = 1.0 - (float(d) / max_dist)
        return scores

    def search(self, query: str, top_k: int = 5, semantic_weight: float = 0.6,
               keyword_weight: float = 0.4):
        kw_scores = self._keyword_scores(query)
        sem_scores = self._semantic_scores(query, top_k=top_k)

        combined = []
        for i in range(self.n_docs):
            score = (semantic_weight * sem_scores[i]) + (keyword_weight * kw_scores[i])
            combined.append((i, score))

        combined.sort(key=lambda x: x[1], reverse=True)
        results = []
        for i, score in combined[:top_k]:
            results.append({
                "id": self.ids[i],
                "title": self.titles[i],
                "category": self.categories[i],
                "content": self.texts[i],
                "score": round(float(score), 4),
            })
        return results

    def answer(self, query: str, top_k: int = 3):
        results = self.search(query, top_k=top_k)
        if not results:
            return "I couldn't find any relevant information in the knowledge base for your question.", []

        context = "\n\n".join(
            f"[{r['title']} ({r['category']})] {r['content']}" for r in results
        )
        answer = (
            "Based on the available documents, here's what I found:\n\n"
            + context
        )
        return answer, results


qa_agent = QAAgent()


def query_knowledge_base(query: str, top_k: int = 3):
    answer, results = qa_agent.answer(query, top_k=top_k)
    return {"answer": answer, "sources": results}

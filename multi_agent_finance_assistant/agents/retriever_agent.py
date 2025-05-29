from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrieverAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documents = []

    def build_index(self, docs):
        self.documents = docs
        embeddings = self.model.encode(docs, convert_to_numpy=True)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def retrieve(self, query, top_k=3):
        if not self.index:
            raise ValueError("Index not built.")
        
        query_vec = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_vec, top_k)
        return [self.documents[i] for i in indices[0]]

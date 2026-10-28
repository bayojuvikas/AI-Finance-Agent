from fastapi import APIRouter, Query
from multi_agent_finance_assistant.agents.qa_agent import query_knowledge_base

router = APIRouter(prefix="/qa", tags=["QA Agent"])

@router.get("/")
def qa(query: str = Query(..., description="Question to ask against the knowledge base"), top_k: int = 3):
    return query_knowledge_base(query, top_k=top_k)

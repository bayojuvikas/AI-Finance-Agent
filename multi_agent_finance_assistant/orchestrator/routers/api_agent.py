from fastapi import APIRouter
from multi_agent_finance_assistant.agents.api_agent import get_stock_summary

router = APIRouter(prefix="/api", tags=["API Agent"])

@router.get("/stock_summary/{ticker}")
def stock_summary(ticker: str):
    return get_stock_summary(ticker)

from fastapi import APIRouter
from multi_agent_finance_assistant.agents.analysis_agent import analyze_portfolio, yesterday_portfolio, real_portfolio

router = APIRouter(prefix="/analyze", tags=["Analysis Agent"])

@router.get("/")
def analyze():
    return analyze_portfolio(yesterday_portfolio, real_portfolio)

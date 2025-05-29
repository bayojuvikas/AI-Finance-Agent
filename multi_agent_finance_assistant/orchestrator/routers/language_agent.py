from fastapi import APIRouter
from multi_agent_finance_assistant.agents.analysis_agent import analyze_portfolio, yesterday_portfolio, real_portfolio
from multi_agent_finance_assistant.agents.language_agent import generate_market_brief

router = APIRouter(prefix="/summarize", tags=["Language Agent"])

@router.get("/")
def summarize():
    summary = analyze_portfolio(yesterday_portfolio, real_portfolio)
    return {"brief": generate_market_brief(summary)}

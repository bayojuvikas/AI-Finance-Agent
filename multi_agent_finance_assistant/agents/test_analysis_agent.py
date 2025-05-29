from multi_agent_finance_assistant.agents.analysis_agent import analyze_portfolio, yesterday_portfolio, real_portfolio

summary = analyze_portfolio(yesterday_portfolio, real_portfolio)

print(f"Asia Tech Exposure: {summary['current_exposure']}% (was {summary['prev_exposure']}%, {summary['trend']})")
print("\nEarnings Summary:")
for e in summary["earnings_data"]:
    print(f"{e['ticker']}: ΔPrice = {e['price_change']} | Surprise = {e['earnings_surprise']}")

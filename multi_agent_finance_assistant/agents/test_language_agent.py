from analysis_agent import analyze_portfolio, yesterday_portfolio, real_portfolio
from language_agent import generate_market_brief

summary = analyze_portfolio(yesterday_portfolio, real_portfolio)
brief = generate_market_brief(summary)

print("\n🗣️ Market Brief:\n")
print(brief)

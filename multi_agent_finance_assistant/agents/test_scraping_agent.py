from multi_agent_finance_assistant.agents.scraping_agent import scrape_yahoo_rss_feed, fallback_scrape_marketwatch

print("== Primary: Yahoo Finance RSS ==")
rss_headlines = scrape_yahoo_rss_feed()
for h in rss_headlines:
    print(f"- {h['title']}")

print("\n== Fallback: MarketWatch (HTML scraping) ==")
fallbacks = fallback_scrape_marketwatch()
for h in fallbacks:
    print(f"- {h}")

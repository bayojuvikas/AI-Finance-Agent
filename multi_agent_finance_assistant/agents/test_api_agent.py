from multi_agent_finance_assistant.agents.api_agent import try_fallback_ticker

tickers_to_try = {
    "TSMC": ["TSM", "2330.TW"],
    "Samsung": ["005930.KS"]
}

for name, ticker_list in tickers_to_try.items():
    print(f"{name} ➤", try_fallback_ticker(ticker_list))

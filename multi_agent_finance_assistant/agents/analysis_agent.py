from multi_agent_finance_assistant.agents.api_agent import get_stock_summary
from typing import List, Dict

# Define your portfolio here (real tickers + region + sector)
real_portfolio = [
    {"ticker": "TSM", "region": "Asia", "sector": "Tech", "allocation": 12.0},
    {"ticker": "005930.KS", "region": "Asia", "sector": "Tech", "allocation": 10.0},
    {"ticker": "BIDU", "region": "Asia", "sector": "Tech", "allocation": 5.0},
    {"ticker": "AAPL", "region": "US", "sector": "Tech", "allocation": 20.0},  # control
]

# Simulate "yesterday" allocation
yesterday_portfolio = [
    {"ticker": "TSM", "region": "Asia", "sector": "Tech", "allocation": 10.0},
    {"ticker": "005930.KS", "region": "Asia", "sector": "Tech", "allocation": 8.0},
    {"ticker": "BIDU", "region": "Asia", "sector": "Tech", "allocation": 4.0},
    {"ticker": "AAPL", "region": "US", "sector": "Tech", "allocation": 20.0},
]

def calculate_exposure(holdings: List[Dict], region="Asia", sector="Tech") -> float:
    return sum(h["allocation"] for h in holdings if h["region"] == region and h["sector"] == sector)

def analyze_portfolio(yesterday: List[Dict], today: List[Dict]):
    prev_exposure = calculate_exposure(yesterday)
    current_exposure = calculate_exposure(today)
    delta = current_exposure - prev_exposure

    # Fetch market data
    earnings_data = []
    for holding in today:
        if holding["region"] == "Asia" and holding["sector"] == "Tech":
            result = get_stock_summary(holding["ticker"])
            earnings_data.append(result)

    return {
        "prev_exposure": round(prev_exposure, 2),
        "current_exposure": round(current_exposure, 2),
        "delta": round(delta, 2),
        "trend": "up" if delta > 0 else "down" if delta < 0 else "unchanged",
        "earnings_data": earnings_data
    }

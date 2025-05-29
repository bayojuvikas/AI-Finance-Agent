import yfinance as yf
from datetime import datetime, timedelta

def get_stock_summary(ticker: str):
    stock = yf.Ticker(ticker)
    
    # Try broader historical range
    end = datetime.today()
    start = end - timedelta(days=5)
    hist = stock.history(start=start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'))

    price_change = None
    if not hist.empty and len(hist["Close"]) > 1:
        price_change = round(hist["Close"].iloc[-1] - hist["Close"].iloc[0], 2)

    # Earnings surprise placeholder
    try:
        earnings = stock.earnings_dates
        latest = earnings.iloc[0]
        surprise = latest.get('Surprise(%)', None)
    except:
        surprise = None  # Can use mock value if needed

    return {
        "ticker": ticker,
        "price_change": price_change,
        "earnings_surprise": surprise
    }

# Optional fallback: try alt ticker (e.g., 2330.TW for TSMC)
def try_fallback_ticker(ticker_list):
    for t in ticker_list:
        try:
            result = get_stock_summary(t)
            if result["price_change"] is not None:
                return result
        except:
            continue
    return {"ticker": ticker_list[0], "price_change": None, "earnings_surprise": None}

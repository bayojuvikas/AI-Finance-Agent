import feedparser
from bs4 import BeautifulSoup
import requests

def scrape_yahoo_rss_feed():
    rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^IXIC&region=US&lang=en-US"
    feed = feedparser.parse(rss_url)

    headlines = []
    for entry in feed.entries[:10]:  # Limit to top 10
        headlines.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    return headlines


# Optional: fallback using HTML scraping if RSS fails
def fallback_scrape_marketwatch():
    url = "https://www.marketwatch.com/tools/earningscalendar"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for item in soup.select("div.element--article"):
        title = item.find("a")
        if title:
            headlines.append(title.get_text(strip=True))
    return headlines[:10]

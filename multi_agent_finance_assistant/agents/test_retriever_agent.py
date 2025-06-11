from retriever_agent import RetrieverAgent
from scraping_agent import scrape_yahoo_rss_feed

agent = RetrieverAgent()

# Use headlines as documents
docs = [item["title"] for item in scrape_yahoo_rss_feed()]
agent.build_index(docs)

query = "tech earnings surprise"
results = agent.retrieve(query)

print("🔍 Query:", query)
print("📄 Top Results:")
for r in results:
    print("-", r)

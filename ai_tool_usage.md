## 📓 `docs/ai_tool_usage.md`

```markdown
# 📑 AI Tool Usage Log

This document tracks where and how AI tools and open-source models were used during development.

---

## 🤖 ChatGPT / Copilot Assistance

| Component             | Usage                                                   |
|-----------------------|---------------------------------------------------------|
| api_agent.py          | Help with yfinance API for historical + earnings data   |
| analysis_agent.py     | Logic to compute exposure delta                         |
| language_agent.py     | Prompt tuning for narrative summaries                   |
| orchestrator setup    | FastAPI route structure and modular microservice design |
| streamlit_app/app.py  | Conditional logic for button + TTS integration          |
| requirements.txt      | Dependency generation                                   |

---

## 🧠 LLM Components

| Model / Library          | Use Case                                  |
|--------------------------|-------------------------------------------|
| LangChain                | Retriever interface for chunking + RAG    |
| OpenAI / GPT-4(optional) | Narrative summarization logic             |

---

## 📊 Finance APIs / Sources

| Source        | Description                                |
|---------------|--------------------------------------------|
| Yahoo Finance | Real-time & historical stock data          |
| RSS Feeds     | Company filings + earnings via scraping    |

---

## 🧰 Toolkits

| Toolkit         | Function               |
|-----------------|------------------------|
| BeautifulSoup   | HTML parsing of RSS    |
| feedparser      | Lightweight RSS loader |
| Whisper         | Voice to text          |
| pyttsx3         | Text to voice (TTS)    |

---

## 🚧 Limitations & Fallbacks

- Used fallback tickers like `2330.TW` if primary failed
- Manual triggers preferred over voice input for assignment timeline

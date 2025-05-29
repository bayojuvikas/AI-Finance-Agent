# 🧠📈 Multi-Agent Voice Finance Assistant – RagaAI Internship Project https://ai-finance-agent.streamlit.app/

This project is a modular, voice-enabled finance assistant built for the RagaAI internship assignment. It delivers daily market briefs via real-time data agents, document scrapers, LLM-based summarizers, and voice interfaces.

> Example Query (asked at 8:00 AM daily):
> _"What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?"_

---

## ✅ Features

- 🔍 Real-time stock data via Yahoo Finance
- 📰 Earnings parsing via RSS + BeautifulSoup
- 🧠 Portfolio exposure analysis (Asia tech allocation)
- 📚 RAG pipeline using LangChain-compatible structure
- 🗣️ Whisper STT + Pyttsx3 TTS for full voice interaction
- 🌐 Modular FastAPI microservices
- 🖥️ Streamlit frontend with deployment-ready UX

---

## 🧩 Architecture

🎤 (Voice)
↓ Whisper STT
↓
🧠 Orchestrator (FastAPI)
↓
📦 Agents:

-API Agent

-Scraper Agent

-Retriever Agent

-Analysis Agent

-Language Agent (LLM)
↓
🔊 Pyttsx3 TTS
↓
📺 Streamlit UI

---

## 🛠️ Setup Instructions

# Clone repo & activate virtual env
git clone https://github.com/<your-username>/finance-assistant

cd finance-assistant

python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI microservices
uvicorn orchestrator.main:app --reload

# In another terminal, run the Streamlit frontend
cd streamlit_app 

streamlit run app.py


# 🧪 Sample Output

Asia Tech Exposure: 27.0% (was 22.0%, up)
Earnings Summary:

TSMC: ΔPrice = -4.21 | Surprise = nan

Samsung: ΔPrice = 0.00 | Surprise = nan

Baidu: ΔPrice = -0.26 | Surprise = nan


📌 Credits & Tools
| **Tool**                 | **Purpose**                      |
| ------------------------ | -------------------------------- |
| FastAPI                  | Agent microservices              |
| yFinance                 | Stock data (TSMC, Samsung, etc.) |
| BeautifulSoup            | RSS feed parsing                 |
| Whisper                  | Speech-to-text                   |
| pyttsx3                  | Text-to-speech                   |
| Streamlit                | Web UI                           |
| LangChain                | LLM interfacing                  |
| GitHub Copilot / ChatGPT | Coding assistance                |


# Streamlit Application URL:
https://ai-finance-agent.streamlit.app/

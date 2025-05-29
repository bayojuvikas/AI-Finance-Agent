from multi_agent_finance_assistant.agents.voice_agent import record_voice, transcribe_audio, speak_text

audio, sr = record_voice()
text = transcribe_audio(audio, sr)

print(f"🧾 You said: {text}")
speak_text(f"You asked: {text}")
from voice_agent import record_voice, transcribe_audio, speak_text
from analysis_agent import analyze_portfolio, yesterday_portfolio, real_portfolio
from language_agent import generate_market_brief

audio, sr = record_voice()
query = transcribe_audio(audio, sr)

print(f"🧾 You said: {query}")

# Simple trigger — in real system you'd use RAG or intent match
if "asia tech" in query.lower():
    summary = analyze_portfolio(yesterday_portfolio, real_portfolio)
    reply = generate_market_brief(summary)
else:
    reply = "Sorry, I didn't understand. Try asking about Asia tech exposure."

print("🗣️ Responding...")
print(reply)
speak_text(reply)

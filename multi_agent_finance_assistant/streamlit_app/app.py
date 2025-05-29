import streamlit as st
import requests

st.set_page_config(page_title="Finance Assistant", layout="centered")
st.title("🧠📈 Multi-Agent Finance Assistant")
st.markdown("Ask: *What's our risk exposure in Asia tech stocks today, and highlight any earnings surprises?*")

# Trigger analysis
if st.button("🔍 Get Market Brief"):
    with st.spinner("Running analysis..."):
        response = requests.get("http://localhost:8000/summarize/")
        if response.status_code == 200:
            brief = response.json()["brief"]
            st.success("📊 Market Summary:")
            st.markdown(f"```\n{brief}\n```")

            # Speak result
            speak = st.checkbox("🔊 Speak out loud?")
            if speak:
                requests.post("http://localhost:8000/speak/", json={"text": brief})
        else:
            st.error("Failed to get summary from orchestrator.")

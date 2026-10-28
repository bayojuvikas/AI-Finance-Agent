import streamlit as st
import requests

st.set_page_config(page_title="Finance QA Assistant", layout="centered")
st.title("💬📈 Finance QA Assistant")
st.markdown("Ask questions about your portfolio (e.g., *What is my Asia tech allocation?*, *Did TSM beat earnings?*).")

query = st.text_input("Your question:", placeholder="e.g. What is my Asia tech allocation?")

if st.button("🔍 Ask", key="ask_btn"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching knowledge base..."):
            try:
                response = requests.get("http://localhost:8001/qa/", params={"query": query, "top_k": 3}, timeout=120)
                if response.status_code == 200:
                    data = response.json()
                    st.success("📊 Answer:")
                    st.markdown(data["answer"])
                    with st.expander("Sources"):
                        for s in data.get("sources", []):
                            st.markdown(f"- **{s['title']}** ({s['category']}) — score {s['score']}")
                else:
                    st.error(f"Failed to get answer from orchestrator (status {response.status_code}).")
            except Exception as e:
                st.error(f"Error connecting to orchestrator: {e}")

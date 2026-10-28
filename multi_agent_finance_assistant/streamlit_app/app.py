import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from agents.qa_agent import query_knowledge_base

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
                data = query_knowledge_base(query, top_k=3)
                st.success("📊 Answer:")
                st.markdown(data["answer"])
                with st.expander("Sources"):
                    for s in data.get("sources", []):
                        st.markdown(f"- **{s['title']}** ({s['category']}) — score {s['score']}")
            except Exception as e:
                st.error(f"Error searching knowledge base: {e}")

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RAG Support Assistant", page_icon="💬", layout="wide")

st.title("💬 RAG Customer Support Assistant")
st.caption("Local-first Knowledge Base Assistant (citations, strict context-only answers)")

with st.sidebar:
    st.header("Settings")
    st.write("Mode: **Local (Ollama)**")
    st.divider()

    st.subheader("API Status")
    try:
        r = requests.get(f"{API_URL}/health", timeout=2)
        if r.status_code == 200:
            st.success("API connected")
        else:
            st.warning("API reachable, unexpected response")
    except Exception:
        st.error("API not reachable. Start FastAPI on :8000")

    st.divider()
    st.subheader("Upload (coming next)")
    st.file_uploader("Upload KB document", type=["pdf", "txt", "md"], disabled=True)

st.divider()

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Chat")
    st.info("Chat endpoint will be wired in Milestone 2. First we build ingestion + vector store.")
with col2:
    st.subheader("Citations")
    st.info("Citations UI will appear here after retrieval is implemented.")

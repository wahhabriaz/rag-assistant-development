# RAG Customer Support Assistant (Local-First)

A professional, portfolio-ready Customer Support / Knowledge Base RAG assistant.

## Features (MVP)

- Upload knowledge base documents (PDF/TXT/MD)
- Ask questions and get answers with citations
- Strict "answer only from context" behavior
- “I don’t know” fallback when context is missing
- 100% local development (free): Chroma + sentence-transformers + Ollama

## Tech Stack

- UI: Streamlit
- API: FastAPI
- RAG: LangChain
- Vector DB: Chroma (local, persisted)
- Embeddings: sentence-transformers (all-MiniLM-L6-v2)
- Local LLM: Ollama (phi3:mini)
- Optional later: OpenAI (switchable mode)

## Setup (Local)

### 1) Create venv + install deps

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

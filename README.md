# 🧠 RAG Mastery — 21 Day Challenge

> Building production-grade Retrieval Augmented Generation systems from scratch in Python.

---

## What is This?

This repository documents my 21-day journey from zero to production-ready RAG engineer. Every day is a new concept, a new script, and a new commit — building toward a fully deployed document Q&A system by Day 21.

**Stack:** Python · LangChain · ChromaDB · sentence-transformers · Flask · Docker

---

## The Pipeline
```
Documents → Chunking → Embedding → Vector Store
                                        ↑
Query → Embed Query → Similarity Search → Top-K Chunks → Prompt → LLM → Answer
```

RAG solves two problems with standard LLMs:
- They have a knowledge cutoff — they don't know recent or private information
- They hallucinate — RAG grounds answers in real retrieved documents

---

## Progress

| Day | Topic | Status |
|-----|-------|--------|
| 01 | RAG Theory + Pipeline Mental Model | ✅ Done |
| 02 | Text Chunking with RecursiveCharacterTextSplitter | ✅ Done |
| 03 | Embeddings — Text to Vectors | 🔄 Up next |
| 04 | Vector Stores with ChromaDB | ⬜ Pending |
| 05 | Retrieval — Top-K Similarity Search | ⬜ Pending |
| 06 | Generation — LLM + Context | ⬜ Pending |
| 07 | Project 1: Basic RAG over a PDF | ⬜ Pending |
| 08 | Hybrid Search (Dense + Sparse) | ⬜ Pending |
| 09 | Re-ranking with Cross-Encoders | ⬜ Pending |
| 10 | Query Transformation (HyDE) | ⬜ Pending |
| 11 | Metadata Filtering | ⬜ Pending |
| 12 | Contextual Compression | ⬜ Pending |
| 13 | LangChain & LlamaIndex Frameworks | ⬜ Pending |
| 14 | Project 2: Advanced RAG + Flask API | ⬜ Pending |
| 15 | RAG Evaluation with RAGAS | ⬜ Pending |
| 16 | Agentic RAG with LangGraph | ⬜ Pending |
| 17 | Caching & Cost Optimization | ⬜ Pending |
| 18 | Multi-modal RAG | ⬜ Pending |
| 19 | Observability & Logging | ⬜ Pending |
| 20 | Docker + Cloud Deployment | ⬜ Pending |
| 21 | Capstone: Full Production RAG App | ⬜ Pending |

---

## Project Structure
```
rag-mastery/
├── day2_chunking.py       # Text splitting with RecursiveCharacterTextSplitter
├── sample.txt             # Test document used for chunking experiments
├── requirements.txt       # All dependencies
├── venv/                  # Virtual environment (not tracked)
└── README.md
```

---

## Setup
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/rag-mastery.git
cd rag-mastery

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Day 2 — Chunking

**Concept:** Before text can be embedded and stored, it must be split into small, focused pieces called chunks. Each chunk gets its own vector in the database, enabling precise retrieval.

**Key parameters:**
- `chunk_size=500` — max characters per chunk
- `chunk_overlap=50` — characters shared between consecutive chunks to prevent meaning loss at boundaries

**Run it:**
```bash
python day2_chunking.py
```

**Output:**
```
Text length: 2083
Number of chunks: 6
i is printed as 0 k is printed as Artificial Intelligence (AI) is the simulation...
i is printed as 1 k is printed as Machine Learning is a subset of AI...
...
```

**Why RecursiveCharacterTextSplitter?**
It splits at natural boundaries — paragraphs first, then sentences, then words — keeping every chunk semantically meaningful. A dumb character split would cut mid-word and destroy meaning.

---

## Author

**William** — Python Developer, Kenya
Junior Developer | Odoo | RAG | Flask
21 days. Zero to production RAG engineer.

---

## License

MIT
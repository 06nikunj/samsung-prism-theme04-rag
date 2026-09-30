# Streaming Live RAG Engine (Samsung PRISM Hackathon 2026–27)
## Theme 04: Real-Time Incremental Retrieval, Multi-Intent Decomposition, & State-Preserving Refinement

[![GitHub Tag](https://img.shields.io/badge/Release%20Tag-PRISM__GENAI__HACKATHON__Y2026-purple.svg)](https://github.com/06nikunj/samsung-prism-theme04-rag/releases/tag/PRISM_GENAI_HACKATHON_Y2026)
[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Executive Summary

Traditional Retrieval-Augmented Generation (RAG) operates in a static batch loop: the user finishes speaking or typing, submits a query, waits for vector database retrieval, and receives a synthesized response. In live voice applications or interactive support sessions, this turn-taking model causes multi-second pauses and breaks down when users express compound requests or introduce late-arriving constraints mid-sentence.

Our **Streaming Live RAG Engine** provides an event-driven, real-time pipeline built around four architectural pillars:
1. **Incremental Retrieval Controller:** Evaluates incoming transcript stream chunks to predict retrieval intent *before* the user finishes speaking.
2. **Multi-Intent Decomposer:** Deconstructs compound, multi-part user utterances into parallel sub-queries.
3. **Session State Refiner:** Mutates existing answer claims in-place when late constraints arrive without clearing conversation memory or restarting full corpus search.
4. **Strict Factual Grounding & Provenance:** Enforces explicit citation mapping (`[Doc_ID §Section]`) and emits explicit uncertainty indicators when corpus evidence is missing.

---

## 🏗️ System Architecture & Pipeline

```
Incoming Stream: [Chunk 0.0s] ──> [Chunk 0.8s] ──> [Chunk 1.6s] ──> [Utterance End 2.1s]
                                      │
                                      ▼
                      ┌──────────────────────────────┐
                      │   [1] Retrieval Controller   │
                      │   Intent Stability Check     │
                      │   Decision: Wait | Retrieve  │
                      └──────────────┬───────────────┘
                                     │ (Retrieve Triggered)
                                     ▼
                      ┌──────────────────────────────┐
                      │ [2] Multi-Intent Decomposer  │
                      │ Extract Parallel Sub-Queries │
                      └──────────────┬───────────────┘
                                     │
                                     ▼
                      ┌──────────────────────────────┐
                      │ [3] Corpus Retrieval & Fusion│
                      │ BM25 + Vector Hybrid Scoring │
                      └──────────────┬───────────────┘
                                     │
                                     ▼
                      ┌──────────────────────────────┐
                      │  [4] Session State Refiner   │
                      │  Version Lineage & Citation  │
                      └──────────────────────────────┘
```

---

## 🛠️ Core Engineering Components

### 1. Retrieval Controller (`IntentStabilityClassifier`)
Evaluates incoming transcript fragments in real-time to select one of three execution paths:
- **WAIT:** Suppresses premature retrieval when transcript chunks are semantically unstable or incomplete (< 4 tokens).
- **RETRIEVE:** Triggers speculative retrieval when key entities (capacity, dates, locations) or late-arriving constraints are identified.
- **SUPPRESS:** Bypasses corpus search entirely when the user requests formatting or presentation restructuring (e.g., *"Summarize your last answer in two bullets"*).

### 2. Multi-Intent Decomposer (`MultiIntentDecomposer`)
Parses compound utterances containing multiple distinct needs (e.g., venue capacity + cancellation policy + catering options) and extracts orthogonal sub-queries for parallel execution across the retrieval pool.

### 3. Hybrid Corpus Retrieval & Fusion (`HybridCorpusRetriever`)
Combines BM25 sparse keyword matching with dense vector cosine similarity using **Reciprocal Rank Fusion (RRF)**. Strictly isolated to the provided document corpus to prevent parametric hallucination.

### 4. Session State Refiner (`SessionStateRefiner`)
Maintains an ephemeral session memory graph with explicit answer version lineage ($v1 \rightarrow v2$). When a late constraint arrives (*"Actually, the trip was international"*), it updates affected claims without re-querying the baseline topic. If corpus evidence is missing, it injects an explicit uncertainty flag into the output payload.

---

## 📋 Evaluation Gates & Acceptance Criteria (G1–G6)

Our engine is evaluated against six automated benchmark gates:

| Gate | Evaluation Criterion | Target Threshold | Implementation & Validation |
| :---: | :--- | :---: | :--- |
| **G1** | **Reproducibility** | Pass / Fail | Single-command automated container execution. |
| **G2** | **Early Retrieval** | $\ge 80\%$ | Triggers retrieval speculative search prior to utterance completion. |
| **G3** | **Multi-Intent ID** | $\ge 70\%$ | Deconstructs compound queries into discrete sub-queries. |
| **G4** | **Factual Grounding** | $\ge 85\%$ | 100% citations backed by valid document section markers (`[Doc_XX §Y]`). |
| **G5** | **Session Refinement** | Verified | Preserves prior citation lineage during late-constraint updates. |
| **G6** | **Telemetry Coverage** | $100\%$ | Structured JSON log output capturing timestamps, triggers, & version history. |

---

## 🚀 Quickstart & Setup Guide

### Prerequisites
- Python 3.10, 3.11, or 3.12
- Git

### Installation
```bash
# 1. Clone repository
git clone https://github.com/06nikunj/samsung-prism-theme04-rag.git
cd samsung-prism-theme04-rag

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the Streaming Live RAG Engine
```bash
python streaming_live_rag.py
```

### Generating the Presentation Deck (`.pptx`)
```bash
python generate_theme04_ppt.py
```

---

## 🎥 Demo Video & Submission Resources

- **Demo Video (YouTube / Google Drive):** [Add your Google Drive / YouTube video link here]
- **PowerPoint Submission Deck:** [Samsung_PRISM_Theme04_Submission_Deck.md](./Samsung_PRISM_Theme04_Submission_Deck.md)
- **GitHub Release Tag:** `PRISM_GENAI_HACKATHON_Y2026`

---

## 📦 Project Directory Structure

```
.
├── README.md                              # Comprehensive project README & documentation
├── requirements.txt                       # Project dependencies
├── streaming_live_rag.py                  # Core Streaming Live RAG Engine implementation
├── generate_theme04_ppt.py                # PowerPoint presentation generator script
├── Samsung_PRISM_Theme04_Submission_Deck.md# Slide-by-slide markdown deck & speaker notes
└── .gitignore                             # Git ignore rules
```

---

## ⚖️ License & Acknowledgments

Organised by the **Language AI Team** and the **PRISM Team**, **Samsung R&D Institute India**. Built for the Samsung PRISM Generative AI Hackathon (3rd Edition 2026–27).

# AI Disclosure Statement

**Project Name:** Streaming Live RAG Engine  
**Theme ID:** Theme 04 (Streaming Live RAG)  
**Team Name:** Code_Blooded  
**College Name:** SRM Institute of Science and Technology (SRM)  
**Team Members:** Nikunj Purohit (Lead), Nishchay Bansal, Priyanshu Swami  
**Submission Tag:** `PRISM_GENAI_HACKATHON_Y2026`  

---

### AI & LLM Utilization Disclosure

1. **Core Algorithmic Architecture:**  
   The core event loop, real-time transcript streaming simulator, intent stability classification heuristics, sub-query decomposition, BM25 sparse index, vector cosine distance scoring, and Reciprocal Rank Fusion (RRF) re-ranking algorithms were designed and implemented directly in Python 3.11 using deterministic data structures and standard scientific libraries (`scikit-learn`, `rank-bm25`, `pydantic`).

2. **Generative Model Integration:**  
   Generative AI Large Language Models (LLMs) are used strictly as modular downstream synthesis engines to produce natural language responses from retrieved document chunks. 

3. **Grounding & Zero-Hallucination Enforcement:**  
   No precomputed, hardcoded, or parametric knowledge base answers are embedded within the application codebase. Every synthesized claim is strictly constrained to, and attributed against, retrieved document chunks with explicit provenance markers (`[Doc_ID §Section]`). If the retrieved corpus lacks sufficient evidence for a sub-intent, the system emits an explicit uncertainty indicator instead of fabricating facts.

4. **Code Assistance Disclosure:**  
   AI coding assistants were utilized for routine syntax formatting, boilerplate generation, and documentation drafting. All algorithmic logic, evaluation gate benchmarks, and system pipeline decisions were directed, audited, and validated by Team Code_Blooded.

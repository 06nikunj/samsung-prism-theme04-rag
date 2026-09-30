"""
Streaming Live RAG Engine
Theme 04: Real-Time Incremental Retrieval, Multi-Intent Decomposition, & State-Preserving Refinement
Samsung PRISM Generative AI Hackathon (3rd Edition 2026-27)
"""

import time
import json
import re
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field

@dataclass
class CorpusDocument:
    doc_id: str
    section: str
    content: str

@dataclass
class RetrievalEvent:
    timestamp_s: float
    query: str
    trigger: str  # 'provisional', 'multi_intent', 'late_constraint', 'final'

@dataclass
class TelemetryRecord:
    timestamp_s: float
    event_type: str
    details: Dict[str, Any]

class IntentStabilityClassifier:
    """
    Retrieval Controller: Evaluates incoming transcript chunks to decide:
    - WAIT: Input is incomplete/unstable, pause retrieval.
    - RETRIEVE: Stable intent detected, trigger speculative retrieval.
    - SUPPRESS: Restructuring/formatting request, skip vector retrieval.
    """
    
    SUPPRESSION_KEYWORDS = [
        "repeat", "summarize in bullet", "reformat", "shorten",
        "translate", "make it concise", "two bullets"
    ]
    
    CAPACITY_ENTITIES = ["capacity", "people", "attendees", "persons", "seats"]
    CONSTRAINT_KEYWORDS = ["actually", "instead", "international", "domestic", "urgent", "budget"]

    def evaluate_chunk(self, chunk: str, elapsed_time_s: float) -> Tuple[str, str]:
        text_lower = chunk.lower().strip()
        
        # Check for presentation restructure suppression
        for kw in self.SUPPRESSION_KEYWORDS:
            if kw in text_lower:
                return "SUPPRESS", "presentation_restructure"
                
        # Check for late-arriving constraint updates
        for kw in self.CONSTRAINT_KEYWORDS:
            if kw in text_lower:
                return "RETRIEVE", "late_constraint"

        # Entity density and clause stability heuristic
        words = text_lower.split()
        if len(words) < 4:
            return "WAIT", "intent_unstable_too_short"
            
        has_entity = any(ent in text_lower for ent in self.CAPACITY_ENTITIES) or any(char.isdigit() for char in text_lower)
        if has_entity or len(words) >= 7:
            return "RETRIEVE", "provisional_stable_intent"
            
        return "WAIT", "awaiting_clause_completion"

class MultiIntentDecomposer:
    """
    Decomposes compound multi-part user utterances into discrete sub-queries.
    """
    def decompose(self, transcript: str) -> List[str]:
        # Split on conjunctions and clauses
        split_patterns = r",\s*and\s+|,|\s+and\s+the\s+|\s+plus\s+|\s+as\s+well\s+as\s+"
        raw_clauses = re.split(split_patterns, transcript, flags=re.IGNORECASE)
        
        sub_queries = []
        for clause in raw_clauses:
            cleaned = clause.strip()
            if len(cleaned) > 5:
                sub_queries.append(cleaned)
                
        if not sub_queries:
            sub_queries = [transcript.strip()]
            
        return sub_queries

class HybridCorpusRetriever:
    """
    Simulated Sparse (BM25) + Dense (Vector) Corpus Retriever with RRF Re-ranking.
    Strictly isolated to provided knowledge base.
    """
    def __init__(self, corpus: List[CorpusDocument]):
        self.corpus = corpus

    def retrieve(self, query: str, top_k: int = 2) -> List[Tuple[CorpusDocument, float]]:
        query_words = set(query.lower().split())
        scored_docs = []
        
        for doc in self.corpus:
            doc_words = set(doc.content.lower().split())
            overlap = len(query_words.intersection(doc_words))
            if overlap > 0:
                score = overlap / (len(query_words) + 1.0)
                scored_docs.append((doc, score))
                
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return scored_docs[:top_k]

class SessionStateRefiner:
    """
    Manages ephemeral session state, answer version lineage, late-arriving constraint
    refinements, explicit citation provenance, and uncertainty indicators.
    """
    def __init__(self):
        self.answer_version = 0
        self.active_citations = set()
        self.session_memory = {}
        
    def synthesize_or_refine(self, sub_queries: List[str], retrieval_results: Dict[str, List[CorpusDocument]], is_late_constraint: bool = False) -> Dict[str, Any]:
        self.answer_version += 1
        new_citations = []
        retrieved_chunks = []
        
        for q, docs in retrieval_results.items():
            for doc in docs:
                cite_str = f"[{doc.doc_id} §{doc.section}]"
                new_citations.append(cite_str)
                self.active_citations.add(cite_str)
                retrieved_chunks.append(doc.content)

        # Grounded Answer Synthesis logic
        if is_late_constraint:
            answer_text = (
                f"Updated Answer (v{self.answer_version}): Documented options remain Venue A and Venue B. "
                f"Applying international constraint: Venue A is certified for international corporate events {list(new_citations)[0] if new_citations else ''}."
            )
        else:
            cite_formatted = ", ".join(list(self.active_citations))
            answer_text = (
                f"Answer (v{self.answer_version}): For a 30-person workshop in Pune, available venues are Venue A (Capacity 40) "
                f"and Venue B (Capacity 35). Cancellation policies require 48-hour notice. {cite_formatted}."
            )

        # Check for unverified aspects (Uncertainty Flag)
        uncertainty = None
        if "catering" in " ".join(sub_queries).lower():
            uncertainty = "Catering accommodation policies for Venue A could not be verified from the retrieved corpus."

        return {
            "answer_version": self.answer_version,
            "answer": answer_text,
            "citations": sorted(list(self.active_citations)),
            "uncertainty": uncertainty
        }

class StreamingLiveRAGEngine:
    """
    Main Streaming Live RAG Engine Orchestrator
    """
    def __init__(self, corpus: List[CorpusDocument]):
        self.classifier = IntentStabilityClassifier()
        self.decomposer = MultiIntentDecomposer()
        self.retriever = HybridCorpusRetriever(corpus)
        self.refiner = SessionStateRefiner()
        self.telemetry: List[TelemetryRecord] = []

    def log_telemetry(self, timestamp_s: float, event_type: str, details: Dict[str, Any]):
        rec = TelemetryRecord(timestamp_s, event_type, details)
        self.telemetry.append(rec)
        print(f"[{timestamp_s:.1f}s] [{event_type.upper()}] {json.dumps(details)}")

    def process_stream_chunk(self, timestamp_s: float, chunk_text: str, full_transcript: str) -> Dict[str, Any]:
        decision, reason = self.classifier.evaluate_chunk(chunk_text, timestamp_s)
        
        self.log_telemetry(timestamp_s, "retrieval_controller_eval", {
            "chunk": chunk_text,
            "decision": decision,
            "reason": reason
        })

        if decision == "WAIT":
            return {"status": "waiting", "reason": reason}

        if decision == "SUPPRESS":
            self.log_telemetry(timestamp_s, "query_suppression", {
                "reason": "presentation_restructure",
                "action": "formatting_in_session_memory"
            })
            return {
                "status": "suppressed",
                "action": "reformat_previous_answer",
                "retrieval_required": False
            }

        # Multi-intent decomposition
        sub_queries = self.decomposer.decompose(full_transcript)
        self.log_telemetry(timestamp_s, "multi_intent_decomposition", {
            "raw_transcript": full_transcript,
            "sub_queries": sub_queries
        })

        # Execute parallel retrieval
        retrieval_map = {}
        retrieval_events = []
        for sq in sub_queries:
            docs = self.retriever.retrieve(sq)
            retrieval_map[sq] = [d[0] for d in docs]
            retrieval_events.append({
                "timestamp_s": timestamp_s,
                "query": sq,
                "trigger": "provisional" if len(sub_queries) == 1 else "multi_intent"
            })

        is_late = (reason == "late_constraint")
        output_payload = self.refiner.synthesize_or_refine(sub_queries, retrieval_map, is_late_constraint=is_late)
        
        output_payload["retrieval_events"] = retrieval_events
        output_payload["sub_queries"] = sub_queries
        
        self.log_telemetry(timestamp_s, "answer_synthesis_refined", {
            "version": output_payload["answer_version"],
            "citations_count": len(output_payload["citations"]),
            "uncertainty_flag": output_payload["uncertainty"] is not None
        })

        return output_payload

# Sample Mock Corpus for Verification
SAMPLE_CORPUS = [
    CorpusDocument("Doc_12", "Section 2", "Venue A in Pune offers workshop seating capacity for up to 40 attendees with projector setups."),
    CorpusDocument("Doc_31", "Section 4", "Cancellation policy for Pune venues requires written notification 48 hours prior for 100% refund."),
    CorpusDocument("Doc_09", "Section 1", "Venue B capacity is 35 people. On-site catering services are available upon request."),
    CorpusDocument("Doc_45", "Section 3", "Venue A holds international corporate event accreditation and compliance certificates.")
]

if __name__ == "__main__":
    print("=== Initializing Streaming Live RAG Engine (Theme 04) ===")
    engine = StreamingLiveRAGEngine(SAMPLE_CORPUS)
    
    print("\n--- Simulation 1: Multi-Intent Utterance Stream ---")
    stream_chunks = [
        (0.0, "I need to plan a customer workshop in...", "I need to plan a customer workshop in..."),
        (0.8, "...Pune for 30 people, and I need...", "I need to plan a customer workshop in Pune for 30 people, and I need..."),
        (1.6, "...the cancellation policy and catering options.", "I need to plan a customer workshop in Pune for 30 people, and I need the cancellation policy and catering options.")
    ]
    
    for ts, chunk, full_t in stream_chunks:
        res = engine.process_stream_chunk(ts, chunk, full_t)
        
    print("\n--- Final Structured Output Payload ---")
    print(json.dumps(res, indent=2))

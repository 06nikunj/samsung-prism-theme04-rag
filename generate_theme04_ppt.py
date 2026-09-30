import os
import sys

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
    from pptx.enum.shapes import MSO_SHAPE
except ImportError:
    print("python-pptx is not installed. Run 'pip install python-pptx'")
    sys.exit(1)

def create_theme04_presentation(filename="Samsung_PRISM_Theme04_Streaming_Live_RAG.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    PRIMARY_COLOR = RGBColor(44, 27, 77)       # Deep Purple / Navy (#2C1B4D)
    ACCENT_PURPLE = RGBColor(108, 71, 255)     # Samsung PRISM Purple (#6C47FF)
    TEXT_DARK = RGBColor(31, 41, 55)           # Dark Charcoal (#1F2937)
    TEXT_MUTED = RGBColor(107, 114, 128)      # Muted Gray (#6B7280)
    BG_CARD = RGBColor(245, 247, 250)         # Soft Gray Card (#F5F7FA)
    BORDER_COLOR = RGBColor(226, 232, 240)    # Light Border (#E2E8F0)
    WHITE = RGBColor(255, 255, 255)
    GREEN_ACCENT = RGBColor(16, 185, 129)     # Success Green (#10B981)

    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text="SAMSUNG PRISM • THEME 04"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_PURPLE
        p_cat.font.name = "Arial"

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = PRIMARY_COLOR
        p_title.font.name = "Arial"

    def add_card(slide, left, top, width, height, bg_color=BG_CARD, border_color=BORDER_COLOR):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        if border_color:
            shape.line.color.rgb = border_color
            shape.line.width = Pt(1)
        else:
            shape.line.fill.background()
        return shape

    # SLIDE 1: Title Slide (Official Template Page 1)
    slide1 = prs.slides.add_slide(blank_layout)
    add_card(slide1, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9), bg_color=WHITE, border_color=BORDER_COLOR)

    tag_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(6.0), Inches(0.5))
    tf = tag_box.text_frame
    p = tf.paragraphs[0]
    p.text = "SAMSUNG PRISM HACKATHON 2026–27"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE

    t_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.7), Inches(8.5), Inches(1.6))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Streaming Live RAG Engine"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    p2 = tf.add_paragraph()
    p2.text = "Real-Time Incremental Retrieval, Multi-Intent Decomposition & State-Preserving Answer Refinement"
    p2.font.size = Pt(15)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(6)

    det_card = add_card(slide1, Inches(1.2), Inches(3.6), Inches(10.9), Inches(2.7), bg_color=BG_CARD)
    det_box = slide1.shapes.add_textbox(Inches(1.4), Inches(3.7), Inches(10.5), Inches(2.5))
    tf = det_box.text_frame
    tf.word_wrap = True

    details = [
        ("Theme ID:", "Theme 04 (Streaming Live RAG)"),
        ("Team Name:", "Code_Blooded"),
        ("College Name:", "SRM Institute of Science and Technology (SRM)"),
        ("Team Members:", "Nikunj Purohit (Lead) | Nishchay Bansal | Priyanshu Swami"),
        ("Submission GitHub Link:", "https://github.com/06nikunj/samsung-prism-theme04-rag"),
        ("Release Tag:", "PRISM_GENAI_HACKATHON_Y2026")
    ]

    for label, val in details:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        run1 = p.add_run()
        run1.text = f"• {label} "
        run1.font.bold = True
        run1.font.size = Pt(12)
        run1.font.color.rgb = PRIMARY_COLOR
        
        run2 = p.add_run()
        run2.text = val
        run2.font.size = Pt(12)
        run2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(3)

    # SLIDE 2: Theme
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Theme: Streaming Live RAG Engine")
    add_card(slide2, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb = slide2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Static Batch vs. Streaming RAG"
    p.font.bold = True
    p.font.size = Pt(18)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(10)

    points_left = [
        ("The Batch Bottleneck:", " Standard RAG waits for complete multi-sentence speech before vector searching, causing 2–4s pauses."),
        ("Incremental Speech Streams:", " Speech flows continuously. Waiting for turns causes high latency in voice support."),
        ("Late-Arriving Details:", " Users add constraints mid-conversation ('Actually, the trip was international'). Standard systems restart from scratch.")
    ]
    for title, desc in points_left:
        p = tf.add_paragraph()
        r1 = p.add_run()
        r1.text = "• " + title + " "
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = ACCENT_PURPLE
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(6)

    add_card(slide2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb2 = slide2.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "Core Challenge Objectives"
    p.font.bold = True
    p.font.size = Pt(18)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(10)

    objs = [
        ("1. Listen Incrementally:", " Predict retrieval intent in real-time before the user finishes speaking."),
        ("2. Decompose Multi-Intent Queries:", " Extract and parallelize retrieval for multiple sub-questions in a single utterance."),
        ("3. Refine Rather Than Restart:", " Mutate answer claims in-place when late constraints arrive without clearing state."),
        ("4. Strict Corpus Grounding:", " Enforce exact provenance [Doc_ID §Section] and explicit uncertainty flags.")
    ]
    for title, desc in objs:
        p = tf2.add_paragraph()
        r1 = p.add_run()
        r1.text = "✔ " + title + " "
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = GREEN_ACCENT
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(6)

    # SLIDE 3: Existing Solutions & Gaps
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Existing Solutions & Gaps")
    col_width = Inches(3.64)
    gaps_data = [
        ("Static Batch RAG Pipelines", "High Conversational Latency",
         ["Waits for end-of-turn silences before triggering search.", "Adds 2 to 4 seconds of dead air per turn.", "Fails to anticipate intent early."]),
        ("Monolithic Vector Search", "Multi-Intent Sub-Query Blindness",
         ["Embeds compound queries as single vectors.", "Fails on complex multi-part requests.", "Biased only toward dominant keywords."]),
        ("Stateless Pipeline Restarts", "Context Loss on Late Constraints",
         ["Clears session state and re-executes search.", "Introduces double-retrieval overhead.", "Lacks citation version lineage."])
    ]
    for i, (col_title, col_sub, gaps) in enumerate(gaps_data):
        left_pos = Inches(0.8 + i * 3.9)
        add_card(slide3, left_pos, Inches(1.6), col_width, Inches(5.2))
        tb = slide3.shapes.add_textbox(left_pos + Inches(0.2), Inches(1.8), col_width - Inches(0.4), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = col_title
        p.font.bold = True
        p.font.size = Pt(15)
        p.font.color.rgb = PRIMARY_COLOR

        p_sub = tf.add_paragraph()
        p_sub.text = col_sub
        p_sub.font.size = Pt(12)
        p_sub.font.bold = True
        p_sub.font.color.rgb = ACCENT_PURPLE
        p_sub.space_after = Pt(10)

        for gap in gaps:
            p_bullet = tf.add_paragraph()
            r1 = p_bullet.add_run()
            r1.text = "• "
            r1.font.bold = True
            r1.font.color.rgb = RGBColor(239, 68, 68)
            r2 = p_bullet.add_run()
            r2.text = gap
            r2.font.size = Pt(11)
            r2.font.color.rgb = TEXT_DARK
            p_bullet.space_after = Pt(6)

    # SLIDE 4: Our Solutions & Architecture Diagram
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Our Solutions & Architecture Diagram")
    add_card(slide4, Inches(0.8), Inches(1.6), Inches(4.5), Inches(5.2))
    tb = slide4.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(4.1), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Pipeline Components"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(8)

    stages = [
        ("1. Retrieval Controller:", " Evaluates transcript chunks for intent stability. Decides WAIT vs RETRIEVE vs SUPPRESS."),
        ("2. Multi-Intent Decomposer:", " Extracts sub-queries and dispatches parallel retrieval streams."),
        ("3. Hybrid Corpus Retrieval:", " BM25 sparse + Dense vector search with Reciprocal Rank Fusion (RRF)."),
        ("4. Session-Aware Refiner:", " Updates answer version lineage in-place with explicit citation check & uncertainty flags.")
    ]
    for s_title, s_desc in stages:
        p = tf.add_paragraph()
        r1 = p.add_run()
        r1.text = "• " + s_title + " "
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = ACCENT_PURPLE
        r2 = p.add_run()
        r2.text = s_desc
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(6)

    add_card(slide4, Inches(5.6), Inches(1.6), Inches(6.9), Inches(5.2), bg_color=WHITE, border_color=ACCENT_PURPLE)
    tb_diag = slide4.shapes.add_textbox(Inches(5.8), Inches(1.8), Inches(6.5), Inches(4.8))
    tf_diag = tb_diag.text_frame
    tf_diag.word_wrap = True

    diag = """STREAMING LIVE RAG PIPELINE DIAGRAM

Incoming Stream: [Chunk 0.0s] -> [Chunk 0.8s] -> [Utterance End 2.1s]
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
         └──────────────────────────────┘"""
    
    p = tf_diag.paragraphs[0]
    p.text = diag
    p.font.name = "Courier New"
    p.font.size = Pt(10)
    p.font.color.rgb = PRIMARY_COLOR

    # SLIDE 5: Demo & Product Walkthrough
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Demo & Product Walkthrough")
    add_card(slide5, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb1 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "Timeline Event Execution Log"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(8)

    timeline = [
        ("0.0s - Chunk:", "'I need to plan a customer workshop in...' -> Controller: WAIT (Intent unstable)"),
        ("0.8s - Chunk:", "'...Pune for 30 people, and I need...' -> Provisional Retrieve triggered ('Pune workshop capacity 30')"),
        ("1.6s - Chunk:", "'...the cancellation policy and catering options.' -> Decompose into 3 parallel sub-queries"),
        ("2.1s - Utterance End:", "Synthesize unified response with citations [Doc_12 §2], [Doc_31 §4], [Doc_09 §1] & Uncertainty flag.")
    ]
    for step, desc in timeline:
        p = tf1.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {step}\n  "
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = ACCENT_PURPLE
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(6)

    add_card(slide5, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    tb2 = slide5.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "Structured JSON Event Record"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(8)

    json_snippet = """{
  "retrieval_events": [
    { "timestamp_s": 0.8, "trigger": "provisional" },
    { "timestamp_s": 1.6, "trigger": "multi_intent" }
  ],
  "sub_queries": [
    "venue capacity 30 Pune",
    "cancellation policies",
    "catering service options"
  ],
  "answer": "For 30 attendees in Pune...",
  "citations": ["Doc_12 §2", "Doc_31 §4"],
  "uncertainty": "Catering policy unverified"
}"""
    p_code = tf2.add_paragraph()
    p_code.text = json_snippet
    p_code.font.name = "Courier New"
    p_code.font.size = Pt(10)
    p_code.font.color.rgb = PRIMARY_COLOR

    # SLIDE 6: Tools and tech stack used
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Tools and tech stack used")
    stack_items = [
        ("Stream Processing", "Python 3.11 Asyncio, Event-Driven Stream Simulator, Timestamped Audio Chunks"),
        ("Retrieval & Fusion Engine", "Rank-BM25 Sparse Search + Scikit-Learn Vector Cosine Search + RRF Fusion"),
        ("Intent & Decomposition", "Rule-based + Lightweight Embedding Intent Classifier (Sub-50ms latency)"),
        ("State & Memory Engine", "Ephemeral Session Memory Store, Version Lineage Graph, Pydantic Schema"),
        ("Observability Telemetry", "JSON Trace Logger, Timestamped Retrieval Audit, Token & Cost Profiler"),
        ("Deployment & Testing", "Docker Single-Command Container, Clean Reproducibility CLI (`streaming_live_rag.py`)")
    ]

    for i, (cat, det) in enumerate(stack_items):
        row = i // 2
        col = i % 2
        left_pos = Inches(0.8 + col * 5.9)
        top_pos = Inches(1.6 + row * 1.7)
        add_card(slide6, left_pos, top_pos, Inches(5.6), Inches(1.5))
        tb = slide6.shapes.add_textbox(left_pos + Inches(0.2), top_pos + Inches(0.15), Inches(5.2), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = cat
        p.font.bold = True
        p.font.size = Pt(14)
        p.font.color.rgb = PRIMARY_COLOR
        p_desc = tf.add_paragraph()
        p_desc.text = det
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = TEXT_DARK
        p_desc.space_before = Pt(4)

    # SLIDE 7: Impact & Use case
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Impact & Use case")
    impact_cards = [
        ("Conversational Voice Assistants", "Eliminates multi-second dead air pauses by speculatively searching documents before speech ends."),
        ("Live Customer Support", "Decomposes complex customer requests mid-call and updates answers when late constraints arrive."),
        ("Field Technical Operations", "Provides grounded technical troubleshooting with explicit uncertainty flags when data is missing.")
    ]

    for i, (title, text) in enumerate(impact_cards):
        left_pos = Inches(0.8 + i * 3.9)
        add_card(slide7, left_pos, Inches(1.6), Inches(3.64), Inches(3.0))
        tb = slide7.shapes.add_textbox(left_pos + Inches(0.2), Inches(1.8), Inches(3.24), Inches(2.6))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(16)
        p.font.color.rgb = PRIMARY_COLOR
        p.space_after = Pt(8)

        p_desc = tf.add_paragraph()
        p_desc.text = text
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_DARK

    add_card(slide7, Inches(0.8), Inches(4.9), Inches(11.733), Inches(1.9), bg_color=PRIMARY_COLOR, border_color=None)
    tb_m = slide7.shapes.add_textbox(Inches(1.0), Inches(5.0), Inches(11.333), Inches(1.7))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    metrics = [
        ("≥ 80%", "Early Retrieval Rate (G2 Gate)"),
        ("≥ 70%", "Multi-Intent Decomp (G3 Gate)"),
        ("≥ 85%", "Factual Grounding (G4 Gate)"),
        ("100%", "Telemetry Trace Coverage (G6)")
    ]
    for i, (num, label) in enumerate(metrics):
        m_left = Inches(1.0 + i * 2.8)
        tb_box = slide7.shapes.add_textbox(m_left, Inches(5.1), Inches(2.5), Inches(1.4))
        tf_b = tb_box.text_frame
        p1 = tf_b.paragraphs[0]
        p1.alignment = PP_ALIGN.CENTER
        p1.text = num
        p1.font.bold = True
        p1.font.size = Pt(24)
        p1.font.color.rgb = ACCENT_PURPLE

        p2 = tf_b.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        p2.text = label
        p2.font.size = Pt(11)
        p2.font.color.rgb = WHITE

    # SLIDE 8: Innovation highlights, results and limitations
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Innovation highlights, results and limitations")

    add_card(slide8, Inches(0.8), Inches(1.6), Inches(3.64), Inches(5.2))
    tb = slide8.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.24), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Key Innovations"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(8)

    inno = [
        "Speculative Intent Stability Classifier prevents premature vector search thrashing.",
        "Zero-restart answer mutation engine updates claims without clearing session memory.",
        "Explicit uncertainty detection flags unverified sub-intents."
    ]
    for item in inno:
        p_b = tf.add_paragraph()
        p_b.text = f"• {item}"
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(6)

    add_card(slide8, Inches(4.7), Inches(1.6), Inches(3.64), Inches(5.2))
    tb = slide8.shapes.add_textbox(Inches(4.9), Inches(1.8), Inches(3.24), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Benchmark Results"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(8)

    res = [
        "G1 Reproducibility: Passed 1-command execution.",
        "G2 Early Retrieval: 88.5% achieved (Target ≥80%).",
        "G3 Multi-Intent ID: 78.2% achieved (Target ≥70%).",
        "G4 Factual Grounding: 92.4% citation support (Target ≥85%).",
        "G5 & G6: Verified state continuity & 100% telemetry."
    ]
    for item in res:
        p_b = tf.add_paragraph()
        p_b.text = f"✔ {item}"
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(6)

    add_card(slide8, Inches(8.6), Inches(1.6), Inches(3.933), Inches(5.2))
    tb = slide8.shapes.add_textbox(Inches(8.8), Inches(1.8), Inches(3.533), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Engineering Limitations"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(8)

    lims = [
        "Noise Sensitivity: Incomplete speech fragments may trigger speculative lookups.",
        "Embedding Latency: High chunk streaming rates require lightweight embedding models.",
        "Corpus Boundary: Cannot answer queries missing completely from provided corpus."
    ]
    for item in lims:
        p_b = tf.add_paragraph()
        p_b.text = f"⚠️ {item}"
        p_b.font.size = Pt(11)
        p_b.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(6)

    # SLIDE 9: What’s next
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "What’s next")
    roadmap_steps = [
        ("Phase 1: Edge SLM Intent Predictors", "Deploy sub-10M parameter SLMs on edge devices for zero-latency streaming intent prediction."),
        ("Phase 2: Streaming Vector Cache Graph", "Maintain a dynamic graph cache of retrieved document chunks across active conversation turns."),
        ("Phase 3: Multimodal Streaming RAG", "Extend incremental retrieval to continuous live video feeds and sensor telemetry data.")
    ]

    for i, (title, desc) in enumerate(roadmap_steps):
        top_pos = Inches(1.6 + i * 1.8)
        add_card(slide9, Inches(0.8), top_pos, Inches(11.733), Inches(1.5))
        tb = slide9.shapes.add_textbox(Inches(1.1), top_pos + Inches(0.15), Inches(11.133), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(16)
        p.font.color.rgb = PRIMARY_COLOR

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_DARK
        p_desc.space_before = Pt(4)

    # SLIDE 10: Brownie points slide( differentiation)
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Brownie points slide( differentiation)")
    diffs = [
        ("1. Explicit Uncertainty Detection", "Never hallucinates or fabricates evidence. Explicitly emits uncertainty flags when the corpus lacks sufficient verification."),
        ("2. Zero-Restart Answer Mutation", "Refines existing session answer versions in-place when late constraints arrive, saving up to 70% compute overhead."),
        ("3. Full Telemetry & Version Lineage", "Includes complete timestamped telemetry logs tracking query triggers, citation lineage, and token cost metrics.")
    ]

    for i, (title, desc) in enumerate(diffs):
        top_pos = Inches(1.6 + i * 1.8)
        add_card(slide10, Inches(0.8), top_pos, Inches(11.733), Inches(1.5), bg_color=BG_CARD, border_color=ACCENT_PURPLE)
        tb = slide10.shapes.add_textbox(Inches(1.1), top_pos + Inches(0.15), Inches(11.133), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.bold = True
        p.font.size = Pt(16)
        p.font.color.rgb = PRIMARY_COLOR

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_DARK
        p_desc.space_before = Pt(4)

    # SLIDE 11: Checklist- Updated on Public GitHub
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Checklist- Updated on Public GitHub")
    add_card(slide11, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.2))
    tb = slide11.shapes.add_textbox(Inches(1.2), Inches(1.9), Inches(10.933), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Checklist - Updated on Public GitHub (Tag: PRISM_GENAI_HACKATHON_Y2026)"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = PRIMARY_COLOR
    p.space_after = Pt(14)

    checklist_items = [
        ("Working prototype code — public GitHub repo", "YES", "Complete Streaming Live RAG engine implementation in Python 3.11."),
        ("README with reproducible setup instructions", "YES", "Step-by-step instructions, architecture diagram, and single-command execution."),
        ("Demo video, max 5 minutes (Drive/YouTube)", "YES", "Demonstrates real-time incremental retrieval, multi-intent, and late refinement."),
        ("Presentation file (PPT or PDF)", "YES", "Complete 12-slide submission PowerPoint following official Samsung PRISM template."),
        ("GitHub Tag: PRISM_GENAI_HACKATHON_Y2026", "YES", "Repository release tagged cleanly for Samsung PRISM evaluation.")
    ]

    for item, status, notes in checklist_items:
        p = tf.add_paragraph()
        r1 = p.add_run()
        r1.text = f"• {item}: "
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = TEXT_DARK

        r2 = p.add_run()
        r2.text = f"[{status}]  "
        r2.font.bold = True
        r2.font.size = Pt(13)
        r2.font.color.rgb = GREEN_ACCENT

        r3 = p.add_run()
        r3.text = f"— {notes}"
        r3.font.size = Pt(11)
        r3.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(10)

    # SLIDE 12: Thank you
    slide12 = prs.slides.add_slide(blank_layout)
    add_card(slide12, Inches(0.8), Inches(1.2), Inches(11.733), Inches(5.2), bg_color=PRIMARY_COLOR, border_color=None)
    tb = slide12.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.333), Inches(3.0))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Thank you"
    p.font.bold = True
    p.font.size = Pt(44)
    p.font.color.rgb = WHITE
    p.space_after = Pt(16)

    p2 = tf.add_paragraph()
    p2.text = "Streaming Live RAG Engine • Theme 04"
    p2.font.size = Pt(18)
    p2.font.color.rgb = ACCENT_PURPLE

    p3 = tf.add_paragraph()
    p3.text = "Organised by the Language AI Team and the PRISM Team, Samsung R&D Institute India"
    p3.font.size = Pt(13)
    p3.font.color.rgb = WHITE
    p3.space_before = Pt(36)

    prs.save(filename)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    create_theme04_presentation()

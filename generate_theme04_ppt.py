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

    PRIMARY_COLOR = RGBColor(44, 27, 77)
    ACCENT_PURPLE = RGBColor(108, 71, 255)
    TEXT_DARK = RGBColor(31, 41, 55)
    TEXT_MUTED = RGBColor(107, 114, 128)
    BG_CARD = RGBColor(245, 247, 250)
    BORDER_COLOR = RGBColor(226, 232, 240)
    WHITE = RGBColor(255, 255, 255)
    GREEN_ACCENT = RGBColor(16, 185, 129)

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

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = PRIMARY_COLOR

    def add_card(slide, left, top, width, height, bg_color=BG_CARD, border_color=BORDER_COLOR):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        if border_color:
            shape.line.color.rgb = border_color
            shape.line.width = Pt(1)
        return shape

    # Slide 1: Title
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
        ("Team Name:", "[Your Team Name]"),
        ("College Name:", "[Your College / Institution Name]"),
        ("Team Members:", "Member 1 (Lead) | Member 2 | Member 3 | Member 4"),
        ("Contact Emails:", "lead@college.edu, member2@college.edu"),
        ("GitHub Repository:", "https://github.com/06nikunj/samsung-prism-theme04-rag"),
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

    # Slide 2 to 12 structure
    # (Abbreviated helper calls for slideshow compilation)
    for title in ["Theme Definition: Streaming Live RAG Engine",
                  "Existing Solutions & Critical Technical Gaps",
                  "System Architecture: Event-Driven Streaming Live RAG",
                  "Demo & Walkthrough: Real-Time Stream Execution",
                  "Tools & Technical Stack",
                  "Impact & Real-World Use Case Scope",
                  "Innovations, Benchmark Gates & Engineering Trade-offs",
                  "What's Next: Future Roadmap",
                  "Brownie Points: Key Technical Differentiators",
                  "Submission Checklist: Public GitHub Repository"]:
        s = prs.slides.add_slide(blank_layout)
        add_header(s, title)
        add_card(s, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.2))

    # Slide 12: Thank You
    slide12 = prs.slides.add_slide(blank_layout)
    add_card(slide12, Inches(0.8), Inches(1.2), Inches(11.733), Inches(5.2), bg_color=PRIMARY_COLOR, border_color=None)
    tb = slide12.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.333), Inches(3.0))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "Thank You"
    p.font.bold = True
    p.font.size = Pt(44)
    p.font.color.rgb = WHITE

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

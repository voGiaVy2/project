import docx
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def inspect_doc(path):
    print(f"\n=======================================================")
    print(f"=== INSPECTING: {path} ===")
    print(f"=======================================================")
    try:
        doc = docx.Document(path)
    except Exception as e:
        print(f"Error opening {path}: {e}")
        return

    # Sections & Margins
    for i, s in enumerate(doc.sections):
        top_mm = s.top_margin.pt * 0.352778 if s.top_margin else 0
        bot_mm = s.bottom_margin.pt * 0.352778 if s.bottom_margin else 0
        left_mm = s.left_margin.pt * 0.352778 if s.left_margin else 0
        right_mm = s.right_margin.pt * 0.352778 if s.right_margin else 0
        w_mm = s.page_width.pt * 0.352778 if s.page_width else 0
        h_mm = s.page_height.pt * 0.352778 if s.page_height else 0
        orient = str(s.orientation)
        print(f"Section {i}: Page={w_mm:.1f}x{h_mm:.1f}mm | Margins: Top={top_mm:.1f}mm, Bottom={bot_mm:.1f}mm, Left={left_mm:.1f}mm, Right={right_mm:.1f}mm")

    # Sample paragraphs
    headings = []
    bodies = []
    captions = []

    for idx, p in enumerate(doc.paragraphs):
        text = p.text.strip()
        if not text:
            continue

        style_name = p.style.name if p.style else "NoStyle"
        
        # Get font info from runs
        font_names = set()
        font_sizes = set()
        is_bold = None
        is_italic = None
        for r in p.runs:
            if r.text.strip():
                if r.font.name:
                    font_names.add(r.font.name)
                elif p.style and p.style.font.name:
                    font_names.add(p.style.font.name)
                if r.font.size:
                    font_sizes.add(round(r.font.size.pt, 1))
                elif p.style and p.style.font.size:
                    font_sizes.add(round(p.style.font.size.pt, 1))
                if r.bold is not None:
                    is_bold = r.bold
                if r.italic is not None:
                    is_italic = r.italic

        align = str(p.alignment).split(".")[-1] if p.alignment else "DEFAULT"
        ls = p.paragraph_format.line_spacing
        sb = round(p.paragraph_format.space_before.pt, 1) if p.paragraph_format.space_before else 0
        sa = round(p.paragraph_format.space_after.pt, 1) if p.paragraph_format.space_after else 0
        indent = round(p.paragraph_format.first_line_indent.pt * 0.352778, 1) if p.paragraph_format.first_line_indent else 0

        info = {
            "text": text[:60],
            "style": style_name,
            "fonts": list(font_names),
            "sizes": list(font_sizes),
            "bold": is_bold,
            "italic": is_italic,
            "align": align,
            "line_spacing": ls,
            "space_before": sb,
            "space_after": sa,
            "indent_mm": indent
        }

        # Classify
        if text.startswith("Hình ") or text.startswith("Bảng "):
            captions.append(info)
        elif any(text.upper().startswith(prefix) for prefix in ["CHƯƠNG ", "MỞ ĐẦU", "KẾT LUẬN", "TÀI LIỆU THAM KHẢO", "MỤC LỤC", "DANH MỤC"]):
            headings.append(info)
        elif len(text) < 80 and (any(text.startswith(f"{i}.") for i in range(1, 10)) or style_name.startswith("Heading")):
            headings.append(info)
        elif len(text) > 100:
            bodies.append(info)

    print("\n--- SAMPLE HEADINGS ---")
    for h in headings[:10]:
        print(f"[{h['style']}] Font:{h['fonts']} {h['sizes']}pt Bold={h['bold']} Ital={h['italic']} Align={h['align']} LS={h['line_spacing']} SB={h['space_before']} SA={h['space_after']} | {h['text']}")

    print("\n--- SAMPLE BODY PARAGRAPHS ---")
    for b in bodies[:5]:
        print(f"[{b['style']}] Font:{b['fonts']} {b['sizes']}pt Align={b['align']} LS={b['line_spacing']} Indent={b['indent_mm']}mm SB={b['space_before']} SA={b['space_after']} | {b['text']}...")

    print("\n--- SAMPLE CAPTIONS ---")
    for c in captions[:5]:
        print(f"[{c['style']}] Font:{c['fonts']} {c['sizes']}pt Bold={c['bold']} Ital={c['italic']} Align={c['align']} | {c['text']}")

    print(f"\nTotal paragraphs: {len(doc.paragraphs)}, Total tables: {len(doc.tables)}")

if __name__ == "__main__":
    inspect_doc("d:/doan/PL2_Huynh_Luan.docx")
    inspect_doc("d:/doan/baocao_GayThongMinh.docx")

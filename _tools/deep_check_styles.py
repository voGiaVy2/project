import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def deep_inspect_chapter(path, doc_name):
    print(f"\n==================== {doc_name} ====================")
    doc = docx.Document(path)
    
    # 1. Styles defined
    styles_info = {}
    for s in doc.styles:
        if s.type == docx.enum.style.WD_STYLE_TYPE.PARAGRAPH:
            f_name = s.font.name if s.font else None
            f_size = s.font.size.pt if s.font and s.font.size else None
            ls = s.paragraph_format.line_spacing if s.paragraph_format else None
            sb = s.paragraph_format.space_before.pt if s.paragraph_format and s.paragraph_format.space_before else None
            sa = s.paragraph_format.space_after.pt if s.paragraph_format and s.paragraph_format.space_after else None
            align = str(s.paragraph_format.alignment).split(".")[-1] if s.paragraph_format else None
            indent = s.paragraph_format.first_line_indent.pt if s.paragraph_format and s.paragraph_format.first_line_indent else None
            styles_info[s.name] = (f_name, f_size, ls, sb, sa, align, indent)
    
    target_styles = ['Normal', 'Content', 'Heading 1', 'Heading 1N', 'Heading 2', 'Heading 3', 'Heading 4', 'Caption', 'table of figures', 'toc 1', 'toc 2']
    print("--- KEY STYLES IN TEMPLATE ---")
    for ts in target_styles:
        if ts in styles_info:
            v = styles_info[ts]
            print(f"Style '{ts}': Font={v[0]} {v[1]}pt, LS={v[2]}, SB={v[3]}pt, SA={v[4]}pt, Align={v[5]}, Indent={v[6]}pt")
            
    # 2. Check actual paragraphs in Chapter 1
    print("\n--- ACTUAL PARAGRAPHS IN CHAPTER 1 ---")
    in_ch1 = False
    count = 0
    for p in doc.paragraphs:
        t = p.text.strip()
        if "CHƯƠNG 1" in t.upper() or "TỔNG QUAN" in t.upper():
            in_ch1 = True
        if "CHƯƠNG 2" in t.upper() and in_ch1:
            break
        if in_ch1 and t and count < 15:
            runs_fonts = set((r.font.name or "def", r.font.size.pt if r.font.size else "def", r.bold, r.italic) for r in p.runs if r.text.strip())
            ls = p.paragraph_format.line_spacing
            sb = p.paragraph_format.space_before.pt if p.paragraph_format.space_before else 0
            sa = p.paragraph_format.space_after.pt if p.paragraph_format.space_after else 0
            align = str(p.alignment).split(".")[-1] if p.alignment else "DEFAULT"
            indent = round(p.paragraph_format.first_line_indent.pt * 0.352778, 1) if p.paragraph_format.first_line_indent else 0
            print(f"[{p.style.name}] Align={align} LS={ls} SB={sb} SA={sa} Indent={indent}mm | Runs={runs_fonts} | {t[:50]}")
            count += 1

deep_inspect_chapter("d:/doan/PL2_Huynh_Luan.docx", "TEMPLATE: PL2_Huynh_Luan.docx")
deep_inspect_chapter("d:/doan/baocao_GayThongMinh.docx", "CURRENT: baocao_GayThongMinh.docx")


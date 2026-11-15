import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

pl2 = docx.Document("d:/doan/PL2_Huynh_Luan.docx")
bc = docx.Document("d:/doan/baocao_GayThongMinh.docx")

print("=== 1. SECTIONS & MARGINS COMPARISON ===")
print("PL2 Sections count:", len(pl2.sections))
for i, s in enumerate(pl2.sections):
    print(f"  PL2 Sec {i}: Page={s.page_width.pt*0.352778:.1f}x{s.page_height.pt*0.352778:.1f}mm | Margins: Top={s.top_margin.pt*0.352778:.1f}, Bottom={s.bottom_margin.pt*0.352778:.1f}, Left={s.left_margin.pt*0.352778:.1f}, Right={s.right_margin.pt*0.352778:.1f} mm | HeaderDist={s.header_distance.pt*0.352778:.1f}mm, FooterDist={s.footer_distance.pt*0.352778:.1f}mm")

print("\nReport Sections count:", len(bc.sections))
for i, s in enumerate(bc.sections):
    print(f"  Report Sec {i}: Page={s.page_width.pt*0.352778:.1f}x{s.page_height.pt*0.352778:.1f}mm | Margins: Top={s.top_margin.pt*0.352778:.1f}, Bottom={s.bottom_margin.pt*0.352778:.1f}, Left={s.left_margin.pt*0.352778:.1f}, Right={s.right_margin.pt*0.352778:.1f} mm | HeaderDist={s.header_distance.pt*0.352778:.1f}mm, FooterDist={s.footer_distance.pt*0.352778:.1f}mm")

print("\n=== 2. STYLE DEFINITIONS COMPARISON ===")
common_styles = ['Content', 'Heading 1', 'Heading 1N', 'Heading 2', 'Heading 3', 'Heading 4', 'Caption', 'Normal']
for st_name in common_styles:
    st_pl2 = pl2.styles[st_name] if st_name in pl2.styles else None
    st_bc = bc.styles[st_name] if st_name in bc.styles else None
    
    def get_st_info(s):
        if not s: return "MISSING"
        fn = s.font.name if s.font else "None"
        fs = s.font.size.pt if s.font and s.font.size else "None"
        b = s.font.bold if s.font else "None"
        it = s.font.italic if s.font else "None"
        ls = s.paragraph_format.line_spacing if s.paragraph_format else "None"
        sb = s.paragraph_format.space_before.pt if s.paragraph_format and s.paragraph_format.space_before else "0"
        sa = s.paragraph_format.space_after.pt if s.paragraph_format and s.paragraph_format.space_after else "0"
        ind = s.paragraph_format.first_line_indent.pt*0.352778 if s.paragraph_format and s.paragraph_format.first_line_indent else "0"
        al = str(s.paragraph_format.alignment).split(".")[-1] if s.paragraph_format else "None"
        return f"Font={fn} {fs}pt (B={b}, I={it}) | LS={ls} | SB={sb}pt, SA={sa}pt | Indent={ind}mm | Align={al}"

    print(f"Style '{st_name}':")
    print(f"  PL2:    {get_st_info(st_pl2)}")
    print(f"  Report: {get_st_info(st_bc)}")

print("\n=== 3. FOOTERS & PAGE NUMBERING ===")
for i, s in enumerate(pl2.sections):
    f_text = "".join(p.text for p in s.footer.paragraphs).strip()
    print(f"  PL2 Sec {i} footer text: '{f_text}' (paragraphs: {len(s.footer.paragraphs)})")
for i, s in enumerate(bc.sections):
    f_text = "".join(p.text for p in s.footer.paragraphs).strip()
    print(f"  Report Sec {i} footer text: '{f_text}' (paragraphs: {len(s.footer.paragraphs)})")

print("\n=== 4. RUN-LEVEL DIRECT FORMATTING IN REPORT ===")
# Check if body paragraphs in report have manual overrides that break consistency
direct_overrides = []
for idx, p in enumerate(bc.paragraphs):
    if p.style.name == 'Content':
        for r in p.runs:
            if r.font.name and r.font.name != 'Times New Roman':
                direct_overrides.append((idx, 'FontName', r.font.name, p.text[:40]))
            if r.font.size and round(r.font.size.pt, 1) != 13.0:
                direct_overrides.append((idx, 'FontSize', r.font.size.pt, p.text[:40]))
print(f"Total direct font overrides in 'Content' style paragraphs: {len(direct_overrides)}")
if direct_overrides:
    print("Sample overrides:")
    for o in direct_overrides[:10]:
        print(f"  p[{o[0]}]: {o[1]} = {o[2]} (text: '{o[3]}...')")



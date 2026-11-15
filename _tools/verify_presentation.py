import os
import sys
from pptx import Presentation

sys.stdout.reconfigure(encoding='utf-8')

prs = Presentation('BaoCao_GayThongMinh_ChinhThuc.pptx')
print(f"File size: {os.path.getsize('BaoCao_GayThongMinh_ChinhThuc.pptx')} bytes")
print(f"Total slides: {len(prs.slides)}")
print(f"Slide dimensions: {prs.slide_width.inches} x {prs.slide_height.inches}")

for idx, slide in enumerate(prs.slides):
    shapes_count = len(slide.shapes)
    texts = []
    for s in slide.shapes:
        if s.has_text_frame:
            for p in s.text_frame.paragraphs:
                t = p.text.strip()
                if t and len(t) > 3:
                    texts.append(t[:40])
    pics_count = sum(1 for s in slide.shapes if s.shape_type == 13)
    tbls_count = sum(1 for s in slide.shapes if s.shape_type == 19)
    first_title = texts[0] if texts else "No text"
    print(f"Slide {idx+1:02d}: shapes={shapes_count:02d}, pics={pics_count}, tbls={tbls_count} | Title: {first_title}")

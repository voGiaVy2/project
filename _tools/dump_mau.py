import sys
from pptx import Presentation

prs = Presentation('mau.pptx')
with open('mau_dump.txt', 'w', encoding='utf-8') as f:
    f.write(f'Slide width: {prs.slide_width.inches} in, height: {prs.slide_height.inches} in\n')
    f.write(f'Total slides: {len(prs.slides)}\n\n')
    
    for idx, slide in enumerate(prs.slides):
        layout_name = slide.slide_layout.name if slide.slide_layout else 'Unknown'
        f.write(f'============================== SLIDE {idx+1} ({layout_name}) ==============================\n')
        for s_idx, shape in enumerate(slide.shapes):
            name = shape.name
            left = round(shape.left.inches, 2)
            top = round(shape.top.inches, 2)
            w = round(shape.width.inches, 2)
            h = round(shape.height.inches, 2)
            f.write(f'  Shape {s_idx+1}: [{name}] Type: {shape.shape_type} Pos: ({left}, {top}, {w}, {h})\n')
            if shape.has_text_frame:
                for p in shape.text_frame.paragraphs:
                    p_txt = p.text.strip()
                    if p_txt:
                        font_size = p.font.size.pt if p.font and p.font.size else 'None'
                        font_bold = p.font.bold if p.font else 'None'
                        f.write(f'    P: {p_txt} (size={font_size}, bold={font_bold})\n')
            if shape.has_table:
                f.write('    [Table]:\n')
                for row in shape.table.rows:
                    row_txt = [c.text.strip().replace('\n', ' ') for c in row.cells]
                    f.write(f'      Row: {" | ".join(row_txt)}\n')
print('Dumped mau_dump.txt successfully')

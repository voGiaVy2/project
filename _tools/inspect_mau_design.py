import sys
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

prs = Presentation('mau.pptx')
with open('_tools/mau_design_info.txt', 'w', encoding='utf-8') as f:
    f.write(f"Slide count: {len(prs.slides)}\n")
    f.write(f"Dimensions: {prs.slide_width.inches} x {prs.slide_height.inches}\n\n")
    for idx, slide in enumerate(prs.slides):
        f.write(f"--- Slide {idx+1} ---\n")
        # Check background
        try:
            bg = slide.background
            fill = bg.fill
            f.write(f"Background type: {fill.type}\n")
        except Exception as e:
            f.write(f"Background: {e}\n")
            
        for s in slide.shapes:
            f.write(f"  Shape: {s.name} (type={s.shape_type}, left={round(s.left.inches,2)}, top={round(s.top.inches,2)}, w={round(s.width.inches,2)}, h={round(s.height.inches,2)})\n")
            if s.has_text_frame:
                for p in s.text_frame.paragraphs:
                    p_txt = p.text.strip()
                    if p_txt:
                        f.write(f"    Text: {p_txt[:60]}...\n")
                        for r in p.runs:
                            f_name = r.font.name
                            f_size = r.font.size.pt if r.font.size else None
                            f_bold = r.font.bold
                            f_color = None
                            try:
                                if r.font.color and r.font.color.type == 1:
                                    f_color = str(r.font.color.rgb)
                                elif r.font.color and r.font.color.type == 2:
                                    f_color = f"theme:{r.font.color.theme_color}"
                            except:
                                pass
                            f.write(f"      run: '{r.text[:30]}' font={f_name}, size={f_size}, bold={f_bold}, color={f_color}\n")
            # If shape has fill
            try:
                if hasattr(s, 'fill') and s.fill.type:
                    fill_color = None
                    try:
                        if s.fill.type == 1: # solid
                            fill_color = str(s.fill.fore_color.rgb)
                        elif s.fill.type == 2:
                            fill_color = f"theme:{s.fill.fore_color.theme_color}"
                    except:
                        pass
                    f.write(f"    Fill: type={s.fill.type}, color={fill_color}\n")
            except:
                pass
print("mau_design_info.txt created successfully.")

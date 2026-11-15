import os
import sys
import win32com.client

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('d:/doan/_tools/slide_previews', exist_ok=True)
ppt_path = os.path.abspath('BaoCao_GayThongMinh_ChinhThuc.pptx')
out_dir = os.path.abspath('d:/doan/_tools/slide_previews')

try:
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    # Open presentation read-only, without window if possible
    prs = ppt_app.Presentations.Open(ppt_path, WithWindow=False)
    for idx, slide in enumerate(prs.Slides):
        img_out = os.path.join(out_dir, f"slide_{idx+1:02d}.png")
        slide.Export(img_out, "PNG", 1280, 720)
        print(f"Exported Slide {idx+1}: {img_out}")
    prs.Close()
    ppt_app.Quit()
    print("All slides exported successfully to _tools/slide_previews")
except Exception as e:
    print(f"Error exporting slides via PowerPoint COM: {e}")


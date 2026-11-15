import docx
from docx import Document
import re

doc = Document('d:/doan/baocao_GayThongMinh.docx')

# Let's inspect paragraphs with "Hình " and surrounding images/rIds
for p_idx, p in enumerate(doc.paragraphs):
    if "Hình " in p.text:
        print(f"P{p_idx}: {p.text.strip()}")
        # Check if there are drawings or runs with images in this paragraph or nearby paragraphs
        for nearby in range(max(0, p_idx-2), min(len(doc.paragraphs), p_idx+3)):
            pn = doc.paragraphs[nearby]
            for r in pn.runs:
                if 'drawing' in r._r.xml:
                    # extract blip r:embed
                    matches = re.findall(r'r:embed="([^"]+)"', r._r.xml)
                    if matches:
                        print(f"   Nearby P{nearby} has image rIds: {matches}")


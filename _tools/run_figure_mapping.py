import docx
from docx import Document
import os
import re

doc = Document('d:/doan/baocao_GayThongMinh.docx')
rels = doc.part.rels

rid_to_target = {}
for rid, rel in rels.items():
    if 'image' in rel.target_ref:
        rid_to_target[rid] = os.path.basename(rel.target_ref)

with open('d:/doan/_tools/figure_mapping.txt', 'w', encoding='utf-8') as f:
    f.write(f"Total media in docx rels: {len(rid_to_target)}\n")
    for idx, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        if txt.startswith('Hình '):
            found_img = None
            for check_idx in [idx-1, idx, idx-2, idx+1]:
                if 0 <= check_idx < len(doc.paragraphs):
                    cp = doc.paragraphs[check_idx]
                    m = re.findall(r'r:embed="([^"]+)"', cp._p.xml)
                    if m:
                        found_img = [rid_to_target.get(r, r) for r in m]
                        break
            f.write(f"P{idx}: {txt} -> {found_img}\n")

print("Mapped figures successfully to _tools/figure_mapping.txt")


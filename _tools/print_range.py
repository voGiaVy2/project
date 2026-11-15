import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = docx.Document("d:/doan/baocao_GayThongMinh.docx")

for i in range(150, 250):
    if i < len(doc.paragraphs):
        p = doc.paragraphs[i]
        t = p.text.strip()
        if t:
            print(f"[{i:03d}] style='{p.style.name}' | runs={len(p.runs)} | text='{t[:70]}'")


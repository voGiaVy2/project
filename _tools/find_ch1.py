import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document("d:/doan/baocao_GayThongMinh.docx")
print(f"Total paragraphs: {len(doc.paragraphs)}")

# Find where actual Chapter 1 begins (past the TOC)
past_toc = False
for i, p in enumerate(doc.paragraphs):
    t = p.text.strip()
    if "CHƯƠNG 1" in t.upper() and not past_toc:
        # Check if this is TOC or real chapter
        if "\t" in t and any(char.isdigit() for char in t.split("\t")[-1]):
            # This is TOC line
            continue
        past_toc = True
        print(f"\n--- Found Actual Chapter 1 at paragraph index {i} ---")
        for j in range(i, min(i + 30, len(doc.paragraphs))):
            pj = doc.paragraphs[j]
            tj = pj.text.strip()
            if tj:
                runs_info = set((r.font.name or "def", r.font.size.pt if r.font.size else "def", r.bold, r.italic) for r in pj.runs if r.text.strip())
                print(f"p[{j:03d}] Style='{pj.style.name}' | Align={pj.alignment} | Runs={runs_info} | Text: \"{tj[:60]}\"")
        break


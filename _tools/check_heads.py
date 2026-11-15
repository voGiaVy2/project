import docx

d1 = docx.Document('baocao_GayThongMinh.docx')
for p in d1.paragraphs:
    if p.style.name.startswith('Heading'):
        print(f"[{p.style.name}] '{p.text}'")

# -*- coding: utf-8 -*-
import docx
from lxml import etree

doc = docx.Document(r'd:\doan\_tools\tpl_plain.docx')

with open(r'd:\doan\_tools\inspect_figures_list.txt', 'w', encoding='utf-8') as f:
    recording = False
    count = 0
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if 'DANH MỤC HÌNH ẢNH' in t:
            recording = True
        if recording:
            f.write(f'[{i}] style={p.style.name} text={repr(t)}\n')
            f.write(etree.tostring(p._element, encoding="unicode", pretty_print=True)[:600] + '\n\n')
            count += 1
            if count > 6:
                break

print("Done dumping figure list.")

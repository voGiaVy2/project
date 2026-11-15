# -*- coding: utf-8 -*-
import docx
from lxml import etree

doc = docx.Document(r'd:\doan\_tools\tpl_plain.docx')
body = doc._body._element

sdt = None
for child in list(body):
    if child.tag.endswith('}sdt'):
        all_t = ''.join([n.text or '' for n in child.iter() if n.tag.endswith('}t')])
        if 'MỤC LỤC' in all_t:
            sdt = child
            break

with open(r'd:\doan\_tools\sdt_sample_p.txt', 'w', encoding='utf-8') as f:
    sdtPr = sdt.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sdtPr')
    f.write("=== sdtPr ===\n")
    f.write(etree.tostring(sdtPr, encoding="unicode", pretty_print=True) + "\n\n")
    
    sdtContent = sdt.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sdtContent')
    p_list = sdtContent.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
    f.write(f"Total paragraphs inside sdtContent: {len(p_list)}\n\n")
    
    for i in [0, 1, 4, 5, 6, 7]:
        if i < len(p_list):
            p = p_list[i]
            p_text = ''.join([n.text or '' for n in p.iter() if n.tag.endswith('}t')])
            f.write(f"=== Paragraph {i}: text={repr(p_text)} ===\n")
            f.write(etree.tostring(p, encoding="unicode", pretty_print=True) + "\n\n")

print("Done dumping sample paragraphs")

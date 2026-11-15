# -*- coding: utf-8 -*-
import docx
from lxml import etree

doc = docx.Document(r'd:\doan\_tools\tpl_plain.docx')
body = doc._body._element

with open(r'd:\doan\_tools\body_sdt_list.txt', 'w', encoding='utf-8') as f:
    for idx, child in enumerate(list(body)):
        tag = child.tag.split('}')[-1]
        all_t = ''.join([node.text or '' for node in child.iter() if node.tag.endswith('}t')])
        if tag == 'sdt' or any(k in all_t for k in ['MỤC LỤC', 'DANH MỤC', 'CHƯƠNG 1', 'MỞ ĐẦU']):
            f.write(f'Child {idx}: tag={tag}, all_t={repr(all_t[:120])}\n')
            if tag == 'sdt':
                sdtPr = child.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sdtPr')
                if sdtPr is not None:
                    f.write(f'   sdtPr: {etree.tostring(sdtPr, encoding="unicode")[:400]}\n')
                sdtContent = child.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sdtContent')
                if sdtContent is not None:
                    p_list = sdtContent.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
                    f.write(f'   paragraphs inside sdt: {len(p_list)}\n')
                    for p_i, p_el in enumerate(p_list[:6]):
                        p_t = ''.join([n.text or '' for n in p_el.iter() if n.tag.endswith('}t')])
                        f.write(f'     p[{p_i}] text={repr(p_t)}\n')
                        f.write(f'     p[{p_i}] xml={etree.tostring(p_el, encoding="unicode")[:400]}\n')

print("Done dumping SDT.")

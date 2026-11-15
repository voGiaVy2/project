# -*- coding: utf-8 -*-
import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Pt

doc = docx.Document(r'd:\doan\baocao_GayThongMinh_backup.docx')

# Tạo paragraph thử nghiệm
p1 = doc.add_paragraph(style='toc 1')
tabs1 = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
p1._element.get_or_add_pPr().append(tabs1)
r1 = p1.add_run("DANH MỤC HÌNH ẢNH")
r1.bold = True
p1.add_run("\t")
p1.add_run("vi")

p2 = doc.add_paragraph(style='toc 1')
tabs2 = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="1440"/><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
p2._element.get_or_add_pPr().append(tabs2)
r2_1 = p2.add_run("CHƯƠNG 1")
r2_1.bold = True
p2.add_run("\t")
r2_2 = p2.add_run("TỔNG QUAN VỀ ĐỀ TÀI")
r2_2.bold = True
p2.add_run("\t")
p2.add_run("5")

p3 = doc.add_paragraph(style='toc 2')
tabs3 = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="960"/><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
p3._element.get_or_add_pPr().append(tabs3)
p3.add_run("1.1")
p3.add_run("\t")
p3.add_run("Thực trạng già hóa dân số và nguy cơ té ngã ở người cao tuổi")
p3.add_run("\t")
p3.add_run("5")

p4 = doc.add_paragraph(style='table of figures')
tabs4 = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="1200"/><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
p4._element.get_or_add_pPr().append(tabs4)
p4.add_run("Hình 1.1")
p4.add_run("\t")
p4.add_run("Các phương pháp phát hiện và cảnh báo té ngã hiện nay")
p4.add_run("\t")
p4.add_run("13")

from lxml import etree
with open(r'd:\doan\_tools\test_toc_out.txt', 'w', encoding='utf-8') as f:
    f.write("=== P1 XML ===\n")
    f.write(etree.tostring(p1._element, encoding='unicode', pretty_print=True) + "\n\n")
    f.write("=== P2 XML ===\n")
    f.write(etree.tostring(p2._element, encoding='unicode', pretty_print=True) + "\n\n")
    f.write("=== P3 XML ===\n")
    f.write(etree.tostring(p3._element, encoding='unicode', pretty_print=True) + "\n\n")
    f.write("=== P4 XML ===\n")
    f.write(etree.tostring(p4._element, encoding='unicode', pretty_print=True) + "\n\n")
print("Done writing test_toc_out.txt")

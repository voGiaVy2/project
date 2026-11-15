# -*- coding: utf-8 -*-
"""Kiểm tra việc thêm heading, content, bảng và hình ảnh vào docx bằng python-docx."""
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

doc = docx.Document('baocao_GayThongMinh.docx')
print('Loaded styles:', len(doc.styles))
# Check if styles exist
for s in ['Heading 1', 'Heading 2', 'Heading 3', 'Heading 4', 'Heading 1N', 'Content', 'Caption']:
    try:
        st = doc.styles[s]
        print('Style exists:', s)
    except KeyError:
        print('Style NOT found:', s)

# -*- coding: utf-8 -*-
"""Script tạo toàn bộ nội dung báo cáo Khóa luận tốt nghiệp Gậy Thông Minh chuẩn mẫu IUH."""
import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

FIG_DIR = r'd:\doan\_tools\fig'
DOCX_IN = r'd:\doan\baocao_GayThongMinh.docx'
DOCX_OUT = r'd:\doan\baocao_GayThongMinh.docx'

print("Starting report builder...")

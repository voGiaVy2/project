# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls
import os

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def add_p(doc, text, style='Content', bold_prefix=None, align=None):
    if style not in doc.styles:
        s = doc.styles.add_style(style, docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
        base = doc.styles['Content'] if 'Content' in doc.styles else doc.styles['Normal']
        s.base_style = base
        s.font.name = 'Times New Roman'
        s.font.size = Pt(13)
        if 'Bold' in style:
            s.font.bold = True
            s.paragraph_format.space_before = Pt(6)
            s.paragraph_format.space_after = Pt(6)
            s.paragraph_format.line_spacing = 1.2
    p = doc.add_paragraph(style=style)
    if align:
        p.alignment = align
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        r_bold.bold = True
    p.add_run(text)
    return p

def add_heading1N(doc, text):
    p = doc.add_paragraph(text, style='Heading 1N')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p

def add_heading1_no_num(doc, text):
    # Thêm page break trước mỗi phần không đánh số (MỤC LỤC, MỞ ĐẦU, KẾT LUẬN, PHỤ LỤC)
    p_br = doc.add_paragraph()
    r = p_br.add_run()
    r.add_break(docx.enum.text.WD_BREAK.PAGE)
    return add_heading1N(doc, text)

def add_heading1(doc, text):
    # Thêm page break trước mỗi chương
    p_br = doc.add_paragraph()
    r = p_br.add_run()
    r.add_break(docx.enum.text.WD_BREAK.PAGE)
    p = doc.add_paragraph('\t\t' + text, style='Heading 1')
    return p

def add_heading2(doc, text):
    return doc.add_paragraph(text, style='Heading 2')

def add_heading3(doc, text):
    return doc.add_paragraph(text, style='Heading 3')

def add_heading4(doc, text):
    return doc.add_paragraph(text, style='Heading 4')

def add_toc_line(doc, level, label, title, page_str):
    style_name = 'toc 1' if level == 1 else ('toc 2' if level == 2 else 'toc 3')
    p = doc.add_paragraph(style=style_name)
    pPr = p._element.get_or_add_pPr()
    
    if level == 1:
        if label:
            tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="1440"/><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
        else:
            tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
    elif level == 2:
        tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="960"/><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
    else:
        tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="1440"/><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
    pPr.append(tabs)
    
    if level == 1:
        if label:
            r_lbl = p.add_run(label)
            r_lbl.bold = True
            r_lbl.font.size = Pt(13)
            r_lbl.font.name = 'Times New Roman'
            p.add_run("\t")
            r_ttl = p.add_run(title)
            r_ttl.bold = True
            r_ttl.font.size = Pt(13)
            r_ttl.font.name = 'Times New Roman'
        else:
            r_ttl = p.add_run(title)
            r_ttl.bold = True
            r_ttl.font.size = Pt(13)
            r_ttl.font.name = 'Times New Roman'
        
        p.add_run("\t")
        r_pg = p.add_run(str(page_str))
        r_pg.bold = True
        r_pg.font.size = Pt(13)
        r_pg.font.name = 'Times New Roman'
    else:
        if label:
            r_lbl = p.add_run(label)
            r_lbl.font.size = Pt(13)
            r_lbl.font.name = 'Times New Roman'
            p.add_run("\t")
            r_ttl = p.add_run(title)
            r_ttl.font.size = Pt(13)
            r_ttl.font.name = 'Times New Roman'
        else:
            r_ttl = p.add_run(title)
            r_ttl.font.size = Pt(13)
            r_ttl.font.name = 'Times New Roman'
        
        p.add_run("\t")
        r_pg = p.add_run(str(page_str))
        r_pg.font.size = Pt(13)
        r_pg.font.name = 'Times New Roman'
    
    return p

def add_tof_line(doc, label, title, page_str):
    p = doc.add_paragraph(style='table of figures')
    pPr = p._element.get_or_add_pPr()
    tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="left" w:pos="1200"/><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>')
    pPr.append(tabs)
    
    r_lbl = p.add_run(label)
    r_lbl.font.size = Pt(13)
    r_lbl.font.name = 'Times New Roman'
    p.add_run("\t")
    r_ttl = p.add_run(title)
    r_ttl.font.size = Pt(13)
    r_ttl.font.name = 'Times New Roman'
    
    p.add_run("\t")
    r_pg = p.add_run(str(page_str))
    r_pg.font.size = Pt(13)
    r_pg.font.name = 'Times New Roman'
    return p

def add_fig(doc, img_path, caption_text, width=Inches(6.15)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph(style='Content')
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.keep_with_next = True
        r = p_img.add_run()
        r.add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph(caption_text, style='Caption')
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return p_img, p_cap
    else:
        print(f"Warning: Figure not found: {img_path}")
        return None, None

def add_table_data(doc, headers, rows, col_widths, caption_text):
    p_cap = doc.add_paragraph(caption_text, style='Caption')
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap.paragraph_format.keep_with_next = True
    
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    
    # Header
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        hdr_cells[i].paragraphs[0].runs[0].font.size = Pt(11)
        set_cell_margins(hdr_cells[i], top=120, bottom=120)
        set_cell_shading(hdr_cells[i], 'EBF1F5')
        hdr_cells[i].vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    # Data
    for r_idx, row in enumerate(rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_col = 'FFFFFF' if r_idx % 2 == 0 else 'F9FBFC'
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = str(val)
            row_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(10.5)
            # Center if short number or percentage
            if len(str(val)) <= 8 or '%' in str(val) or str(val).isdigit():
                row_cells[c_idx].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                row_cells[c_idx].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
            set_cell_margins(row_cells[c_idx], top=80, bottom=80)
            set_cell_shading(row_cells[c_idx], bg_col)
            row_cells[c_idx].vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    # Set column widths
    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    # Thêm khoảng trống sau bảng
    doc.add_paragraph(style='Normal')
    return table

def add_tbl(doc, headers, rows, title=""):
    num_cols = len(headers)
    total_w = 6.4 # inches
    col_w = [Inches(total_w / num_cols)] * num_cols
    return add_table_data(doc, headers, rows, col_w, title)

def add_code(doc, code_str, title=""):
    if title:
        p_t = doc.add_paragraph(title, style='Caption')
        p_t.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_t.paragraph_format.keep_with_next = True
    
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_shading(cell, 'F4F6F8')
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    # Border
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'  <w:left w:val="single" w:sz="18" w:space="0" w:color="0288D1"/>'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>'
        f'</w:tcBorders>'
    )
    cell._tc.get_or_add_tcPr().append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_str)
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(36, 41, 47)
    
    doc.add_paragraph(style='Normal')

print("Docx helpers defined successfully.")

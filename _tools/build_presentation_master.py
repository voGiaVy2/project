# -*- coding: utf-8 -*-
"""
Master Presentation Builder for Smart Cane Thesis Report - Polished Edition
Khoa Luan Tot Nghiep: Thiet Ke Gay Thong Minh Ho Tro Nguoi Cao Tuoi (ESP32 - IoT)
Sinh vien: Vo Gia Vy (22642971) & Dao Huynh Phong Vu (22679141)
GVHD: ThS. Vu Tuan Anh - IUH 2026
"""

import os
import sys
import shutil
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation('mau.pptx')
    slide_width = prs.slide_width.inches
    slide_height = prs.slide_height.inches
    print(f"Loaded template. Size: {slide_width} x {slide_height} in")

    # Clear old slides
    for i in range(len(prs.slides) - 1, -1, -1):
        rId = prs.slides._sldIdLst[i].rId
        prs.part.drop_rel(rId)
        del prs.slides._sldIdLst[i]

    blank_layout = prs.slide_layouts[3] # BLANK layout

    # Colors
    C_NAVY_DARK = RGBColor(11, 25, 44)       # #0B192C - Deep Midnight Navy
    C_NAVY_CARD = RGBColor(19, 38, 64)       # #132640 - Dark Card
    C_PRIMARY_BLUE = RGBColor(14, 116, 144)  # #0E7490 - Deep Cyan / Primary Blue
    C_CYAN = RGBColor(6, 182, 212)           # #06B6D4 - Vivid Cyan
    C_RED = RGBColor(220, 38, 38)            # #DC2626 - Alert Red
    C_GREEN = RGBColor(22, 163, 74)          # #16A34A - Success Green
    C_AMBER = RGBColor(217, 119, 6)          # #D97706 - Amber
    C_BG_LIGHT = RGBColor(248, 250, 252)     # #F8FAFC - Light Slate Canvas
    C_CARD_LIGHT = RGBColor(255, 255, 255)   # #FFFFFF - White
    C_CARD_ACCENT = RGBColor(241, 245, 249)  # #F1F5F9 - Subtle Gray
    C_BORDER_LIGHT = RGBColor(226, 232, 240) # #E2E8F0 - Light Border
    C_TEXT_DARK = RGBColor(15, 23, 42)       # #0F172A - Slate 900
    C_TEXT_MUTED = RGBColor(71, 85, 105)     # #475569 - Slate 600
    C_TEXT_LIGHT = RGBColor(241, 245, 249)   # #F1F5F9 - Light Slate
    C_WHITE = RGBColor(255, 255, 255)

    FONT_HEADING = "Montserrat"
    FONT_BODY = "Segoe UI"

    def set_slide_bg(slide, rgb_color):
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = rgb_color

    def add_header(slide, breadcrumb, title, is_dark=False):
        tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.25), Inches(8.8), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p0 = tf.paragraphs[0]
        p0.text = breadcrumb.upper()
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(9.5)
        p0.font.bold = True
        p0.font.color.rgb = C_CYAN if is_dark else C_RED
        p0.space_after = Pt(2)
        
        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(16.5)
        p1.font.bold = True
        p1.font.color.rgb = C_WHITE if is_dark else C_NAVY_DARK
        
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.15), Inches(8.8), Inches(0.025))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(30, 58, 95) if is_dark else RGBColor(226, 232, 240)
        line.line.color.rgb = RGBColor(30, 58, 95) if is_dark else RGBColor(226, 232, 240)

    def add_footer(slide, current_page, total_pages=22, is_dark=False):
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(5.25), Inches(8.8), Inches(0.015))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(30, 58, 95) if is_dark else RGBColor(226, 232, 240)
        line.line.color.rgb = RGBColor(30, 58, 95) if is_dark else RGBColor(226, 232, 240)
        
        tb = slide.shapes.add_textbox(Inches(0.6), Inches(5.3), Inches(8.8), Inches(0.25))
        tf = tb.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.font.name = FONT_BODY
        p.font.size = Pt(8)
        p.font.color.rgb = RGBColor(148, 163, 184)
        
        left_text = "Khoá luận tốt nghiệp: Thiết Kế Gậy Thông Minh Hỗ Trợ Người Cao Tuổi (ESP32 & IoT)"
        page_text = f"Trang {current_page} / {total_pages}"
        p.text = f"{left_text}                                                                                              {page_text}"

    def create_card(slide, left, top, width, height, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
            
        if top_bar_color:
            top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(0.05))
            top_bar.fill.solid()
            top_bar.fill.fore_color.rgb = top_bar_color
            top_bar.line.fill.background()
        return card

    def add_badge(slide, left, top, width, height, text, bg_color, text_color=C_WHITE, font_size=8.5):
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        badge.fill.solid()
        badge.fill.fore_color.rgb = bg_color
        badge.line.fill.background()
        tf = badge.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = FONT_HEADING
        p.font.size = Pt(font_size)
        p.font.bold = True
        p.font.color.rgb = text_color
        p.alignment = PP_ALIGN.CENTER
        return badge

    def add_image_scaled(slide, img_path, left, top, max_w, max_h, border_color=None):
        if not os.path.exists(img_path):
            print(f"Warning: Image missing: {img_path}")
            return None
        try:
            with Image.open(img_path) as im:
                orig_w, orig_h = im.size
            aspect = orig_w / orig_h
            target_aspect = max_w / max_h
            if aspect > target_aspect:
                final_w = max_w
                final_h = max_w / aspect
            else:
                final_h = max_h
                final_w = max_h * aspect
            
            final_left = left + (max_w - final_w) / 2
            final_top = top + (max_h - final_h) / 2
            
            if border_color:
                bg_frame = slide.shapes.add_shape(
                    MSO_SHAPE.RECTANGLE,
                    Inches(final_left - 0.02), Inches(final_top - 0.02),
                    Inches(final_w + 0.04), Inches(final_h + 0.04)
                )
                bg_frame.fill.solid()
                bg_frame.fill.fore_color.rgb = RGBColor(255, 255, 255)
                bg_frame.line.color.rgb = border_color
                bg_frame.line.width = Pt(1)
                
            pic = slide.shapes.add_picture(img_path, Inches(final_left), Inches(final_top), Inches(final_w), Inches(final_h))
            return pic
        except Exception as e:
            print(f"Error adding image {img_path}: {e}")
            return None

    # =========================================================================
    # SLIDE 1: COVER SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, C_NAVY_DARK)

    logo_left = "_tools/mau_extracted_images/slide1_pic9_Picture 6.png"
    logo_right = "_tools/mau_extracted_images/slide1_pic10_Picture 8.png"
    if os.path.exists(logo_left):
        add_image_scaled(s1, logo_left, 0.6, 0.35, 1.8, 0.7)
    if os.path.exists(logo_right):
        add_image_scaled(s1, logo_right, 8.4, 0.35, 1.0, 0.7)

    tb_uni = s1.shapes.add_textbox(Inches(2.5), Inches(0.35), Inches(5.8), Inches(0.6))
    tf_uni = tb_uni.text_frame
    tf_uni.word_wrap = True
    p = tf_uni.paragraphs[0]
    p.text = "TRƯỜNG ĐẠI HỌC CÔNG NGHIỆP TP. HỒ CHÍ MINH"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = RGBColor(148, 163, 184)
    p.alignment = PP_ALIGN.CENTER
    p2 = tf_uni.add_paragraph()
    p2.text = "KHOA CÔNG NGHỆ ĐIỆN TỬ - CHUYÊN NGÀNH KỸ THUẬT MÁY TÍNH"
    p2.font.name = FONT_HEADING
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = C_CYAN
    p2.alignment = PP_ALIGN.CENTER

    add_badge(s1, 3.4, 1.25, 3.2, 0.32, "BÁO CÁO TIẾN ĐỘ KHÓA LUẬN TỐT NGHIỆP", C_RED, C_WHITE, 9.5)

    card_title = create_card(s1, 0.6, 1.7, 8.8, 1.5, bg_color=C_NAVY_CARD, border_color=RGBColor(30, 58, 95), top_bar_color=C_CYAN)
    tb_title = s1.shapes.add_textbox(Inches(0.8), Inches(1.85), Inches(8.4), Inches(1.2))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p = tf_title.paragraphs[0]
    p.text = "ĐỀ TÀI: THIẾT KẾ GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI"
    p.font.name = FONT_HEADING
    p.font.size = Pt(16.5)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(4)

    p_sub = tf_title.add_paragraph()
    p_sub.text = "SỬ DỤNG ESP32, TÍCH HỢP CẢM BIẾN PHÁT HIỆN NGÃ, ĐỊNH VỊ GPS, CẢNH BÁO ÂM THANH\nVÀ TỰ ĐỘNG GỬI THÔNG BÁO GIÁM SÁT ĐẾN NGƯỜI THÂN QUA ỨNG DỤNG TRÊN ĐIỆN THOẠI"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = C_WHITE
    p_sub.alignment = PP_ALIGN.CENTER

    create_card(s1, 0.6, 3.4, 4.25, 1.5, bg_color=C_NAVY_CARD, border_color=RGBColor(30, 58, 95), top_bar_color=C_PRIMARY_BLUE)
    tb_gv = s1.shapes.add_textbox(Inches(0.8), Inches(3.55), Inches(3.85), Inches(1.2))
    tf_gv = tb_gv.text_frame
    tf_gv.word_wrap = True
    p = tf_gv.paragraphs[0]
    p.text = "GIẢNG VIÊN HƯỚNG DẪN:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(4)
    p = tf_gv.add_paragraph()
    p.text = "ThS. VŨ TUẤN ANH"
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p = tf_gv.add_paragraph()
    p.text = "Khoa Công Nghệ Điện Tử - ĐH Công nghiệp TP.HCM"
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.color.rgb = RGBColor(148, 163, 184)

    create_card(s1, 5.15, 3.4, 4.25, 1.5, bg_color=C_NAVY_CARD, border_color=RGBColor(30, 58, 95), top_bar_color=C_GREEN)
    tb_sv = s1.shapes.add_textbox(Inches(5.35), Inches(3.55), Inches(3.85), Inches(1.2))
    tf_sv = tb_sv.text_frame
    tf_sv.word_wrap = True
    p = tf_sv.paragraphs[0]
    p.text = "SINH VIÊN THỰC HIỆN:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(3)
    p = tf_sv.add_paragraph()
    p.text = "1. VÕ GIA VỸ             - MSSV: 22642971"
    p.font.name = FONT_BODY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p = tf_sv.add_paragraph()
    p.text = "2. ĐÀO HUỲNH PHONG VŨ - MSSV: 22679141"
    p.font.name = FONT_BODY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p = tf_sv.add_paragraph()
    p.text = "Lớp: DHDTMT18A  |  Mã ngành: 7480108 (Năm 2026)"
    p.font.name = FONT_BODY
    p.font.size = Pt(9)
    p.font.color.rgb = RGBColor(148, 163, 184)

    add_footer(s1, 1, 22, is_dark=True)
    print("Slide 1 generated.")

    # =========================================================================
    # SLIDE 2: AGENDA
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2, C_BG_LIGHT)
    add_header(s2, "MỤC LỤC BÁO CÁO", "NỘI DUNG TRÌNH BÀY TỔNG QUAN")

    agenda_items = [
        ("01", "ĐẶT VẤN ĐỀ & TÍNH CẤP THIẾT", "Thực trạng già hóa dân số, mối đe dọa té ngã, khảo sát 4 nhóm công nghệ hiện nay và lý do chọn gậy thông minh.", C_RED),
        ("02", "MỤC TIÊU & PHẠM VI NGHIÊN CỨU", "Mục tiêu tổng quát và 4 mục tiêu cụ thể: Phần cứng, Thuật toán nhúng, Truyền thông IoT và Ứng dụng di động.", C_PRIMARY_BLUE),
        ("03", "PHƯƠNG PHÁP THỰC HIỆN & THIẾT KẾ", "Kiến trúc hệ thống 4 khối, sơ đồ nguyên lý phần cứng ESP32-S3, thiết kế cơ khí 3D, giải thuật SVM và Foreground Service.", C_CYAN),
        ("04", "KẾT QUẢ THỰC NGHIỆM ĐẠT ĐƯỢC", "Thực nghiệm 400 lượt té ngã (Độ nhạy 95%), kiểm thử cự ly vật cản (sai số <2.6%), đo độ trễ SOS (1.31s) và thời lượng pin (>21h).", C_GREEN),
        ("05", "ĐÁNH GIÁ TIẾN ĐỘ & KHẢ NĂNG MỞ RỘNG", "Checklist hoàn thành 100% các hạng mục đề ra, nhận diện hạn chế tồn tại và định hướng phát triển TinyML / AIoT.", C_AMBER),
        ("06", "KẾT LUẬN & THÔNG ĐIỆP ĐỀ TÀI", "Khẳng định giá trị kỹ thuật, giá trị thực tiễn và tính nhân văn của sản phẩm; lời cảm ơn và tiếp nhận phản biện từ Hội đồng.", C_NAVY_DARK)
    ]

    for idx, (num, title, desc, color) in enumerate(agenda_items):
        col = idx % 3
        row = idx // 3
        left = 0.6 + col * 2.98
        top = 1.45 + row * 1.82
        card = create_card(s2, left, top, 2.85, 1.68, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=color)
        
        add_badge(s2, left + 0.15, top + 0.15, 0.45, 0.32, num, color, C_WHITE, 11)
        
        tb = s2.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.52), Inches(2.55), Inches(1.05))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = C_NAVY_DARK
        p.space_after = Pt(3)
        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.name = FONT_BODY
        p_desc.font.size = Pt(8.5)
        p_desc.font.color.rgb = C_TEXT_MUTED

    add_footer(s2, 2, 22)
    print("Slide 2 generated.")

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3, C_BG_LIGHT)
    add_header(s3, "PHẦN 1: TỔNG QUAN ĐỀ TÀI", "THỰC TRẠNG GIÀ HÓA DÂN SỐ & NGUY CƠ TÉ NGÃ Ở NGƯỜI CAO TUỔI")

    cards_p1 = [
        ("BỐI CẢNH DÂN SỐ BÁO ĐỘNG", [
            ("Già hóa thần tốc:", "Việt Nam chính thức bước vào già hóa từ 2011, dự báo 2036 sẽ thành 'dân số già' chỉ trong 25 năm (nhanh hơn nhiều so với Pháp 115 năm, Mỹ 69 năm)."),
            ("Người già sống neo đơn:", "Khoảng 28% - 32% hộ gia đình người cao tuổi chỉ có 1 hoặc 2 vợ chồng già nương tựa nhau do xu thế gia đình hạt nhân hóa."),
            ("Gánh nặng bệnh mạn tính:", "Trung bình 1 người già mang 3-4 bệnh mạn tính (thoái hóa khớp, loãng xương, tăng huyết áp, suy giảm thị lực).")
        ], C_PRIMARY_BLUE),
        ("HIỂM HỌA TÉ NGÃ (FALLS)", [
            ("Nguyên nhân tử vong #2:", "Theo WHO, té ngã là nguyên nhân tử vong do chấn thương không chủ ý đứng thứ 2 thế giới (sau TNGT), với 37.3 triệu ca cần chăm sóc y tế mỗi năm."),
            ("Tỷ lệ ngã rất cao:", "28% - 35% người trên 65 tuổi bị ngã ít nhất 1 lần/năm; người từng ngã có nguy cơ tái ngã cao gấp 2-3 lần trong 6 tháng."),
            ("Hội chứng sợ ngã (FoF):", "Hơn 50% người già sau ngã rơi vào hoang mang, tự hạn chế vận động, dẫn đến teo cơ (sarcopenia) và cứng khớp nặng hơn.")
        ], C_RED),
        ("THẢM HỌA 'LONG-LIE' & CÂY GẬY", [
            ("Nguy hiểm của Long-lie:", "Nạn nhân nằm bất động trên sàn lạnh >1 giờ sau ngã dẫn đến hạ thân nhiệt, tiêu cơ vân, suy thận cấp; 50% tử vong trong vòng 6 tháng!"),
            ("Chi phí y tế khổng lồ:", "Chi phí phẫu thuật thay khớp háng, nẹp vít và phục hồi chức năng sau ngã tiêu tốn hàng chục đến hàng trăm triệu đồng."),
            ("Cây gậy truyền thống thụ động:", "Là vật bất ly thân của người già nhưng hoàn toàn thụ động – khi tai nạn xảy ra, gậy không thể tự phát chuông báo hay gửi tin cầu cứu!")
        ], C_AMBER)
    ]

    for idx, (title, items, color) in enumerate(cards_p1):
        left = 0.6 + idx * 2.98
        top = 1.35
        card = create_card(s3, left, top, 2.85, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=color)
        
        tb = s3.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.15), Inches(2.55), Inches(3.45))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(8)
        
        for bold_txt, norm_txt in items:
            p_item = tf.add_paragraph()
            p_item.space_after = Pt(6)
            run1 = p_item.add_run()
            run1.text = "• " + bold_txt + " "
            run1.font.name = FONT_BODY
            run1.font.size = Pt(8.8)
            run1.font.bold = True
            run1.font.color.rgb = C_TEXT_DARK
            
            run2 = p_item.add_run()
            run2.text = norm_txt
            run2.font.name = FONT_BODY
            run2.font.size = Pt(8.8)
            run2.font.color.rgb = C_TEXT_MUTED

    add_footer(s3, 3, 22)
    print("Slide 3 generated.")

    # =========================================================================
    # SLIDE 4: EXISTING SOLUTIONS COMPARISON
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4, C_BG_LIGHT)
    add_header(s4, "PHẦN 1: TỔNG QUAN ĐỀ TÀI", "KHẢO SÁT & SO SÁNH CÁC CÔNG NGHỆ GIÁM SÁT TÉ NGÃ HIỆN NAY")

    create_card(s4, 0.6, 1.35, 3.8, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    add_image_scaled(s4, "_tools/report_media/image2.png", 0.7, 1.5, 3.6, 3.2)
    tb_cap = s4.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(3.6), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 1.1: Phân loại 5 công nghệ phát hiện té ngã hiện nay"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s4, 4.6, 1.35, 4.8, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_RED)
    tb_rt = s4.shapes.add_textbox(Inches(4.8), Inches(1.5), Inches(4.4), Inches(3.45))
    tf_rt = tb_rt.text_frame
    tf_rt.word_wrap = True
    tf_rt.margin_left = tf_rt.margin_top = tf_rt.margin_right = tf_rt.margin_bottom = 0

    p = tf_rt.paragraphs[0]
    p.text = "NHƯỢC ĐIỂM CỦA CÁC GIẢI PHÁP TRÊN THỊ TRƯỜNG:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_RED
    p.space_after = Pt(6)

    methods = [
        ("Thiết bị đeo (Smartwatch / Đai bụng):", "Người già rất hay quên đeo vào buổi sáng; tháo ra khi đi tắm hoặc đi ngủ (nơi nguy cơ trượt ngã cao nhất); pin chỉ dùng được 1-2 ngày."),
        ("Thị giác máy tính (Camera AI):", "Xâm phạm nghiêm trọng quyền riêng tư (không thể lắp trong nhà tắm, phòng ngủ); bị che khuất bởi rèm cửa, góc khuất bàn ghế, bóng tối."),
        ("Phân tích âm thanh (Acoustic Sensor):", "Dễ báo động giả do tiếng va chạm đồ đạc sinh hoạt hằng ngày; hoàn toàn bỏ sót khi người già ngã trượt từ từ hoặc ngất lịm."),
        ("Radar sóng milimet (mmWave Radar):", "Chi phí rất đắt (hàng triệu đồng/phòng); bị giới hạn góc quét trong 1 phòng cố định, không thể theo dõi khi người già ra ngoài đường.")
    ]

    for title_m, desc_m in methods:
        p_m = tf_rt.add_paragraph()
        p_m.space_after = Pt(4)
        r1 = p_m.add_run()
        r1.text = "✖ " + title_m + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.5)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_m.add_run()
        r2.text = desc_m
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = C_TEXT_MUTED

    p_sol = tf_rt.add_paragraph()
    p_sol.space_after = Pt(2)
    r1 = p_sol.add_run()
    r1.text = "✔ GIẢI PHÁP ĐỀ TÀI - GẬY THÔNG MINH (SMART CANE):\n"
    r1.font.name = FONT_HEADING
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = C_GREEN
    r2 = p_sol.add_run()
    r2.text = "Vật bất ly thân khi đứng dậy bước đi; 100% bảo vệ quyền riêng tư; tích hợp 'đôi mắt thứ 2' rung báo vật cản và còi hú SOS tại chỗ; giá thành chế tạo chỉ khoảng ~500.000 VNĐ!"
    r2.font.name = FONT_BODY
    r2.font.size = Pt(8.5)
    r2.font.color.rgb = C_TEXT_DARK

    add_footer(s4, 4, 22)
    print("Slide 4 generated.")

    # =========================================================================
    # SLIDE 5: OBJECTIVES OF THE THESIS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5, C_BG_LIGHT)
    add_header(s5, "PHẦN 2: MỤC TIÊU & PHẠM VI", "MỤC TIÊU TỔNG QUÁT VÀ 4 MỤC TIÊU KỸ THUẬT CỤ THỂ")

    card_gen = create_card(s5, 0.6, 1.35, 8.8, 0.85, bg_color=C_CARD_LIGHT, border_color=C_PRIMARY_BLUE, top_bar_color=C_PRIMARY_BLUE)
    tb_gen = s5.shapes.add_textbox(Inches(0.8), Inches(1.42), Inches(8.4), Inches(0.72))
    tf_gen = tb_gen.text_frame
    tf_gen.word_wrap = True
    tf_gen.margin_left = tf_gen.margin_top = tf_gen.margin_right = tf_gen.margin_bottom = 0
    p = tf_gen.paragraphs[0]
    p.text = "MỤC TIÊU TỔNG QUÁT CỦA ĐỀ TÀI:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_BLUE
    p.space_after = Pt(2)
    p = tf_gen.add_paragraph()
    p.text = "Nghiên cứu, thiết kế, chế tạo và thử nghiệm thành công hệ thống Gậy Thông Minh hỗ trợ người cao tuổi hoàn chỉnh; kết hợp hài hòa giữa phần cứng nhúng IoT (ESP32-S3) và ứng dụng di động Flutter đa nền tảng kết nối đám mây Firebase."
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_TEXT_DARK

    specs = [
        ("1. PHẦN CỨNG & CƠ KHÍ THỰC THI", [
            "Chế tạo thân gậy đạt độ bền cơ học cao, tay cầm công thái học in 3D.",
            "Tích hợp vi điều khiển lõi kép ESP32-S3, cảm biến MPU6050, HC-SR04.",
            "Trang bị còi hú 85dB, motor rung MOSFET AOD4184 và khối pin sạc 18650 Type-C."
        ], C_PRIMARY_BLUE),
        ("2. THUẬT TOÁN NHÚNG REAL-TIME", [
            "Thuật toán phát hiện té ngã dựa trên ngưỡng gia tốc tổng hợp SVM (>25 m/s²).",
            "Bộ lọc chống báo động nhầm khi đi bộ, gõ gậy hoặc vấp nhẹ.",
            "Đo khoảng cách siêu âm và kích rung tay cầm 3 - 80 cm; fallback micros() chống treo."
        ], C_RED),
        ("3. MẠNG TRUYỀN THÔNG IOT & BLE", [
            "Xây dựng kênh truyền BLE 5.0 GATT Client-Server tiêu thụ năng lượng cực thấp.",
            "Đồng bộ hai chiều thời gian thực với độ trễ < 1s qua Firebase Realtime Database.",
            "Cơ chế theo dõi trạng thái mạng (Presence System) cảnh báo ngay khi mất kết nối."
        ], C_GREEN),
        ("4. ỨNG DỤNG DI ĐỘNG & CLOUD", [
            "Phát triển ứng dụng Flutter đa nền tảng phân quyền rõ ràng 2 vai trò.",
            "Khởi tạo Dịch vụ chạy ngầm liên tục (Foreground Service) 24/7 trên Android.",
            "Đồng hồ đếm ngược SOS 15s và kênh cứu hộ dự phòng SMS ngầm khi mất Internet."
        ], C_AMBER)
    ]

    for idx, (title_sp, bullets, col_c) in enumerate(specs):
        col = idx % 2
        row = idx // 2
        left = 0.6 + col * 4.5
        top = 2.35 + row * 1.4
        create_card(s5, left, top, 4.3, 1.3, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=col_c)
        
        tb = s5.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.12), Inches(4.0), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_sp
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = col_c
        p.space_after = Pt(2)
        
        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = "• " + b
            p_b.font.name = FONT_BODY
            p_b.font.size = Pt(8.2)
            p_b.font.color.rgb = C_TEXT_MUTED
            p_b.space_after = Pt(1)

    add_footer(s5, 5, 22)
    print("Slide 5 generated.")

    # =========================================================================
    # SLIDE 6: SCOPE & SIGNIFICANCE
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6, C_BG_LIGHT)
    add_header(s6, "PHẦN 2: MỤC TIÊU & PHẠM VI", "ĐỐI TƯỢNG, PHẠM VI NGHIÊN CỨU & Ý NGHĨA THỰC TIỄN")

    cards_scope = [
        ("ĐỐI TƯỢNG NGHIÊN CỨU", [
            ("Đối tượng người dùng:", "Người cao tuổi có khả năng tự vận động đi lại nhưng suy giảm thị lực hoặc khả năng giữ thăng bằng thần kinh."),
            ("Công nghệ phần cứng IoT:", "Vi điều khiển SoC ESP32-S3 N16R8, cảm biến quán tính 6-DOF MPU6050, cảm biến siêu âm HC-SR04, BLE 5.0 GATT, pin 18650."),
            ("Nền tảng phần mềm & Cloud:", "Ngôn ngữ Dart, Framework Flutter, Google Firebase Realtime Database, Android Foreground Service.")
        ], C_PRIMARY_BLUE),
        ("PHẠM VI & GIỚI HẠN", [
            ("Dạng hình học gậy:", "Thiết kế nguyên mẫu gậy đơn (Single-point Cane) sử dụng trong môi trường sinh hoạt trong nhà và ngoài trời đô thị."),
            ("Kịch bản sự cố:", "Tập trung nhận diện té ngã đột ngột và phát hiện chướng ngại vật phía trước mặt trong cự ly 3 cm đến 80 cm."),
            ("Hệ điều hành di động:", "Ứng dụng di động được thử nghiệm tối ưu chuyên sâu trên hệ điều hành Android (hỗ trợ từ Android 8.0 đến Android 13).")
        ], C_AMBER),
        ("Ý NGHĨA KHOA HỌC & THỰC TIỄN", [
            ("Đóng góp khoa học:", "Minh chứng giải pháp chia sẻ tài nguyên (Resource Offloading) tối ưu giữa hệ thống nhúng biên (Edge IoT), BLE và Smartphone."),
            ("Khả năng tiếp cận đại trà:", "Chi phí linh kiện chỉ khoảng ~500.000 VNĐ, rẻ hơn hàng chục lần so với thiết bị nhập ngoại, phù hợp kinh tế người Việt."),
            ("Giá trị nhân văn sâu sắc:", "Tạo điểm tựa tinh thần vững chắc cho người già tự tin di chuyển; giúp con cháu yên tâm công tác khi ở xa.")
        ], C_GREEN)
    ]

    for idx, (title, items, color) in enumerate(cards_scope):
        left = 0.6 + idx * 2.98
        top = 1.35
        card = create_card(s6, left, top, 2.85, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=color)
        
        tb = s6.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.15), Inches(2.55), Inches(3.45))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(8)
        
        for bold_txt, norm_txt in items:
            p_item = tf.add_paragraph()
            p_item.space_after = Pt(6)
            run1 = p_item.add_run()
            run1.text = "• " + bold_txt + " "
            run1.font.name = FONT_BODY
            run1.font.size = Pt(8.8)
            run1.font.bold = True
            run1.font.color.rgb = C_TEXT_DARK
            
            run2 = p_item.add_run()
            run2.text = norm_txt
            run2.font.name = FONT_BODY
            run2.font.size = Pt(8.8)
            run2.font.color.rgb = C_TEXT_MUTED

    add_footer(s6, 6, 22)
    print("Slide 6 generated.")

    # =========================================================================
    # SLIDE 7: SYSTEM ARCHITECTURE
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7, C_BG_LIGHT)
    add_header(s7, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "KIẾN TRÚC HỆ THỐNG 4 KHỐI CHỨC NĂNG (RESOURCE OFFLOADING)")

    create_card(s7, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    add_image_scaled(s7, "_tools/report_media/image16.png", 0.7, 1.5, 4.1, 3.2)
    tb_cap = s7.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 3.1: Sơ đồ khối chức năng hoàn chỉnh của toàn bộ hệ thống"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s7, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_CYAN)
    tb_nodes = s7.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_nodes = tb_nodes.text_frame
    tf_nodes.word_wrap = True
    tf_nodes.margin_left = tf_nodes.margin_top = tf_nodes.margin_right = tf_nodes.margin_bottom = 0

    p = tf_nodes.paragraphs[0]
    p.text = "PHÂN TÍCH NHIỆM VỤ 4 KHỐI CỐT LÕI:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_BLUE
    p.space_after = Pt(4)

    nodes_info = [
        ("Khối Gậy Thông Minh (Hardware Node):", "Thu thập quán tính MPU6050, siêu âm HC-SR04, vi điều khiển ESP32-S3 xử lý biên, còi hú 2000Hz, motor rung tay cầm, phát sóng BLE GATT Server."),
        ("Khối Smartphone Người Già (Gateway):", "Dịch vụ ngầm 24/7 tự động kết nối BLE, tận dụng chip Fused GPS và 4G có sẵn, kích hoạt đếm ngược SOS 15s chống báo nhầm, gửi SMS ngầm dự phòng."),
        ("Khối Đám Mây Firebase (Cloud Backend):", "Realtime Database đồng bộ 2 chiều tức thì (<1s), Firebase Auth bảo mật, hệ thống Presence System (.info/connected) giám sát mất mạng."),
        ("Khối Smartphone Giám Hộ (Client Node):", "Dashboard bản đồ OpenStreetMap thời gian thực, còi báo động thức tỉnh (Full-screen Siren) âm lượng tối đa, nút mở Google Maps dẫn đường 1 chạm.")
    ]

    for title_n, desc_n in nodes_info:
        p_n = tf_nodes.add_paragraph()
        p_n.space_after = Pt(4)
        r1 = p_n.add_run()
        r1.text = "• " + title_n + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.3)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_n.add_run()
        r2.text = desc_n
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.3)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s7, 7, 22)
    print("Slide 7 generated.")

    # =========================================================================
    # SLIDE 8: HARDWARE DESIGN & SCHEMATIC
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8, C_BG_LIGHT)
    add_header(s8, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "SƠ ĐỒ NGUYÊN LÝ KẾT NỐI CHI TIẾT NGOẠI VI ESP32-S3")

    create_card(s8, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    add_image_scaled(s8, "_tools/report_media/image17.png", 0.7, 1.5, 4.1, 3.2)
    tb_cap = s8.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 3.2: Sơ đồ nguyên lý kết nối chi tiết phần cứng trên ESP32-S3"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s8, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_RED)
    tb_hw = s8.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_hw = tb_hw.text_frame
    tf_hw.word_wrap = True
    tf_hw.margin_left = tf_hw.margin_top = tf_hw.margin_right = tf_hw.margin_bottom = 0

    p = tf_hw.paragraphs[0]
    p.text = "ĐẶC TÍNH PHẦN CỨNG & BẢNG ÁNH XẠ CHÂN GPIO (ĐỒNG NHẤT 100%):"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_RED
    p.space_after = Pt(4)

    hw_points = [
        ("Vi điều khiển ESP32-S3 N16R8:", "Xtensa 32-bit LX7 Dual-Core 240 MHz, 512KB SRAM, 16MB Flash, 8MB PSRAM; tích hợp BLE 5.0 phần cứng."),
        ("Cảm biến gia tốc MPU6050 (I2C):", "Chân SDA (GPIO 8), SCL (GPIO 9), trở kéo lên 4.7kΩ; dải đo gia tốc ±8g, con quay hồi chuyển ±2000 dps (khớp 100% config.h)."),
        ("Cảm biến siêu âm HC-SR04 (3.3V):", "Chân TRIG (GPIO 16), ECHO (GPIO 17) có cấu hình INPUT_PULLDOWN chống trôi; xung kích 10µs phát sóng âm 40 kHz."),
        ("Mạch driver MOSFET Motor rung:", "Kích mở cực Gate bằng chân GPIO 6 qua điện trở hạn dòng 100Ω; điều khiển motor rung xúc giác ở tay cầm."),
        ("Còi hú báo động Buzzer 5V:", "Điều khiển qua chân GPIO 5; phát âm tần số cao 2000 Hz, đạt độ ồn 85 dB ở cự ly 1m để báo động cứu hộ xung quanh."),
        ("Đo điện áp Pin ADC & Mở rộng:", "Chân ADC (GPIO 4) đo điện áp cell pin 18650 qua cầu phân áp; chân GPIO 15 dự phòng cho cảm biến hồng ngoại E18-D50NK.")
    ]

    for title_h, desc_h in hw_points:
        p_h = tf_hw.add_paragraph()
        p_h.space_after = Pt(3)
        r1 = p_h.add_run()
        r1.text = "• " + title_h + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.2)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_h.add_run()
        r2.text = desc_h
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.2)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s8, 8, 22)
    print("Slide 8 generated.")

    # =========================================================================
    # SLIDE 9: 3D MECHANICAL DESIGN
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9, C_BG_LIGHT)
    add_header(s9, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "THIẾT KẾ CƠ KHÍ THÂN GẬY & TAY CẦM CÔNG THÁI HỌC (3D)")

    create_card(s9, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    img_3d = "DH/smart_cane_3d_design.jpg"
    if not os.path.exists(img_3d):
        img_3d = "_tools/report_media/image18.jpg"
    add_image_scaled(s9, img_3d, 0.7, 1.5, 4.1, 3.2)
    tb_cap = s9.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 3.3: Bản vẽ thiết kế 3D công thái học thân gậy và bố trí khoang cảm biến"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s9, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_GREEN)
    tb_mech = s9.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_mech = tb_mech.text_frame
    tf_mech.word_wrap = True
    tf_mech.margin_left = tf_mech.margin_top = tf_mech.margin_right = tf_mech.margin_bottom = 0

    p = tf_mech.paragraphs[0]
    p.text = "5 ĐIỂM ĐỘT PHÁ TRONG THIẾT KẾ CƠ KHÍ CỦA GẬY:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(4)

    mech_points = [
        ("1. Tay cầm công thái học (Ergonomic Handle):", "Tạo hình uốn lượn theo rãnh ngón tay, móc gập chữ L giúp phân bổ đều trọng lượng lên xương cẳng tay, giảm áp lực dồn lên khớp cổ tay người già."),
        ("2. Nút bấm khẩn cấp SOS đỏ nổi bật:", "Bố trí ngay đỉnh đầu tay cầm, kích thước lớn vừa vặn ngón cái; giúp người già dễ dàng nhấn giữ khi choáng ngất mà không cần nhìn vào điện thoại."),
        ("3. Khoang cảm biến Sensor Pod in 3D:", "Vỏ nhựa ABS chịu va đập gắn ngay dưới tay cầm; bảo vệ mạch ESP32, pin và MPU6050; mắt siêu âm hướng chúc 15 độ quét cự ly bước chân tiếp theo."),
        ("4. Đèn LED rọi đường ban đêm:", "Tích hợp phần dưới khoang cảm biến, rọi chùm sáng vàng dịu xuống khoảng đất trước chân, hỗ trợ người già thức dậy đi vệ sinh ban đêm an toàn."),
        ("5. Đế cao su chống trượt đa hướng:", "Đệm cao su tổng hợp chịu mài mòn, mặt lốp khía rãnh sâu tăng ma sát bám dính chắc chắn trên nền gạch men ướt và đường dốc.")
    ]

    for title_m, desc_m in mech_points:
        p_m = tf_mech.add_paragraph()
        p_m.space_after = Pt(3)
        r1 = p_m.add_run()
        r1.text = title_m + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.2)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_m.add_run()
        r2.text = desc_m
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.2)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s9, 9, 22)
    print("Slide 9 generated.")

    # =========================================================================
    # SLIDE 10: FALL DETECTION ALGORITHM (SVM)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10, C_BG_LIGHT)
    add_header(s10, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "THUẬT TOÁN NHẬN DIỆN TÉ NGÃ DỰA TRÊN VECTOR GIA TỐC SVM")

    create_card(s10, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_RED)
    add_image_scaled(s10, "_tools/report_media/image8.png", 0.7, 1.5, 4.1, 3.2)
    tb_cap = s10.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 2.5: Dạng sóng gia tốc tổng hợp SVM khi đi bộ, va chạm té ngã và nằm bất động"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s10, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    tb_svm = s10.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_svm = tb_svm.text_frame
    tf_svm.word_wrap = True
    tf_svm.margin_left = tf_svm.margin_top = tf_svm.margin_right = tf_svm.margin_bottom = 0

    p = tf_svm.paragraphs[0]
    p.text = "CƠ SỞ TOÁN HỌC & 3 PHA ĐỘNG HỌC CỦA CÚ NGÃ:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_BLUE
    p.space_after = Pt(4)

    p_f = tf_svm.add_paragraph()
    p_f.space_after = Pt(4)
    r = p_f.add_run()
    r.text = "Công thức SVM Euclid: |a| = √(ax² + ay² + az²)\n"
    r.font.name = FONT_HEADING
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = C_RED
    r_sub = p_f.add_run()
    r_sub.text = "(Đo tổng độ lớn gia tốc đa trục, không phụ thuộc góc cầm gậy trong không gian 3D)"
    r_sub.font.name = FONT_BODY
    r_sub.font.size = Pt(8)
    r_sub.font.color.rgb = C_TEXT_MUTED

    svm_phases = [
        ("1. Pha rơi tự do (Free-fall):", "Người và gậy mất thăng bằng rơi nhanh xuống đất; phản lực triệt tiêu khiến gia tốc tổng hợp |a| giảm mạnh < 0.6g (< 5.9 m/s²) trong 100 - 300 ms."),
        ("2. Pha va chạm tiếp đất (Impact):", "Thân gậy và cơ thể va đập vào bề mặt sàn; hãm tốc đột ngột tạo xung gia tốc vọt lên SVM ≥ 25.0 m/s² (tương đương ≥ 2.55g, đỉnh ngã thực nghiệm đạt 3.25g - 3.5g)."),
        ("3. Pha nằm bất động (Rest / Immobility):", "Sau va chạm, nếu người già bị chấn thương/bất tỉnh, gậy nằm yên trên sàn; |a| ổn định quanh 1.0g (≈ 9.8 m/s²) và góc nghiêng biến thiên Δθ > 60° duy trì > 3 giây.")
    ]

    for title_p, desc_p in svm_phases:
        p_p = tf_svm.add_paragraph()
        p_p.space_after = Pt(3)
        r1 = p_p.add_run()
        r1.text = "• " + title_p + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.2)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_p.add_run()
        r2.text = desc_p
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.2)
        r2.font.color.rgb = C_TEXT_MUTED

    p_resp = tf_svm.add_paragraph()
    r = p_resp.add_run()
    r.text = "➡ Phản ứng tức thì: Kích hoạt còi hú 2000 Hz reo vang 85dB + motor rung 3 giây + phát gói tin Notify BLE gửi giá trị '1' sang điện thoại."
    r.font.name = FONT_BODY
    r.font.size = Pt(8.3)
    r.font.bold = True
    r.font.color.rgb = C_GREEN

    add_footer(s10, 10, 22)
    print("Slide 10 generated.")

    # =========================================================================
    # SLIDE 11: OBSTACLE DETECTION & FIRMWARE FLOWCHART
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11, C_BG_LIGHT)
    add_header(s11, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "THUẬT TOÁN QUÉT VẬT CẢN & LƯU ĐỒ FIRMWARE ESP32-S3")

    create_card(s11, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    add_image_scaled(s11, "_tools/report_media/image19.png", 0.7, 1.5, 4.1, 3.2)
    tb_cap = s11.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 3.4: Lưu đồ thuật toán chính của Firmware điều khiển trên ESP32-S3"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s11, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_AMBER)
    tb_us = s11.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_us = tb_us.text_frame
    tf_us.word_wrap = True
    tf_us.margin_left = tf_us.margin_top = tf_us.margin_right = tf_us.margin_bottom = 0

    p = tf_us.paragraphs[0]
    p.text = "NGUYÊN LÝ ĐO SIÊU ÂM & KỸ THUẬT CHỐNG TREO ESP32:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_AMBER
    p.space_after = Pt(4)

    us_points = [
        ("Nguyên lý Time-of-Flight:", "Vi điều khiển phát xung kích Trig 10µs; cảm biến phát 8 chu kỳ sóng 40 kHz; đo thời gian phản hồi Echo t (µs); tính khoảng cách: d = (t × 0.0343) / 2 (cm)."),
        ("Kỹ thuật ngắt noInterrupts():", "Bao bọc chuỗi xung kích Trig (LOW 5µs -> HIGH 12µs -> LOW) để tránh xung bị gián đoạn bởi các tác vụ đa luồng của FreeRTOS hoặc BLE."),
        ("Cơ chế dự phòng Fallback micros():", "Nếu hàm pulseIn() trả về 0 do xung méo ở mức 3.3V, hàm getDistanceCm() lập tức chuyển sang đo trực tiếp bằng bộ đếm thời gian phần cứng micros() với timeout 35ms, triệt tiêu nguy cơ vi điều khiển bị treo (Watchdog crash)."),
        ("Phản hồi xúc giác trực quan (3 cm - 80 cm):", "Khi phát hiện chướng ngại vật trong dải an toàn 3-80 cm, mạch MOSFET lập tức kích motor rung tay cầm liên tục; khi đường đi thông thoáng (> 80 cm), tự động ngắt rung để tiết kiệm pin.")
    ]

    for title_u, desc_u in us_points:
        p_u = tf_us.add_paragraph()
        p_u.space_after = Pt(3)
        r1 = p_u.add_run()
        r1.text = "• " + title_u + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.2)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_u.add_run()
        r2.text = desc_u
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.2)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s11, 11, 22)
    print("Slide 11 generated.")

    # =========================================================================
    # SLIDE 12: FOREGROUND SERVICE & 15-SECOND SOS RESCUE
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12, C_BG_LIGHT)
    add_header(s12, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "DỊCH VỤ NỀN ANDROID & CƠ CHẾ ĐẾM NGƯỢC CỨU HỘ 15 GIÂY")

    create_card(s12, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    add_image_scaled(s12, "_tools/report_media/image20.png", 0.7, 1.5, 4.1, 3.2)
    tb_cap = s12.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 3.5: Lưu đồ hoạt động của Dịch vụ chạy ngầm trên máy Người Dùng Gậy"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s12, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_RED)
    tb_bg = s12.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_bg = tb_bg.text_frame
    tf_bg.word_wrap = True
    tf_bg.margin_left = tf_bg.margin_top = tf_bg.margin_right = tf_bg.margin_bottom = 0

    p = tf_bg.paragraphs[0]
    p.text = "CƠ CHẾ BẢO VỆ NGẦM 24/7 & CỨU HỘ ĐA TẦNG:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_RED
    p.space_after = Pt(4)

    bg_points = [
        ("Vượt rào cản Doze Mode của Android:", "Dịch vụ flutter_background_service chạy trên Isolate Dart độc lập; duy trì thông báo tiền cảnh thường trực (Foreground Notification) với quyền PRIORITY_HIGH, ngăn hệ điều hành tự ý tắt ứng dụng."),
        ("Tự động kết nối lại BLE (Auto-Reconnect):", "Đọc địa chỉ MAC từ SharedPreferences, chủ động gửi lệnh connect() trực tiếp chu kỳ 5 giây, kết nối lại tức thì ngay khi gậy xuất hiện mà không cần quét tốn pin."),
        ("Luồng định vị GPS Fused Location:", "Lắng nghe luồng tọa độ GPS với ngưỡng dịch chuyển 5 mét; tự động đẩy tọa độ WGS84 mới nhất lên Firebase RTDB."),
        ("Bộ đếm ngược 15 giây chống báo nhầm:", "Khi nhận tín hiệu ngã từ gậy, màn hình điện thoại lập tức sáng rực với giao diện đỏ khẩn cấp và nút 'TÔI ỔN - HỦY BÁO ĐỘNG'; cho phép người già tự hủy nếu chỉ va chạm nhẹ."),
        ("Hết 15 giây không hủy (Ngất xỉu / Bất tỉnh):", "Hệ thống tự động kích hoạt còi báo thức trên máy Giám hộ, gửi tin nhắn SMS ngầm chứa link Google Maps và tự động quay số cuộc gọi khẩn cấp SOS!")
    ]

    for title_b, desc_b in bg_points:
        p_b = tf_bg.add_paragraph()
        p_b.space_after = Pt(3)
        r1 = p_b.add_run()
        r1.text = "• " + title_b + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.2)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_b.add_run()
        r2.text = desc_b
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.2)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s12, 12, 22)
    print("Slide 12 generated.")

    # =========================================================================
    # SLIDE 13: FLUTTER MOBILE APP & FIREBASE CLOUD
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s13, C_BG_LIGHT)
    add_header(s13, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "ỨNG DỤNG FLUTTER ĐA NỀN TẢNG & ĐỒNG BỘ ĐÁM MÂY FIREBASE")

    create_card(s13, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    add_image_scaled(s13, "_tools/report_media/image23.png", 0.7, 1.45, 2.0, 3.2)
    add_image_scaled(s13, "_tools/report_media/image24.png", 2.8, 1.45, 2.0, 3.2)
    tb_cap = s13.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 3.8 & 3.9: Giao diện Người già (bình thường/SOS) và Dashboard Giám hộ"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s13, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_CYAN)
    tb_app = s13.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_app = tb_app.text_frame
    tf_app.word_wrap = True
    tf_app.margin_left = tf_app.margin_top = tf_app.margin_right = tf_app.margin_bottom = 0

    p = tf_app.paragraphs[0]
    p.text = "ĐẶC ĐIỂM THIẾT KẾ PHẦN MỀM & BACKEND CLOUD:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.space_after = Pt(4)

    app_features = [
        ("Mô hình 'Single Account - Dual Roles':", "Cả gia đình dùng chung 1 tài khoản Email/Password trên Firebase. Máy 1 chọn 'Người Giám Hộ' sẽ lưu deviceId; máy 2 đăng nhập tự động trở thành 'Người Dùng Gậy'."),
        ("Giao diện Người già (Elderly Screen):", "Thiết kế tối giản, độ tương phản cao, phím bấm kích thước lớn; tích hợp 2 nút tiện ích '🏠 VỀ NHÀ' và '📍 ĐIỂM HẸN' mở Google Maps ở chế độ đi bộ (mode=w) dẫn đường thẳng về nhà."),
        ("Dashboard Giám hộ (Guardian Screen):", "Hiển thị bản đồ số OpenStreetMap thời gian thực; tự động ghim vị trí gậy, nhà và điểm hẹn; tính năng điều hướng 1 chạm mở Google Maps vẽ lộ trình cấp cứu ngắn nhất."),
        ("Hệ thống còi báo thức thức tỉnh (Alarm Siren):", "Sử dụng FlutterRingtonePlayer phát âm thanh cảnh báo ở mức âm lượng tối đa, đánh thức người thân kể cả khi điện thoại đang ở chế độ im lặng."),
        ("Firebase Presence System (.info/connected):", "Lắng nghe socket kết nối; lệnh onDisconnect().set(false) tự động kích hoạt banner đỏ cảnh báo trên máy giám hộ nếu điện thoại người già hết pin hoặc mất mạng.")
    ]

    for title_a, desc_a in app_features:
        p_a = tf_app.add_paragraph()
        p_a.space_after = Pt(3)
        r1 = p_a.add_run()
        r1.text = "• " + title_a + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.2)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_a.add_run()
        r2.text = desc_a
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.2)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s13, 13, 22)
    print("Slide 13 generated.")

    # =========================================================================
    # SLIDE 14: EXPERIMENTAL RESULTS: FALL DETECTION
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s14, C_BG_LIGHT)
    add_header(s14, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "KIỂM THỬ THUẬT TOÁN PHÁT HIỆN TÉ NGÃ TRÊN 400 LƯỢT THỰC TẾ")

    create_card(s14, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_GREEN)
    add_image_scaled(s14, "_tools/report_media/image28.png", 0.7, 1.45, 2.0, 1.8)
    add_image_scaled(s14, "_tools/report_media/image27.png", 2.8, 1.45, 2.0, 1.8)
    add_image_scaled(s14, "_tools/report_media/image25.png", 0.7, 3.35, 4.1, 1.35)
    tb_cap = s14.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 4.4 & 4.3: Ma trận nhầm lẫn phân loại và Serial Monitor ghi nhận ngã"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s14, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    tb_res = s14.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True
    tf_res.margin_left = tf_res.margin_top = tf_res.margin_right = tf_res.margin_bottom = 0

    p = tf_res.paragraphs[0]
    p.text = "KẾT QUẢ THỰC NGHIỆM TRÊN 8 KỊCH BẢN VẬN ĐỘNG:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_BLUE
    p.space_after = Pt(4)

    p_m = tf_res.add_paragraph()
    p_m.space_after = Pt(6)
    r1 = p_m.add_run()
    r1.text = "🎯 ĐỘ NHẠY (SENSITIVITY): 95.0%  (190/200 lượt ngã thật)\n"
    r1.font.name = FONT_HEADING
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = C_GREEN
    r2 = p_m.add_run()
    r2.text = "🛡 ĐỘ ĐẶC HIỆU (SPECIFICITY): 96.0%  (192/200 lượt sinh hoạt)\n"
    r2.font.name = FONT_HEADING
    r2.font.size = Pt(10)
    r2.font.bold = True
    r2.font.color.rgb = C_PRIMARY_BLUE
    r3 = p_m.add_run()
    r3.text = "⭐ ĐỘ CHÍNH XÁC TỔNG THỂ (ACCURACY): 95.5% (382/400 lượt)"
    r3.font.name = FONT_HEADING
    r3.font.size = Pt(10)
    r3.font.bold = True
    r3.font.color.rgb = C_RED

    fall_details = [
        ("Ngã ngửa ra sau (Backward Fall):", "Đạt tỉ lệ phát hiện cao nhất 98.0% (49/50 ca) do quán tính cơ thể tạo xung va chạm cực mạnh (>3.5g)."),
        ("Ngã chúi trước & Ngã nghiêng:", "Đạt 96.0% (48/50) và 94.0% (47/50), đỉnh gia tốc SVM đều vượt ngưỡng 25 m/s² rõ ràng."),
        ("Trượt ngã khụy gối (Slump Fall):", "Đạt 92.0% (46/50 ca); 4 ca bỏ sót do tay người bám vào mép ghế làm giảm xung tiếp đất."),
        ("Hoạt động sinh hoạt ADL:", "Đi bộ gõ gậy xuống nền gạch (49/50 không báo nhầm), ngồi nhanh xuống ghế sofa (48/50 không báo nhầm), cúi nhặt đồ (50/50 hoàn hảo).")
    ]

    for title_f, desc_f in fall_details:
        p_f = tf_res.add_paragraph()
        p_f.space_after = Pt(2.5)
        r1 = p_f.add_run()
        r1.text = "• " + title_f + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.1)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_f.add_run()
        r2.text = desc_f
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.1)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s14, 14, 22)
    print("Slide 14 generated.")

    # =========================================================================
    # SLIDE 15: EXPERIMENTAL RESULTS: OBSTACLE SENSING (Refined Layout)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s15, C_BG_LIGHT)
    add_header(s15, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "KIỂM THỬ ĐO CỰ LY VẬT CẢN & PHẢN HỒI XÚC GIÁC MOTOR RUNG")

    # Left: Circuit Photo + Serial Monitor + Distance Error Curve
    create_card(s15, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_AMBER)
    add_image_scaled(s15, "_tools/report_media/image31.png", 0.7, 1.45, 1.9, 1.7)
    add_image_scaled(s15, "_tools/report_media/image32.png", 2.8, 1.45, 2.0, 1.7)
    add_image_scaled(s15, "_tools/report_media/image29.png", 0.7, 3.25, 4.1, 1.45)
    tb_cap = s15.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 4.7 & 4.8: Thực nghiệm benchtop đo khoảng cách & kích rung MOSFET (Pha kiểm thử vi mạch)"
    p.font.name = FONT_BODY
    p.font.size = Pt(7.8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s15, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    tb_obs = s15.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_obs = tb_obs.text_frame
    tf_obs.word_wrap = True
    tf_obs.margin_left = tf_obs.margin_top = tf_obs.margin_right = tf_obs.margin_bottom = 0

    p = tf_obs.paragraphs[0]
    p.text = "ĐÁNH GIÁ ĐỘ CHÍNH XÁC & ĐỘ NHẠY PHẢN HỒI:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_BLUE
    p.space_after = Pt(4)

    p_m = tf_obs.add_paragraph()
    p_m.space_after = Pt(6)
    r1 = p_m.add_run()
    r1.text = "📏 SAI SỐ ĐO KHOẢNG CÁCH: < 2.5 cm  (Sai số tương đối < 2.6%)\n"
    r1.font.name = FONT_HEADING
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = C_GREEN
    r2 = p_m.add_run()
    r2.text = "⚡ THỜI GIAN ĐÁP ỨNG RUNG: 12 - 20 ms  (Nhanh gấp 20 lần mắt người!)"
    r2.font.name = FONT_HEADING
    r2.font.size = Pt(9.5)
    r2.font.bold = True
    r2.font.color.rgb = C_RED

    obs_details = [
        ("Cự ly nguy hiểm cốt lõi (3 cm - 80 cm):", "Cảm biến HC-SR04 đo chuẩn xác trên cả 3 bề mặt (Bê tông phẳng, Bàn ghế gỗ và Quần áo vải mềm). Sai số chỉ từ 0.1 cm đến 2.1 cm."),
        ("Kích hoạt rung tức thời:", "Ngay khi vật cản xuất hiện ở cự ly 3.6 cm - 4.9 cm, Serial xuất log '🚧 CÓ VẬT CẢN! (Đang rung cảnh báo...)' và đèn LED đỏ trên module MOSFET sáng rực, kích motor rung ngay."),
        ("Tự động ngắt rung khi an toàn:", "Khi vật cản di chuyển ra ngoài 80 cm hoặc đường đi thông thoáng, hệ thống xuất log '✅ Đường thoáng - Hết vật cản (Đã tắt rung)' và ngắt hoàn toàn motor rung."),
        ("Ý nghĩa an toàn thực tế:", "Thời gian đáp ứng 12-20 ms nhanh vượt trội so với thời gian phản xạ thị giác người già (300-500 ms), giúp tránh va đụng vào cạnh bàn, bậc tam cấp tự nhiên.")
    ]

    for title_o, desc_o in obs_details:
        p_o = tf_obs.add_paragraph()
        p_o.space_after = Pt(2.5)
        r1 = p_o.add_run()
        r1.text = "• " + title_o + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.1)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_o.add_run()
        r2.text = desc_o
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.1)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s15, 15, 22)
    print("Slide 15 generated.")

    # =========================================================================
    # SLIDE 16: LATENCY BREAKDOWN & SOS CHAIN
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s16, C_BG_LIGHT)
    add_header(s16, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "PHÂN RÃ ĐỘ TRỄ TOÀN TRÌNH & CHUỖI CỨU HỘ KHẨN CẤP SOS")

    create_card(s16, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    add_image_scaled(s16, "_tools/report_media/image33.png", 0.7, 1.5, 4.1, 3.2)
    tb_cap = s16.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 4.9: Phân rã thời gian đáp ứng và độ trễ toàn trình của chuỗi cảnh báo SOS"
    p.font.name = FONT_BODY
    p.font.size = Pt(8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s16, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_GREEN)
    tb_lat = s16.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_lat = tb_lat.text_frame
    tf_lat.word_wrap = True
    tf_lat.margin_left = tf_lat.margin_top = tf_lat.margin_right = tf_lat.margin_bottom = 0

    p = tf_lat.paragraphs[0]
    p.text = "PHÂN RÃ ĐỘ TRỄ TỪNG CHẶNG (ĐỒNG NHẤT VỚI BIỂU ĐỒ HÌNH 4.9):"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.0)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(3)

    p_hl = tf_lat.add_paragraph()
    p_hl.space_after = Pt(4)
    r1 = p_hl.add_run()
    r1.text = "⏱ TỔNG ĐỘ TRỄ TOÀN TRÌNH: CHỈ 760 ms (≈ 0.76 GIÂY)!\n"
    r1.font.name = FONT_HEADING
    r1.font.size = Pt(10.5)
    r1.font.bold = True
    r1.font.color.rgb = C_GREEN
    r2 = p_hl.add_run()
    r2.text = "⏳ Thời gian chờ an toàn: 15.0 s (chủ đích hủy báo nhầm)  ➡ Tổng chuỗi SOS: 15.76 s\n"
    r2.font.name = FONT_BODY
    r2.font.size = Pt(8.2)
    r2.font.bold = True
    r2.font.color.rgb = C_TEXT_DARK
    r3 = p_hl.add_run()
    r3.text = "📶 4G Jitter tối đa: ≤ 1.31 giây  |  📲 Kênh SMS ngoại tuyến: 3.2 giây"
    r3.font.name = FONT_BODY
    r3.font.size = Pt(8.2)
    r3.font.bold = True
    r3.font.color.rgb = C_RED

    lat_steps = [
        ("Chặng 1 (Quét & Phát hiện ngã ESP32 FSM):", "42 ms (5.5%) - Lấy mẫu cảm biến MPU6050 và tính toán SVM tức thời."),
        ("Chặng 2 (Truyền tin BLE 5.0 Gậy ➡ Phone):", "28 ms (3.7%) - Bắn gói tin Notify qua đặc tính BLE GATT không dây."),
        ("Chặng 3 (Xử lý nền & GPS Mobile Gateway):", "85 ms (11.2%) - Flutter Foreground Service thức tỉnh và chốt tọa độ GPS."),
        ("Chặng 4 (Đẩy đám mây 4G Firebase RTDB):", "410 ms (53.9%) - Đồng bộ dữ liệu sự cố và tọa độ qua kết nối WebSocket."),
        ("Chặng 5 (Đồng bộ & Báo động App Giám Hộ):", "195 ms (25.7%) - Lắng nghe sự kiện onValue và phát còi hú âm lượng tối đa."),
        ("Kênh cứu hộ SMS ngầm dự phòng:", "Khi mất hoàn toàn Wi-Fi/4G, tự động gửi SMS ngầm chứa tọa độ và link Google Maps sau đúng 3.2s!")
    ]

    for title_l, desc_l in lat_steps:
        p_l = tf_lat.add_paragraph()
        p_l.space_after = Pt(2)
        r1 = p_l.add_run()
        r1.text = "• " + title_l + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.0)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_l.add_run()
        r2.text = desc_l
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.0)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s16, 16, 22)
    print("Slide 16 generated.")

    # =========================================================================
    # SLIDE 17: OFFLINE RESILIENCY & BATTERY LIFE (Refined Layout)
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s17, C_BG_LIGHT)
    add_header(s17, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "KHẢ NĂNG HOẠT ĐỘNG NGOẠI TUYẾN & THỜI LƯỢNG PIN THỰC TẾ")

    # Left: Battery cell photo + Charging module photo (stacked nicely)
    create_card(s17, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_GREEN)
    add_image_scaled(s17, "anh/pin_va_mach_sac/mach_sac_va_tang_ap.png", 0.7, 1.45, 4.1, 1.6)
    add_image_scaled(s17, "_tools/report_media/image35.png", 0.7, 3.15, 4.1, 1.55)
    tb_cap = s17.shapes.add_textbox(Inches(0.7), Inches(4.75), Inches(4.1), Inches(0.3))
    tf_cap = tb_cap.text_frame
    p = tf_cap.paragraphs[0]
    p.text = "Hình 4.10 & 4.11: Thực nghiệm khối nguồn sạc Type-C & cell pin 18650 (Trước khi đóng gói khoang 3D)"
    p.font.name = FONT_BODY
    p.font.size = Pt(7.8)
    p.font.italic = True
    p.font.color.rgb = C_TEXT_MUTED
    p.alignment = PP_ALIGN.CENTER

    create_card(s17, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_PRIMARY_BLUE)
    tb_pwr = s17.shapes.add_textbox(Inches(5.25), Inches(1.45), Inches(4.0), Inches(3.55))
    tf_pwr = tb_pwr.text_frame
    tf_pwr.word_wrap = True
    tf_pwr.margin_left = tf_pwr.margin_top = tf_pwr.margin_right = tf_pwr.margin_bottom = 0

    p = tf_pwr.paragraphs[0]
    p.text = "CHỐNG CHỊU LỖI MẠNG & THỜI LƯỢNG SỬ DỤNG:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY_BLUE
    p.space_after = Pt(4)

    p_off = tf_pwr.add_paragraph()
    p_off.space_after = Pt(4)
    r1 = p_off.add_run()
    r1.text = "📶 KHẢ NĂNG NGOẠI TUYẾN (OFFLINE RESILIENCY):\n"
    r1.font.name = FONT_HEADING
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = C_AMBER
    r2 = p_off.add_run()
    r2.text = "• Thử nghiệm ngắt hoàn toàn Wi-Fi/4G (20 lượt): 20/20 lần (100%) ứng dụng tự bật sáng màn hình (WakeLock), gửi thành công tin nhắn SMS ngầm kèm tọa độ GPS và link Google Maps!\n• Tự động lưu cache offline và đồng bộ bù dữ liệu lên Firebase ngay khi có mạng trở lại mà không mất dữ liệu."
    r2.font.name = FONT_BODY
    r2.font.size = Pt(8.2)
    r2.font.color.rgb = C_TEXT_DARK

    p_bat = tf_pwr.add_paragraph()
    p_bat.space_after = Pt(4)
    r1 = p_bat.add_run()
    r1.text = "🔋 THỜI LƯỢNG PIN & QUẢN TRỊ NGUỒN:\n"
    r1.font.name = FONT_HEADING
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = C_GREEN
    r2 = p_bat.add_run()
    r2.text = "• Cell pin Lithium-ion 18650 dung lượng 2000 mAh (3.7V - 7.4 Wh).\n• Dòng tiêu thụ trung bình chế độ hỗn hợp: 95 mA.\n• Thời lượng hoạt động liên tục: > 21 GIỜ sau 1 lần sạc đầy (người già chỉ cần cắm sạc qua đêm là dùng thoải mái cả ngày hôm sau).\n• Module MH-CD42 hỗ trợ vừa sạc vừa dùng (Pass-through Charging) qua cổng Type-C an toàn, có 4 đèn LED hiển thị mức pin 25%-50%-75%-100%."
    r2.font.name = FONT_BODY
    r2.font.size = Pt(8.2)
    r2.font.color.rgb = C_TEXT_DARK

    add_footer(s17, 17, 22)
    print("Slide 17 generated.")

    # =========================================================================
    # SLIDE 18: COMPARISON WITH MARKET SOLUTIONS
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s18, C_BG_LIGHT)
    add_header(s18, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "SO SÁNH TỔNG HỢP VỚI CÁC GIẢI PHÁP TRÊN THỊ TRƯỜNG HIỆN NAY")

    table_shape = s18.shapes.add_table(7, 8, Inches(0.6), Inches(1.35), Inches(8.8), Inches(3.75))
    tbl = table_shape.table

    tbl.columns[0].width = Inches(2.0)
    tbl.columns[1].width = Inches(1.0)
    tbl.columns[2].width = Inches(1.0)
    tbl.columns[3].width = Inches(0.9)
    tbl.columns[4].width = Inches(1.1)
    tbl.columns[5].width = Inches(1.0)
    tbl.columns[6].width = Inches(0.9)
    tbl.columns[7].width = Inches(0.9)

    headers = ["Giải pháp", "Báo ngã tự động", "Quét vật cản", "Còi hú SOS", "Định vị GPS", "Bảo vệ riêng tư", "Thời lượng pin", "Chi phí"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY_DARK
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_HEADING
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

    data = [
        ["Gậy Thông Minh (Đề Tài)", "✔ Có (95%)", "✔ Có (3-80cm)", "✔ Còi 85dB", "✔ GPS Fused", "✔ 100% Kín đáo", "✔ > 21 giờ", "⭐ ~500.000 đ"],
        ["Smartwatch (Apple Watch)", "✔ Có (92%)", "✖ Không", "✖ Không", "✔ Có GPS", "✔ Có", "✖ 18 giờ", "10 - 15 triệu"],
        ["Gậy Smart WeWALK (Anh)", "✖ Không có", "✔ Có siêu âm", "✖ Không", "✔ Có bản đồ", "✔ Có", "15 - 20 giờ", "12 - 18 triệu"],
        ["Camera AI (Thị giác máy)", "✔ Có (94%)", "✖ Không", "✖ Không", "✖ Không (cố định)", "✖ Rất nguy hại", "Nguồn điện lưới", "3 - 5 triệu"],
        ["Radar mmWave Fall Sensor", "✔ Có (90%)", "✖ Không", "✖ Không", "✖ Không (cố định)", "✔ Không camera", "Nguồn điện lưới", "2 - 4 triệu"],
        ["Gậy chống cơ học thường", "✖ Không", "✖ Không", "✖ Không", "✖ Không", "✔ Có", "Không dùng điện", "100 - 200.000 đ"]
    ]

    for row_idx, row_data in enumerate(data):
        is_highlight = (row_idx == 0)
        bg_c = RGBColor(236, 253, 245) if is_highlight else (C_WHITE if row_idx % 2 == 1 else C_CARD_ACCENT)
        for col_idx, cell_data in enumerate(row_data):
            cell = tbl.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            p = cell.text_frame.paragraphs[0]
            p.text = cell_data
            p.font.name = FONT_BODY
            p.font.size = Pt(8)
            p.font.bold = is_highlight
            p.font.color.rgb = (C_GREEN if is_highlight else C_TEXT_DARK)
            p.alignment = PP_ALIGN.LEFT if col_idx == 0 else PP_ALIGN.CENTER

    add_footer(s18, 18, 22)
    print("Slide 18 generated.")

    # =========================================================================
    # SLIDE 19: PROJECT PROGRESS CHECKLIST
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s19, C_BG_LIGHT)
    add_header(s19, "PHẦN 5: TIẾN ĐỘ & KẾ HOẠCH", "BÁO CÁO TIẾN ĐỘ THỰC HIỆN CÁC HẠNG MỤC CỦA ĐỀ TÀI")

    table_shape = s19.shapes.add_table(9, 4, Inches(0.6), Inches(1.35), Inches(8.8), Inches(3.75))
    tbl = table_shape.table

    tbl.columns[0].width = Inches(0.8)
    tbl.columns[1].width = Inches(4.5)
    tbl.columns[2].width = Inches(1.7)
    tbl.columns[3].width = Inches(1.8)

    headers_chk = ["Hạng mục", "Nội dung thực hiện chi tiết", "Tiến độ đạt được", "Trạng thái nghiệm thu"]
    for i, h in enumerate(headers_chk):
        cell = tbl.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY_DARK
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_HEADING
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

    checklist_data = [
        ("HM 01", "Nghiên cứu tài liệu, xác định mục tiêu, khảo sát 5 nhóm công nghệ té ngã", "100% Hoàn thành", "✔ Đạt xuất sắc"),
        ("HM 02", "Thiết kế kiến trúc hệ thống 4 khối, sơ đồ nguyên lý phần cứng ESP32-S3", "100% Hoàn thành", "✔ Đạt xuất sắc"),
        ("HM 03", "Thiết kế 3D công thái học vỏ gậy, khoang chứa vi mạch, cụm nút bấm SOS", "100% Hoàn thành", "✔ Bản vẽ 3D CAD"),
        ("HM 04", "Kiểm thử vi mạch rời (Benchtop) & Đóng gói trọn vẹn mạch vào thân gậy in 3D", "95% Hoàn thành", "✔ Sẵn sàng demo"),
        ("HM 05", "Lập trình Firmware ESP32-S3: Thuật toán SVM, quét vật cản, BLE GATT Server", "100% Hoàn thành", "✔ Chạy ổn định"),
        ("HM 06", "Lập trình ứng dụng di động Flutter: 2 vai trò, Foreground Service 24/7, Map", "100% Hoàn thành", "✔ Build APK thật"),
        ("HM 07", "Thiết lập Cloud Firebase Realtime Database, Auth và cơ chế cảnh báo SMS", "100% Hoàn thành", "✔ Đồng bộ < 1s"),
        ("HM 08", "Thực nghiệm 400 lượt ngã, đo cự ly vật cản, đo trễ SOS, pin & viết báo cáo", "100% Hoàn thành", "✔ Khóa luận 144 trang")
    ]

    for row_idx, row_data in enumerate(checklist_data):
        bg_c = C_WHITE if row_idx % 2 == 1 else C_CARD_ACCENT
        for col_idx, cell_data in enumerate(row_data):
            cell = tbl.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            p = cell.text_frame.paragraphs[0]
            p.text = cell_data
            p.font.name = FONT_BODY
            p.font.size = Pt(8.3)
            p.font.bold = (col_idx in [0, 2, 3])
            if col_idx == 2:
                p.font.color.rgb = C_GREEN
            elif col_idx == 3:
                p.font.color.rgb = C_PRIMARY_BLUE
            else:
                p.font.color.rgb = C_TEXT_DARK
            p.alignment = PP_ALIGN.LEFT if col_idx == 1 else PP_ALIGN.CENTER

    add_footer(s19, 19, 22)
    print("Slide 19 generated.")

    # =========================================================================
    # SLIDE 20: LIMITATIONS & FUTURE EXTENSIONS
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s20, C_BG_LIGHT)
    add_header(s20, "PHẦN 5: TIẾN ĐỘ & KẾ HOẠCH", "NHẬN XÉT HẠN CHẾ & HƯỚNG PHÁT TRIỂN TIẾP THEO")

    create_card(s20, 0.6, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_AMBER)
    tb_lim = s20.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(3.9), Inches(3.45))
    tf_lim = tb_lim.text_frame
    tf_lim.word_wrap = True
    tf_lim.margin_left = tf_lim.margin_top = tf_lim.margin_right = tf_lim.margin_bottom = 0

    p = tf_lim.paragraphs[0]
    p.text = "CÁC HẠN CHẾ CÒN TỒN TẠI:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_AMBER
    p.space_after = Pt(6)

    limits = [
        ("Góc quét siêu âm giới hạn (15 độ):", "Chỉ phát hiện hiệu quả các vật cản ở tầm ngang đầu gối đến thắt lưng; chưa quét được vật cản tầm thấp sát bàn chân (mép thảm, gờ cửa) hoặc hố sâu, bậc thang đi xuống."),
        ("Nhận diện cú ngã trượt từ từ (Slump Fall):", "Trường hợp người già bị hạ huyết áp từ từ trượt người xuống sàn theo mép tường hoặc ghế sofa, xung gia tốc va đập thấp chưa vượt ngưỡng SVM cứng 25 m/s²."),
        ("Phụ thuộc vào điện thoại thông minh:", "Hệ thống tận dụng smartphone của người già làm trạm IoT Gateway. Nếu người già để quên điện thoại ở nhà và chỉ cầm gậy ra ngoài thì tính năng cảnh báo từ xa bị gián đoạn.")
    ]

    for title_lim, desc_lim in limits:
        p_l = tf_lim.add_paragraph()
        p_l.space_after = Pt(4)
        r1 = p_l.add_run()
        r1.text = "▲ " + title_lim + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.5)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_l.add_run()
        r2.text = desc_lim
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = C_TEXT_MUTED

    create_card(s20, 5.1, 1.35, 4.3, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=C_GREEN)
    tb_fut = s20.shapes.add_textbox(Inches(5.3), Inches(1.5), Inches(3.9), Inches(3.45))
    tf_fut = tb_fut.text_frame
    tf_fut.word_wrap = True
    tf_fut.margin_left = tf_fut.margin_top = tf_fut.margin_right = tf_fut.margin_bottom = 0

    p = tf_fut.paragraphs[0]
    p.text = "4 HƯỚNG PHÁT TRIỂN & NÂNG CẤP TIẾP THEO:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p.space_after = Pt(6)

    futures = [
        ("1. Trí tuệ nhân tạo biên (TinyML & Edge AI):", "Thu thập tập dữ liệu lớn về dáng đi người già Việt Nam; nén mô hình học sâu CNN/LSTM qua TensorFlow Lite chạy trực tiếp trên ESP32-S3 để nhận diện chính xác cú ngã trượt êm."),
        ("2. Tích hợp cảm biến sinh trắc học:", "Lắp đặt cảm biến quang phổ MAX30102 đo nồng độ oxy SpO2 và nhịp tim tại tay cầm; cảm biến nhiệt độ không tiếp xúc MLX90614 phát hiện sốc nhiệt."),
        ("3. Độc lập hóa hoàn toàn phần cứng gậy:", "Tích hợp module viễn thông 4G LTE-M / NB-IoT (SIM7080G) và ăng-ten chip GNSS trực tiếp trong thân gậy; giúp gậy hoạt động độc lập không cần mang theo điện thoại."),
        ("4. Nâng cấp công nghệ vật liệu vỏ gậy:", "Sử dụng vật liệu sợi Carbon (Carbon Fiber) siêu nhẹ kết hợp lò xo giảm chấn cổ tay và gioăng silicon chống nước đạt chuẩn IP67 khi đi mưa.")
    ]

    for title_f, desc_f in futures:
        p_f = tf_fut.add_paragraph()
        p_f.space_after = Pt(3.5)
        r1 = p_f.add_run()
        r1.text = "➡ " + title_f + " "
        r1.font.name = FONT_BODY
        r1.font.size = Pt(8.5)
        r1.font.bold = True
        r1.font.color.rgb = C_TEXT_DARK
        r2 = p_f.add_run()
        r2.text = desc_f
        r2.font.name = FONT_BODY
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer(s20, 20, 22)
    print("Slide 20 generated.")

    # =========================================================================
    # SLIDE 21: CONCLUSION & IMPACT
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s21, C_BG_LIGHT)
    add_header(s21, "KẾT LUẬN", "TỔNG KẾT NHỮNG ĐÓNG GÓP NỔI BẬT CỦA ĐỀ TÀI")

    cards_conc = [
        ("GIÁ TRỊ KỸ THUẬT & CÔNG NGHỆ", [
            ("Làm chủ công nghệ IoT nhúng:", "Hiện thực hóa trọn vẹn giải pháp phân tán kết hợp vi điều khiển ESP32-S3, truyền thông không dây BLE 5.0 GATT và điện toán đám mây Firebase."),
            ("Thuật toán thời gian thực tối ưu:", "Chạy ổn định thuật toán SVM nhận diện té ngã và thuật toán quét khoảng cách siêu âm chống treo chip trên FreeRTOS."),
            ("Đột phá phần mềm di động:", "Xây dựng thành công Dịch vụ chạy ngầm liên tục (Foreground Service) trên Android, vượt qua cơ chế tiết kiệm pin Doze Mode ngặt nghèo.")
        ], C_PRIMARY_BLUE),
        ("GIÁ TRỊ THỰC TIỄN & KHẢ THI", [
            ("Nguyên mẫu thực tế hoàn chỉnh:", "Đã chế tạo và lắp ráp thành công sản phẩm phần cứng vật lý, cài đặt ứng dụng Flutter hoàn thiện và thử nghiệm trên người thật."),
            ("Độ chính xác và độ tin cậy cao:", "Đạt độ nhạy 95.0% và độ đặc hiệu 96.0% trên 400 lượt thử nghiệm thực tế; chuỗi cứu hộ kỹ thuật chỉ trễ 1.31 giây; pin bền bỉ > 21 giờ."),
            ("Chi phí siêu tiết kiệm:", "Tổng chi phí linh kiện chỉ khoảng ~500.000 VNĐ, hoàn toàn có thể sản xuất đại trà để trang bị cho đông đảo người cao tuổi Việt Nam.")
        ], C_GREEN),
        ("GIÁ TRỊ NHÂN VĂN & XÃ HỘI", [
            ("Chuyển đổi số thiết bị truyền thống:", "Biến cây gậy thô sơ thành 'người bảo vệ kỹ thuật số' thông minh, chủ động bảo vệ tính mạng người già trong 'Thời gian vàng'."),
            ("Tự tin và độc lập cho cha mẹ:", "Xóa tan 'hội chứng sợ ngã' (FoF), khuyến khích người cao tuổi duy trì thói quen đi bộ, vận động rèn luyện thể chất hằng ngày."),
            ("An tâm trọn vẹn cho con cháu:", "Giúp con cháu đang công tác ngoài xã hội luôn theo dõi được tình trạng an toàn của cha mẹ và kịp thời ứng cứu khi có sự cố.")
        ], C_RED)
    ]

    for idx, (title, items, color) in enumerate(cards_conc):
        left = 0.6 + idx * 2.98
        top = 1.35
        card = create_card(s21, left, top, 2.85, 3.75, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT, top_bar_color=color)
        
        tb = s21.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.15), Inches(2.55), Inches(3.45))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(8)
        
        for bold_txt, norm_txt in items:
            p_item = tf.add_paragraph()
            p_item.space_after = Pt(6)
            run1 = p_item.add_run()
            run1.text = "✔ " + bold_txt + " "
            run1.font.name = FONT_BODY
            run1.font.size = Pt(8.8)
            run1.font.bold = True
            run1.font.color.rgb = C_TEXT_DARK
            
            run2 = p_item.add_run()
            run2.text = norm_txt
            run2.font.name = FONT_BODY
            run2.font.size = Pt(8.8)
            run2.font.color.rgb = C_TEXT_MUTED

    add_footer(s21, 21, 22)
    print("Slide 21 generated.")

    # =========================================================================
    # SLIDE 22: THANK YOU & Q&A
    # =========================================================================
    s22 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s22, C_NAVY_DARK)

    if os.path.exists(logo_left):
        add_image_scaled(s22, logo_left, 0.6, 0.4, 2.0, 0.8)
    if os.path.exists(logo_right):
        add_image_scaled(s22, logo_right, 8.4, 0.4, 1.0, 0.8)

    tb_ty = s22.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(8.0), Inches(1.6))
    tf_ty = tb_ty.text_frame
    tf_ty.word_wrap = True
    p = tf_ty.paragraphs[0]
    p.text = "CẢM ƠN HỘI ĐỒNG THẦY CÔ & CÁC BẠN\nĐÃ CHÚ Ý THEO DÕI BÁO CÁO!"
    p.font.name = FONT_HEADING
    p.font.size = Pt(21)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(8)

    p_sub = tf_ty.add_paragraph()
    p_sub.text = "Kính mong nhận được những nhận xét và góp ý quý báu của Quý Thầy Cô trong Hội đồng\nđể nhóm có thể hoàn thiện đề tài được tốt hơn nữa!"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = C_CYAN
    p_sub.alignment = PP_ALIGN.CENTER

    create_card(s22, 1.5, 3.4, 7.0, 1.5, bg_color=C_NAVY_CARD, border_color=RGBColor(30, 58, 95), top_bar_color=C_GREEN)
    tb_c = s22.shapes.add_textbox(Inches(1.7), Inches(3.55), Inches(6.6), Inches(1.2))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    p = tf_c.paragraphs[0]
    p.text = "THÔNG TIN LIÊN HỆ NHÓM THỰC HIỆN:"
    p.font.name = FONT_HEADING
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_GREEN
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(4)

    p = tf_c.add_paragraph()
    p.text = "• Võ Gia Vỹ             - MSSV: 22642971 - Email: giavylyson@gmail.com - SĐT: 0349.793.189"
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    p = tf_c.add_paragraph()
    p.text = "• Đào Huỳnh Phong Vũ - MSSV: 22679141 - Email: daohuynhphongvu2004@gmail.com - SĐT: 0938.294.593"
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    p = tf_c.add_paragraph()
    p.text = "Lớp: DHDTMT18A  |  Khoa Công Nghệ Điện Tử - Đại học Công nghiệp TP. Hồ Chí Minh (IUH)"
    p.font.name = FONT_BODY
    p.font.size = Pt(9)
    p.font.color.rgb = RGBColor(148, 163, 184)
    p.alignment = PP_ALIGN.CENTER

    add_footer(s22, 22, 22, is_dark=True)
    print("Slide 22 generated.")

    out_file = 'BaoCao_GayThongMinh_ChinhThuc.pptx'
    prs.save(out_file)
    print(f"Successfully generated all 22 slides in: {out_file}")

    shutil.copyfile(out_file, 'BaoCao_TienDo_GayThongMinh.pptx')
    print("Copied to BaoCao_TienDo_GayThongMinh.pptx")

if __name__ == '__main__':
    build_presentation()

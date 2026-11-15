import sys
import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
import shutil

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# COLOR PALETTE: HIGH-END TECH CORPORATE (IUH ELECTRONICS & IOT)
# ==============================================================================
C_NAVY_BG      = RGBColor(10, 25, 47)      # #0A192F - Dark Master Slide BG
C_NAVY_CARD    = RGBColor(17, 34, 64)      # #112240 - Dark Card Container
C_NAVY_BORDER  = RGBColor(35, 53, 84)      # #233554 - Dark Border
C_WHITE        = RGBColor(255, 255, 255)
C_CANVAS_LIGHT = RGBColor(241, 245, 249)   # #F1F5F9 - Ultra-clean Light Slide BG
C_CARD_WHITE   = RGBColor(255, 255, 255)   # #FFFFFF - Crisp Light Card Container
C_CARD_ALT     = RGBColor(248, 250, 252)   # #F8FAFC - Soft Accent Card
C_BORDER_LIGHT = RGBColor(226, 232, 240)   # #E2E8F0 - Subtle Border
C_TEXT_MAIN    = RGBColor(15, 23, 42)      # #0F172A - Deep Slate Black
C_TEXT_MUTED   = RGBColor(100, 116, 139)   # #64748B - Slate Muted
C_TEXT_LIGHT   = RGBColor(148, 163, 184)   # #94A3B8 - Dark mode muted

# Brand Accent Colors (Vibrant, high-contrast)
C_BLUE_BRAND   = RGBColor(37, 99, 235)     # #2563EB - Royal Blue
C_CYAN_TECH    = RGBColor(6, 182, 212)     # #06B6D4 - Electric Cyan
C_GREEN_ACC    = RGBColor(16, 185, 129)    # #10B981 - Emerald Green
C_RED_ACC      = RGBColor(239, 68, 68)     # #EF4444 - Crimson Red
C_AMBER_ACC    = RGBColor(245, 158, 11)    # #F59E0B - Amber Orange
C_PURPLE_ACC   = RGBColor(139, 92, 246)    # #8B5CF6 - Modern Violet

FONT_FAMILY    = "Segoe UI"  # Clean, modern, highly legible across Windows & Mac

MEDIA_DIR = "d:/doan/_tools/report_media"
LOGO_IUH  = "d:/doan/_tools/mau_extracted_images/slide1_pic9_Picture 6.png"
LOGO_FET  = "d:/doan/_tools/mau_extracted_images/slide1_pic10_Picture 8.png"

# ==============================================================================
# HELPER FUNCTIONS: MODERN SHAPES, HERO CARDS & STAT METRICS
# ==============================================================================
def create_rect(slide, left, top, width, height, fill_color, border_color=None, border_width=1):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(border_width)
    else:
        shape.line.fill.background()
    return shape

def create_rounded_card(slide, left, top, width, height, fill_color, border_color=None, top_accent=None, border_width=1.5):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = fill_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
    else:
        card.line.fill.background()
    
    if top_accent:
        bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left + 0.05), Inches(top + 0.03), Inches(width - 0.1), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = top_accent
        bar.line.fill.background()
    return card

def add_header_banner(slide, section_tag, title_text, is_dark=False):
    # Top banner container
    bg_c = C_NAVY_CARD if is_dark else C_CARD_WHITE
    bdr_c = C_NAVY_BORDER if is_dark else C_BORDER_LIGHT
    create_rect(slide, 0.4, 0.25, 9.2, 0.82, bg_c, bdr_c, 1)
    
    # Left vertical accent line
    accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.4), Inches(0.25), Inches(0.08), Inches(0.82))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = C_CYAN_TECH if is_dark else C_BLUE_BRAND
    accent_bar.line.fill.background()
    
    # Text container
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.28), Inches(8.8), Inches(0.75))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
    
    # Section Tag
    p1 = tf.paragraphs[0]
    p1.text = section_tag.upper()
    p1.font.name = FONT_FAMILY
    p1.font.size = Pt(8.5)
    p1.font.bold = True
    p1.font.color.rgb = C_CYAN_TECH if is_dark else C_BLUE_BRAND
    p1.space_after = Pt(1)
    
    # Slide Title
    p2 = tf.add_paragraph()
    p2.text = title_text
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE if is_dark else C_TEXT_MAIN

def add_footer_bar(slide, current_slide, total_slides=22, is_dark=False):
    tb = slide.shapes.add_textbox(Inches(0.4), Inches(5.25), Inches(9.2), Inches(0.3))
    tf = tb.text_frame
    tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
    p = tf.paragraphs[0]
    
    r1 = p.add_run()
    r1.text = "Khóa luận tốt nghiệp: Thiết Kế Gậy Thông Minh Hỗ Trợ Người Cao Tuổi (ESP32-S3 & IoT)"
    r1.font.name = FONT_FAMILY
    r1.font.size = Pt(7.5)
    r1.font.color.rgb = C_TEXT_LIGHT if is_dark else C_TEXT_MUTED
    
    r2 = p.add_run()
    r2.text = f"                                                                               Trang {current_slide:02d} / {total_slides:02d}"
    r2.font.name = FONT_FAMILY
    r2.font.size = Pt(7.5)
    r2.font.bold = True
    r2.font.color.rgb = C_CYAN_TECH if is_dark else C_BLUE_BRAND

def add_stat_card(slide, left, top, width, height, stat_number, stat_label, subtext="", color_accent=C_BLUE_BRAND, is_dark=False):
    # Container card
    bg_c = C_NAVY_CARD if is_dark else C_CARD_WHITE
    bdr_c = C_NAVY_BORDER if is_dark else C_BORDER_LIGHT
    create_rounded_card(slide, left, top, width, height, bg_c, bdr_c, top_accent=color_accent, border_width=1.5)
    
    tb = slide.shapes.add_textbox(Inches(left + 0.1), Inches(top + 0.12), Inches(width - 0.2), Inches(height - 0.2))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
    
    # Big Number
    p_num = tf.paragraphs[0]
    p_num.text = stat_number
    p_num.font.name = FONT_FAMILY
    p_num.font.size = Pt(22)
    p_num.font.bold = True
    p_num.font.color.rgb = color_accent
    p_num.alignment = PP_ALIGN.CENTER
    p_num.space_after = Pt(2)
    
    # Label
    p_lbl = tf.add_paragraph()
    p_lbl.text = stat_label
    p_lbl.font.name = FONT_FAMILY
    p_lbl.font.size = Pt(9.5)
    p_lbl.font.bold = True
    p_lbl.font.color.rgb = C_WHITE if is_dark else C_TEXT_MAIN
    p_lbl.alignment = PP_ALIGN.CENTER
    
    # Subtext if present
    if subtext:
        p_sub = tf.add_paragraph()
        p_sub.text = subtext
        p_sub.font.name = FONT_FAMILY
        p_sub.font.size = Pt(7.5)
        p_sub.font.color.rgb = C_TEXT_LIGHT if is_dark else C_TEXT_MUTED
        p_sub.alignment = PP_ALIGN.CENTER

def add_image_safe(slide, img_path, left, top, width, height, caption=""):
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(left), Inches(top), Inches(width), Inches(height))
    else:
        # Placeholder box
        rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        rect.fill.solid()
        rect.fill.fore_color.rgb = RGBColor(220, 220, 220)
    
    if caption:
        tb = slide.shapes.add_textbox(Inches(left), Inches(top + height + 0.04), Inches(width), Inches(0.25))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
        p = tf.paragraphs[0]
        p.text = caption
        p.font.name = FONT_FAMILY
        p.font.size = Pt(7.5)
        p.font.italic = True
        p.font.color.rgb = C_TEXT_MUTED
        p.alignment = PP_ALIGN.CENTER

# ==============================================================================
# MAIN PRESENTATION BUILDER: 22 HIGH-END SLIDES
# ==============================================================================
def build_premium_deck():
    prs = Presentation()
    prs.slide_width = Inches(10.0)
    prs.slide_height = Inches(5.625)
    blank_layout = prs.slide_layouts[6]

    # --------------------------------------------------------------------------
    # SLIDE 1: COVER SLIDE (LUXURY DEEP TECH DARK THEME)
    # --------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    create_rect(s1, 0, 0, 10.0, 5.625, C_NAVY_BG)
    
    # University Logos
    if os.path.exists(LOGO_IUH):
        s1.shapes.add_picture(LOGO_IUH, Inches(0.6), Inches(0.35), Inches(1.8), Inches(0.7))
    if os.path.exists(LOGO_FET):
        s1.shapes.add_picture(LOGO_FET, Inches(8.4), Inches(0.35), Inches(1.0), Inches(0.7))
    
    # Uni text
    tb_u = s1.shapes.add_textbox(Inches(2.5), Inches(0.35), Inches(5.8), Inches(0.7))
    tf_u = tb_u.text_frame
    tf_u.word_wrap = True
    p = tf_u.paragraphs[0]
    p.text = "TRƯỜNG ĐẠI HỌC CÔNG NGHIỆP TP. HỒ CHÍ MINH"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER
    p2 = tf_u.add_paragraph()
    p2.text = "KHOA CÔNG NGHỆ ĐIỆN TỬ - CHUYÊN NGÀNH KỸ THUẬT MÁY TÍNH"
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(9.5)
    p2.font.bold = True
    p2.font.color.rgb = C_CYAN_TECH
    p2.alignment = PP_ALIGN.CENTER

    # Project Title Box (Hero Glass Card)
    create_rounded_card(s1, 0.6, 1.35, 8.8, 2.05, C_NAVY_CARD, C_NAVY_BORDER, top_accent=C_CYAN_TECH, border_width=2)
    
    # Pill Badge
    pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.2), Inches(1.5), Inches(3.6), Inches(0.3))
    pill.fill.solid()
    pill.fill.fore_color.rgb = C_RED_ACC
    pill.line.fill.background()
    p = pill.text_frame.paragraphs[0]
    p.text = "BÁO CÁO KHÓA LUẬN TỐT NGHIỆP NĂM 2026"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.alignment = PP_ALIGN.CENTER

    # Big Title
    tb_t = s1.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(8.4), Inches(1.4))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p = tf_t.paragraphs[0]
    p.text = "THIẾT KẾ GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(17.5)
    p.font.bold = True
    p.font.color.rgb = C_CYAN_TECH
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(4)
    
    p_sub = tf_t.add_paragraph()
    p_sub.text = "TÍCH HỢP ESP32-S3, CẢM BIẾN PHÁT HIỆN NGÃ SVM, RUNG XÚC GIÁC VẬT CẢN,\nĐỊNH VỊ GPS VÀ TỰ ĐỘNG GỬI CỨU NẠN KHẨN CẤP QUA APP FLUTTER & FIREBASE"
    p_sub.font.name = FONT_FAMILY
    p_sub.font.size = Pt(10.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = C_WHITE
    p_sub.alignment = PP_ALIGN.CENTER

    # Info Cards Bottom
    create_rounded_card(s1, 0.6, 3.6, 4.25, 1.5, C_NAVY_CARD, C_NAVY_BORDER, top_accent=C_BLUE_BRAND)
    tb_gv = s1.shapes.add_textbox(Inches(0.8), Inches(3.75), Inches(3.85), Inches(1.2))
    tf_gv = tb_gv.text_frame
    p = tf_gv.paragraphs[0]
    p.text = "GIẢNG VIÊN HƯỚNG DẪN:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_CYAN_TECH
    p.space_after = Pt(3)
    p = tf_gv.add_paragraph()
    p.text = "ThS. VŨ TUẤN ANH"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p = tf_gv.add_paragraph()
    p.text = "Khoa Công Nghệ Điện Tử - ĐH Công nghiệp TP.HCM"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9)
    p.font.color.rgb = C_TEXT_LIGHT

    create_rounded_card(s1, 5.15, 3.6, 4.25, 1.5, C_NAVY_CARD, C_NAVY_BORDER, top_accent=C_GREEN_ACC)
    tb_sv = s1.shapes.add_textbox(Inches(5.35), Inches(3.75), Inches(3.85), Inches(1.2))
    tf_sv = tb_sv.text_frame
    p = tf_sv.paragraphs[0]
    p.text = "SINH VIÊN THỰC HIỆN (LỚP DHDTMT18A):"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_ACC
    p.space_after = Pt(3)
    p = tf_sv.add_paragraph()
    p.text = "1. VÕ GIA VỸ             - MSSV: 22642971"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p = tf_sv.add_paragraph()
    p.text = "2. ĐÀO HUỲNH PHONG VŨ - MSSV: 22679141"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    # --------------------------------------------------------------------------
    # SLIDE 2: AGENDA (5 PILLARS MODERN HORIZONTAL FLOW)
    # --------------------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    create_rect(s2, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s2, "MỤC LỤC BÁO CÁO", "CẤU TRÚC 5 PHẦN BÁO CÁO TRỌNG TÂM TRƯỚC HỘI ĐỒNG")
    
    pillars = [
        ("01", "TỔNG QUAN\n& BỐI CẢNH", "• Tính cấp thiết y tế\n• Bất cập của gậy cũ\n• Đối tượng & Phạm vi", C_BLUE_BRAND),
        ("02", "MỤC TIÊU\nNGHIÊN CỨU", "• Mục tiêu tổng quát\n• 4 Mục tiêu kỹ thuật\n• Yêu cầu hệ thống", C_CYAN_TECH),
        ("03", "PHƯƠNG PHÁP\nTHỰC HIỆN", "• Kiến trúc 3 tầng IoT\n• Sơ đồ chân ESP32\n• Thuật toán SVM ngã\n• Ứng dụng Flutter", C_AMBER_ACC),
        ("04", "KẾT QUẢ\nTHỰC NGHIỆM", "• 400 lượt thử té ngã\n• Đo cự ly vật cản\n• Độ trễ 760ms & SOS\n• Xả pin > 21 Giờ", C_GREEN_ACC),
        ("05", "TIẾN ĐỘ &\nKẾ HOẠCH", "• Tiến độ 8 hạng mục\n• Đóng góp của đề tài\n• Hướng phát triển\n• Phiên hỏi đáp Q&A", C_PURPLE_ACC)
    ]
    
    for idx, (p_num, p_title, p_desc, p_col) in enumerate(pillars):
        left_p = 0.4 + idx * 1.88
        create_rounded_card(s2, left_p, 1.25, 1.76, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=p_col, border_width=2)
        
        # Number badge
        nb = s2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left_p + 0.53), Inches(1.45), Inches(0.7), Inches(0.7))
        nb.fill.solid()
        nb.fill.fore_color.rgb = p_col
        nb.line.fill.background()
        p = nb.text_frame.paragraphs[0]
        p.text = p_num
        p.font.name = FONT_FAMILY
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER
        
        # Title
        tb = s2.shapes.add_textbox(Inches(left_p + 0.1), Inches(2.25), Inches(1.56), Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = p_title
        p.font.name = FONT_FAMILY
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_MAIN
        p.alignment = PP_ALIGN.CENTER
        
        # Desc
        tb2 = s2.shapes.add_textbox(Inches(left_p + 0.1), Inches(3.1), Inches(1.56), Inches(1.8))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        p = tf2.paragraphs[0]
        p.text = p_desc
        p.font.name = FONT_FAMILY
        p.font.size = Pt(8.5)
        p.font.color.rgb = C_TEXT_MUTED
    
    add_footer_bar(s2, 2)

    # --------------------------------------------------------------------------
    # SLIDE 3: PROBLEM STATEMENT (3 BIG STAT HERO CARDS)
    # --------------------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    create_rect(s3, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s3, "PHẦN 1: TỔNG QUAN ĐỀ TÀI", "TÍNH CẤP THIẾT: NGUY CƠ TÉ NGÃ VÀ 'THỜI GIAN VÀNG' CỨU NẠN")
    
    # 3 Stat Cards
    add_stat_card(s3, 0.4, 1.25, 2.9, 3.8, "28 - 35%", "TỈ LỆ TÉ NGÃ HÀNG NĂM", 
                  "Theo thống kê của WHO, cứ 3 người trên 65 tuổi thì có 1 người bị ngã mỗi năm.\n\n"
                  "Hậu quả: 87% ca gãy xương và chấn thương sọ não bắt nguồn từ sự cố té ngã, tước đi khả năng vận động tự chủ.", C_RED_ACC)
    
    add_stat_card(s3, 3.55, 1.25, 2.9, 3.8, "< 60 PHÚT", "'THỜI GIAN VÀNG' CẤP CỨU", 
                  "Nằm bất động quá 1 giờ trên sàn sau ngã làm tăng nguy cơ tử vong lên gấp 5 lần do hạ thân nhiệt, mất nước và tổn thương mô cơ.\n\n"
                  "Yêu cầu: Cần một hệ thống tự động phát hiện và gọi trợ giúp tức thời, không phụ thuộc vào việc người già có tỉnh táo hay không.", C_AMBER_ACC)
    
    add_stat_card(s3, 6.7, 1.25, 2.9, 3.8, "100% THỤ ĐỘNG", "HẠN CHẾ CỦA GẬY TRUYỀN THỐNG", 
                  "Gậy gỗ và nhôm hiện nay chỉ đơn thuần hỗ trợ nâng đỡ cơ học.\n\n"
                  "Khiếm khuyết: Không cảnh báo được vật cản phía trước, không có còi báo động tại chỗ, và hoàn toàn bất lực khi người già trượt ngã ngất xỉu.", C_BLUE_BRAND)
    
    add_footer_bar(s3, 3)

    # --------------------------------------------------------------------------
    # SLIDE 4: EXISTING SOLUTIONS & PROPOSED CANE (4 CHALLENGES VS 1 HERO SOLUTION)
    # --------------------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    create_rect(s4, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s4, "PHẦN 1: TỔNG QUAN ĐỀ TÀI", "KHẢO SÁT CÔNG NGHỆ HIỆN CÓ VÀ ĐỊNH VỊ GIẢI PHÁP ĐỀ TÀI")
    
    # Left: 4 Challenges of other solutions
    create_rounded_card(s4, 0.4, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_RED_ACC, border_width=1.5)
    tb_ch = s4.shapes.add_textbox(Inches(0.55), Inches(1.35), Inches(4.15), Inches(3.6))
    tf_ch = tb_ch.text_frame
    tf_ch.word_wrap = True
    p = tf_ch.paragraphs[0]
    p.text = "✖ HẠN CHẾ CỦA CÁC GIẢI PHÁP TRÊN THỊ TRƯỜNG:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_RED_ACC
    p.space_after = Pt(4)
    
    ch_list = [
        ("Thiết bị đeo (Smartwatch):", "Người già rất hay quên đeo vào buổi sáng; tháo ra khi tắm/ngủ (nơi nguy cơ ngã cao nhất); pin chỉ được 1-2 ngày."),
        ("Camera AI giám sát:", "Xâm phạm nghiêm trọng quyền riêng tư (không thể gắn trong phòng ngủ, nhà tắm); bị che khuất bởi góc tối, vật cản."),
        ("Cảm biến âm thanh:", "Dễ báo động giả do tiếng rơi vỡ đồ đạc sinh hoạt; hoàn toàn bỏ sót khi người già ngã trượt từ từ hoặc ngất."),
        ("Radar sóng milimet (mmWave):", "Chi phí cực kỳ đắt đỏ; bị giới hạn cố định trong 1 căn phòng, không thể theo dõi khi người già ra ngoài.")
    ]
    for title_c, desc_c in ch_list:
        p_c = tf_ch.add_paragraph()
        p_c.space_after = Pt(3)
        r1 = p_c.add_run()
        r1.text = "• " + title_c + " "
        r1.font.bold = True
        r1.font.size = Pt(8.3)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_c.add_run()
        r2.text = desc_c
        r2.font.size = Pt(8.3)
        r2.font.color.rgb = C_TEXT_MUTED

    # Right: Hero Solution Card
    create_rounded_card(s4, 5.15, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_GREEN_ACC, border_width=2)
    tb_sol = s4.shapes.add_textbox(Inches(5.35), Inches(1.35), Inches(4.05), Inches(3.6))
    tf_sol = tb_sol.text_frame
    tf_sol.word_wrap = True
    p = tf_sol.paragraphs[0]
    p.text = "✔ GIẢI PHÁP ĐỀ TÀI: GẬY THÔNG MINH IoT ĐA NĂNG"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_GREEN_ACC
    p.space_after = Pt(4)
    
    sol_list = [
        ("Vật bất ly thân khi vận động:", "Người già có thói quen cầm gậy mỗi khi đứng dậy bước đi, bảo đảm giám sát 100% thời gian vận động ngoài giường."),
        ("Bảo vệ 100% quyền riêng tư:", "Sử dụng cảm biến quán tính IMU và sóng siêu âm, hoàn toàn không thu thập hình ảnh hay âm thanh nhạy cảm."),
        ("Cảnh báo xúc giác êm ái:", "Motor rung ngay tại tay cầm cảnh báo vật cản sớm 12-20ms, không gây hoảng loạn như còi hú vô cớ."),
        ("Cứu hộ khẩn cấp độc lập:", "Hú còi tại chỗ + 15s đếm ngược hủy báo nhầm + tự động gửi SMS tọa độ GPS kể cả khi mất Internet 4G!"),
        ("Giá thành sản xuất siêu rẻ:", "Chỉ khoảng ~500.000 VNĐ (so với 12 - 15 triệu của các dòng gậy thương mại ngoại nhập WeWALK).")
    ]
    for title_s, desc_s in sol_list:
        p_s = tf_sol.add_paragraph()
        p_s.space_after = Pt(2.5)
        r1 = p_s.add_run()
        r1.text = "✔ " + title_s + " "
        r1.font.bold = True
        r1.font.size = Pt(8.3)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_s.add_run()
        r2.text = desc_s
        r2.font.size = Pt(8.3)
        r2.font.color.rgb = C_TEXT_MUTED
    
    add_footer_bar(s4, 4)

    # --------------------------------------------------------------------------
    # SLIDE 5: RESEARCH OBJECTIVES (BANNER + 4 TECH PILLARS)
    # --------------------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    create_rect(s5, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s5, "PHẦN 2: MỤC TIÊU NGHIÊN CỨU", "MỤC TIÊU TỔNG QUÁT VÀ 4 TRỤ CỘT KỸ THUẬT CỤ THỂ")
    
    # Top Banner: General Objective
    create_rounded_card(s5, 0.4, 1.25, 9.2, 0.75, C_NAVY_CARD, C_NAVY_BORDER, top_accent=C_CYAN_TECH)
    tb_go = s5.shapes.add_textbox(Inches(0.6), Inches(1.3), Inches(8.8), Inches(0.65))
    tf_go = tb_go.text_frame
    tf_go.word_wrap = True
    p = tf_go.paragraphs[0]
    p.text = "🎯 MỤC TIÊU TỔNG QUÁT CỦA ĐỒ ÁN:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_CYAN_TECH
    p = tf_go.add_paragraph()
    p.text = "Nghiên cứu, chế tạo và thử nghiệm thành công thiết bị Gậy thông minh IoT giá rẻ hỗ trợ người cao tuổi tự tin di chuyển nhờ phản hồi xúc giác vật cản sớm, đồng thời tự động phát hiện té ngã và gửi tín hiệu cứu nạn kèm tọa độ GPS thời gian thực đến người thân."
    p.font.name = FONT_FAMILY
    p.font.size = Pt(8.5)
    p.font.color.rgb = C_WHITE

    # 4 Pillars (2x2 Grid)
    pillars_obj = [
        ("1. PHẦN CỨNG NHÚNG & CẢM BIẾN", "• Vi điều khiển ESP32-S3 Dual-Core 240MHz.\n• Cảm biến 6-DOF MPU6050 (I2C) & Siêu âm HC-SR04.\n• Mạch nguồn pin sạc Lithium 18650 qua Type-C an toàn.", C_BLUE_BRAND, 0.4, 2.15),
        ("2. THUẬT TOÁN NHẬN DIỆN & CẢNH BÁO", "• Thuật toán lọc nhiễu và SVM nhận diện ngã 3 pha.\n• Quét cự ly 3 - 80cm với độ trễ phản hồi rung < 20ms.\n• Tần số lấy mẫu cảm biến IMU đạt chuẩn 10 Hz.", C_CYAN_TECH, 5.15, 2.15),
        ("3. MOBILE APP & HẠ TẦNG ĐÁM MÂY", "• Ứng dụng Flutter đa nền tảng phân 2 vai trò rõ ràng.\n• Chạy ngầm Foreground Service 24/7 không bị tắt RAM.\n• Cơ sở dữ liệu thời gian thực Firebase RTDB < 1 giây.", C_AMBER_ACC, 0.4, 3.65),
        ("4. ĐỘ TIN CẬY & ỨNG DỤNG THỰC TẾ", "• Khả năng ngoại tuyến: Gửi SMS ngầm kèm link GPS khi mất mạng.\n• Thời lượng pin hoạt động liên tục > 21 giờ.\n• Chi phí sản xuất tối ưu chỉ ~500.000 VNĐ cho người Việt.", C_GREEN_ACC, 5.15, 3.65)
    ]
    
    for title_o, desc_o, col_o, l_o, t_o in pillars_obj:
        create_rounded_card(s5, l_o, t_o, 4.45, 1.4, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=col_o, border_width=1.5)
        tb = s5.shapes.add_textbox(Inches(l_o + 0.15), Inches(t_o + 0.1), Inches(4.15), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_o
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = col_o
        p.space_after = Pt(2)
        p2 = tf.add_paragraph()
        p2.text = desc_o
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(8.2)
        p2.font.color.rgb = C_TEXT_MUTED
    
    add_footer_bar(s5, 5)

    # --------------------------------------------------------------------------
    # SLIDE 6: SCOPE & TARGET USER
    # --------------------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    create_rect(s6, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s6, "PHẦN 1: TỔNG QUAN ĐỀ TÀI", "ĐỐI TƯỢNG, MÔI TRƯỜNG VÀ PHẠM VI GIỚI HẠN CỦA ĐỀ TÀI")
    
    create_rounded_card(s6, 0.4, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    tb_u = s6.shapes.add_textbox(Inches(0.6), Inches(1.4), Inches(4.05), Inches(3.5))
    tf_u = tb_u.text_frame
    tf_u.word_wrap = True
    p = tf_u.paragraphs[0]
    p.text = "👥 ĐỐI TƯỢNG VÀ MÔI TRƯỜNG PHỤC VỤ:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_BRAND
    p.space_after = Pt(6)
    
    u_points = [
        ("Đối tượng hưởng lợi chính:", "Người cao tuổi (từ 65 tuổi trở lên), người suy giảm thị lực, bệnh nhân phục hồi chức năng sau tai biến hoặc chấn thương xương khớp."),
        ("Môi trường hoạt động tối ưu:", "Khu vực sinh hoạt trong nhà, hành lang, sân vườn, vỉa hè và công viên khu dân cư có địa hình bằng phẳng hoặc dốc thoải."),
        ("Yêu cầu công thái học (Ergonomics):", "Trọng lượng gậy nhẹ (< 450g), tay cầm cao su vừa vặn lòng bàn tay, phím bấm SOS khẩn cấp đặt ngay vị trí ngón cái thao tác tiện lợi.")
    ]
    for t_u, d_u in u_points:
        p_u = tf_u.add_paragraph()
        p_u.space_after = Pt(4)
        r1 = p_u.add_run()
        r1.text = "• " + t_u + "\n"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_u.add_run()
        r2.text = d_u
        r2.font.size = Pt(8.3)
        r2.font.color.rgb = C_TEXT_MUTED

    create_rounded_card(s6, 5.15, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_AMBER_ACC, border_width=1.5)
    tb_sc = s6.shapes.add_textbox(Inches(5.35), Inches(1.4), Inches(4.05), Inches(3.5))
    tf_sc = tb_sc.text_frame
    tf_sc.word_wrap = True
    p = tf_sc.paragraphs[0]
    p.text = "⚙ PHẠM VI KỸ THUẬT VÀ GIỚI HẠN NGHIÊN CỨU:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_AMBER_ACC
    p.space_after = Pt(6)
    
    sc_points = [
        ("Góc quét cảm biến vật cản:", "Cảm biến siêu âm được cố định góc chếch 45° hướng xuống mặt sàn để phát hiện bậc thềm, chân bàn, chướng ngại vật tầm thấp ở cự ly 3 - 80cm."),
        ("Mô hình nhận diện té ngã:", "Tập trung giải quyết các cú va chạm tiếp đất mạnh khi ngã (ngã ngửa, ngã sấp, ngã nghiêng); nhận diện thông qua ngưỡng SVM và biến thiên góc nghiêng."),
        ("Cơ chế phân tải tài nguyên (Offloading):", "Gậy chịu trách nhiệm đo đạc và phản hồi rung tại chỗ; smartphone đóng vai trò Gateway định vị GPS, gửi dữ liệu 4G và SMS giúp gậy nhẹ và tiết kiệm pin.")
    ]
    for t_s, d_s in sc_points:
        p_s = tf_sc.add_paragraph()
        p_s.space_after = Pt(4)
        r1 = p_s.add_run()
        r1.text = "• " + t_s + "\n"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_s.add_run()
        r2.text = d_s
        r2.font.size = Pt(8.3)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s6, 6)

    # --------------------------------------------------------------------------
    # SLIDE 7: SYSTEM ARCHITECTURE (DARK HIGH-TECH 3-TIER PIPELINE)
    # --------------------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    create_rect(s7, 0, 0, 10.0, 5.625, C_NAVY_BG)
    add_header_banner(s7, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "KIẾN TRÚC TỔNG THỂ HỆ THỐNG 3 TẦNG IoT (RESOURCE OFFLOADING)", is_dark=True)
    
    tiers = [
        ("TẦNG 1: THIẾT BỊ GẬY (EDGE)", C_CYAN_TECH, 0.4,
         "• ESP32-S3 Dual-Core\n• Cảm biến 6-DOF MPU6050\n• Cảm biến siêu âm HC-SR04\n• Motor rung phản hồi MOSFET\n• Còi hú Buzzer 85dB\n• Pin 18650 & MH-CD42",
         "Giao tiếp BLE 5.0 Notify\n(Độ trễ < 30ms) ➡"),
        ("TẦNG 2: CỔNG TRUNG GIAN (GATEWAY)", C_BLUE_BRAND, 3.55,
         "• Smartphone người già\n• Flutter Foreground Service\n• Chạy ngầm 24/7 trên Android\n• Định vị GPS toàn cầu\n• Bộ đếm ngược 15s SOS\n• Module SMS ngầm ngoại tuyến",
         "Mạng 4G / Wi-Fi WebSocket\n(Độ trễ < 500ms) ➡"),
        ("TẦNG 3: ĐÁM MÂY & GIÁM HỘ (CLOUD)", C_GREEN_ACC, 6.7,
         "• Firebase Realtime Database\n• Đồng bộ dữ liệu sự cố < 1s\n• Firebase Cloud Messaging\n• Ứng dụng Smartphone Giám Hộ\n• Bản đồ định vị OpenStreetMap\n• Bật còi báo động từ xa",
         "Hệ thống khép kín\nAn toàn tuyệt đối ✔")
    ]
    
    for t_name, t_col, t_left, t_desc, t_link in tiers:
        create_rounded_card(s7, t_left, 1.25, 2.9, 3.8, C_NAVY_CARD, C_NAVY_BORDER, top_accent=t_col, border_width=2)
        
        # Title
        tb = s7.shapes.add_textbox(Inches(t_left + 0.15), Inches(1.35), Inches(2.6), Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = t_name
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = t_col
        p.alignment = PP_ALIGN.CENTER
        
        # Desc
        tb2 = s7.shapes.add_textbox(Inches(t_left + 0.15), Inches(2.05), Inches(2.6), Inches(2.0))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        p = tf2.paragraphs[0]
        p.text = t_desc
        p.font.name = FONT_FAMILY
        p.font.size = Pt(8.5)
        p.font.color.rgb = C_WHITE
        
        # Link badge
        lb = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(t_left + 0.15), Inches(4.3), Inches(2.6), Inches(0.55))
        lb.fill.solid()
        lb.fill.fore_color.rgb = RGBColor(23, 42, 69)
        lb.line.color.rgb = t_col
        p = lb.text_frame.paragraphs[0]
        p.text = t_link
        p.font.name = FONT_FAMILY
        p.font.size = Pt(8.0)
        p.font.bold = True
        p.font.color.rgb = t_col
        p.alignment = PP_ALIGN.CENTER

    add_footer_bar(s7, 7, is_dark=True)

    # --------------------------------------------------------------------------
    # SLIDE 8: HARDWARE SCHEMATIC & GPIO PINOUT (ĐỒNG NHẤT 100% VỚI CONFIG.H)
    # --------------------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    create_rect(s8, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s8, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "SƠ ĐỒ NGUYÊN LÝ & BẢNG ÁNH XẠ CHÂN GPIO CHUẨN XÁC")
    
    # Left: Big Schematic image
    create_rounded_card(s8, 0.4, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    add_image_safe(s8, os.path.join(MEDIA_DIR, "image17.png"), 0.55, 1.4, 4.15, 3.3, 
                   "Hình 3.2: Sơ đồ nguyên lý kết nối chi tiết phần cứng trên ESP32-S3 N16R8")

    # Right: Pinout Cards with color badges
    create_rounded_card(s8, 5.15, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_RED_ACC, border_width=1.5)
    tb_pins = s8.shapes.add_textbox(Inches(5.35), Inches(1.35), Inches(4.05), Inches(3.6))
    tf_pins = tb_pins.text_frame
    tf_pins.word_wrap = True
    p = tf_pins.paragraphs[0]
    p.text = "BẢNG CẤU HÌNH CHÂN GPIO (KHỚP 100% CONFIG.H & SƠ ĐỒ):"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_RED_ACC
    p.space_after = Pt(4)

    pins_data = [
        ("MPU6050 (6-DOF IMU):", "SDA (GPIO 8) | SCL (GPIO 9)", "Giao tiếp I2C tốc độ 400kHz, trở kéo 4.7kΩ; dải đo ±8g, ±2000 dps."),
        ("HC-SR04 (Siêu âm 3.3V):", "TRIG (GPIO 16) | ECHO (GPIO 17)", "ECHO cấu hình INPUT_PULLDOWN chống trôi; xung kích 10µs quét 40 kHz."),
        ("Còi hú báo động Buzzer:", "GPIO 5 (Active HIGH)", "Phát âm tần số cao 2000 Hz, đạt độ ồn 85 dB ở 1m để báo động té ngã."),
        ("Mạch kích Motor rung:", "GPIO 6 (Gate MOSFET)", "Kích mở cực Gate MOSFET FR120N, diode 1N4007 dập xung ngược Flyback."),
        ("Đo điện áp Pin Lithium:", "GPIO 4 (ADC1_CH3)", "Điểm giữa mạch cầu phân áp điện trở đưa về ADC giám sát dung lượng pin."),
        ("Cảm biến mở rộng:", "GPIO 15 (E18-D50NK)", "Chân tín hiệu dự phòng cho cảm biến hồng ngoại tầm gần chống sương mù.")
    ]
    for lbl, pin_num, note in pins_data:
        p_p = tf_pins.add_paragraph()
        p_p.space_after = Pt(2.5)
        r1 = p_p.add_run()
        r1.text = "• " + lbl + " "
        r1.font.bold = True
        r1.font.size = Pt(8.2)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_p.add_run()
        r2.text = "[" + pin_num + "]\n"
        r2.font.bold = True
        r2.font.size = Pt(8.2)
        r2.font.color.rgb = C_BLUE_BRAND
        r3 = p_p.add_run()
        r3.text = "   " + note
        r3.font.size = Pt(7.8)
        r3.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s8, 8)

    # --------------------------------------------------------------------------
    # SLIDE 9: 3D MECHANICAL DESIGN & ERGONOMICS
    # --------------------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    create_rect(s9, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s9, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "THIẾT KẾ CƠ KHÍ CÔNG THÁI HỌC VÀ BẢN VẼ 3D CAD THÂN GẬY")
    
    # Left: 3D Render
    create_rounded_card(s9, 0.4, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    add_image_safe(s9, os.path.join(MEDIA_DIR, "image14.png"), 0.55, 1.4, 4.15, 3.3, 
                   "Hình 3.1: Mô hình thiết kế 3D tổng thể gậy thông minh trên phần mềm CAD")

    # Right: 4 Ergonomic Design Features
    create_rounded_card(s9, 5.15, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_CYAN_TECH, border_width=1.5)
    tb_cad = s9.shapes.add_textbox(Inches(5.35), Inches(1.35), Inches(4.05), Inches(3.6))
    tf_cad = tb_cad.text_frame
    tf_cad.word_wrap = True
    p = tf_cad.paragraphs[0]
    p.text = "TỐI ƯU HÓA CÔNG THÁI HỌC CHO NGƯỜI CAO TUỔI:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_CYAN_TECH
    p.space_after = Pt(4)

    cad_features = [
        ("1. Tay cầm công thái học in 3D:", "Vát theo đường cong lòng bàn tay, đặt motor rung ngay ngón trỏ để truyền lực rung xúc giác rõ nhất mà không cần rung toàn bộ thân gậy."),
        ("2. Nút bấm cứu trợ khẩn cấp SOS:", "Nút cơ học to bản màu đỏ đặt ngay tầm với ngón cái, giúp người già nhấn gọi cấp cứu ngay lập tức khi mệt mỏi hoặc bị lạc."),
        ("3. Góc quét cảm biến nghiêng 45°:", "Đầu phát/thu sóng siêu âm đặt chéo 45° hướng xuống mặt đất 1-2 bước chân, nhận diện chuẩn xác thềm nhà, mép bàn và ổ gà."),
        ("4. Bố trí hạ thấp trọng tâm gậy:", "Khối pin 18650 và mạch nguồn đặt ở khoang thân gậy, giúp trọng tâm dồn xuống dưới, gậy cầm rất đầm tay và không bị chúc đầu.")
    ]
    for tit, desc in cad_features:
        p_c = tf_cad.add_paragraph()
        p_c.space_after = Pt(3)
        r1 = p_c.add_run()
        r1.text = "• " + tit + "\n"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_c.add_run()
        r2.text = desc
        r2.font.size = Pt(8.2)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s9, 9)

    # --------------------------------------------------------------------------
    # SLIDE 10: FALL DETECTION ALGORITHM (SVM 3 PHASES)
    # --------------------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    create_rect(s10, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s10, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "THUẬT TOÁN PHÁT HIỆN TÉ NGÃ 3 PHA DỰA TRÊN VECTOR GIA TỐC SVM")
    
    # Left: Waveform chart
    create_rounded_card(s10, 0.4, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_RED_ACC, border_width=1.5)
    add_image_safe(s10, os.path.join(MEDIA_DIR, "image8.png"), 0.55, 1.4, 4.15, 3.3, 
                   "Hình 2.5: Dạng sóng gia tốc tổng hợp SVM trong chu trình té ngã 3 giai đoạn")

    # Right: Formula & 3 Phases
    create_rounded_card(s10, 5.15, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    tb_svm = s10.shapes.add_textbox(Inches(5.35), Inches(1.35), Inches(4.05), Inches(3.6))
    tf_svm = tb_svm.text_frame
    tf_svm.word_wrap = True
    
    p = tf_svm.paragraphs[0]
    p.text = "CƠ SỞ TOÁN HỌC & ĐỘNG HỌC CÚ NGÃ:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_BRAND
    p.space_after = Pt(2)
    
    # Formula Box
    p_fm = tf_svm.add_paragraph()
    p_fm.text = "CÔNG THỨC VECTOR: SVM = √(ax² + ay² + az²)"
    p_fm.font.name = FONT_FAMILY
    p_fm.font.size = Pt(9.5)
    p_fm.font.bold = True
    p_fm.font.color.rgb = C_RED_ACC
    p_fm.space_after = Pt(3)

    phases = [
        ("Pha 1 - Rơi tự do (Free-fall):", "Trọng tâm đổ xuống, phản lực triệt tiêu làm SVM giảm mạnh < 0.6g (< 5.9 m/s²) trong khoảng 100 - 300ms."),
        ("Pha 2 - Va đập tiếp đất (Impact):", "Thân gậy và người đập sàn, hãm tốc cực mạnh làm SVM vọt lên ≥ 25.0 m/s² (tương đương ≥ 2.55g, đỉnh ngã thực tế đạt 3.25g - 3.5g)."),
        ("Pha 3 - Nằm bất động (Rest / Immobility):", "Sau cú va chạm, gậy nằm yên trên sàn: SVM ổn định quanh 1.0g (≈ 9.8 m/s²) và góc nghiêng Δθ > 60° duy trì liên tục quá 3 giây.")
    ]
    for ph_t, ph_d in phases:
        p_ph = tf_svm.add_paragraph()
        p_ph.space_after = Pt(2.5)
        r1 = p_ph.add_run()
        r1.text = "• " + ph_t + "\n"
        r1.font.bold = True
        r1.font.size = Pt(8.3)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_ph.add_run()
        r2.text = ph_d
        r2.font.size = Pt(8.0)
        r2.font.color.rgb = C_TEXT_MUTED
    
    p_act = tf_svm.add_paragraph()
    p_act.text = "➡ Xử lý tức thời: Bật còi hú 2000Hz 85dB tại chỗ + Rung 3 giây + Bắn gói tin Notify BLE giá trị '1' kích hoạt điện thoại."
    p_act.font.name = FONT_FAMILY
    p_act.font.size = Pt(8.2)
    p_act.font.bold = True
    p_act.font.color.rgb = C_GREEN_ACC

    add_footer_bar(s10, 10)

    # --------------------------------------------------------------------------
    # SLIDE 11: OBSTACLE SENSING ALGORITHM & FIRMWARE FLOWCHART
    # --------------------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    create_rect(s11, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s11, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "THUẬT TOÁN ĐO CỰ LY SIÊU ÂM VÀ LƯU ĐỒ FIRMWARE ESP32-S3")
    
    # Left: Flowchart
    create_rounded_card(s11, 0.4, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_AMBER_ACC, border_width=1.5)
    add_image_safe(s11, os.path.join(MEDIA_DIR, "image19.png"), 0.55, 1.4, 4.15, 3.3, 
                   "Hình 3.4: Lưu đồ thuật toán chính của Firmware điều khiển trên ESP32-S3")

    # Right: Ultrasonic details
    create_rounded_card(s11, 5.15, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    tb_us = s11.shapes.add_textbox(Inches(5.35), Inches(1.35), Inches(4.05), Inches(3.6))
    tf_us = tb_us.text_frame
    tf_us.word_wrap = True
    p = tf_us.paragraphs[0]
    p.text = "NGUYÊN LÝ TIME-OF-FLIGHT & KỸ THUẬT CHỐNG TREO:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_BRAND
    p.space_after = Pt(4)

    us_techs = [
        ("Công thức khoảng cách ToF:", "Khoảng cách d = (t × 0.0343) / 2 (cm), trong đó t là thời gian xung Echo giữ mức HIGH (µs)."),
        ("Khóa ngắt noInterrupts():", "Bao bọc xung kích Trig (LOW 5µs -> HIGH 12µs -> LOW) để tránh xung bị méo dạng bởi ngắt Wi-Fi/BLE đa luồng."),
        ("Cơ chế Fallback phần cứng:", "Nếu hàm pulseIn() trả về 0 do RTOS, hệ thống tự động chuyển sang đo trực tiếp bằng bộ đếm vi giây micros() với timeout 35ms, chống tuyệt đối treo CPU (Watchdog crash)."),
        ("Dải cự ly kích rung 3cm - 80cm:", "Khi có vật cản trong cự ly 1-2 bước chân, kích mở MOSFET rung tay cầm ngay lập tức; khi đường thoáng, ngắt rung tự động để tiết kiệm pin.")
    ]
    for u_t, u_d in us_techs:
        p_u = tf_us.add_paragraph()
        p_u.space_after = Pt(3)
        r1 = p_u.add_run()
        r1.text = "• " + u_t + "\n"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_u.add_run()
        r2.text = u_d
        r2.font.size = Pt(8.0)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s11, 11)

    # --------------------------------------------------------------------------
    # SLIDE 12: 15-SECOND EMERGENCY SOS RESCUE CHAIN (DARK ALERT THEME)
    # --------------------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    create_rect(s12, 0, 0, 10.0, 5.625, C_NAVY_BG)
    add_header_banner(s12, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "CHUỖI PHẢN ỨNG CỨU NẠN KHẨN CẤP VÀ CƠ CHẾ ĐỆM AN TOÀN 15 GIÂY", is_dark=True)
    
    # 4 Steps of SOS chain
    sos_steps = [
        ("BƯỚC 1: TÉ NGÃ\n(t = 0 GIÂY)", C_RED_ACC, 0.4,
         "• Cú ngã chạm đất (SVM ≥ 25 m/s²).\n• Còi gậy hú 2000Hz 85dB tại chỗ.\n• Motor rung tay cầm trong 3 giây.\n• Gửi gói tin Notify BLE sang máy."),
        ("BƯỚC 2: ĐẾM NGƯỢC 15s\n(t = 0 ➡ 15s)", C_AMBER_ACC, 2.7,
         "• Điện thoại tự bật màn hình (WakeLock).\n• Còi báo động điện thoại hú lớn.\n• Đồng hồ đếm ngược 15 giây đệm an toàn.\n• Đặt nút bấm 'HỦY CẢNH BÁO' siêu to."),
        ("BƯỚC 3: HỦY BÁO NHẦM\n(NẾU LỠ RƠI GẬY)", C_GREEN_ACC, 5.0,
         "• Nếu chỉ đánh rơi gậy, người già tỉnh táo nhặt gậy hoặc chạm 'Hủy'.\n• Hệ thống tắt còi ngay lập tức.\n• KHÔNG gửi cảnh báo phiền người thân.\n• Tránh 100% báo động giả!"),
        ("BƯỚC 4: PHÁT LỆNH SOS\n(t > 15 GIÂY)", C_CYAN_TECH, 7.3,
         "• Người già bất tỉnh không hủy sau 15s.\n• Lấy tọa độ GPS tức thời (độ trễ 85ms).\n• Đẩy dữ liệu lên Firebase Cloud RTDB.\n• Tự động gửi SMS ngầm kèm link Map!")
    ]
    
    for s_title, s_col, s_left, s_desc in sos_steps:
        create_rounded_card(s12, s_left, 1.25, 2.25, 3.8, C_NAVY_CARD, C_NAVY_BORDER, top_accent=s_col, border_width=2)
        
        # Header
        tb = s12.shapes.add_textbox(Inches(s_left + 0.1), Inches(1.35), Inches(2.05), Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = s_title
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = s_col
        p.alignment = PP_ALIGN.CENTER
        
        # Desc
        tb2 = s12.shapes.add_textbox(Inches(s_left + 0.1), Inches(2.15), Inches(2.05), Inches(2.7))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        p = tf2.paragraphs[0]
        p.text = s_desc
        p.font.name = FONT_FAMILY
        p.font.size = Pt(8.2)
        p.font.color.rgb = C_WHITE

    add_footer_bar(s12, 12, is_dark=True)

    # --------------------------------------------------------------------------
    # SLIDE 13: FLUTTER MOBILE APP SHOWCASE (4 SCREENS SIDE-BY-SIDE)
    # --------------------------------------------------------------------------
    s13 = prs.slides.add_slide(blank_layout)
    create_rect(s13, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s13, "PHẦN 3: PHƯƠNG PHÁP THỰC HIỆN", "ỨNG DỤNG DI ĐỘNG FLUTTER 2 VAI TRÒ & BACKEND FIREBASE CLOUD")
    
    # Left: App Screen
    create_rounded_card(s13, 0.4, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    add_image_safe(s13, os.path.join(MEDIA_DIR, "image24.png"), 0.55, 1.4, 4.15, 3.3, 
                   "Hình 3.9: Giao diện ứng dụng di động Flutter (Vai trò Người dùng gậy & Người giám hộ)")

    # Right: Software Features
    create_rounded_card(s13, 5.15, 1.25, 4.45, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_AMBER_ACC, border_width=1.5)
    tb_app = s13.shapes.add_textbox(Inches(5.35), Inches(1.35), Inches(4.05), Inches(3.6))
    tf_app = tb_app.text_frame
    tf_app.word_wrap = True
    p = tf_app.paragraphs[0]
    p.text = "CÔNG NGHỆ PHẦN MỀM & ĐỒNG BỘ THỜI GIAN THỰC:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_AMBER_ACC
    p.space_after = Pt(4)

    app_feats = [
        ("Phân quyền 2 vai trò độc lập:", "Giao diện Người già (Tối giản, nút SOS to, đếm ngược 15s) và Giao diện Giám hộ (Bản đồ trực tiếp, danh sách sự cố, điều hướng Google Maps)."),
        ("Flutter Foreground Service 24/7:", "Dịch vụ chạy ngầm liên tục với thanh thông báo thường trực trên Android, chống hiện tượng bị hệ điều hành tắt giải phóng RAM."),
        ("Đồng bộ thời gian thực Firebase RTDB:", "Sử dụng giao thức WebSocket hai chiều, đẩy cờ cảnh báo và tọa độ lên máy chủ với độ trễ siêu thấp dưới 0.5 giây."),
        ("Định vị kép OpenStreetMap & Google Maps:", "Hiển thị vị trí người già trên bản đồ mượt mà, cho phép người thân bấm 1 chạm để dẫn đường đến vị trí gặp nạn nhanh nhất.")
    ]
    for a_t, a_d in app_feats:
        p_a = tf_app.add_paragraph()
        p_a.space_after = Pt(3)
        r1 = p_a.add_run()
        r1.text = "• " + a_t + "\n"
        r1.font.bold = True
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_a.add_run()
        r2.text = a_d
        r2.font.size = Pt(8.0)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s13, 13)

    # --------------------------------------------------------------------------
    # SLIDE 14: EXPERIMENTAL RESULTS: FALL DETECTION (BIG HERO STATS)
    # --------------------------------------------------------------------------
    s14 = prs.slides.add_slide(blank_layout)
    create_rect(s14, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s14, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "KẾT QUẢ THỬ NGHIỆM PHÁT HIỆN TÉ NGÃ TRÊN 400 MẪU THỬ")
    
    # 3 Hero Stat Cards on top
    add_stat_card(s14, 0.4, 1.25, 2.9, 1.2, "95.0%", "ĐỘ NHẠY (SENSITIVITY)", "190/200 lần ngã thật phát hiện chuẩn", C_GREEN_ACC)
    add_stat_card(s14, 3.55, 1.25, 2.9, 1.2, "96.0%", "ĐỘ ĐẶC HIỆU (SPECIFICITY)", "192/200 hoạt động sinh hoạt không báo giả", C_BLUE_BRAND)
    add_stat_card(s14, 6.7, 1.25, 2.9, 1.2, "95.5%", "ĐỘ CHÍNH XÁC TOÀN DIỆN", "Đánh giá trên 8 kịch bản vận động", C_PURPLE_ACC)

    # Bottom Left: 400-trial Chart
    create_rounded_card(s14, 0.4, 2.6, 5.2, 2.45, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_GREEN_ACC, border_width=1.5)
    add_image_safe(s14, os.path.join(MEDIA_DIR, "image28.png"), 0.55, 2.7, 4.9, 2.05, 
                   "Hình 4.4: Ma trận độ chính xác phân loại các kịch bản té ngã và sinh hoạt ADL")

    # Bottom Right: Analysis
    create_rounded_card(s14, 5.75, 2.6, 3.85, 2.45, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    tb_res = s14.shapes.add_textbox(Inches(5.9), Inches(2.7), Inches(3.55), Inches(2.25))
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True
    p = tf_res.paragraphs[0]
    p.text = "PHÂN TÍCH HIỆU NĂNG THỰC NGHIỆM:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_BRAND
    p.space_after = Pt(2)
    
    res_pts = [
        ("Ngã ngửa / Ngã sấp:", "Đạt tỉ lệ phát hiện tuyệt đối 98 - 100% do quán tính rơi tự do mạnh, đỉnh va chạm sàn đạt 3.5g."),
        ("Ngã trượt từ từ (Slump Fall):", "Chiếm phần lớn các ca bỏ sót (10/200) do người già bám víu vào tường làm giảm gia tốc va chạm sàn."),
        ("Sinh hoạt thường nhật (ADL):", "Đi bộ, cúi nhặt đồ, ngồi xuống ghế đạt độ đặc hiệu 95 - 100%, không bị xung gai gõ gậy đánh lừa.")
    ]
    for r_t, r_d in res_pts:
        p_r = tf_res.add_paragraph()
        p_r.space_after = Pt(2)
        r1 = p_r.add_run()
        r1.text = "• " + r_t + " "
        r1.font.bold = True
        r1.font.size = Pt(8.0)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_r.add_run()
        r2.text = r_d
        r2.font.size = Pt(7.8)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s14, 14)

    # --------------------------------------------------------------------------
    # SLIDE 15: EXPERIMENTAL RESULTS: OBSTACLE SENSING (HERO STATS)
    # --------------------------------------------------------------------------
    s15 = prs.slides.add_slide(blank_layout)
    create_rect(s15, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s15, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "KIỂM THỬ ĐO CỰ LY VẬT CẢN VÀ THỜI GIAN ĐÁP ỨNG RUNG XÚC GIÁC")
    
    # 2 Hero Stat Cards on top
    add_stat_card(s15, 0.4, 1.25, 4.45, 1.2, "< 2.5 cm", "SAI SỐ ĐO KHOẢNG CÁCH", "Sai số tương đối bình quân chỉ 1.62% trong cự ly < 150cm", C_GREEN_ACC)
    add_stat_card(s15, 5.15, 1.25, 4.45, 1.2, "12 - 20 ms", "THỜI GIAN ĐÁP ỨNG RUNG", "Nhanh gấp 20 lần phản xạ thị giác người già (300 - 500 ms)!", C_RED_ACC)

    # Bottom Left: Benchtop Photos & Distance Curve
    create_rounded_card(s15, 0.4, 2.6, 4.45, 2.45, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_AMBER_ACC, border_width=1.5)
    add_image_safe(s15, os.path.join(MEDIA_DIR, "image31.png"), 0.55, 2.7, 1.9, 1.1)
    add_image_safe(s15, os.path.join(MEDIA_DIR, "image32.png"), 2.6, 2.7, 2.1, 1.1)
    add_image_safe(s15, os.path.join(MEDIA_DIR, "image29.png"), 0.55, 3.85, 4.15, 1.05, 
                   "Hình 4.7 & 4.8: Mạch benchtop kích rung MOSFET và đồ thị đặc tuyến sai số cự ly")

    # Bottom Right: Details
    create_rounded_card(s15, 5.15, 2.6, 4.45, 2.45, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    tb_obs = s15.shapes.add_textbox(Inches(5.35), Inches(2.7), Inches(4.05), Inches(2.25))
    tf_obs = tb_obs.text_frame
    tf_obs.word_wrap = True
    p = tf_obs.paragraphs[0]
    p.text = "ĐÁNH GIÁ ĐỘ CHÍNH XÁC TRÊN CÁC LOẠI BỀ MẶT:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_BRAND
    p.space_after = Pt(2)

    obs_pts = [
        ("Độ chuẩn xác trên 3 bề mặt:", "Đo tin cậy trên Tường bê tông phẳng, Bàn ghế gỗ và Quần áo vải mềm hấp thụ âm. Sai số chỉ từ 0.1cm đến 2.1cm."),
        ("Kích hoạt rung tức thì (3cm - 80cm):", "Vật cản xuất hiện ở 3.6cm - 4.9cm, Serial xuất log và đèn LED đỏ trên module MOSFET sáng rực, kích motor rung ngay lập tức."),
        ("Tự động ngắt rung khi an toàn:", "Khi vật cản di chuyển ra xa (> 80cm) hoặc đường thoáng, hệ thống tự động tắt motor rung để tiết kiệm năng lượng và thoải mái tay cầm.")
    ]
    for o_t, o_d in obs_pts:
        p_o = tf_obs.add_paragraph()
        p_o.space_after = Pt(2)
        r1 = p_o.add_run()
        r1.text = "• " + o_t + " "
        r1.font.bold = True
        r1.font.size = Pt(8.0)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_o.add_run()
        r2.text = o_d
        r2.font.size = Pt(7.8)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s15, 15)

    # --------------------------------------------------------------------------
    # SLIDE 16: EXPERIMENTAL RESULTS: LATENCY BREAKDOWN (760 MS EXACT)
    # --------------------------------------------------------------------------
    s16 = prs.slides.add_slide(blank_layout)
    create_rect(s16, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s16, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "PHÂN RÃ ĐỘ TRỄ TOÀN TRÌNH 760 MS CỦA CHUỖI CỨU NẠN KHẨN CẤP")
    
    # 3 Stat Cards on top
    add_stat_card(s16, 0.4, 1.25, 2.9, 1.2, "760 ms", "TỔNG ĐỘ TRỄ KỸ THUẬT", "≈ 0.76 giây - Đạt chuẩn cứu hộ khẩn cấp y tế", C_GREEN_ACC)
    add_stat_card(s16, 3.55, 1.25, 2.9, 1.2, "15.0 s", "KHOẢNG CHỜ AN TOÀN", "Thời gian có chủ đích để người già hủy báo nhầm", C_AMBER_ACC)
    add_stat_card(s16, 6.7, 1.25, 2.9, 1.2, "3.2 s", "KÊNH DỰ PHÒNG SMS", "Gửi SMS ngầm kèm link GPS khi mất Internet", C_BLUE_BRAND)

    # Bottom Left: Figure 4.9 Chart
    create_rounded_card(s16, 0.4, 2.6, 4.45, 2.45, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_GREEN_ACC, border_width=1.5)
    add_image_safe(s16, os.path.join(MEDIA_DIR, "image33.png"), 0.55, 2.7, 4.15, 2.15, 
                   "Hình 4.9: Phân rã độ trễ toàn trình của chuỗi cảnh báo té ngã khẩn cấp")

    # Bottom Right: 5 Steps Breakdown Table
    create_rounded_card(s16, 5.15, 2.6, 4.45, 2.45, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    tb_lat = s16.shapes.add_textbox(Inches(5.35), Inches(2.7), Inches(4.05), Inches(2.25))
    tf_lat = tb_lat.text_frame
    tf_lat.word_wrap = True
    p = tf_lat.paragraphs[0]
    p.text = "PHÂN RÃ 5 CHẶNG (ĐỒNG NHẤT 100% VỚI BIỂU ĐỒ):"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_BRAND
    p.space_after = Pt(2)

    lat_data = [
        ("1. ESP32 FSM phát hiện ngã:", "42 ms (5.5%)", "Lấy mẫu IMU và tính toán SVM tức thời."),
        ("2. Truyền tin BLE 5.0:", "28 ms (3.7%)", "Bắn gói tin Notify qua đặc tính GATT không dây."),
        ("3. Xử lý nền & GPS Gateway:", "85 ms (11.2%)", "Flutter Service thức tỉnh và chốt tọa độ GPS."),
        ("4. Đẩy đám mây 4G Firebase:", "410 ms (53.9%)", "Đồng bộ cờ báo động và vị trí qua WebSocket."),
        ("5. Báo động App Giám Hộ:", "195 ms (25.7%)", "Nhận sự kiện onValue và phát còi hú âm lượng tối đa.")
    ]
    for ch_t, ch_time, ch_desc in lat_data:
        p_c = tf_lat.add_paragraph()
        p_c.space_after = Pt(1.5)
        r1 = p_c.add_run()
        r1.text = "• " + ch_t + " "
        r1.font.bold = True
        r1.font.size = Pt(8.0)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_c.add_run()
        r2.text = "[" + ch_time + "] "
        r2.font.bold = True
        r2.font.size = Pt(8.0)
        r2.font.color.rgb = C_GREEN_ACC
        r3 = p_c.add_run()
        r3.text = ch_desc
        r3.font.size = Pt(7.5)
        r3.font.color.rgb = C_TEXT_MUTED

    p_jit = tf_lat.add_paragraph()
    p_jit.text = "Ghi chú: Trong điều kiện mạng 4G jitter nặng nhất, tổng độ trễ vẫn ≤ 1.31s (vượt xa chuẩn y tế < 5s)."
    p_jit.font.name = FONT_FAMILY
    p_jit.font.size = Pt(7.5)
    p_jit.font.italic = True
    p_jit.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s16, 16)

    # --------------------------------------------------------------------------
    # SLIDE 17: OFFLINE RESILIENCY & BATTERY LIFE
    # --------------------------------------------------------------------------
    s17 = prs.slides.add_slide(blank_layout)
    create_rect(s17, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s17, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "KHẢ NĂNG NGOẠI TUYẾN CHỐNG MẤT MẠNG & THỜI LƯỢNG PIN")
    
    # 3 Stat Cards on top
    add_stat_card(s17, 0.4, 1.25, 2.9, 1.2, "100%", "NGOẠI TUYẾN THÀNH CÔNG", "20/20 lần gửi SMS ngầm kèm GPS khi mất 4G/Wi-Fi", C_GREEN_ACC)
    add_stat_card(s17, 3.55, 1.25, 2.9, 1.2, "> 21 GIỜ", "THỜI LƯỢNG PIN LIÊN TỤC", "Cell 18650 2000mAh, người già sạc 1 lần dùng cả ngày", C_BLUE_BRAND)
    add_stat_card(s17, 6.7, 1.25, 2.9, 1.2, "95 mA", "DÒNG TIÊU THỤ TRUNG BÌNH", "Chế độ hoạt động hỗn hợp kèm phát sóng BLE", C_AMBER_ACC)

    # Bottom Left: Battery & Charging module photos
    create_rounded_card(s17, 0.4, 2.6, 4.45, 2.45, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_GREEN_ACC, border_width=1.5)
    add_image_safe(s17, "d:/doan/anh/pin_va_mach_sac/mach_sac_va_tang_ap.png", 0.55, 2.7, 4.15, 1.05)
    add_image_safe(s17, os.path.join(MEDIA_DIR, "image35.png"), 0.55, 3.8, 4.15, 1.05, 
                   "Hình 4.10 & 4.11: Module sạc MH-CD42, pin 18650 và thực nghiệm sạc an toàn Type-C")

    # Bottom Right: Resiliency Analysis
    create_rounded_card(s17, 5.15, 2.6, 4.45, 2.45, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=C_BLUE_BRAND, border_width=1.5)
    tb_off = s17.shapes.add_textbox(Inches(5.35), Inches(2.7), Inches(4.05), Inches(2.25))
    tf_off = tb_off.text_frame
    tf_off.word_wrap = True
    p = tf_off.paragraphs[0]
    p.text = "CƠ CHẾ CHỐNG CHỊU LỖI MẠNG & QUẢN TRỊ NGUỒN:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_BRAND
    p.space_after = Pt(2)

    off_pts = [
        ("Chuyển mạch SMS ngầm dự phòng:", "Khi mất kết nối Internet (ConnectivityResult.none), hệ thống lập tức ưu tiên gửi SMS ngầm chứa tọa độ và link Google Maps trong 3.2 giây."),
        ("Tự động đồng bộ bù dữ liệu (Offline Caching):", "Dữ liệu sự cố được lưu SharedPreferences; khi có mạng trở lại, tự động đẩy lên Firebase mà không mất bất kỳ bản ghi nào."),
        ("Module nguồn MH-CD42 chuẩn công nghiệp:", "Hỗ trợ vừa sạc vừa dùng (Pass-through Charging) qua Type-C, 4 đèn LED hiển thị mức pin 25-50-75-100%, bảo vệ quá dòng và ngắn mạch an toàn.")
    ]
    for o_t, o_d in off_pts:
        p_o = tf_off.add_paragraph()
        p_o.space_after = Pt(2)
        r1 = p_o.add_run()
        r1.text = "• " + o_t + " "
        r1.font.bold = True
        r1.font.size = Pt(8.0)
        r1.font.color.rgb = C_TEXT_MAIN
        r2 = p_o.add_run()
        r2.text = o_d
        r2.font.size = Pt(7.8)
        r2.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s17, 17)

    # --------------------------------------------------------------------------
    # SLIDE 18: MARKET COMPARISON (HIGH CONTRAST MODERN TABLE)
    # --------------------------------------------------------------------------
    s18 = prs.slides.add_slide(blank_layout)
    create_rect(s18, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s18, "PHẦN 4: KẾT QUẢ THỰC NGHIỆM", "BẢNG ĐỐI CHIẾU TÍNH NĂNG & CHI PHÍ VỚI CÁC GIẢI PHÁP THỊ TRƯỜNG")
    
    table_shape = s18.shapes.add_table(7, 5, Inches(0.4), Inches(1.25), Inches(9.2), Inches(3.8))
    tbl = table_shape.table
    tbl.columns[0].width = Inches(2.4)
    tbl.columns[1].width = Inches(1.6)
    tbl.columns[2].width = Inches(1.7)
    tbl.columns[3].width = Inches(1.7)
    tbl.columns[4].width = Inches(1.8)

    headers = ["Tiêu chí so sánh", "Gậy gỗ / nhôm", "Vòng Smartwatch", "Gậy WeWALK (Mỹ)", "Gậy Đề Tài Nghiên Cứu"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY_BG if i < 4 else C_BLUE_BRAND
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

    data_mkt = [
        ("Hỗ trợ trợ lực di chuyển cơ học", "✔ Có hỗ trợ", "✖ Không", "✔ Có hỗ trợ", "✔ Có hỗ trợ"),
        ("Rung xúc giác cảnh báo vật cản", "✖ Không có", "✖ Không có", "✔ Có (tầm ngực)", "✔ Có (tầm thấp 3-80cm)"),
        ("Tự động phát hiện té ngã", "✖ Không có", "✔ Có (Apple/Garmin)", "✖ Không có", "✔ Có (Thuật toán 3 pha)"),
        ("Định vị GPS & Đẩy Cloud Mobile", "✖ Không có", "✔ Có", "✔ Có (kèm App)", "✔ Có (Firebase < 1s)"),
        ("Cơ chế cứu hộ ngoại tuyến SMS", "✖ Không có", "✖ Cần eSIM đắt tiền", "✖ Phụ thuộc mạng", "✔ Có (Tự gửi SMS ngầm)"),
        ("Ước tính chi phí sở hữu", "50.000 - 150.000 đ", "3.000.000 - 10.000.000 đ", "12.000.000 - 15.000.000 đ", "CHỈ ~ 500.000 VNĐ")
    ]
    for row_idx, row_d in enumerate(data_mkt):
        bg_c = C_CARD_WHITE if row_idx % 2 == 1 else C_CARD_ALT
        for col_idx, text_val in enumerate(row_d):
            cell = tbl.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            p = cell.text_frame.paragraphs[0]
            p.text = text_val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(8.5)
            p.alignment = PP_ALIGN.LEFT if col_idx == 0 else PP_ALIGN.CENTER
            
            if col_idx == 4:
                p.font.bold = True
                p.font.color.rgb = C_GREEN_ACC if row_idx == 5 else C_BLUE_BRAND
            elif text_val.startswith("✔"):
                p.font.color.rgb = C_GREEN_ACC
            elif text_val.startswith("✖"):
                p.font.color.rgb = C_RED_ACC
            else:
                p.font.color.rgb = C_TEXT_MAIN

    add_footer_bar(s18, 18)

    # --------------------------------------------------------------------------
    # SLIDE 19: PROJECT PROGRESS CHECKLIST (100% KPI ACCOMPLISHMENT)
    # --------------------------------------------------------------------------
    s19 = prs.slides.add_slide(blank_layout)
    create_rect(s19, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s19, "PHẦN 5: TIẾN ĐỘ & KẾ HOẠCH", "BẢNG TỔNG HỢP TIẾN ĐỘ THỰC HIỆN 8 HẠNG MỤC CỦA ĐỀ TÀI")
    
    table_shape2 = s19.shapes.add_table(9, 4, Inches(0.4), Inches(1.25), Inches(9.2), Inches(3.8))
    tbl2 = table_shape2.table
    tbl2.columns[0].width = Inches(1.0)
    tbl2.columns[1].width = Inches(4.5)
    tbl2.columns[2].width = Inches(1.8)
    tbl2.columns[3].width = Inches(1.9)

    headers_chk = ["Hạng mục", "Nội dung thực hiện chi tiết", "Tiến độ đạt được", "Trạng thái nghiệm thu"]
    for i, h in enumerate(headers_chk):
        cell = tbl2.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY_BG
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

    chk_data = [
        ("HM 01", "Nghiên cứu tài liệu y khoa, xác định mục tiêu và khảo sát công nghệ", "100% Hoàn thành", "✔ Đạt xuất sắc"),
        ("HM 02", "Thiết kế kiến trúc hệ thống 3 tầng, sơ đồ nguyên lý phần cứng ESP32-S3", "100% Hoàn thành", "✔ Đạt xuất sắc"),
        ("HM 03", "Thiết kế 3D công thái học vỏ gậy, khoang chứa vi mạch, cụm nút bấm SOS", "100% Hoàn thành", "✔ Bản vẽ 3D CAD"),
        ("HM 04", "Kiểm thử vi mạch rời (Benchtop) & Đóng gói trọn vẹn mạch vào thân gậy in 3D", "95% Hoàn thành", "✔ Sẵn sàng demo"),
        ("HM 05", "Lập trình Firmware ESP32-S3: Thuật toán SVM, đo siêu âm, BLE GATT Server", "100% Hoàn thành", "✔ Chạy ổn định"),
        ("HM 06", "Lập trình ứng dụng di động Flutter: 2 vai trò, Foreground Service 24/7, Map", "100% Hoàn thành", "✔ Build APK thật"),
        ("HM 07", "Thiết lập Cloud Firebase Realtime Database, Auth và cơ chế cảnh báo SMS", "100% Hoàn thành", "✔ Đồng bộ < 1s"),
        ("HM 08", "Thực nghiệm 400 lượt ngã, đo cự ly vật cản, đo trễ SOS, pin & viết báo cáo", "100% Hoàn thành", "✔ Khóa luận 144 trang")
    ]
    for row_idx, row_d in enumerate(chk_data):
        bg_c = C_CARD_WHITE if row_idx % 2 == 1 else C_CARD_ALT
        for col_idx, text_val in enumerate(row_d):
            cell = tbl2.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            p = cell.text_frame.paragraphs[0]
            p.text = text_val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(8.5)
            p.alignment = PP_ALIGN.LEFT if col_idx == 1 else PP_ALIGN.CENTER
            p.font.bold = (col_idx in [0, 2, 3])
            
            if col_idx == 2:
                p.font.color.rgb = C_GREEN_ACC
            elif col_idx == 3:
                p.font.color.rgb = C_BLUE_BRAND
            else:
                p.font.color.rgb = C_TEXT_MAIN

    add_footer_bar(s19, 19)

    # --------------------------------------------------------------------------
    # SLIDE 20: CONTRIBUTIONS & NOVELTY OF THE THESIS (4 CARDS)
    # --------------------------------------------------------------------------
    s20 = prs.slides.add_slide(blank_layout)
    create_rect(s20, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s20, "PHẦN 5: TIẾN ĐỘ & KẾ HOẠCH", "NHỮNG ĐÓNG GÓP MỚI VÀ GIÁ TRỊ THỰC TIỄN NỔI BẬT CỦA ĐỀ TÀI")
    
    contribs = [
        ("1. CẢNH BÁO XÚC GIÁC NHÂN VĂN", "Thay vì dùng còi hú gây hoảng loạn tinh thần người già, hệ thống dùng motor rung xúc giác ở tay cầm với độ trễ siêu nhanh 12-20ms, giúp người già phản xạ né tránh tự nhiên.", C_BLUE_BRAND, 0.4, 1.25),
        ("2. THUẬT TOÁN 3 PHA LOẠI TRỪ BÁO GIẢ", "Kết hợp chuỗi trạng thái Rơi tự do -> Va đập -> Bất động cùng bộ đệm an toàn 15 giây cho phép hủy nhầm, đạt độ đặc hiệu 96% và độ chính xác toàn diện 95.5%.", C_GREEN_ACC, 5.15, 1.25),
        ("3. CHỐNG CHỊU LỖI MẠNG NGOẠI TUYẾN 100%", "Xây dựng kênh cứu hộ kép SMS ngầm kèm link tọa độ Google Maps gửi sau 3.2s khi mất sóng Internet, bảo đảm tính mạng người già không bị gián đoạn cứu hộ.", C_AMBER_ACC, 0.4, 3.15),
        ("4. LÀM CHỦ CÔNG NGHỆ VỚI CHI PHÍ RẺ", "Thiết kế hoàn chỉnh từ sơ đồ mạch Altium, vi mạch ESP32-S3, ứng dụng di động Flutter đến vỏ in 3D với chi phí chỉ ~500.000 VNĐ, có khả năng thương mại hóa cao.", C_PURPLE_ACC, 5.15, 3.15)
    ]
    for c_tit, c_desc, c_col, c_l, c_t in contribs:
        create_rounded_card(s20, c_l, c_t, 4.45, 1.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=c_col, border_width=1.5)
        tb = s20.shapes.add_textbox(Inches(c_l + 0.15), Inches(c_t + 0.12), Inches(4.15), Inches(1.55))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = c_tit
        p.font.name = FONT_FAMILY
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = c_col
        p.space_after = Pt(3)
        p2 = tf.add_paragraph()
        p2.text = c_desc
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s20, 20)

    # --------------------------------------------------------------------------
    # SLIDE 21: LIMITATIONS & FUTURE EXTENSIONS (3 UPGRADE CARDS)
    # --------------------------------------------------------------------------
    s21 = prs.slides.add_slide(blank_layout)
    create_rect(s21, 0, 0, 10.0, 5.625, C_CANVAS_LIGHT)
    add_header_banner(s21, "PHẦN 5: TIẾN ĐỘ & KẾ HOẠCH", "HẠN CHẾ CÒN TỒN TẠI VÀ ĐỊNH HƯỚNG NÂNG CẤP HOÀN THIỆN")
    
    upgrades = [
        ("1. NÂNG CẤP TINYML (EDGE AI)", C_BLUE_BRAND, 0.4,
         "• Hạn chế hiện tại: Thuật toán SVM dùng ngưỡng cứng vẫn có thể nhầm lẫn khi người già trượt ngã từ từ (Slump Fall).\n\n"
         "• Giải pháp nâng cấp: Huấn luyện mạng nơ-ron tích chập 1D (1D-CNN) trên tập dữ liệu SisFall, lượng tử hóa INT8 chạy trực tiếp bằng TensorFlow Lite Micro trên ESP32-S3."),
        ("2. MODULE 4G LTE-M ĐỘC LẬP", C_AMBER_ACC, 3.55,
         "• Hạn chế hiện tại: Gậy vẫn cần kết nối BLE với smartphone để lấy tọa độ GPS và gửi dữ liệu lên Firebase.\n\n"
         "• Giải pháp nâng cấp: Tích hợp trực tiếp module SIM7080G (4G LTE-M / NB-IoT / GNSS đa vệ tinh) vào trong thân gậy, giúp cây gậy hoạt động độc lập 100% không cần mang điện thoại."),
        ("3. CẢM BIẾN THEO DÕI SỨC KHỎE", C_GREEN_ACC, 6.7,
         "• Hạn chế hiện tại: Gậy mới chỉ tập trung vào phát hiện té ngã và cảnh báo vật cản di chuyển.\n\n"
         "• Giải pháp nâng cấp: Tích hợp cảm biến MAX30102 ở chuôi tay cầm đo nhịp tim và nồng độ oxy trong máu (SpO2), cảnh báo sớm đột quỵ hoặc sốc nhiệt khi người già đi dạo ngoài trời.")
    ]
    for u_tit, u_col, u_l, u_desc in upgrades:
        create_rounded_card(s21, u_l, 1.25, 2.9, 3.8, C_CARD_WHITE, C_BORDER_LIGHT, top_accent=u_col, border_width=1.5)
        tb = s21.shapes.add_textbox(Inches(u_l + 0.15), Inches(1.35), Inches(2.6), Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = u_tit
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = u_col
        p.alignment = PP_ALIGN.CENTER
        
        tb2 = s21.shapes.add_textbox(Inches(u_l + 0.15), Inches(2.05), Inches(2.6), Inches(2.8))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        p = tf2.paragraphs[0]
        p.text = u_desc
        p.font.name = FONT_FAMILY
        p.font.size = Pt(8.3)
        p.font.color.rgb = C_TEXT_MUTED

    add_footer_bar(s21, 21)

    # --------------------------------------------------------------------------
    # SLIDE 22: THANK YOU & Q&A (LUXURY DARK CLOSING)
    # --------------------------------------------------------------------------
    s22 = prs.slides.add_slide(blank_layout)
    create_rect(s22, 0, 0, 10.0, 5.625, C_NAVY_BG)
    
    create_rounded_card(s22, 1.2, 0.8, 7.6, 4.0, C_NAVY_CARD, C_NAVY_BORDER, top_accent=C_CYAN_TECH, border_width=2)
    
    tb_end = s22.shapes.add_textbox(Inches(1.4), Inches(1.0), Inches(7.2), Inches(3.6))
    tf_end = tb_end.text_frame
    tf_end.word_wrap = True
    
    p = tf_end.paragraphs[0]
    p.text = "XIN CHÂN THÀNH CẢM ƠN"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = C_CYAN_TECH
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(4)
    
    p2 = tf_end.add_paragraph()
    p2.text = "QUÝ THẦY CÔ TRONG HỘI ĐỒNG VÀ CÁC BẠN SINH VIÊN ĐÃ LẮNG NGHE!"
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(12)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.alignment = PP_ALIGN.CENTER
    p2.space_after = Pt(16)
    
    # Q&A Pill
    qa_pill = s22.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.5), Inches(2.4), Inches(3.0), Inches(0.6))
    qa_pill.fill.solid()
    qa_pill.fill.fore_color.rgb = C_RED_ACC
    qa_pill.line.fill.background()
    p_qa = qa_pill.text_frame.paragraphs[0]
    p_qa.text = "PHIÊN HỎI ĐÁP & CHẤT VẤN (Q&A)"
    p_qa.font.name = FONT_FAMILY
    p_qa.font.size = Pt(10.5)
    p_qa.font.bold = True
    p_qa.font.color.rgb = C_WHITE
    p_qa.alignment = PP_ALIGN.CENTER
    
    tb_sub = s22.shapes.add_textbox(Inches(1.4), Inches(3.3), Inches(7.2), Inches(1.2))
    tf_sub = tb_sub.text_frame
    tf_sub.word_wrap = True
    p = tf_sub.paragraphs[0]
    p.text = "Nhóm nghiên cứu rất mong nhận được những câu hỏi, ý kiến đóng góp quý báu\ntừ Quý Thầy Cô để hoàn thiện đề tài xuất sắc nhất!"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(10)
    p.font.color.rgb = C_TEXT_LIGHT
    p.alignment = PP_ALIGN.CENTER

    # Save to disk
    out_master = "d:/doan/BaoCao_GayThongMinh_ChinhThuc.pptx"
    out_backup = "d:/doan/BaoCao_TienDo_GayThongMinh.pptx"
    prs.save(out_master)
    shutil.copyfile(out_master, out_backup)
    print("SUCCESS: Masterdeck rebuilt in high-end design at:", out_master)

if __name__ == "__main__":
    build_premium_deck()


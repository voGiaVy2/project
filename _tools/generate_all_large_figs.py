# -*- coding: utf-8 -*-
"""
generate_all_large_figs.py - Part 1
Tạo 7 hình kiến trúc và sơ đồ hệ thống chính với FONT CHỮ CỰC LỚN, ĐẬM, RÕ NÉT TRÊN WORD.
Canvas: 7.2 - 7.5 inch x H | DPI: 300 | Tương thích 100% độ rộng 6.15 inch của văn bản Word A4.
"""
import os, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon, Wedge
from matplotlib import font_manager

for f in ['C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/segoeuib.ttf', 'C:/Windows/Fonts/arial.ttf', 'C:/Windows/Fonts/arialbd.ttf']:
    if os.path.exists(f):
        font_manager.fontManager.addfont(f)

plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

OUT = r'd:\doan\_tools\fig'
os.makedirs(OUT, exist_ok=True)

# Bảng màu cao cấp chuẩn quốc tế
C_SLATE_900 = '#0F172A'
C_SLATE_800 = '#1E293B'
C_SLATE_700 = '#334155'
C_SLATE_500 = '#64748B'
C_SLATE_200 = '#CBD5E1'

C_BLUE_DARK  = '#1E3A8A'
C_BLUE_MED   = '#2563EB'
C_BLUE_LIGHT = '#EFF6FF'
C_BLUE_BORDER= '#93C5FD'

C_EMERALD_DARK  = '#064E3B'
C_EMERALD_MED   = '#059669'
C_EMERALD_LIGHT = '#ECFDF5'
C_EMERALD_BORDER= '#6EE7B7'

C_AMBER_DARK  = '#78350F'
C_AMBER_MED   = '#D97706'
C_AMBER_LIGHT = '#FFFBEB'
C_AMBER_BORDER= '#FCD34D'

C_PURPLE_DARK  = '#4C1D95'
C_PURPLE_MED   = '#7C3AED'
C_PURPLE_LIGHT = '#FAF5FF'
C_PURPLE_BORDER= '#C4B5FD'

C_ROSE_DARK  = '#881337'
C_ROSE_MED   = '#E11D48'
C_ROSE_LIGHT = '#FFF1F2'
C_ROSE_BORDER= '#FDA4AF'

C_CYAN_DARK  = '#164E63'
C_CYAN_MED   = '#0891B2'
C_CYAN_LIGHT = '#ECFEFF'
C_CYAN_BORDER= '#67E8F9'


# ==============================================================================
# 1. HÌNH 1.1: SƠ ĐỒ PHÂN LOẠI CÁC PHƯƠNG PHÁP PHÁT HIỆN TÉ NGÃ (f_methods)
# ==============================================================================
def gen_pro_methods():
    fig = plt.figure(figsize=(7.2, 7.6), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96.5, "PHÂN LOẠI CÁC PHƯƠNG PHÁP PHÁT HIỆN & CẢNH BÁO TÉ NGÃ",
            ha='center', va='center', fontsize=12.0, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.8, "So sánh các hướng tiếp cận công nghệ hiện nay và tính ưu việt của Gậy thông minh IoT",
            ha='center', va='center', fontsize=8.6, color=C_SLATE_500, fontstyle='italic')

    cards = [
        (26, 73.5, 47, 33, "1. THIẾT BỊ ĐEO TAY", "SMARTWATCH / BAND",
         C_AMBER_DARK, '#FFFDF5', C_AMBER_BORDER,
         [("[+] Ưu điểm:", "#059669", 'bold'),
          ("  • Nhỏ gọn, hiển thị giờ và đo nhịp tim", "#334155", 'normal'),
          ("[-] Hạn chế đối với người cao tuổi:", "#DC2626", 'bold'),
          ("  • Người già thường xuyên quên đeo vào tay", "#B91C1C", 'normal'),
          ("  • Phải sạc pin mỗi 1-2 ngày rất bất tiện", "#B91C1C", 'normal'),
          ("  • Thao tác trên màn hình cảm ứng nhỏ khó khăn", "#B91C1C", 'normal')]),

        (74, 73.5, 47, 33, "2. CAMERA THỊ GIÁC", "COMPUTER VISION AI",
         C_BLUE_DARK, '#F8FAFC', C_BLUE_BORDER,
         [("[+] Ưu điểm:", "#059669", 'bold'),
          ("  • Nhận diện tư thế chính xác qua học sâu AI", "#334155", 'normal'),
          ("[-] Hạn chế đối với người cao tuổi:", "#DC2626", 'bold'),
          ("  • Xâm phạm nghiêm trọng quyền riêng tư cá nhân", "#B91C1C", 'normal'),
          ("  • Điểm mù tại khu vực nhạy cảm (nhà tắm, phòng ngủ)", "#B91C1C", 'normal'),
          ("  • Chi phí lắp đặt và bảo trì hệ thống rất cao", "#B91C1C", 'normal')]),

        (26, 38.5, 47, 33, "3. CẢM BIẾN MÔI TRƯỜNG", "ÂM THANH / RUNG SÀN",
         C_CYAN_DARK, '#F0FDFA', C_CYAN_BORDER,
         [("[+] Ưu điểm:", "#059669", 'bold'),
          ("  • Hoạt động thụ động, không gắn trên người", "#334155", 'normal'),
          ("[-] Hạn chế đối với người cao tuổi:", "#DC2626", 'bold'),
          ("  • Rất dễ báo động giả do đồ vật rơi hoặc tiếng ồn", "#B91C1C", 'normal'),
          ("  • Giới hạn trong bán kính căn phòng đã lắp đặt", "#B91C1C", 'normal'),
          ("  • Thi công phức tạp trên sàn nhà và tường", "#B91C1C", 'normal')]),

        (74, 38.5, 47, 33, "4. RADAR KHÔNG DÂY", "mmWAVE / UWB RADAR",
         C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER,
         [("[+] Ưu điểm:", "#059669", 'bold'),
          ("  • Không ghi hình ảnh, bảo đảm tính riêng tư", "#334155", 'normal'),
          ("[-] Hạn chế đối với người cao tuổi:", "#DC2626", 'bold'),
          ("  • Giá thành linh kiện radar chuyên dụng rất đắt", "#B91C1C", 'normal'),
          ("  • Bị che chắn và tán xạ bởi tường và đồ nội thất", "#B91C1C", 'normal'),
          ("  • Không thể mang theo khi đi lại ngoài trời", "#B91C1C", 'normal')]),
    ]

    for cx, cy, cw, ch, title, badge, hcol, bgcol, bcol, lines in cards:
        x0, y0 = cx - cw/2, cy - ch/2
        ax.add_patch(FancyBboxPatch((x0+0.4, y0-0.4), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc='#0F172A', ec='none', alpha=0.08, zorder=1))
        ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc=bgcol, ec=bcol, lw=1.2, zorder=2))
        ax.add_patch(FancyBboxPatch((x0, y0 + ch - 7.5), cw, 7.5, boxstyle='round,pad=0,rounding_size=1.5', fc=hcol, ec='none', zorder=3))
        ax.add_patch(Rectangle((x0, y0 + ch - 7.5), cw, 1.5, fc=hcol, ec='none', zorder=3))
        ax.text(x0 + 2.5, y0 + ch - 2.8, badge, ha='left', va='center', fontsize=7.2, fontweight='bold', color='#CBD5E1', zorder=4)
        ax.text(x0 + 2.5, y0 + ch - 5.5, title, ha='left', va='center', fontsize=9.2, fontweight='bold', color='#FFFFFF', zorder=4)

        ly = y0 + ch - 9.8
        for text, col, fwt in lines:
            fs = 8.0 if '[+]' in text or '[-]' in text else 7.8
            ax.text(x0 + 2.2, ly, text, ha='left', va='center', fontsize=fs, fontweight=fwt, color=col, zorder=4)
            ly -= 3.6

    # Bottom Hero Card: GẬY THÔNG MINH IOT
    bx, by, bw, bh = 50, 11.5, 95, 17.5
    bx0, by0 = bx - bw/2, by - bh/2
    ax.add_patch(FancyBboxPatch((bx0+0.5, by0-0.5), bw, bh, boxstyle='round,pad=0,rounding_size=2.0', fc='#064E3B', ec='none', alpha=0.15, zorder=1))
    ax.add_patch(FancyBboxPatch((bx0, by0), bw, bh, boxstyle='round,pad=0,rounding_size=2.0', fc='#ECFDF5', ec='#059669', lw=2.0, zorder=2))
    ax.add_patch(FancyBboxPatch((bx0, by0 + bh - 6.0), bw, 6.0, boxstyle='round,pad=0,rounding_size=2.0', fc='#064E3B', ec='none', zorder=3))
    ax.add_patch(Rectangle((bx0, by0 + bh - 6.0), bw, 2.0, fc='#064E3B', ec='none', zorder=3))
    ax.text(50, by0 + bh - 3.0, "★ HƯỚNG TIẾP CẬN CỦA ĐỀ TÀI: HỆ THỐNG GẬY THÔNG MINH IOT CẢNH BÁO TÉ NGÃ ★",
            ha='center', va='center', fontsize=9.6, fontweight='bold', color='#FFFFFF', zorder=4)

    feat_cols = [
        (bx0 + 2.5, "1. VẬT BẤT LY THÂN TỰ NHIÊN",
         ["• Người già luôn chủ động cầm gậy khi đi lại",
          "• Không gây cảm giác bị giám sát, không sợ quên"]),
        (bx0 + 34.0, "2. CẢM BIẾN & THUẬT TOÁN KÉP",
         ["• MPU6050 phát hiện ngã tức thì (SVM > 2.8g)",
          "• HC-SR04 quét vật cản và cảnh báo rung"]),
        (bx0 + 66.5, "3. CỨU HỘ ĐA TẦNG TOÀN DIỆN",
         ["• Kênh chính: Firebase RTDB qua Internet/4G",
          "• Kênh dự phòng: SMS và Cuộc gọi khẩn SOS"]),
    ]
    for fx, ftitle, flines in feat_cols:
        ax.text(fx, by0 + 8.5, ftitle, ha='left', va='center', fontsize=8.2, fontweight='bold', color='#064E3B', zorder=4)
        fy = by0 + 5.2
        for fl in flines:
            ax.text(fx, fy, fl, ha='left', va='center', fontsize=7.5, color='#0F172A', zorder=4)
            fy -= 2.8

    p = os.path.join(OUT, 'f_methods.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 2. HÌNH 1.2: MÔ HÌNH KIẾN TRÚC TỔNG THỂ CỦA HỆ THỐNG (f_overview)
# ==============================================================================
def gen_pro_overview():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96.5, "MÔ HÌNH KIẾN TRÚC TỔNG THỂ HỆ THỐNG GẬY THÔNG MINH IOT",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Hạ tầng phân tầng 3 lớp: Thiết bị ngoại vi (Edge Node) -> Cổng di động (Gateway) -> Đám mây (Cloud)",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    columns = [
        (13.5, 48.0, 23.0, 83.0, "GẬY THÔNG MINH IOT", "EDGE HARDWARE",
         C_EMERALD_DARK, '#ECFDF5', C_EMERALD_BORDER,
         [("VI ĐIỀU KHIỂN ESP32-S3", '#064E3B', 'bold'),
          ("• Dual-Core LX7 240MHz", '#334155', 'normal'),
          ("• 16MB Flash, 8MB PSRAM", '#334155', 'normal'),
          ("• BLE 5.0 GATT Server", '#059669', 'bold'),
          ("", '', ''),
          ("CẢM BIẾN ĐẦU VÀO", '#064E3B', 'bold'),
          ("• MPU6050 (Gia tốc + Góc)", '#334155', 'normal'),
          ("• HC-SR04 (Siêu âm 2-400cm)", '#334155', 'normal'),
          ("• ADC đo điện áp pin 18650", '#334155', 'normal'),
          ("", '', ''),
          ("CƠ CẤU CHẤP HÀNH", '#064E3B', 'bold'),
          ("• Còi Buzzer kêu to (GPIO 5)", '#B91C1C', 'bold'),
          ("• Motor rung (GPIO 6)", '#B91C1C', 'bold'),
          ("• Nguồn Pin + Sạc Type-C", '#334155', 'normal')]),

        (38.0, 48.0, 23.0, 83.0, "ĐIỆN THOẠI NGƯỜI DÙNG", "MOBILE GATEWAY",
         C_BLUE_DARK, '#EFF6FF', C_BLUE_BORDER,
         [("FLUTTER BACKGROUND SERVICE", '#1E3A8A', 'bold'),
          ("• Dịch vụ chạy ngầm 24/7", '#2563EB', 'bold'),
          ("• Tự khởi động cùng hệ máy", '#334155', 'normal'),
          ("• Duy trì kết nối BLE liên tục", '#334155', 'normal'),
          ("", '', ''),
          ("ĐỊNH VỊ VÀ ĐIỀU PHỐI", '#1E3A8A', 'bold'),
          ("• GPS lấy tọa độ chính xác", '#334155', 'normal'),
          ("• Nhận diện ngã tức thì", '#334155', 'normal'),
          ("• Đếm ngược 15s tự động", '#D97706', 'bold'),
          ("", '', ''),
          ("CỨU HỘ NGOẠI TUYẾN", '#1E3A8A', 'bold'),
          ("• Gửi SMS kèm vị trí Maps", '#B91C1C', 'bold'),
          ("• Tự động gọi điện SOS", '#B91C1C', 'bold'),
          ("• Hoạt động khi mất mạng", '#059669', 'bold')]),

        (62.5, 48.0, 23.0, 83.0, "FIREBASE CLOUD & GSM", "BACKEND & DỰ PHÒNG",
         C_AMBER_DARK, '#FFFBEB', C_AMBER_BORDER,
         [("FIREBASE REALTIME DB", '#78350F', 'bold'),
          ("• CSDL JSON thời gian thực", '#334155', 'normal'),
          ("• Độ trễ truyền dẫn cực thấp", '#D97706', 'bold'),
          ("• Đồng bộ tức thì tới Giám Hộ", '#334155', 'normal'),
          ("• CSDL lịch sử sự cố ngã", '#334155', 'normal'),
          ("", '', ''),
          ("BẢO MẬT HỆ THỐNG", '#78350F', 'bold'),
          ("• Xác thực Firebase Auth", '#334155', 'normal'),
          ("• Rule bảo mật phân quyền", '#334155', 'normal'),
          ("", '', ''),
          ("KÊNH VIỄN THÔNG DỰ PHÒNG", '#78350F', 'bold'),
          ("• Mạng di động GSM toàn quốc", '#B91C1C', 'bold'),
          ("• Tin nhắn SMS kèm tọa độ", '#B91C1C', 'normal'),
          ("• Cuộc gọi khẩn thoại trực tiếp", '#B91C1C', 'normal')]),

        (87.0, 48.0, 23.0, 83.0, "ĐIỆN THOẠI GIÁM HỘ", "MONITORING APP",
         C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER,
         [("GIÁM SÁT THỜI GIAN THỰC", '#4C1D95', 'bold'),
          ("• Luồng Stream Data trực tiếp", '#7C3AED', 'bold'),
          ("• Bản đồ OpenStreetMap", '#334155', 'normal'),
          ("• Cập nhật Marker vị trí gậy", '#334155', 'normal'),
          ("• Hiển thị mức pin và cự ly", '#334155', 'normal'),
          ("", '', ''),
          ("BÁO ĐỘNG KHẨN CẤP", '#4C1D95', 'bold'),
          ("• Còi báo động hú âm lượng max", '#B91C1C', 'bold'),
          ("• Màn hình đỏ chớp cảnh báo", '#B91C1C', 'bold'),
          ("• Rung chuông liên tục", '#B91C1C', 'normal'),
          ("", '', ''),
          ("HỖ TRỢ CỨU HỘ", '#4C1D95', 'bold'),
          ("• Dẫn đường qua Google Maps", '#059669', 'bold'),
          ("• Xem lịch sử sự cố ngã", '#334155', 'normal'),
          ("• Nút gọi ngay cho người già", '#334155', 'normal')]),
    ]

    for cx, cy, cw, ch, title, badge, hcol, bgcol, bcol, lines in columns:
        x0, y0 = cx - cw/2, cy - ch/2
        ax.add_patch(FancyBboxPatch((x0+0.35, y0-0.35), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc='#0F172A', ec='none', alpha=0.08, zorder=1))
        ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc=bgcol, ec=bcol, lw=1.2, zorder=2))
        ax.add_patch(FancyBboxPatch((x0, y0 + ch - 7.5), cw, 7.5, boxstyle='round,pad=0,rounding_size=1.5', fc=hcol, ec='none', zorder=3))
        ax.add_patch(Rectangle((x0, y0 + ch - 7.5), cw, 1.5, fc=hcol, ec='none', zorder=3))
        ax.text(cx, y0 + ch - 2.5, badge, ha='center', va='center', fontsize=6.8, fontweight='bold', color='#CBD5E1', zorder=4)
        ax.text(cx, y0 + ch - 5.2, title, ha='center', va='center', fontsize=8.2, fontweight='bold', color='#FFFFFF', zorder=4)

        ly = y0 + ch - 9.8
        for text, col, fwt in lines:
            if not text:
                ly -= 1.8
                continue
            fs = 7.6 if any(k in text for k in ['VI ĐIỀU KHIỂN', 'CẢM BIẾN', 'CƠ CẤU', 'FLUTTER', 'ĐỊNH VỊ', 'CỨU HỘ', 'FIREBASE', 'BẢO MẬT', 'KÊNH', 'GIÁM SÁT', 'BÁO ĐỘNG', 'HỖ TRỢ']) else 7.0
            ax.text(x0 + 1.2, ly, text, ha='left', va='center', fontsize=fs, fontweight=fwt, color=col, zorder=4)
            ly -= 3.2

    # Connectors between columns - carefully placed at gaps
    ax.annotate("", xy=(26.5, 60), xytext=(25.0, 60), arrowprops=dict(arrowstyle="->", color=C_EMERALD_MED, lw=2.0))
    ax.add_patch(FancyBboxPatch((23.6, 57.8), 4.3, 4.4, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec=C_EMERALD_MED, lw=1.2, zorder=5))
    ax.text(25.75, 60.0, "BLE\n5.0", ha='center', va='center', fontsize=6.2, fontweight='bold', color=C_EMERALD_DARK, zorder=6)

    ax.annotate("", xy=(51.0, 72), xytext=(49.5, 72), arrowprops=dict(arrowstyle="->", color=C_BLUE_MED, lw=2.0))
    ax.add_patch(FancyBboxPatch((48.2, 69.8), 4.1, 4.4, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec=C_BLUE_MED, lw=1.2, zorder=5))
    ax.text(50.25, 72.0, "WiFi\n4G", ha='center', va='center', fontsize=6.2, fontweight='bold', color=C_BLUE_DARK, zorder=6)

    ax.annotate("", xy=(51.0, 22), xytext=(49.5, 22), arrowprops=dict(arrowstyle="->", color=C_ROSE_MED, lw=2.0, ls='--'))
    ax.add_patch(FancyBboxPatch((48.0, 19.8), 4.5, 4.4, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec=C_ROSE_MED, lw=1.2, zorder=5))
    ax.text(50.25, 22.0, "SMS\nCALL", ha='center', va='center', fontsize=6.0, fontweight='bold', color=C_ROSE_DARK, zorder=6)

    ax.annotate("", xy=(75.5, 72), xytext=(74.0, 72), arrowprops=dict(arrowstyle="->", color=C_AMBER_MED, lw=2.0))
    ax.add_patch(FancyBboxPatch((72.7, 69.8), 4.1, 4.4, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec=C_AMBER_MED, lw=1.2, zorder=5))
    ax.text(74.75, 72.0, "SYNC\nJSON", ha='center', va='center', fontsize=6.0, fontweight='bold', color=C_AMBER_DARK, zorder=6)

    ax.annotate("", xy=(75.5, 22), xytext=(74.0, 22), arrowprops=dict(arrowstyle="->", color=C_ROSE_MED, lw=2.0, ls='--'))
    ax.add_patch(FancyBboxPatch((72.5, 19.8), 4.5, 4.4, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec=C_ROSE_MED, lw=1.2, zorder=5))
    ax.text(74.75, 22.0, "SMS\nSOS", ha='center', va='center', fontsize=6.0, fontweight='bold', color=C_ROSE_DARK, zorder=6)

    p = os.path.join(OUT, 'f_overview.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 3. HÌNH 2.1: SƠ ĐỒ KIẾN TRÚC VI ĐIỀU KHIỂN ESP32-S3 VÀ NGOẠI VI (f_esp32)
# ==============================================================================
def gen_pro_esp32():
    # Width 7.2 in x 5.6 in. No wire label collisions!
    fig = plt.figure(figsize=(7.2, 5.6), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96.5, "SƠ ĐỒ KIẾN TRÚC VI ĐIỀU KHIỂN ESP32-S3 VÀ PHÂN BỔ NGOẠI VI I/O",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Bố trí phân luồng tín hiệu cảm biến đầu vào (Inputs) và cơ cấu chấp hành - truyền thông đầu ra (Outputs)",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # Chip ESP32 ở trung tâm: X = 50, W = 32, H = 83
    cx, cy, cw, ch = 50, 47.0, 32.0, 83.0
    x0, y0 = cx - cw/2, cy - ch/2
    ax.add_patch(FancyBboxPatch((x0+0.4, y0-0.4), cw, ch, boxstyle='round,pad=0,rounding_size=2.0', fc='#0F172A', ec='none', alpha=0.15, zorder=1))
    ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=2.0', fc='#0F172A', ec='#334155', lw=1.5, zorder=2))

    ax.text(cx, y0 + ch - 3.2, "ESPRESSIF SYSTEMS", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#94A3B8', zorder=4)
    ax.text(cx, y0 + ch - 6.0, "ESP32-S3-WROOM-1 (N16R8)", ha='center', va='center', fontsize=8.6, fontweight='bold', color='#FFFFFF', zorder=4)

    # 6 Silicon Cores
    sub_blocks = [
        (cx - 7.5, y0 + ch - 16, 13.5, 12, "CPU XTENSA LX7", "Dual-Core 240MHz\n512KB SRAM nội"),
        (cx + 7.5, y0 + ch - 16, 13.5, 12, "BỘ NHỚ MỞ RỘNG", "16MB SPI Flash\n8MB Octal PSRAM"),
        (cx - 7.5, y0 + ch - 32, 13.5, 12, "VÔ TUYẾN 2.4GHz", "Bluetooth 5.0 BLE\nWi-Fi 802.11 b/g/n"),
        (cx + 7.5, y0 + ch - 32, 13.5, 12, "QUẢN LÝ NĂNG LƯỢNG", "RTC + ULP Coproc\nDeep Sleep 5µA"),
        (cx - 7.5, y0 + ch - 48, 13.5, 12, "NGOẠI VI ANALOG", "12-bit ADC SAR\nĐo điện áp pin"),
        (cx + 7.5, y0 + ch - 48, 13.5, 12, "GIAO TIẾP SỐ I/O", "I2C Fast Mode 400k\nGPIO, UART, PWM"),
    ]
    for sbx, sby, sbw, sbh, sbtitle, sbdesc in sub_blocks:
        ax.add_patch(FancyBboxPatch((sbx - sbw/2, sby - sbh/2), sbw, sbh, boxstyle='round,pad=0,rounding_size=1.0', fc='#1E293B', ec='#475569', lw=1.0, zorder=3))
        ax.text(sbx, sby + 3.0, sbtitle, ha='center', va='center', fontsize=6.6, fontweight='bold', color='#38BDF8', zorder=4)
        ax.text(sbx, sby - 2.2, sbdesc, ha='center', va='center', fontsize=6.0, color='#E2E8F0', zorder=4)

    ax.text(cx, y0 + 13.0, "THUẬT TOÁN FSM PHÁT HIỆN TÉ NGÃ", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FCD34D', zorder=4)
    ax.text(cx, y0 + 7.0, "Gia tốc SVM > 2.8g | Góc nghiêng > 60°\nLọc nhiễu siêu âm | Cảnh báo tự động", ha='center', va='center', fontsize=6.2, color='#E2E8F0', zorder=4)

    # 3 Khối INPUTS bên trái (X = 15.0, W = 26)
    # Gap giữa Input và Chip: x_max = 28.0, x_chip = 34.0 (gap = 6.0)
    inputs = [
        (15.0, 73.0, 26, 21, "CẢM BIẾN QUÁN TÍNH MPU6050", "I2C BUS", C_AMBER_DARK, '#FFFDF5', C_AMBER_BORDER,
         ["• Gia tốc 3 trục (±8g) & Con quay", "• Ngưỡng phát hiện ngã SVM > 2.8g", "• Tần số lấy mẫu: 50Hz liên tục", "• Giao tiếp: GPIO 8 (SDA), GPIO 9 (SCL)"],
         73.0),

        (15.0, 47.0, 26, 21, "CẢM BIẾN SIÊU ÂM HC-SR04", "SONAR", C_CYAN_DARK, '#F0FDFA', C_CYAN_BORDER,
         ["• Phát sóng siêu âm tần số 40kHz", "• Khoảng cách phát hiện: 2cm - 400cm", "• Cự ly kích hoạt rung: < 150cm", "• Kết nối: TRIG: GPIO 16 | ECHO: GPIO 17"],
         47.0),

        (15.0, 21.0, 26, 21, "MẠCH ĐO ĐIỆN ÁP PIN 18650", "ADC 12-BIT", C_EMERALD_DARK, '#ECFDF5', C_EMERALD_BORDER,
         ["• Cầu phân áp 1:2 (R1=100k, R2=100k)", "• Điện áp Pin: 3.0V - 4.2V an toàn", "• Báo động pin yếu khi Vbat < 3.3V", "• Kết nối chân: ADC1_CH3 (GPIO 4)"],
         21.0),
    ]

    for ix, iy, iw, ih, ititle, ibadge, ihcol, ibgcol, ibcol, ilines, line_y in inputs:
        ix0, iy0 = ix - iw/2, iy - ih/2
        ax.add_patch(FancyBboxPatch((ix0+0.35, iy0-0.35), iw, ih, boxstyle='round,pad=0,rounding_size=1.2', fc='#0F172A', ec='none', alpha=0.08, zorder=1))
        ax.add_patch(FancyBboxPatch((ix0, iy0), iw, ih, boxstyle='round,pad=0,rounding_size=1.2', fc=ibgcol, ec=ibcol, lw=1.2, zorder=2))
        ax.add_patch(FancyBboxPatch((ix0, iy0 + ih - 6.0), iw, 6.0, boxstyle='round,pad=0,rounding_size=1.2', fc=ihcol, ec='none', zorder=3))
        ax.add_patch(Rectangle((ix0, iy0 + ih - 6.0), iw, 1.2, fc=ihcol, ec='none', zorder=3))
        ax.text(ix, iy0 + ih - 2.0, ibadge, ha='center', va='center', fontsize=6.4, fontweight='bold', color='#CBD5E1', zorder=4)
        ax.text(ix, iy0 + ih - 4.2, ititle, ha='center', va='center', fontsize=7.4, fontweight='bold', color='#FFFFFF', zorder=4)

        ly = iy0 + ih - 8.2
        for line in ilines:
            is_pin = 'Giao tiếp:' in line or 'Kết nối:' in line
            fcol = ihcol if is_pin else '#0F172A'
            fwt = 'bold' if is_pin else 'normal'
            ax.text(ix0 + 1.2, ly, line, ha='left', va='center', fontsize=6.6, color=fcol, fontweight=fwt, zorder=4)
            ly -= 2.5

        # Wire connecting to ESP32 with arrow
        ax.annotate("", xy=(cx - cw/2, line_y), xytext=(ix + iw/2, line_y),
                    arrowprops=dict(arrowstyle="->", color=ihcol, lw=2.0))

    # 3 Khối OUTPUTS bên phải (X = 85.0, W = 26)
    outputs = [
        (85.0, 73.0, 26, 21, "CÒI BÁO ĐỘNG BUZZER 5V", "ALARM", C_ROSE_DARK, '#FFF1F2', C_ROSE_BORDER,
         ["• Còi chíp Active 5V công suất lớn", "• Âm lượng > 85dB gây chú ý xung quanh", "• Kích hoạt ngay khi có va chạm té ngã", "• Điều khiển: DIGITAL OUT (GPIO 5)"],
         73.0),

        (85.0, 47.0, 26, 21, "MẠCH CÔNG SUẤT MOTOR RUNG", "MOSFET", C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER,
         ["• MOSFET AOD4184N đóng ngắt tốc độ cao", "• Diode dập xung ngược 1N4007 bảo vệ", "• Rung xúc giác khi có vật cản gần", "• Điều khiển: GATE CONTROL (GPIO 6)"],
         47.0),

        (85.0, 21.0, 26, 21, "GIAO THỨC BLUETOOTH 5.0 LE", "GATT", C_BLUE_DARK, '#EFF6FF', C_BLUE_BORDER,
         ["• GATT Server (Service UUID: ...FFE0)", "• Đặc tính té ngã (Notify Characteristic)", "• Khoảng cách kết nối 10m ổn định", "• Phần cứng: 2.4GHz RF ANTENNA"],
         21.0),
    ]

    for ox, oy, ow, oh, otitle, obadge, ohcol, obgcol, obcol, olines, line_y in outputs:
        ox0, oy0 = ox - ow/2, oy - oh/2
        ax.add_patch(FancyBboxPatch((ox0+0.35, oy0-0.35), ow, oh, boxstyle='round,pad=0,rounding_size=1.2', fc='#0F172A', ec='none', alpha=0.08, zorder=1))
        ax.add_patch(FancyBboxPatch((ox0, oy0), ow, oh, boxstyle='round,pad=0,rounding_size=1.2', fc=obgcol, ec=obcol, lw=1.2, zorder=2))
        ax.add_patch(FancyBboxPatch((ox0, oy0 + oh - 6.0), ow, 6.0, boxstyle='round,pad=0,rounding_size=1.2', fc=ohcol, ec='none', zorder=3))
        ax.add_patch(Rectangle((ox0, oy0 + oh - 6.0), ow, 1.2, fc=ohcol, ec='none', zorder=3))
        ax.text(ox, oy0 + oh - 2.0, obadge, ha='center', va='center', fontsize=6.4, fontweight='bold', color='#CBD5E1', zorder=4)
        ax.text(ox, oy0 + oh - 4.2, otitle, ha='center', va='center', fontsize=7.4, fontweight='bold', color='#FFFFFF', zorder=4)

        ly = oy0 + oh - 8.2
        for line in olines:
            is_pin = 'Điều khiển:' in line or 'Phần cứng:' in line
            fcol = ohcol if is_pin else '#0F172A'
            fwt = 'bold' if is_pin else 'normal'
            ax.text(ox0 + 1.2, ly, line, ha='left', va='center', fontsize=6.6, color=fcol, fontweight=fwt, zorder=4)
            ly -= 2.5

        # Wire connecting from ESP32 to Output with arrow
        ax.annotate("", xy=(ox - ow/2, line_y), xytext=(cx + cw/2, line_y),
                    arrowprops=dict(arrowstyle="->", color=ohcol, lw=2.0))

    p = os.path.join(OUT, 'f_esp32.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 4. HÌNH 3.1: SƠ ĐỒ KHỐI CHỨC NĂNG HOÀN CHỈNH (f_block_diag)
# ==============================================================================
def gen_pro_block_diag():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96.5, "SƠ ĐỒ KHỐI CHỨC NĂNG HOÀN CHỈNH CỦA HỆ THỐNG GẬY THÔNG MINH",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Cấu trúc 3 phân hệ chính: Phần cứng Edge -> Mobile Gateway -> Cloud & Giám Sát",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # 3 Khối lớn tương ứng 3 cột
    # Cột 1: PHẦN CỨNG GẬY (X = 18, W = 31, H = 84)
    # Cột 2: CỔNG DI ĐỘNG (X = 50, W = 29, H = 84)
    # Cột 3: CLOUD & GIÁM SÁT (X = 82, W = 31, H = 84)
    cols = [
        (18, 48, 31, 84, "PHẦN CỨNG GẬY THÔNG MINH", "EDGE HARDWARE", C_EMERALD_DARK, '#ECFDF5', C_EMERALD_BORDER),
        (50, 48, 29, 84, "MOBILE GATEWAY (NGƯỜI DÙNG)", "SMARTPHONE", C_BLUE_DARK, '#EFF6FF', C_BLUE_BORDER),
        (82, 48, 31, 84, "ĐÁM MÂY & GIÁM SÁT", "CLOUD & GUARDIAN", C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER),
    ]

    for cx, cy, cw, ch, title, badge, hcol, bgcol, bcol in cols:
        x0, y0 = cx - cw/2, cy - ch/2
        ax.add_patch(FancyBboxPatch((x0+0.35, y0-0.35), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc='#0F172A', ec='none', alpha=0.08, zorder=1))
        ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc=bgcol, ec=bcol, lw=1.2, zorder=2))
        ax.add_patch(FancyBboxPatch((x0, y0 + ch - 7.5), cw, 7.5, boxstyle='round,pad=0,rounding_size=1.5', fc=hcol, ec='none', zorder=3))
        ax.add_patch(Rectangle((x0, y0 + ch - 7.5), cw, 1.5, fc=hcol, ec='none', zorder=3))
        ax.text(cx, y0 + ch - 2.5, badge, ha='center', va='center', fontsize=6.6, fontweight='bold', color='#CBD5E1', zorder=4)
        ax.text(cx, y0 + ch - 5.2, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#FFFFFF', zorder=4)

    # Sub-boxes bên trong Cột 1 (Phần cứng)
    # 4 sub-boxes: Nguồn, Cảm biến, ESP32, Cảnh báo (sắp xếp từ trên xuống dưới không chạm header)
    sub1 = [
        (18, 73.0, 27, 13, "KHỐI XỬ LÝ TRUNG TÂM", "ESP32-S3 Dual-Core 240MHz\nThuật toán FSM phân loại té ngã\nBLE 5.0 GATT Server truyền dữ liệu", C_EMERALD_DARK),
        (18, 56.5, 27, 13, "KHỐI CẢM BIẾN ĐẦU VÀO", "MPU6050: Gia tốc 3 trục + Con quay\nHC-SR04: Đo khoảng cách vật cản\nADC: Đo điện áp pin thời gian thực", '#047857'),
        (18, 40.0, 27, 13, "KHỐI CẢNH BÁO TẠI CHỖ", "Còi chíp Buzzer kêu to (GPIO 5)\nMotor rung phản hồi (GPIO 6)\nKích hoạt tức thì khi va chạm", '#B91C1C'),
        (18, 23.5, 27, 13, "KHỐI NGUỒN HỆ THỐNG", "Pin sạc Li-ion 18650 3.7V 2600mAh\nMạch MH-CD42 tăng áp 5V ổn định\nCổng sạc Type-C tiện lợi", '#334155'),
    ]
    for sx, sy, sw, sh, stitle, sdesc, scol in sub1:
        ax.add_patch(FancyBboxPatch((sx - sw/2, sy - sh/2), sw, sh, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec=scol, lw=1.1, zorder=4))
        ax.text(sx, sy + 3.8, stitle, ha='center', va='center', fontsize=7.0, fontweight='bold', color=scol, zorder=5)
        ax.text(sx, sy - 1.8, sdesc, ha='center', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    # Sub-boxes bên trong Cột 2 (Mobile Gateway)
    sub2 = [
        (50, 73.0, 25, 13, "FLUTTER BACKGROUND SERVICE", "Dịch vụ chạy ngầm 24/7 trên Android\nDuy trì kết nối BLE liên tục\nTự động phục hồi khi ngắt kết nối", C_BLUE_DARK),
        (50, 56.5, 25, 13, "ĐỊNH VỊ GPS VÀ XỬ LÝ CỨU HỘ", "Lấy tọa độ vị trí hiện tại của gậy\nKích hoạt đếm ngược 15 giây hủy\nNgăn chặn hoàn toàn báo động sai", '#1D4ED8'),
        (50, 40.0, 25, 13, "KÊNH TRUYỀN DỮ LIỆU CHÍNH", "Đồng bộ trạng thái lên Firebase qua 4G\nĐẩy sự kiện té ngã thời gian thực\nĐộ trễ truyền dẫn dưới 1.2 giây", '#059669'),
        (50, 23.5, 25, 13, "KÊNH DỰ PHÒNG GSM / SMS", "Tự động gửi SMS tọa độ Google Maps\nQuay số gọi khẩn cấp cho người thân\nHoạt động ngay cả khi không có mạng", '#B91C1C'),
    ]
    for sx, sy, sw, sh, stitle, sdesc, scol in sub2:
        ax.add_patch(FancyBboxPatch((sx - sw/2, sy - sh/2), sw, sh, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec=scol, lw=1.1, zorder=4))
        ax.text(sx, sy + 3.8, stitle, ha='center', va='center', fontsize=6.8, fontweight='bold', color=scol, zorder=5)
        ax.text(sx, sy - 1.8, sdesc, ha='center', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    # Sub-boxes bên trong Cột 3 (Cloud & Guardian)
    sub3 = [
        (82, 73.0, 27, 13, "FIREBASE REALTIME DATABASE", "Cơ sở dữ liệu đám mây JSON trực tiếp\nĐồng bộ hai chiều theo luồng Stream\nLưu trữ lịch sử vị trí và nhật ký sự cố", '#78350F'),
        (82, 56.5, 27, 13, "ỨNG DỤNG DI ĐỘNG GIÁM HỘ", "Flutter App giao diện thân thiện\nBản đồ số định vị thời gian thực\nHiển thị chi tiết mức pin và tình trạng", C_PURPLE_DARK),
        (82, 40.0, 27, 13, "HỆ THỐNG CẢNH BÁO TỨC THÌ", "Còi hú báo động âm lượng tối đa\nBanner đỏ khẩn cấp toàn màn hình\nRung chuông cảnh báo người giám hộ", '#B91C1C'),
        (82, 23.5, 27, 13, "ĐIỀU HƯỚNG CỨU TRỢ KHẨN CẤP", "Tích hợp Google Maps dẫn đường\nĐịnh tuyến đường đi ngắn nhất tới nạn nhân\nNút gọi nhanh hỗ trợ cứu hộ y tế", '#047857'),
    ]
    for sx, sy, sw, sh, stitle, sdesc, scol in sub3:
        ax.add_patch(FancyBboxPatch((sx - sw/2, sy - sh/2), sw, sh, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec=scol, lw=1.1, zorder=4))
        ax.text(sx, sy + 3.8, stitle, ha='center', va='center', fontsize=6.8, fontweight='bold', color=scol, zorder=5)
        ax.text(sx, sy - 1.8, sdesc, ha='center', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    # Connecting arrows across columns
    ax.annotate("", xy=(37.5, 73), xytext=(33.5, 73), arrowprops=dict(arrowstyle="->", color=C_EMERALD_MED, lw=2.2))
    ax.text(35.5, 75.2, "BLE 5.0", ha='center', va='center', fontsize=6.4, fontweight='bold', color=C_EMERALD_DARK)

    ax.annotate("", xy=(68.5, 73), xytext=(64.5, 73), arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.2))
    ax.text(66.5, 75.2, "WiFi / 4G", ha='center', va='center', fontsize=6.4, fontweight='bold', color='#1D4ED8')

    ax.annotate("", xy=(68.5, 23.5), xytext=(64.5, 23.5), arrowprops=dict(arrowstyle="->", color='#B91C1C', lw=2.2, ls='--'))
    ax.text(66.5, 25.7, "GSM / SMS", ha='center', va='center', fontsize=6.4, fontweight='bold', color='#B91C1C')

    p = os.path.join(OUT, 'f_block_diag.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 5. HÌNH 3.2: SƠ ĐỒ NGUYÊN LÝ KẾT NỐI CHI TIẾT (f_schematic)
# ==============================================================================
def gen_pro_schematic():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96.5, "SƠ ĐỒ NGUYÊN LÝ KẾT NỐI CHI TIẾT PHẦN CỨNG ESP32-S3",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Sơ đồ đấu nối dây mạch điện tử thực tế chuẩn xác 100% theo mã nguồn firmware config.h",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # Trung tâm: ESP32-S3 Module IC (X = 50, Y = 48, W = 32, H = 82)
    cx, cy, cw, ch = 50, 48.0, 32.0, 82.0
    x0, y0 = cx - cw/2, cy - ch/2
    ax.add_patch(FancyBboxPatch((x0+0.4, y0-0.4), cw, ch, boxstyle='round,pad=0,rounding_size=2.0', fc='#0F172A', ec='none', alpha=0.15, zorder=1))
    ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=2.0', fc='#0F172A', ec='#334155', lw=1.5, zorder=2))

    ax.text(cx, y0 + ch - 3.5, "ESP32-S3-WROOM-1 (N16R8)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF', zorder=4)
    ax.text(cx, y0 + ch - 6.5, "Xtensa Dual-Core 240MHz | 16MB Flash | 8MB PSRAM", ha='center', va='center', fontsize=6.2, color='#94A3B8', zorder=4)

    # Bố trí danh sách chân ESP32 ở 2 mép chip
    # Mép trái: SDA (8), SCL (9), TRIG (16), ECHO (17), ADC_PIN (4), 3V3, GND
    # Mép phải: BUZZER (5), VIBRATOR (6), 5V_IN, GND_COM
    pins_left = [
        ("GPIO 8 (SDA)", 74.0, '#D97706'),
        ("GPIO 9 (SCL)", 68.0, '#D97706'),
        ("GPIO 16 (TRIG)", 52.0, '#0891B2'),
        ("GPIO 17 (ECHO)", 46.0, '#0891B2'),
        ("GPIO 4 (ADC1)", 30.0, '#059669'),
        ("3V3 OUT", 18.0, '#DC2626'),
        ("GND", 12.0, '#64748B'),
    ]
    for pname, py, pcol in pins_left:
        ax.plot([x0, x0 + 1.8], [py, py], color=pcol, lw=2.5, zorder=4)
        ax.text(x0 + 2.5, py, pname, ha='left', va='center', fontsize=5.8, fontfamily='monospace', fontweight='bold', color='#E2E8F0', zorder=5)

    pins_right = [
        ("GPIO 5 (BUZZER)", 74.0, '#E11D48'),
        ("GPIO 6 (VIBRATOR)", 52.0, '#7C3AED'),
        ("VIN (5V DC)", 30.0, '#DC2626'),
        ("GND (CHUNG)", 18.0, '#64748B'),
    ]
    for pname, py, pcol in pins_right:
        ax.plot([x0 + cw - 1.8, x0 + cw], [py, py], color=pcol, lw=2.5, zorder=4)
        ax.text(x0 + cw - 2.5, py, pname, ha='right', va='center', fontsize=5.8, fontfamily='monospace', fontweight='bold', color='#E2E8F0', zorder=5)

    # Core chip center box
    ax.add_patch(FancyBboxPatch((cx - 10, y0 + 10), 20, 24, boxstyle='round,pad=0,rounding_size=1.0', fc='#1E293B', ec='#475569', lw=1.0, zorder=3))
    ax.text(cx, y0 + 26, "RF TRANCEIVER", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#38BDF8', zorder=4)
    ax.text(cx, y0 + 22, "BLE 5.0 + 2.4GHz Wi-Fi", ha='center', va='center', fontsize=6.0, color='#E2E8F0', zorder=4)
    ax.text(cx, y0 + 16, "GATT Server: SmartCane", ha='center', va='center', fontsize=6.0, fontfamily='monospace', color='#FCD34D', zorder=4)

    # Left Peripheral Cards
    # 1. MPU6050
    ax.add_patch(FancyBboxPatch((3.0, 62.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFDF5', ec=C_AMBER_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((3.0, 77.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_AMBER_DARK, ec='none', zorder=4))
    ax.text(15.5, 79.5, "MPU6050 (6-DOF IMU)", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(4.5, 73.5, "• VCC -> 3.3V, GND -> GND", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(4.5, 69.5, "• SDA -> GPIO 8 (Kéo 4.7kΩ)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_AMBER_DARK, zorder=5)
    ax.text(4.5, 65.5, "• SCL -> GPIO 9 (Kéo 4.7kΩ)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_AMBER_DARK, zorder=5)

    # Wire MPU6050 to ESP32
    ax.plot([28.0, 34.0], [74.0, 74.0], color='#D97706', lw=1.8, zorder=6)
    ax.plot([28.0, 34.0], [68.0, 68.0], color='#D97706', lw=1.8, zorder=6)

    # 2. HC-SR04
    ax.add_patch(FancyBboxPatch((3.0, 38.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#F0FDFA', ec=C_CYAN_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((3.0, 53.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_CYAN_DARK, ec='none', zorder=4))
    ax.text(15.5, 55.5, "HC-SR04 (SIÊU ÂM)", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(4.5, 49.5, "• VCC -> 5V (Nguồn pin MH-CD42)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(4.5, 45.5, "• TRIG -> GPIO 16 (Xung 10µs)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_CYAN_DARK, zorder=5)
    ax.text(4.5, 41.5, "• ECHO -> GPIO 17 (Cầu 1k/2k)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_CYAN_DARK, zorder=5)

    # Wire HC-SR04 to ESP32
    ax.plot([28.0, 34.0], [52.0, 52.0], color='#0891B2', lw=1.8, zorder=6)
    ax.plot([28.0, 34.0], [46.0, 46.0], color='#0891B2', lw=1.8, zorder=6)

    # 3. Cầu phân áp Pin 18650
    ax.add_patch(FancyBboxPatch((3.0, 14.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#ECFDF5', ec=C_EMERALD_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((3.0, 29.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_EMERALD_DARK, ec='none', zorder=4))
    ax.text(15.5, 31.5, "MẠCH PHÂN ÁP ĐO PIN", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(4.5, 25.5, "• Pin 18650 (3.0V - 4.2V)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(4.5, 21.5, "• R1 = 100kΩ, R2 = 100kΩ (Chia 2)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(4.5, 17.5, "• Vout -> GPIO 4 (ADC1_CH3)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_EMERALD_DARK, zorder=5)

    # Wire Battery to ESP32
    ax.plot([28.0, 34.0], [30.0, 30.0], color='#059669', lw=1.8, zorder=6)

    # Right Peripheral Cards
    # 1. Buzzer
    ax.add_patch(FancyBboxPatch((72.0, 62.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFF1F2', ec=C_ROSE_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((72.0, 77.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_ROSE_DARK, ec='none', zorder=4))
    ax.text(84.5, 79.5, "CÒI BÁO ĐỘNG BUZZER", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(73.5, 73.5, "• Active Buzzer 5V (> 85dB)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(73.5, 69.5, "• Chân điều khiển: GPIO 5", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_ROSE_DARK, zorder=5)
    ax.text(73.5, 65.5, "• Kích mức CAO (HIGH) khi ngã", ha='left', va='center', fontsize=6.2, color='#B91C1C', zorder=5)

    # Wire ESP32 to Buzzer
    ax.plot([66.0, 72.0], [74.0, 74.0], color='#E11D48', lw=1.8, zorder=6)

    # 2. MOSFET Motor rung
    ax.add_patch(FancyBboxPatch((72.0, 38.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FAF5FF', ec=C_PURPLE_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((72.0, 53.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_PURPLE_DARK, ec='none', zorder=4))
    ax.text(84.5, 55.5, "MẠCH KÍCH MOTOR RUNG", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(73.5, 49.5, "• MOSFET AOD4184N (N-Channel)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(73.5, 45.5, "• Gate Control: GPIO 6", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_PURPLE_DARK, zorder=5)
    ax.text(73.5, 41.5, "• Diode 1N4007 dập xung ngược", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    # Wire ESP32 to Motor
    ax.plot([66.0, 72.0], [52.0, 52.0], color='#7C3AED', lw=1.8, zorder=6)

    # 3. Nguồn MH-CD42
    ax.add_patch(FancyBboxPatch((72.0, 14.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#EFF6FF', ec=C_BLUE_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((72.0, 29.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_BLUE_DARK, ec='none', zorder=4))
    ax.text(84.5, 31.5, "KHỐI NGUỒN MH-CD42", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(73.5, 25.5, "• Input: Pin Li-ion 3.7V 18650", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(73.5, 21.5, "• Output: 5V DC cấp ESP32 VIN", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_BLUE_DARK, zorder=5)
    ax.text(73.5, 17.5, "• Hỗ trợ vừa sạc vừa dùng (Type-C)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    # Wire MH-CD42 to ESP32
    ax.plot([66.0, 72.0], [30.0, 30.0], color='#DC2626', lw=1.8, zorder=6)

    p = os.path.join(OUT, 'f_schematic.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 6. HÌNH 2.2: CẤU TRÚC GATT PROFILE CỦA BLUETOOTH LOW ENERGY (f_gatt)
# ==============================================================================
def gen_pro_gatt():
    fig = plt.figure(figsize=(7.2, 5.6), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96.5, "CẤU TRÚC PHÂN TẦNG VÀ GATT PROFILE CỦA BLUETOOTH 5.0 LE",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Kiến trúc máy chủ GATT (GATT Server) trên firmware ESP32-S3 kết nối tới ứng dụng di động",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # Top Root Box: GATT PROFILE
    ax.add_patch(FancyBboxPatch((25, 81.0), 50, 9.0, boxstyle='round,pad=0,rounding_size=1.5', fc=C_SLATE_900, ec='none', zorder=2))
    ax.text(50, 86.8, "SMART CANE GATT PROFILE (DEVICE: ESP32-S3)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF', zorder=3)
    ax.text(50, 83.2, "Quản trị cơ chế đóng gói dữ liệu thuộc tính cảm biến và điều khiển thiết bị", ha='center', va='center', fontsize=6.8, color='#CBD5E1', zorder=3)

    # Connecting line to Primary Service
    ax.plot([50, 50], [81.0, 75.0], color=C_BLUE_DARK, lw=2.2, zorder=1)

    # Primary Service Card
    ax.add_patch(FancyBboxPatch((15, 60.0), 70, 15.0, boxstyle='round,pad=0,rounding_size=1.5', fc='#EFF6FF', ec=C_BLUE_MED, lw=1.5, zorder=2))
    ax.add_patch(FancyBboxPatch((15, 69.0), 70, 6.0, boxstyle='round,pad=0,rounding_size=1.5', fc=C_BLUE_DARK, ec='none', zorder=3))
    ax.text(50, 72.0, "PRIMARY SERVICE: DỊCH VỤ GẬY THÔNG MINH IOT", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#FFFFFF', zorder=4)
    ax.text(50, 65.5, "UUID: 0000FFE0-0000-1000-8000-00805F9B34FB | Khởi tạo bởi BLEDevice::createServer()", ha='center', va='center', fontsize=6.8, fontfamily='monospace', fontweight='bold', color=C_BLUE_DARK, zorder=4)
    ax.text(50, 62.0, "Đóng vai trò Service gốc, quản lý và phân phối 4 Characteristic chuyên biệt", ha='center', va='center', fontsize=6.4, color='#334155', zorder=4)

    # Connecting bus to 4 Characteristics
    ax.plot([50, 50], [60.0, 55.0], color=C_SLATE_700, lw=2.0, zorder=1)
    ax.plot([14, 86], [55.0, 55.0], color=C_SLATE_700, lw=2.0, zorder=1)

    # 4 Characteristics Cards
    chars = [
        (14.0, 27.0, 22.0, 48.0, "FALL ALERT", "UUID: ...FFE1", C_ROSE_DARK, '#FFF1F2', C_ROSE_BORDER,
         [("PROPERTIES", C_ROSE_DARK, 'bold'),
          ("• NOTIFY, READ", '#1E293B', 'normal'),
          ("", '', ''),
          ("PAYLOAD JSON", C_ROSE_DARK, 'bold'),
          ("• is_falling: bool", '#B91C1C', 'bold'),
          ("• svm_g: float", '#1E293B', 'normal'),
          ("• pitch_deg: float", '#1E293B', 'normal'),
          ("", '', ''),
          ("HOẠT ĐỘNG", C_ROSE_DARK, 'bold'),
          ("• Đẩy ngay tức thì khi", '#1E293B', 'normal'),
          ("  SVM > 2.8g", '#B91C1C', 'bold'),
          ("• Kích hoạt SOS", '#B91C1C', 'bold')]),

        (38.0, 27.0, 22.0, 48.0, "OBSTACLE DIST", "UUID: ...FFE2", C_CYAN_DARK, '#F0FDFA', C_CYAN_BORDER,
         [("PROPERTIES", C_CYAN_DARK, 'bold'),
          ("• NOTIFY, READ", '#1E293B', 'normal'),
          ("", '', ''),
          ("PAYLOAD JSON", C_CYAN_DARK, 'bold'),
          ("• distance_cm: int", '#0891B2', 'bold'),
          ("• is_warning: bool", '#0891B2', 'bold'),
          ("• buzz_active: bool", '#1E293B', 'normal'),
          ("", '', ''),
          ("HOẠT ĐỘNG", C_CYAN_DARK, 'bold'),
          ("• Cập nhật chu kỳ 50ms", '#1E293B', 'normal'),
          ("• Báo động vật cản", '#1E293B', 'normal'),
          ("  d < 150cm", '#0891B2', 'bold')]),

        (62.0, 27.0, 22.0, 48.0, "BATTERY LEVEL", "UUID: ...FFE3", C_EMERALD_DARK, '#ECFDF5', C_EMERALD_BORDER,
         [("PROPERTIES", C_EMERALD_DARK, 'bold'),
          ("• READ, NOTIFY", '#1E293B', 'normal'),
          ("", '', ''),
          ("PAYLOAD JSON", C_EMERALD_DARK, 'bold'),
          ("• percent: int (%)", '#059669', 'bold'),
          ("• vbat_mv: int", '#1E293B', 'normal'),
          ("• is_charging: bool", '#1E293B', 'normal'),
          ("", '', ''),
          ("HOẠT ĐỘNG", C_EMERALD_DARK, 'bold'),
          ("• Đọc ADC1_CH3", '#1E293B', 'normal'),
          ("• Chu kỳ gửi 10 giây", '#1E293B', 'normal'),
          ("• Cảnh báo pin < 20%", '#D97706', 'bold')]),

        (86.0, 27.0, 22.0, 48.0, "DEVICE CONTROL", "UUID: ...FFE4", C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER,
         [("PROPERTIES", C_PURPLE_DARK, 'bold'),
          ("• WRITE, READ", '#1E293B', 'normal'),
          ("", '', ''),
          ("PAYLOAD JSON", C_PURPLE_DARK, 'bold'),
          ("• cmd: RESET_ALARM", '#7C3AED', 'bold'),
          ("• set_dist_max: int", '#1E293B', 'normal'),
          ("• trigger_buzzer: int", '#1E293B', 'normal'),
          ("", '', ''),
          ("HOẠT ĐỘNG", C_PURPLE_DARK, 'bold'),
          ("• Nhận lệnh từ App", '#1E293B', 'normal'),
          ("• Tắt còi khi người già", '#1E293B', 'normal'),
          ("  hủy cảnh báo ngã", '#059669', 'bold')]),
    ]

    for cx, cy, cw, ch, title, badge, hcol, bgcol, bcol, lines in chars:
        # Connecting line from bus
        ax.plot([cx, cx], [55.0, cy + ch/2], color=hcol, lw=1.8, zorder=1)

        x0, y0 = cx - cw/2, cy - ch/2
        ax.add_patch(FancyBboxPatch((x0+0.35, y0-0.35), cw, ch, boxstyle='round,pad=0,rounding_size=1.2', fc='#0F172A', ec='none', alpha=0.08, zorder=2))
        ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=1.2', fc=bgcol, ec=bcol, lw=1.2, zorder=3))
        ax.add_patch(FancyBboxPatch((x0, y0 + ch - 6.5), cw, 6.5, boxstyle='round,pad=0,rounding_size=1.2', fc=hcol, ec='none', zorder=4))
        ax.add_patch(Rectangle((x0, y0 + ch - 6.5), cw, 1.2, fc=hcol, ec='none', zorder=4))
        ax.text(cx, y0 + ch - 2.2, badge, ha='center', va='center', fontsize=6.2, fontfamily='monospace', fontweight='bold', color='#CBD5E1', zorder=5)
        ax.text(cx, y0 + ch - 4.8, title, ha='center', va='center', fontsize=7.4, fontweight='bold', color='#FFFFFF', zorder=5)

        ly = y0 + ch - 8.5
        for text, col, fwt in lines:
            if not text:
                ly -= 1.6
                continue
            fs = 6.6 if 'PROPERTIES' in text or 'PAYLOAD' in text or 'HOẠT ĐỘNG' in text else 6.2
            ax.text(x0 + 1.2, ly, text, ha='left', va='center', fontsize=fs, fontweight=fwt, color=col, zorder=5)
            ly -= 2.6

    p = os.path.join(OUT, 'f_gatt.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 7. HÌNH 2.10: ĐỒNG BỘ HAI CHIỀU TRÊN FIREBASE RTDB (f_rtdb)
# ==============================================================================
def gen_pro_rtdb():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96.5, "CƠ CHẾ ĐỒNG BỘ DỮ LIỆU HAI CHIỀU TRÊN FIREBASE REALTIME DATABASE",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Cấu trúc dữ liệu JSON NoSQL và mô hình Publish/Subscribe qua kết nối WebSocket bảo mật",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # 3 Cột:
    # Cột 1: Mobile Gateway (X = 18, W = 30)
    # Cột 2: Firebase Realtime Database (X = 50, W = 30)
    # Cột 3: Monitor App Giám Hộ (X = 82, W = 30)
    rtdb_cols = [
        (18, 47, 30, 82, "APP NGƯỜI DÙNG GẬY", "MOBILE GATEWAY", C_BLUE_DARK, '#EFF6FF', C_BLUE_BORDER),
        (50, 47, 30, 82, "FIREBASE REALTIME DB", "CLOUD BACKEND", C_AMBER_DARK, '#FFFBEB', C_AMBER_BORDER),
        (82, 47, 30, 82, "APP NGƯỜI GIÁM HỘ", "MONITORING APP", C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER),
    ]

    for cx, cy, cw, ch, title, badge, hcol, bgcol, bcol in rtdb_cols:
        x0, y0 = cx - cw/2, cy - ch/2
        ax.add_patch(FancyBboxPatch((x0+0.35, y0-0.35), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc='#0F172A', ec='none', alpha=0.08, zorder=1))
        ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc=bgcol, ec=bcol, lw=1.2, zorder=2))
        ax.add_patch(FancyBboxPatch((x0, y0 + ch - 7.5), cw, 7.5, boxstyle='round,pad=0,rounding_size=1.5', fc=hcol, ec='none', zorder=3))
        ax.add_patch(Rectangle((x0, y0 + ch - 7.5), cw, 1.5, fc=hcol, ec='none', zorder=3))
        ax.text(cx, y0 + ch - 2.5, badge, ha='center', va='center', fontsize=6.6, fontweight='bold', color='#CBD5E1', zorder=4)
        ax.text(cx, y0 + ch - 5.2, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#FFFFFF', zorder=4)

    # Chi tiết Cột 1: Mobile Gateway
    ax.text(18, 80.0, "PHÁT HIỆN TÉ NGÃ & ĐẨY DỮ LIỆU", ha='center', va='center', fontsize=7.0, fontweight='bold', color=C_BLUE_DARK)
    ax.text(5.0, 75.5, "• Nhận Notify BLE từ gậy", ha='left', va='center', fontsize=6.4, color='#1E293B')
    ax.text(5.0, 72.0, "• Lấy tọa độ GPS thiết bị", ha='left', va='center', fontsize=6.4, color='#1E293B')
    ax.text(5.0, 68.5, "• Ghi JSON vào RTDB qua REST API", ha='left', va='center', fontsize=6.4, fontweight='bold', color='#2563EB')
    ax.text(5.0, 65.0, "• Thời gian phản hồi < 800ms", ha='left', va='center', fontsize=6.4, color='#059669')

    # Code snippet JSON Cột 1
    ax.add_patch(FancyBboxPatch((5.0, 16.0), 26.0, 45.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#0F172A', ec='#334155', lw=1.0, zorder=3))
    ax.text(18, 58.0, "JSON PAYLOAD (GỬI LÊN)", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#38BDF8', zorder=4)
    code_lines1 = [
        "{",
        '  "is_falling": true,',
        '  "timestamp": 1730501234,',
        '  "fall_type": "HARD_FALL",',
        '  "battery": 87,',
        '  "location": {',
        '    "lat": 10.85023,',
        '    "lng": 106.77192,',
        '    "accuracy": 4.5',
        '  },',
        '  "status": "SOS_ACTIVE"',
        "}"
    ]
    cy1 = 54.0
    for cl in code_lines1:
        ccol = '#F43F5E' if 'is_falling' in cl or 'SOS' in cl else ('#34D399' if 'location' in cl or 'lat' in cl or 'lng' in cl else '#E2E8F0')
        ax.text(6.5, cy1, cl, ha='left', va='center', fontsize=5.8, fontfamily='monospace', color=ccol, zorder=4)
        cy1 -= 3.2

    # Chi tiết Cột 2: Firebase Realtime Database
    ax.text(50, 80.0, "CÂY DỮ LIỆU ĐÁM MÂY (JSON)", ha='center', va='center', fontsize=7.0, fontweight='bold', color=C_AMBER_DARK)
    ax.add_patch(FancyBboxPatch((37.0, 16.0), 26.0, 59.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#1E293B', ec='#475569', lw=1.0, zorder=3))
    ax.text(50, 72.0, "DATABASE ROOT (JSON TREE)", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#FCD34D', zorder=4)
    tree_lines = [
        "root:",
        " └── users/",
        "      └── {user_id}/",
        "           ├── profile/",
        '           │    ├── name: "Cụ An"',
        '           │    └── age: 78',
        "           ├── cane_device/",
        '           │    ├── mac: "C8:2B..."',
        '           │    └── bat: 87',
        "           ├── current_state/",
        '           │    ├── is_falling: TRUE',
        '           │    └── alarm: ACTIVE',
        "           └── fall_history/",
        '                └── {event_id}/...'
    ]
    ty = 68.0
    for tl in tree_lines:
        tcol = '#F43F5E' if 'is_falling' in tl or 'alarm' in tl else ('#38BDF8' if 'cane' in tl or 'profile' in tl else '#E2E8F0')
        fwt = 'bold' if 'TRUE' in tl or 'ACTIVE' in tl else 'normal'
        ax.text(38.5, ty, tl, ha='left', va='center', fontsize=5.6, fontfamily='monospace', fontweight=fwt, color=tcol, zorder=4)
        ty -= 3.6

    # Chi tiết Cột 3: Monitor App Giám Hộ
    ax.text(82, 80.0, "LẮNG NGHE & PHẢN HỒI KHẨN", ha='center', va='center', fontsize=7.0, fontweight='bold', color=C_PURPLE_DARK)
    ax.text(69.0, 75.5, "• Luồng Stream .onValue()", ha='left', va='center', fontsize=6.4, color='#1E293B')
    ax.text(69.0, 72.0, "• Nhận ngay khi is_falling=true", ha='left', va='center', fontsize=6.4, fontweight='bold', color='#B91C1C')
    ax.text(69.0, 68.5, "• Kích hoạt còi hú max volume", ha='left', va='center', fontsize=6.4, fontweight='bold', color='#B91C1C')
    ax.text(69.0, 65.0, "• Cập nhật Marker bản đồ Maps", ha='left', va='center', fontsize=6.4, color='#059669')

    # Code snippet JSON Cột 3
    ax.add_patch(FancyBboxPatch((69.0, 16.0), 26.0, 45.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#0F172A', ec='#334155', lw=1.0, zorder=3))
    ax.text(82, 58.0, "EVENT STREAM (NHẬN VỀ)", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#A855F7', zorder=4)
    code_lines3 = [
        "EVENT: onDataChange()",
        "{",
        '  "alarm": "CRITICAL",',
        '  "victim": "Cụ An (78t)",',
        '  "location": "10.85, 106.77",',
        '  "dist_to_home": "350m",',
        '  "action": "ROUTE_MAPS",',
        '  "siren": "MAX_VOLUME"',
        "}"
    ]
    cy3 = 54.0
    for cl in code_lines3:
        ccol = '#F43F5E' if 'CRITICAL' in cl or 'MAX' in cl else ('#34D399' if 'location' in cl or 'dist' in cl else '#E2E8F0')
        fwt = 'bold' if 'CRITICAL' in cl or 'EVENT' in cl else 'normal'
        ax.text(70.5, cy3, cl, ha='left', va='center', fontsize=5.8, fontfamily='monospace', fontweight=fwt, color=ccol, zorder=4)
        cy3 -= 3.6

    # Arrows connecting columns
    ax.annotate("", xy=(36.5, 48), xytext=(33.5, 48), arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.2))
    ax.text(35.0, 50.2, "PUT", ha='center', va='center', fontsize=6.4, fontweight='bold', color='#2563EB')

    ax.annotate("", xy=(68.5, 48), xytext=(65.5, 48), arrowprops=dict(arrowstyle="->", color='#7C3AED', lw=2.2))
    ax.text(67.0, 50.2, "LIVE", ha='center', va='center', fontsize=6.4, fontweight='bold', color='#7C3AED')

    p = os.path.join(OUT, 'f_rtdb.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_part1():
    print("=== TẠO PHẦN 1: CÁC HÌNH KIẾN TRÚC & SƠ ĐỒ CHÍNH ===")
    gen_pro_methods()
    gen_pro_overview()
    gen_pro_esp32()
    gen_pro_block_diag()
    gen_pro_schematic()
    gen_pro_gatt()
    gen_pro_rtdb()
    print("=== HOÀN TẤT PHẦN 1 ===")

if __name__ == '__main__':
    gen_part1()

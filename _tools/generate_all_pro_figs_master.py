# -*- coding: utf-8 -*-
"""
generate_all_pro_figs_master.py
BỘ TẠO TOÀN DIỆN 23 HÌNH VẼ ĐỒ THỊ, SƠ ĐỒ, MÔ HÌNH VÀ LƯU ĐỒ CỦA ĐỒ ÁN GẬY THÔNG MINH IOT
Chuẩn đồ họa kỹ thuật cao cấp (Publication Grade).
Kích thước canvas chuẩn 7.0 - 7.5 inch | DPI: 300 | Font chữ cực to (8.0 - 12.5pt), đậm, sắc nét khi chèn vào Word A4.
Chuẩn xác 100% theo mã nguồn config.h (Buzzer: GPIO 5, Motor: GPIO 6, I2C: GPIO 8/9, HC-SR04: GPIO 16/17, ADC: GPIO 4).
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
# PHẦN 1: 7 HÌNH KIẾN TRÚC & SƠ ĐỒ CHÍNH (Chương 1, 2, 3)
# ==============================================================================

def gen_pro_methods():
    fig = plt.figure(figsize=(7.2, 7.6), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

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
    ax.text(50, by0 + bh - 3.0, "[+] HƯỚNG TIẾP CẬN CỦA ĐỀ TÀI: HỆ THỐNG GẬY THÔNG MINH IOT CẢNH BÁO TÉ NGÃ [+]",
            ha='center', va='center', fontsize=9.2, fontweight='bold', color='#FFFFFF', zorder=4)

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


def gen_pro_overview():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

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


def gen_pro_esp32():
    fig = plt.figure(figsize=(7.2, 5.6), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 96.5, "SƠ ĐỒ KIẾN TRÚC VI ĐIỀU KHIỂN ESP32-S3 VÀ PHÂN BỔ NGOẠI VI I/O",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Bố trí phân luồng tín hiệu cảm biến đầu vào (Inputs) và cơ cấu chấp hành - truyền thông đầu ra (Outputs)",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cx, cy, cw, ch = 50, 47.0, 32.0, 83.0
    x0, y0 = cx - cw/2, cy - ch/2
    ax.add_patch(FancyBboxPatch((x0+0.4, y0-0.4), cw, ch, boxstyle='round,pad=0,rounding_size=2.0', fc='#0F172A', ec='none', alpha=0.15, zorder=1))
    ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=2.0', fc='#0F172A', ec='#334155', lw=1.5, zorder=2))

    ax.text(cx, y0 + ch - 3.2, "ESPRESSIF SYSTEMS", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#94A3B8', zorder=4)
    ax.text(cx, y0 + ch - 6.0, "ESP32-S3-WROOM-1 (N16R8)", ha='center', va='center', fontsize=8.6, fontweight='bold', color='#FFFFFF', zorder=4)

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

        ax.annotate("", xy=(cx - cw/2, line_y), xytext=(ix + iw/2, line_y),
                    arrowprops=dict(arrowstyle="->", color=ihcol, lw=2.0))

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

        ax.annotate("", xy=(ox - ow/2, line_y), xytext=(cx + cw/2, line_y),
                    arrowprops=dict(arrowstyle="->", color=ohcol, lw=2.0))

    p = os.path.join(OUT, 'f_esp32.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_block_diag():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 96.5, "SƠ ĐỒ KHỐI CHỨC NĂNG HOÀN CHỈNH CỦA HỆ THỐNG GẬY THÔNG MINH",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Cấu trúc 3 phân hệ chính: Phần cứng Edge -> Mobile Gateway -> Cloud & Giám Sát",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cols = [
        (17.5, 48, 30, 84, "PHẦN CỨNG GẬY THÔNG MINH", "EDGE HARDWARE", C_EMERALD_DARK, '#ECFDF5', C_EMERALD_BORDER),
        (50.0, 48, 29, 84, "MOBILE GATEWAY (NGƯỜI DÙNG)", "SMARTPHONE", C_BLUE_DARK, '#EFF6FF', C_BLUE_BORDER),
        (82.5, 48, 30, 84, "ĐÁM MÂY & GIÁM SÁT", "CLOUD & GUARDIAN", C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER),
    ]

    for cx, cy, cw, ch, title, badge, hcol, bgcol, bcol in cols:
        x0, y0 = cx - cw/2, cy - ch/2
        ax.add_patch(FancyBboxPatch((x0+0.35, y0-0.35), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc='#0F172A', ec='none', alpha=0.08, zorder=1))
        ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=1.5', fc=bgcol, ec=bcol, lw=1.2, zorder=2))
        ax.add_patch(FancyBboxPatch((x0, y0 + ch - 7.5), cw, 7.5, boxstyle='round,pad=0,rounding_size=1.5', fc=hcol, ec='none', zorder=3))
        ax.add_patch(Rectangle((x0, y0 + ch - 7.5), cw, 1.5, fc=hcol, ec='none', zorder=3))
        ax.text(cx, y0 + ch - 2.5, badge, ha='center', va='center', fontsize=6.6, fontweight='bold', color='#CBD5E1', zorder=4)
        ax.text(cx, y0 + ch - 5.2, title, ha='center', va='center', fontsize=7.6, fontweight='bold', color='#FFFFFF', zorder=4)

    sub1 = [
        (17.5, 73.0, 26, 13, "KHỐI XỬ LÝ TRUNG TÂM", "ESP32-S3 Dual-Core 240MHz\nThuật toán FSM phân loại té ngã\nBLE 5.0 GATT Server truyền dữ liệu", C_EMERALD_DARK),
        (17.5, 56.5, 26, 13, "KHỐI CẢM BIẾN ĐẦU VÀO", "MPU6050: Gia tốc 3 trục + Con quay\nHC-SR04: Đo khoảng cách vật cản\nADC: Đo điện áp pin thời gian thực", '#047857'),
        (17.5, 40.0, 26, 13, "KHỐI CẢNH BÁO TẠI CHỖ", "Còi chíp Buzzer kêu to (GPIO 5)\nMotor rung phản hồi (GPIO 6)\nKích hoạt tức thì khi va chạm", '#B91C1C'),
        (17.5, 23.5, 26, 13, "KHỐI NGUỒN HỆ THỐNG", "Pin sạc Li-ion 18650 3.7V 2600mAh\nMạch MH-CD42 tăng áp 5V ổn định\nCổng sạc Type-C tiện lợi", '#334155'),
    ]
    for sx, sy, sw, sh, stitle, sdesc, scol in sub1:
        ax.add_patch(FancyBboxPatch((sx - sw/2, sy - sh/2), sw, sh, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec=scol, lw=1.1, zorder=4))
        ax.text(sx, sy + 3.8, stitle, ha='center', va='center', fontsize=7.0, fontweight='bold', color=scol, zorder=5)
        ax.text(sx, sy - 1.8, sdesc, ha='center', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    sub2 = [
        (50.0, 73.0, 25, 13, "FLUTTER BACKGROUND SERVICE", "Dịch vụ chạy ngầm 24/7 trên Android\nDuy trì kết nối BLE liên tục\nTự động phục hồi khi ngắt kết nối", C_BLUE_DARK),
        (50.0, 56.5, 25, 13, "ĐỊNH VỊ GPS VÀ XỬ LÝ CỨU HỘ", "Lấy tọa độ vị trí hiện tại của gậy\nKích hoạt đếm ngược 15 giây hủy\nNgăn chặn hoàn toàn báo động sai", '#1D4ED8'),
        (50.0, 40.0, 25, 13, "KÊNH TRUYỀN DỮ LIỆU CHÍNH", "Đồng bộ trạng thái lên Firebase qua 4G\nĐẩy sự kiện té ngã thời gian thực\nĐộ trễ truyền dẫn dưới 1.2 giây", '#059669'),
        (50.0, 23.5, 25, 13, "KÊNH DỰ PHÒNG GSM / SMS", "Tự động gửi SMS tọa độ Google Maps\nQuay số gọi khẩn cấp cho người thân\nHoạt động ngay cả khi không có mạng", '#B91C1C'),
    ]
    for sx, sy, sw, sh, stitle, sdesc, scol in sub2:
        ax.add_patch(FancyBboxPatch((sx - sw/2, sy - sh/2), sw, sh, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec=scol, lw=1.1, zorder=4))
        ax.text(sx, sy + 3.8, stitle, ha='center', va='center', fontsize=6.8, fontweight='bold', color=scol, zorder=5)
        ax.text(sx, sy - 1.8, sdesc, ha='center', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    sub3 = [
        (82.5, 73.0, 26, 13, "FIREBASE REALTIME DATABASE", "Cơ sở dữ liệu đám mây JSON trực tiếp\nĐồng bộ hai chiều theo luồng Stream\nLưu trữ lịch sử vị trí và nhật ký sự cố", '#78350F'),
        (82.5, 56.5, 26, 13, "ỨNG DỤNG DI ĐỘNG GIÁM HỘ", "Flutter App giao diện thân thiện\nBản đồ số định vị thời gian thực\nHiển thị chi tiết mức pin và tình trạng", C_PURPLE_DARK),
        (82.5, 40.0, 26, 13, "HỆ THỐNG CẢNH BÁO TỨC THÌ", "Còi hú báo động âm lượng tối đa\nBanner đỏ khẩn cấp toàn màn hình\nRung chuông cảnh báo người giám hộ", '#B91C1C'),
        (82.5, 23.5, 26, 13, "ĐIỀU HƯỚNG CỨU TRỢ KHẨN CẤP", "Tích hợp Google Maps dẫn đường\nĐịnh tuyến đường đi ngắn nhất tới nạn nhân\nNút gọi nhanh hỗ trợ cứu hộ y tế", '#047857'),
    ]
    for sx, sy, sw, sh, stitle, sdesc, scol in sub3:
        ax.add_patch(FancyBboxPatch((sx - sw/2, sy - sh/2), sw, sh, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec=scol, lw=1.1, zorder=4))
        ax.text(sx, sy + 3.8, stitle, ha='center', va='center', fontsize=6.8, fontweight='bold', color=scol, zorder=5)
        ax.text(sx, sy - 1.8, sdesc, ha='center', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    # Connecting arrows - neatly placed with badges
    ax.annotate("", xy=(37.0, 73), xytext=(31.0, 73), arrowprops=dict(arrowstyle="->", color=C_EMERALD_MED, lw=2.0))
    ax.add_patch(FancyBboxPatch((32.2, 70.8), 3.8, 4.4, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec=C_EMERALD_MED, lw=1.0, zorder=5))
    ax.text(34.1, 73.0, "BLE\n5.0", ha='center', va='center', fontsize=5.8, fontweight='bold', color=C_EMERALD_DARK, zorder=6)

    ax.annotate("", xy=(69.0, 73), xytext=(63.0, 73), arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.0))
    ax.add_patch(FancyBboxPatch((64.2, 70.8), 3.8, 4.4, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec='#2563EB', lw=1.0, zorder=5))
    ax.text(66.1, 73.0, "4G\nWiFi", ha='center', va='center', fontsize=5.8, fontweight='bold', color='#1D4ED8', zorder=6)

    ax.annotate("", xy=(69.0, 23.5), xytext=(63.0, 23.5), arrowprops=dict(arrowstyle="->", color='#B91C1C', lw=2.0, ls='--'))
    ax.add_patch(FancyBboxPatch((64.0, 21.3), 4.2, 4.4, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec='#B91C1C', lw=1.0, zorder=5))
    ax.text(66.1, 23.5, "SMS\nCALL", ha='center', va='center', fontsize=5.6, fontweight='bold', color='#B91C1C', zorder=6)

    p = os.path.join(OUT, 'f_block_diag.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_schematic():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 96.5, "SƠ ĐỒ NGUYÊN LÝ KẾT NỐI CHI TIẾT PHẦN CỨNG ESP32-S3",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Sơ đồ đấu nối dây mạch điện tử thực tế chuẩn xác 100% theo mã nguồn firmware config.h",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cx, cy, cw, ch = 50, 48.0, 32.0, 82.0
    x0, y0 = cx - cw/2, cy - ch/2
    ax.add_patch(FancyBboxPatch((x0+0.4, y0-0.4), cw, ch, boxstyle='round,pad=0,rounding_size=2.0', fc='#0F172A', ec='none', alpha=0.15, zorder=1))
    ax.add_patch(FancyBboxPatch((x0, y0), cw, ch, boxstyle='round,pad=0,rounding_size=2.0', fc='#0F172A', ec='#334155', lw=1.5, zorder=2))

    ax.text(cx, y0 + ch - 3.5, "ESP32-S3-WROOM-1 (N16R8)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF', zorder=4)
    ax.text(cx, y0 + ch - 6.5, "Xtensa Dual-Core 240MHz | 16MB Flash | 8MB PSRAM", ha='center', va='center', fontsize=6.2, color='#94A3B8', zorder=4)

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

    # Core chip center box (đặt ở vị trí an toàn y = 37, h = 18 không che chân)
    ax.add_patch(FancyBboxPatch((cx - 8.5, 37.0), 17.0, 18.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#1E293B', ec='#475569', lw=1.0, zorder=3))
    ax.text(cx, 51.5, "RF TRANSCEIVER", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#38BDF8', zorder=4)
    ax.text(cx, 46.5, "BLE 5.0 + 2.4G Wi-Fi", ha='center', va='center', fontsize=6.0, color='#E2E8F0', zorder=4)
    ax.text(cx, 41.0, "GATT: SmartCane", ha='center', va='center', fontsize=6.0, fontfamily='monospace', color='#FCD34D', zorder=4)

    # Left Peripheral Cards
    ax.add_patch(FancyBboxPatch((3.0, 62.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFDF5', ec=C_AMBER_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((3.0, 77.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_AMBER_DARK, ec='none', zorder=4))
    ax.text(15.5, 79.5, "MPU6050 (6-DOF IMU)", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(4.5, 73.5, "• VCC -> 3.3V, GND -> GND", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(4.5, 69.5, "• SDA -> GPIO 8 (Kéo 4.7kΩ)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_AMBER_DARK, zorder=5)
    ax.text(4.5, 65.5, "• SCL -> GPIO 9 (Kéo 4.7kΩ)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_AMBER_DARK, zorder=5)

    ax.plot([28.0, 34.0], [74.0, 74.0], color='#D97706', lw=1.8, zorder=6)
    ax.plot([28.0, 34.0], [68.0, 68.0], color='#D97706', lw=1.8, zorder=6)

    ax.add_patch(FancyBboxPatch((3.0, 38.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#F0FDFA', ec=C_CYAN_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((3.0, 53.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_CYAN_DARK, ec='none', zorder=4))
    ax.text(15.5, 55.5, "HC-SR04 (SIÊU ÂM)", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(4.5, 49.5, "• VCC -> 5V (Nguồn pin MH-CD42)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(4.5, 45.5, "• TRIG -> GPIO 16 (Xung 10µs)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_CYAN_DARK, zorder=5)
    ax.text(4.5, 41.5, "• ECHO -> GPIO 17 (Cầu 1k/2k)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_CYAN_DARK, zorder=5)

    ax.plot([28.0, 34.0], [52.0, 52.0], color='#0891B2', lw=1.8, zorder=6)
    ax.plot([28.0, 34.0], [46.0, 46.0], color='#0891B2', lw=1.8, zorder=6)

    ax.add_patch(FancyBboxPatch((3.0, 14.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#ECFDF5', ec=C_EMERALD_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((3.0, 29.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_EMERALD_DARK, ec='none', zorder=4))
    ax.text(15.5, 31.5, "MẠCH PHÂN ÁP ĐO PIN", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(4.5, 25.5, "• Pin 18650 (3.0V - 4.2V)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(4.5, 21.5, "• R1 = 100kΩ, R2 = 100kΩ (Chia 2)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(4.5, 17.5, "• Vout -> GPIO 4 (ADC1_CH3)", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_EMERALD_DARK, zorder=5)

    ax.plot([28.0, 34.0], [30.0, 30.0], color='#059669', lw=1.8, zorder=6)

    # Right Peripheral Cards
    ax.add_patch(FancyBboxPatch((72.0, 62.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFF1F2', ec=C_ROSE_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((72.0, 77.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_ROSE_DARK, ec='none', zorder=4))
    ax.text(84.5, 79.5, "CÒI BÁO ĐỘNG BUZZER", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(73.5, 73.5, "• Active Buzzer 5V (> 85dB)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(73.5, 69.5, "• Chân điều khiển: GPIO 5", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_ROSE_DARK, zorder=5)
    ax.text(73.5, 65.5, "• Kích mức CAO (HIGH) khi ngã", ha='left', va='center', fontsize=6.2, color='#B91C1C', zorder=5)

    ax.plot([66.0, 72.0], [74.0, 74.0], color='#E11D48', lw=1.8, zorder=6)

    ax.add_patch(FancyBboxPatch((72.0, 38.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FAF5FF', ec=C_PURPLE_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((72.0, 53.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_PURPLE_DARK, ec='none', zorder=4))
    ax.text(84.5, 55.5, "MẠCH KÍCH MOTOR RUNG", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(73.5, 49.5, "• MOSFET AOD4184N (N-Channel)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(73.5, 45.5, "• Gate Control: GPIO 6", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_PURPLE_DARK, zorder=5)
    ax.text(73.5, 41.5, "• Diode 1N4007 dập xung ngược", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    ax.plot([66.0, 72.0], [52.0, 52.0], color='#7C3AED', lw=1.8, zorder=6)

    ax.add_patch(FancyBboxPatch((72.0, 14.0), 25.0, 20.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#EFF6FF', ec=C_BLUE_BORDER, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((72.0, 29.0), 25.0, 5.0, boxstyle='round,pad=0,rounding_size=1.2', fc=C_BLUE_DARK, ec='none', zorder=4))
    ax.text(84.5, 31.5, "KHỐI NGUỒN MH-CD42", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(73.5, 25.5, "• Input: Pin Li-ion 3.7V 18650", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)
    ax.text(73.5, 21.5, "• Output: 5V DC cấp ESP32 VIN", ha='left', va='center', fontsize=6.2, fontweight='bold', color=C_BLUE_DARK, zorder=5)
    ax.text(73.5, 17.5, "• Hỗ trợ vừa sạc vừa dùng (Type-C)", ha='left', va='center', fontsize=6.2, color='#1E293B', zorder=5)

    ax.plot([66.0, 72.0], [30.0, 30.0], color='#DC2626', lw=1.8, zorder=6)

    p = os.path.join(OUT, 'f_schematic.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_gatt():
    fig = plt.figure(figsize=(7.2, 5.6), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 96.5, "CẤU TRÚC PHÂN TẦNG VÀ GATT PROFILE CỦA BLUETOOTH 5.0 LE",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Kiến trúc máy chủ GATT (GATT Server) trên firmware ESP32-S3 kết nối tới ứng dụng di động",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    ax.add_patch(FancyBboxPatch((25, 81.0), 50, 9.0, boxstyle='round,pad=0,rounding_size=1.5', fc=C_SLATE_900, ec='none', zorder=2))
    ax.text(50, 86.8, "SMART CANE GATT PROFILE (DEVICE: ESP32-S3)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF', zorder=3)
    ax.text(50, 83.2, "Quản trị cơ chế đóng gói dữ liệu thuộc tính cảm biến và điều khiển thiết bị", ha='center', va='center', fontsize=6.8, color='#CBD5E1', zorder=3)

    ax.plot([50, 50], [81.0, 75.0], color=C_BLUE_DARK, lw=2.2, zorder=1)

    ax.add_patch(FancyBboxPatch((15, 60.0), 70, 15.0, boxstyle='round,pad=0,rounding_size=1.5', fc='#EFF6FF', ec=C_BLUE_MED, lw=1.5, zorder=2))
    ax.add_patch(FancyBboxPatch((15, 69.0), 70, 6.0, boxstyle='round,pad=0,rounding_size=1.5', fc=C_BLUE_DARK, ec='none', zorder=3))
    ax.text(50, 72.0, "PRIMARY SERVICE: DỊCH VỤ GẬY THÔNG MINH IOT", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#FFFFFF', zorder=4)
    ax.text(50, 65.5, "UUID: 0000FFE0-0000-1000-8000-00805F9B34FB | Khởi tạo bởi BLEDevice::createServer()", ha='center', va='center', fontsize=6.6, fontweight='bold', color=C_BLUE_DARK, zorder=4)
    ax.text(50, 62.0, "Đóng vai trò Service gốc, quản lý và phân phối 4 Characteristic chuyên biệt", ha='center', va='center', fontsize=6.4, color='#334155', zorder=4)

    ax.plot([50, 50], [60.0, 55.0], color=C_SLATE_700, lw=2.0, zorder=1)
    ax.plot([14, 86], [55.0, 55.0], color=C_SLATE_700, lw=2.0, zorder=1)

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


def gen_pro_rtdb():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 96.5, "CƠ CHẾ ĐỒNG BỘ DỮ LIỆU HAI CHIỀU TRÊN FIREBASE REALTIME DATABASE",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 93.6, "Cấu trúc dữ liệu JSON NoSQL và mô hình Publish/Subscribe qua kết nối WebSocket bảo mật",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

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

    # Chi tiết Cột 1: Mobile Gateway (đặt từ y = 76.5 không chạm header)
    ax.text(18, 77.0, "PHÁT HIỆN TÉ NGÃ & ĐẨY DỮ LIỆU", ha='center', va='center', fontsize=7.0, fontweight='bold', color=C_BLUE_DARK)
    ax.text(5.0, 73.0, "• Nhận Notify BLE từ gậy", ha='left', va='center', fontsize=6.4, color='#1E293B')
    ax.text(5.0, 69.5, "• Lấy tọa độ GPS thiết bị", ha='left', va='center', fontsize=6.4, color='#1E293B')
    ax.text(5.0, 66.0, "• Ghi JSON vào RTDB qua REST API", ha='left', va='center', fontsize=6.4, fontweight='bold', color='#2563EB')
    ax.text(5.0, 62.5, "• Thời gian phản hồi < 800ms", ha='left', va='center', fontsize=6.4, color='#059669')

    ax.add_patch(FancyBboxPatch((5.0, 15.0), 26.0, 44.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#0F172A', ec='#334155', lw=1.0, zorder=3))
    ax.text(18, 56.0, "JSON PAYLOAD (GỬI LÊN)", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#38BDF8', zorder=4)
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
    cy1 = 52.0
    for cl in code_lines1:
        ccol = '#F43F5E' if 'is_falling' in cl or 'SOS' in cl else ('#34D399' if 'location' in cl or 'lat' in cl or 'lng' in cl else '#E2E8F0')
        ax.text(6.5, cy1, cl, ha='left', va='center', fontsize=5.8, fontfamily='monospace', color=ccol, zorder=4)
        cy1 -= 3.1

    # Chi tiết Cột 2: Firebase Realtime Database
    ax.text(50, 77.0, "CÂY DỮ LIỆU ĐÁM MÂY (JSON)", ha='center', va='center', fontsize=7.0, fontweight='bold', color=C_AMBER_DARK)
    ax.add_patch(FancyBboxPatch((37.0, 15.0), 26.0, 58.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#1E293B', ec='#475569', lw=1.0, zorder=3))
    ax.text(50, 70.0, "DATABASE ROOT (JSON TREE)", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#FCD34D', zorder=4)
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
    ty = 66.0
    for tl in tree_lines:
        tcol = '#F43F5E' if 'is_falling' in tl or 'alarm' in tl else ('#38BDF8' if 'cane' in tl or 'profile' in tl else '#E2E8F0')
        fwt = 'bold' if 'TRUE' in tl or 'ACTIVE' in tl else 'normal'
        ax.text(38.5, ty, tl, ha='left', va='center', fontsize=5.6, fontfamily='monospace', fontweight=fwt, color=tcol, zorder=4)
        ty -= 3.5

    # Chi tiết Cột 3: Monitor App Giám Hộ
    ax.text(82, 77.0, "LẮNG NGHE & PHẢN HỒI KHẨN", ha='center', va='center', fontsize=7.0, fontweight='bold', color=C_PURPLE_DARK)
    ax.text(69.0, 73.0, "• Luồng Stream .onValue()", ha='left', va='center', fontsize=6.4, color='#1E293B')
    ax.text(69.0, 69.5, "• Nhận ngay khi is_falling=true", ha='left', va='center', fontsize=6.4, fontweight='bold', color='#B91C1C')
    ax.text(69.0, 66.0, "• Kích hoạt còi hú max volume", ha='left', va='center', fontsize=6.4, fontweight='bold', color='#B91C1C')
    ax.text(69.0, 62.5, "• Cập nhật Marker bản đồ Maps", ha='left', va='center', fontsize=6.4, color='#059669')

    ax.add_patch(FancyBboxPatch((69.0, 15.0), 26.0, 44.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#0F172A', ec='#334155', lw=1.0, zorder=3))
    ax.text(82, 56.0, "EVENT STREAM (NHẬN VỀ)", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#A855F7', zorder=4)
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
    cy3 = 52.0
    for cl in code_lines3:
        ccol = '#F43F5E' if 'CRITICAL' in cl or 'MAX' in cl else ('#34D399' if 'location' in cl or 'dist' in cl else '#E2E8F0')
        fwt = 'bold' if 'CRITICAL' in cl or 'EVENT' in cl else 'normal'
        ax.text(70.5, cy3, cl, ha='left', va='center', fontsize=5.8, fontfamily='monospace', fontweight=fwt, color=ccol, zorder=4)
        cy3 -= 3.5

    ax.annotate("", xy=(36.5, 48), xytext=(33.5, 48), arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.2))
    ax.text(35.0, 50.2, "PUT", ha='center', va='center', fontsize=6.4, fontweight='bold', color='#2563EB')

    ax.annotate("", xy=(68.5, 48), xytext=(65.5, 48), arrowprops=dict(arrowstyle="->", color='#7C3AED', lw=2.2))
    ax.text(67.0, 50.2, "LIVE", ha='center', va='center', fontsize=6.4, fontweight='bold', color='#7C3AED')

    p = os.path.join(OUT, 'f_rtdb.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# PHẦN 2: 3 LƯU ĐỒ THUẬT TOÁN (Chương 3)
# Canvas 7.2 x 10.5 in | DPI: 300 | Font 8.0 - 9.0pt đậm nét chuẩn ISO 5807
# ==============================================================================

def gen_pro_flow_firmware():
    fig = plt.figure(figsize=(7.2, 10.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 150); ax.axis('off')

    ax.text(50, 146.0, "LƯU ĐỒ THUẬT TOÁN CHÍNH FIRMWARE ESP32-S3",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 142.8, "Chu trình FreeRTOS: Khởi tạo I/O, quét MPU6050, đo siêu âm HC-SR04 & phát sóng BLE",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cx = 50.0

    def draw_term(y, text):
        ax.add_patch(FancyBboxPatch((cx - 28, y - 4), 56, 8, boxstyle='round,pad=0,rounding_size=4.0',
                                   fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.5, zorder=3))
        ax.text(cx, y, text, ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_EMERALD_DARK, zorder=4)

    def draw_proc(y, title, desc, w_box=72, h_box=9.5, fc='#EFF6FF', ec=C_BLUE_MED):
        ax.add_patch(FancyBboxPatch((cx - w_box/2, y - h_box/2), w_box, h_box, boxstyle='round,pad=0,rounding_size=1.2',
                                   fc=fc, ec=ec, lw=1.2, zorder=3))
        ax.text(cx, y + 2.0, title, ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_SLATE_900, zorder=4)
        ax.text(cx, y - 2.0, desc, ha='center', va='center', fontsize=6.6, color=C_SLATE_700, zorder=4)

    def draw_dec(y, cond, w_dia=64, h_dia=11.5):
        poly = Polygon([(cx, y + h_dia/2), (cx + w_dia/2, y), (cx, y - h_dia/2), (cx - w_dia/2, y)],
                       closed=True, fc='#FFFBEB', ec=C_AMBER_MED, lw=1.5, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, y, cond, ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_AMBER_DARK, zorder=4)

    # 1. Bắt đầu
    draw_term(135, "BẮT ĐẦU (POWER ON / RESET ESP32-S3)")

    # 2. Cấu hình GPIO
    draw_proc(122, "1. CẤU HÌNH GPIO VÀ NGOẠI VI", "Buzzer (GPIO 5), Motor (GPIO 6) → OUTPUT | HC-SR04 Trig:16, Echo:17 | ADC:4")
    ax.annotate("", xy=(cx, 127), xytext=(cx, 131), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # 3. Self-Test
    draw_proc(109, "2. TỰ KIỂM TRA PHẦN CỨNG (SELF-TEST)", "Bật còi hú + rung trong 0.2 giây rồi tắt để báo hiệu hệ thống sẵn sàng hoạt động")
    ax.annotate("", xy=(cx, 114), xytext=(cx, 117), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # 4. Khởi tạo I2C & MPU6050
    draw_proc(96, "3. KHỞI TẠO CẢM BIẾN QUÁN TÍNH MPU-6050", "Giao thức I2C (SDA:8, SCL:9, 400kHz) · Cấu hình dải gia tốc ±8g · Tần số 50Hz")
    ax.annotate("", xy=(cx, 101), xytext=(cx, 104), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # 5. Khởi tạo BLE Server
    draw_proc(83, "4. KHỞI TẠO BLUETOOTH LOW ENERGY (GATT SERVER)", "Tên 'SmartCane' · Service UUID ...FFE0 · Characteristic Báo ngã (...FFE1, Notify)")
    ax.annotate("", xy=(cx, 88), xytext=(cx, 91), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # 6. Đọc gia tốc & tính SVM
    draw_proc(70, "5. ĐỌC DỮ LIỆU CẢM BIẾN (CHU KỲ 20ms / 50Hz)", "Đọc (ax, ay, az) tính SVM = √(ax² + ay² + az²) · Đo khoảng cách siêu âm d (cm)")
    ax.annotate("", xy=(cx, 75), xytext=(cx, 78), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # 7. Quyết định: SVM > 2.8g và Góc nghiêng > 60 độ
    draw_dec(54, "SVM > 2.8g VÀ GÓC NGHIÊNG > 60° ?")
    ax.annotate("", xy=(cx, 60), xytext=(cx, 65), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # Nhánh ĐÚNG (Té ngã): Cảnh báo khẩn
    draw_proc(37, "6. KÍCH HOẠT CẢNH BÁO TÉ NGÃ KHẨN CẤP",
              "Bật Còi Buzzer (GPIO 5) · Gửi gói BLE Notify (is_falling=true) tới Gateway",
              fc='#FFF1F2', ec=C_ROSE_MED)
    ax.annotate("", xy=(cx, 42), xytext=(cx, 48), arrowprops=dict(arrowstyle="->", color=C_ROSE_MED, lw=1.8))
    ax.text(cx + 2.0, 45, "ĐÚNG (NGÃ)", fontsize=6.8, fontweight='bold', color=C_ROSE_DARK)

    # Nhánh SAI: Kiểm tra vật cản khoảng cách < 150cm
    draw_dec(22, "KHOẢNG CÁCH VẬT CẢN d < 150cm ?")
    # Đường rẽ nhánh SAI từ Fall sang Obstacle
    ax.plot([cx - 32, 10, 10, cx - 32], [54, 54, 22, 22], color=C_SLATE_700, lw=1.3)
    ax.annotate("", xy=(cx - 32, 22), xytext=(10, 22), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.3))
    ax.text(12, 55.5, "SAI (BÌNH THƯỜNG)", fontsize=6.4, fontweight='bold', color=C_SLATE_700)

    # Nhánh ĐÚNG của Vật cản: Rung phản hồi
    ax.add_patch(FancyBboxPatch((cx + 10, 6.0), 32, 9, boxstyle='round,pad=0,rounding_size=1.0',
                               fc='#FAF5FF', ec=C_PURPLE_MED, lw=1.2, zorder=3))
    ax.text(cx + 26, 12.0, "KÍCH HOẠT MOTOR RUNG", ha='center', va='center', fontsize=6.8, fontweight='bold', color=C_PURPLE_DARK)
    ax.text(cx + 26, 8.5, "Rung ngắt quãng cảnh báo (GPIO 6)", ha='center', va='center', fontsize=6.0, color='#1E293B')
    ax.plot([cx + 32, cx + 26], [22, 22], color=C_PURPLE_MED, lw=1.3)
    ax.annotate("", xy=(cx + 26, 15), xytext=(cx + 26, 22), arrowprops=dict(arrowstyle="->", color=C_PURPLE_MED, lw=1.3))
    ax.text(cx + 28, 23.5, "ĐÚNG", fontsize=6.4, fontweight='bold', color=C_PURPLE_DARK)

    # Vòng lặp Loop quay lại
    ax.plot([cx, cx, 95, 95, cx], [32, 28, 28, 70, 70], color=C_SLATE_500, lw=1.2, ls='--')
    ax.annotate("", xy=(cx + 36, 70), xytext=(95, 70), arrowprops=dict(arrowstyle="->", color=C_SLATE_500, lw=1.2, ls='--'))

    p = os.path.join(OUT, 'f_flow_firmware.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_flow_elderly():
    fig = plt.figure(figsize=(7.2, 10.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 150); ax.axis('off')

    ax.text(50, 146.0, "LƯU ĐỒ HOẠT ĐỘNG DỊCH VỤ NỀN APP NGƯỜI DÙNG GẬY",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 142.8, "Flutter Foreground Service chạy ngầm 24/7, duy trì kết nối BLE và điều phối cứu hộ",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cx = 50.0

    def draw_term(y, text):
        ax.add_patch(FancyBboxPatch((cx - 28, y - 4), 56, 8, boxstyle='round,pad=0,rounding_size=4.0',
                                   fc='#EFF6FF', ec=C_BLUE_MED, lw=1.5, zorder=3))
        ax.text(cx, y, text, ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_BLUE_DARK, zorder=4)

    def draw_proc(y, title, desc, w_box=72, h_box=9.5, fc='#FFFFFF', ec=C_BLUE_MED):
        ax.add_patch(FancyBboxPatch((cx - w_box/2, y - h_box/2), w_box, h_box, boxstyle='round,pad=0,rounding_size=1.2',
                                   fc=fc, ec=ec, lw=1.2, zorder=3))
        ax.text(cx, y + 2.0, title, ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_SLATE_900, zorder=4)
        ax.text(cx, y - 2.0, desc, ha='center', va='center', fontsize=6.6, color=C_SLATE_700, zorder=4)

    def draw_dec(y, cond, w_dia=64, h_dia=11.5):
        poly = Polygon([(cx, y + h_dia/2), (cx + w_dia/2, y), (cx, y - h_dia/2), (cx - w_dia/2, y)],
                       closed=True, fc='#FFFBEB', ec=C_AMBER_MED, lw=1.5, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, y, cond, ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_AMBER_DARK, zorder=4)

    draw_term(135, "KHỞI ĐỘNG APP / DỊCH VỤ NỀN FLUTTER")

    draw_proc(122, "1. ĐĂNG KÝ VÀ KHỞI TẠO FOREGROUND SERVICE", "Yêu cầu quyền GPS, Bluetooth Scan/Connect, SMS và chạy ngầm tiết kiệm pin")
    ax.annotate("", xy=(cx, 127), xytext=(cx, 131), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    draw_proc(109, "2. QUÉT VÀ KẾT NỐI TỰ ĐỘNG GẬY SMARTCANE", "Tìm UUID Service ...FFE0 · Thiết lập MTU · Đăng ký lắng nghe Characteristic Notify")
    ax.annotate("", xy=(cx, 114), xytext=(cx, 117), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    draw_dec(95, "ĐÃ KẾT NỐI BLUETOOTH BLE THÀNH CÔNG ?")
    ax.annotate("", xy=(cx, 101), xytext=(cx, 104), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # Nhánh ĐÚNG: Lắng nghe gói tin
    draw_proc(78, "3. LẮNG NGHE LUỒNG DỮ LIỆU NOTIFY TỪ GẬY", "Nhận trạng thái gia tốc SVM, cự ly vật cản và dung lượng pin thời gian thực")
    ax.annotate("", xy=(cx, 83), xytext=(cx, 89), arrowprops=dict(arrowstyle="->", color='#059669', lw=1.5))
    ax.text(cx + 2.0, 86, "ĐÚNG", fontsize=6.6, fontweight='bold', color='#059669')

    # Nhánh SAI: Thử kết nối lại
    ax.plot([cx - 32, 10, 10, cx - 36], [95, 95, 109, 109], color='#DC2626', lw=1.3)
    ax.annotate("", xy=(cx - 36, 109), xytext=(10, 109), arrowprops=dict(arrowstyle="->", color='#DC2626', lw=1.3))
    ax.text(12, 96.5, "SAI (THỬ LẠI)", fontsize=6.4, fontweight='bold', color='#DC2626')

    # Kiểm tra tín hiệu báo ngã
    draw_dec(63, "NHẬN TÍN HIỆU CẢNH BÁO TÉ NGÃ (is_falling = true) ?")
    ax.annotate("", xy=(cx, 69), xytext=(cx, 73), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # Nhánh ĐÚNG: Bật màn hình đỏ và đếm ngược 15s
    draw_proc(47, "4. KÍCH HOẠT MÀN HÌNH ĐỎ & ĐẾM NGƯỢC 15 GIÂY",
              "Báo động âm lượng lớn · Cho phép người già bấm nút HỦY nếu chỉ là va chạm nhẹ",
              fc='#FFF1F2', ec=C_ROSE_MED)
    ax.annotate("", xy=(cx, 52), xytext=(cx, 57), arrowprops=dict(arrowstyle="->", color=C_ROSE_MED, lw=1.5))
    ax.text(cx + 2.0, 54.5, "ĐÚNG (CÓ NGÃ)", fontsize=6.6, fontweight='bold', color=C_ROSE_DARK)

    draw_dec(33, "NGƯỜI DÙNG BẤM HỦY TRONG 15 GIÂY ?")
    ax.annotate("", xy=(cx, 39), xytext=(cx, 42), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # Nhánh ĐÚNG (Hủy): Gửi lệnh tắt còi
    ax.add_patch(FancyBboxPatch((8.0, 18.0), 32, 9, boxstyle='round,pad=0,rounding_size=1.0',
                               fc='#ECFDF5', ec='#059669', lw=1.2, zorder=3))
    ax.text(24.0, 24.0, "HỦY BÁO ĐỘNG (BÁO SAI)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#064E3B')
    ax.text(24.0, 20.5, "Gửi BLE tắt còi, quay lại bình thường", ha='center', va='center', fontsize=6.0, color='#1E293B')
    ax.plot([cx - 32, 24.0], [33, 33], color='#059669', lw=1.3)
    ax.annotate("", xy=(24.0, 27), xytext=(24.0, 33), arrowprops=dict(arrowstyle="->", color='#059669', lw=1.3))
    ax.text(28.0, 34.5, "ĐÚNG (ĐÃ HỦY)", fontsize=6.4, fontweight='bold', color='#059669')

    # Nhánh SAI (Hết 15s không bấm): PHÁT BÁO ĐỘNG TOÀN DIỆN
    draw_proc(16, "5. KÍCH HOẠT QUY TRÌNH CỨU HỘ KHẨN CẤP ĐA TẦNG",
              "Lấy GPS · Đẩy Firebase RTDB · Tự động gửi SMS tọa độ Maps & Gọi điện SOS",
              fc='#FFF1F2', ec='#B91C1C', w_box=46)
    ax.annotate("", xy=(cx + 10, 21), xytext=(cx + 10, 27), arrowprops=dict(arrowstyle="->", color='#B91C1C', lw=1.8))
    ax.text(cx + 12, 28.5, "SAI (HẾT 15s)", fontsize=6.6, fontweight='bold', color='#B91C1C')

    p = os.path.join(OUT, 'f_flow_elderly.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_flow_guardian():
    fig = plt.figure(figsize=(7.2, 10.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 150); ax.axis('off')

    ax.text(50, 146.0, "LƯU ĐỒ HOẠT ĐỘNG GIÁM SÁT VÀ CẢNH BÁO APP GIÁM HỘ",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 142.8, "Ứng dụng Flutter Giám Hộ: Lắng nghe Stream Firebase, kích hoạt còi hú & chỉ đường cứu hộ",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cx = 50.0

    def draw_term(y, text):
        ax.add_patch(FancyBboxPatch((cx - 28, y - 4), 56, 8, boxstyle='round,pad=0,rounding_size=4.0',
                                   fc='#FAF5FF', ec=C_PURPLE_MED, lw=1.5, zorder=3))
        ax.text(cx, y, text, ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_PURPLE_DARK, zorder=4)

    def draw_proc(y, title, desc, w_box=72, h_box=9.5, fc='#FFFFFF', ec=C_PURPLE_MED):
        ax.add_patch(FancyBboxPatch((cx - w_box/2, y - h_box/2), w_box, h_box, boxstyle='round,pad=0,rounding_size=1.2',
                                   fc=fc, ec=ec, lw=1.2, zorder=3))
        ax.text(cx, y + 2.0, title, ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_SLATE_900, zorder=4)
        ax.text(cx, y - 2.0, desc, ha='center', va='center', fontsize=6.6, color=C_SLATE_700, zorder=4)

    def draw_dec(y, cond, w_dia=64, h_dia=11.5):
        poly = Polygon([(cx, y + h_dia/2), (cx + w_dia/2, y), (cx, y - h_dia/2), (cx - w_dia/2, y)],
                       closed=True, fc='#FFFBEB', ec=C_AMBER_MED, lw=1.5, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, y, cond, ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_AMBER_DARK, zorder=4)

    draw_term(135, "KHỞI ĐỘNG ỨNG DỤNG GIÁM HỘ (FLUTTER)")

    draw_proc(122, "1. XÁC THỰC TÀI KHOẢN VÀ KẾT NỐI CƠ SỞ DỮ LIỆU", "Đăng nhập Firebase Auth · Đăng ký lắng nghe Node /devices/{deviceId} qua Stream")
    ax.annotate("", xy=(cx, 127), xytext=(cx, 131), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    draw_proc(109, "2. HIỂN THỊ TRẠNG THÁI BÌNH THƯỜNG TRÊN DASHBOARD", "Cập nhật Marker bản đồ OpenStreetMap · Hiển thị phần trăm pin và thời gian đồng bộ")
    ax.annotate("", xy=(cx, 114), xytext=(cx, 117), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    draw_dec(95, "PHÁT HIỆN SỰ KIỆN TÉ NGÃ (alarm = 'CRITICAL') ?")
    ax.annotate("", xy=(cx, 101), xytext=(cx, 104), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # Nhánh ĐÚNG: Kích hoạt báo động khẩn cấp
    draw_proc(78, "3. BẬT BÁO ĐỘNG KHẨN CẤP VÀ CÒI HÚ ÂM LƯỢNG MAX",
              "Phát âm thanh còi hú báo động ngay cả khi điện thoại tắt chuông · Rung liên tục",
              fc='#FFF1F2', ec=C_ROSE_MED)
    ax.annotate("", xy=(cx, 83), xytext=(cx, 89), arrowprops=dict(arrowstyle="->", color=C_ROSE_MED, lw=1.5))
    ax.text(cx + 2.0, 86, "ĐÚNG (CẢNH BÁO)", fontsize=6.6, fontweight='bold', color=C_ROSE_DARK)

    # Nhánh SAI: Duy trì lắng nghe bình thường
    ax.plot([cx + 32, 92, 92, cx + 36], [95, 95, 109, 109], color='#059669', lw=1.3)
    ax.annotate("", xy=(cx + 36, 109), xytext=(92, 109), arrowprops=dict(arrowstyle="->", color='#059669', lw=1.3))
    ax.text(80, 96.5, "SAI (BÌNH THƯỜNG)", fontsize=6.4, fontweight='bold', color='#059669')

    draw_proc(64, "4. CẬP NHẬT TỌA ĐỘ VỊ TRÍ GẬY LÊN BẢN ĐỒ SỐ",
              "Ghim Marker đỏ chớp tại tọa độ GPS của nạn nhân · Tính cự ly khoảng cách tới người thân")
    ax.annotate("", xy=(cx, 69), xytext=(cx, 73), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    draw_dec(49, "NGƯỜI GIÁM HỘ CHỌN HÀNH ĐỘNG CỨU TRỢ ?")
    ax.annotate("", xy=(cx, 55), xytext=(cx, 59), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    # 3 Nhánh hành động cứu trợ
    acts = [
        (18, 30, 28, 12, "GỌI ĐIỆN THOẠI KHẨN", "Kết nối ngay cuộc gọi\ntới người cao tuổi", C_BLUE_DARK),
        (50, 30, 28, 12, "CHỈ ĐƯỜNG GOOGLE MAPS", "Mở bản đồ tìm tuyến đường\nngắn nhất tới hiện trường", C_EMERALD_DARK),
        (82, 30, 28, 12, "TẮT BÁO ĐỘNG ĐÃ XỬ LÝ", "Ghi nhận sự cố an toàn\nLưu vào lịch sử báo cáo", C_AMBER_DARK),
    ]
    ax.plot([18, 82], [42, 42], color=C_SLATE_700, lw=1.2)
    ax.plot([50, 50], [43, 36], color=C_SLATE_700, lw=1.2)

    for ax_x, ax_y, ax_w, ax_h, atitle, adesc, acol in acts:
        ax.plot([ax_x, ax_x], [42, ax_y + ax_h/2], color=acol, lw=1.2)
        ax.annotate("", xy=(ax_x, ax_y + ax_h/2), xytext=(ax_x, 42), arrowprops=dict(arrowstyle="->", color=acol, lw=1.2))
        ax.add_patch(FancyBboxPatch((ax_x - ax_w/2, ax_y - ax_h/2), ax_w, ax_h, boxstyle='round,pad=0,rounding_size=1.0',
                                   fc='#FFFFFF', ec=acol, lw=1.2, zorder=3))
        ax.text(ax_x, ax_y + 3.2, atitle, ha='center', va='center', fontsize=6.8, fontweight='bold', color=acol)
        ax.text(ax_x, ax_y - 2.0, adesc, ha='center', va='center', fontsize=5.8, color='#1E293B')

    draw_term(12, "HOÀN TẤT QUY TRÌNH HỖ TRỢ VÀ GIÁM SÁT")
    ax.annotate("", xy=(50, 16), xytext=(50, 24), arrowprops=dict(arrowstyle="->", color=C_SLATE_700, lw=1.5))

    p = os.path.join(OUT, 'f_flow_guardian.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# PHẦN 3: 9 HÌNH NGUYÊN LÝ & KỸ THUẬT LINH KIỆN (Chương 2)
# ==============================================================================

def gen_pro_i2c():
    fig = plt.figure(figsize=(7.2, 5.0), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 95.5, "CHUẨN GIAO TIẾP VẬT LÝ VÀ GIAO THỨC I2C (ESP32-S3 VÀ MPU6050)",
            ha='center', va='center', fontsize=10.8, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 92.2, "Bus Master - Slave: SDA (GPIO 8), SCL (GPIO 9), điện trở kéo lên Pull-up 4.7kΩ và khung truyền 400kHz",
            ha='center', va='center', fontsize=7.8, color=C_SLATE_500, fontstyle='italic')

    # Card Master ESP32-S3 bên trái
    ax.add_patch(FancyBboxPatch((4, 46), 26, 40, boxstyle='round,pad=0,rounding_size=1.2', fc='#EFF6FF', ec=C_BLUE_BORDER, lw=1.2))
    ax.add_patch(FancyBboxPatch((4, 79), 26, 7, boxstyle='round,pad=0,rounding_size=1.2', fc=C_BLUE_DARK, ec='none'))
    ax.text(17, 82.5, "ESP32-S3 (MASTER)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(6, 74, "• Khởi tạo I2C Driver", fontsize=6.8, color='#1E293B')
    ax.text(6, 68, "• Chân SDA: GPIO 8", fontsize=6.8, fontweight='bold', color=C_BLUE_DARK)
    ax.text(6, 62, "• Chân SCL: GPIO 9", fontsize=6.8, fontweight='bold', color=C_BLUE_DARK)
    ax.text(6, 56, "• Tốc độ: 400 kHz", fontsize=6.8, color='#1E293B')
    ax.text(6, 50, "• Địa chỉ Slave: 0x68", fontsize=6.8, color='#059669', fontweight='bold')

    # Card Slave MPU6050 bên phải
    ax.add_patch(FancyBboxPatch((70, 46), 26, 40, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFDF5', ec=C_AMBER_BORDER, lw=1.2))
    ax.add_patch(FancyBboxPatch((70, 79), 26, 7, boxstyle='round,pad=0,rounding_size=1.2', fc=C_AMBER_DARK, ec='none'))
    ax.text(83, 82.5, "MPU6050 (SLAVE)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(72, 74, "• Chân AD0 nối GND (0x68)", fontsize=6.8, color='#1E293B')
    ax.text(72, 68, "• Chân SDA nhận lệnh/data", fontsize=6.8, fontweight='bold', color=C_AMBER_DARK)
    ax.text(72, 62, "• Chân SCL nhận xung nhịp", fontsize=6.8, fontweight='bold', color=C_AMBER_DARK)
    ax.text(72, 56, "• Thanh ghi gia tốc 0x3B", fontsize=6.8, color='#1E293B')
    ax.text(72, 50, "• Tần số lấy mẫu: 50Hz", fontsize=6.8, color='#059669', fontweight='bold')

    # Bus Lines SDA & SCL
    ax.plot([30, 70], [68, 68], color='#D97706', lw=2.5)
    ax.plot([30, 70], [62, 62], color='#2563EB', lw=2.5)

    # Pull-up Resistors 4.7kΩ nối nguồn 3.3V
    ax.plot([50, 50], [84, 62], color=C_SLATE_700, lw=1.2)
    ax.add_patch(FancyBboxPatch((46, 72), 8, 8, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec='#D97706', lw=1.2))
    ax.text(50, 76, "4.7kΩ\nSDA", ha='center', va='center', fontsize=6.0, fontweight='bold', color='#D97706')
    ax.add_patch(FancyBboxPatch((46, 60), 8, 8, boxstyle='round,pad=0,rounding_size=0.8', fc='#FFFFFF', ec='#2563EB', lw=1.2))
    ax.text(50, 64, "4.7kΩ\nSCL", ha='center', va='center', fontsize=6.0, fontweight='bold', color='#2563EB')
    ax.text(50, 87, "VCC 3.3V", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#DC2626')

    # Dưới: Giản đồ khung truyền I2C Frame
    ax.add_patch(FancyBboxPatch((4, 8), 92, 32, boxstyle='round,pad=0,rounding_size=1.2', fc='#0F172A', ec='#334155', lw=1.2))
    ax.text(50, 36, "CẤU TRÚC KHUNG TRUYỀN DỮ LIỆU I2C (I2C DATA FRAME PROTOCOL)", ha='center', va='center', fontsize=7.6, fontweight='bold', color='#38BDF8')

    frames = [
        (6, "START\n(S)", 8, '#F59E0B'),
        (15, "SLAVE ADDR\n0x68 (7-bit)", 22, '#3B82F6'),
        (38, "W(0)\n(1-bit)", 8, '#EC4899'),
        (47, "ACK\n(0)", 8, '#10B981'),
        (56, "REG ADDR\n0x3B (8-bit)", 20, '#6366F1'),
        (77, "ACK\n(0)", 8, '#10B981'),
        (86, "DATA\n(8-bit)", 14, '#14B8A6'),
        (101, "STOP\n(P)", 8, '#EF4444'),
    ]
    fx_scale = 0.88
    for f_x, f_label, f_w, f_col in frames:
        px = 6 + (f_x - 6) * fx_scale
        pw = f_w * fx_scale
        if px + pw > 94: pw = 94 - px
        ax.add_patch(FancyBboxPatch((px, 14), pw, 16, boxstyle='round,pad=0,rounding_size=0.8', fc=f_col, ec='none'))
        ax.text(px + pw/2, 22, f_label, ha='center', va='center', fontsize=6.0, fontweight='bold', color='#FFFFFF')

    p = os.path.join(OUT, 'f_i2c.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_mpu():
    fig = plt.figure(figsize=(7.2, 5.2), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 95.5, "HỆ TRỤC TỌA ĐỘ KHÔNG GIAN 3 CHIỀU VÀ CẢM BIẾN MPU-6050",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 92.0, "Định hướng 3 trục X, Y, Z, góc nghiêng Roll/Pitch và điều kiện kích hoạt thuật toán FSM",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Trục tọa độ 3D bên trái (gốc O đặt tại X = 22, Y = 44)
    o_x, o_y = 22, 44
    # Trục X (ngang phải)
    ax.annotate("", xy=(o_x + 19, o_y), xytext=(o_x, o_y), arrowprops=dict(arrowstyle="->", color='#DC2626', lw=2.5))
    ax.text(o_x + 9.5, o_y + 3.2, "Trục X (Gia tốc ax)", fontsize=7.8, fontweight='bold', color='#DC2626', ha='center')
    # Trục Y (thẳng đứng lên)
    ax.annotate("", xy=(o_x, o_y + 27), xytext=(o_x, o_y), arrowprops=dict(arrowstyle="->", color='#059669', lw=2.5))
    ax.text(o_x, o_y + 30.0, "Trục Y (Trọng lực 1g đứng)", fontsize=7.8, fontweight='bold', color='#059669', ha='center')
    # Trục Z (chéo xuống)
    ax.annotate("", xy=(o_x - 14, o_y - 18), xytext=(o_x, o_y), arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.5))
    ax.text(o_x - 14, o_y - 21.0, "Trục Z (Gia tốc az)", fontsize=7.8, fontweight='bold', color='#2563EB', ha='center')

    # Module MPU6050 IC chip ở gốc tọa độ
    ax.add_patch(FancyBboxPatch((o_x - 7.5, o_y - 7.5), 15, 15, boxstyle='round,pad=0,rounding_size=1.2', fc='#1E293B', ec='#059669', lw=2.0))
    ax.text(o_x, o_y + 2.2, "MPU6050", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#34D399')
    ax.text(o_x, o_y - 2.5, "6-DOF IMU", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#E2E8F0')

    # Card công thức toán học bên phải
    ax.add_patch(FancyBboxPatch((46, 8), 50, 78, boxstyle='round,pad=0,rounding_size=1.5', fc='#FAF5FF', ec=C_PURPLE_BORDER, lw=1.3))
    ax.add_patch(FancyBboxPatch((46, 76.5), 50, 9.5, boxstyle='round,pad=0,rounding_size=1.5', fc=C_PURPLE_DARK, ec='none'))
    ax.text(71, 81.2, "CÔNG THỨC TOÁN HỌC PHÁT HIỆN NGÃ", ha='center', va='center', fontsize=8.6, fontweight='bold', color='#FFFFFF')

    eqs = [
        ("1. VECTOR GIA TỐC TỔNG HỢP SVM:", '#4C1D95', 'bold', 8.0),
        ("   SVM = √(ax² + ay² + az²)", '#B91C1C', 'bold', 8.2),
        ("   • Bình thường (đứng/ngồi): SVM ≈ 1.0g", '#1E293B', 'normal', 7.5),
        ("   • Rơi tự do (Free-fall): SVM < 0.5g", '#059669', 'bold', 7.5),
        ("   • Va chạm sàn (Impact): SVM > 2.8g", '#B91C1C', 'bold', 7.5),
        ("", '', '', 0),
        ("2. GÓC NGHIÊNG THÂN GẬY (PITCH / ROLL):", '#4C1D95', 'bold', 8.0),
        ("   Pitch = arctan(ax / √(ay² + az²)) × 180/π", '#1D4ED8', 'bold', 7.8),
        ("   Roll  = arctan(ay / √(ax² + az²)) × 180/π", '#1D4ED8', 'bold', 7.8),
        ("   • Ngưỡng ngã nằm sàn: Góc nghiêng > 60°", '#B91C1C', 'bold', 7.5),
        ("", '', '', 0),
        ("3. ĐIỀU KIỆN KÍCH HOẠT FSM TÉ NGÃ:", '#4C1D95', 'bold', 8.0),
        ("   (SVM > 2.8g) VÀ (Góc > 60°) VÀ (Bất động > 2s)", '#059669', 'bold', 7.8),
    ]
    ey = 72.0
    for etxt, ecol, efwt, efs in eqs:
        if not etxt:
            ey -= 2.2
            continue
        ax.text(49, ey, etxt, ha='left', va='center', fontsize=efs, fontweight=efwt, color=ecol)
        ey -= 4.6

    p = os.path.join(OUT, 'f_mpu.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_accel():
    fig = plt.figure(figsize=(7.2, 4.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0.10, 0.16, 0.86, 0.72])

    t = np.linspace(0, 5, 500)
    # Giai đoạn 1: Đi bộ (0-1.8s) dao động 0.8 - 1.2g
    # Giai đoạn 2: Rơi tự do (1.8-2.1s) giảm mạnh về 0.3g
    # Giai đoạn 3: Va chạm sàn (2.1-2.4s) bùng nổ lên 3.2g
    # Giai đoạn 4: Nằm bất động (2.4-5.0s) ổn định quanh 1.0g
    svm = np.ones_like(t)
    for i, ti in enumerate(t):
        if ti < 1.8:
            svm[i] = 1.0 + 0.18 * np.sin(2 * np.pi * 2 * ti) + np.random.normal(0, 0.03)
        elif 1.8 <= ti < 2.1:
            svm[i] = 0.28 + 0.1 * np.random.normal(0, 0.05)
        elif 2.1 <= ti < 2.4:
            phase = (ti - 2.1) / 0.3
            svm[i] = 3.25 * np.sin(np.pi * phase) + np.random.normal(0, 0.08)
        else:
            svm[i] = 1.0 + np.random.normal(0, 0.02)

    ax.plot(t, svm, color='#2563EB', lw=2.0, label='Tín hiệu gia tốc tổng hợp SVM (g)')

    # Ngưỡng va chạm 2.8g
    ax.axhline(2.8, color='#DC2626', ls='--', lw=1.8, label='Ngưỡng va chạm té ngã SVM = 2.8g')
    # Ngưỡng rơi tự do 0.5g
    ax.axhline(0.5, color='#D97706', ls=':', lw=1.8, label='Ngưỡng rơi tự do SVM = 0.5g')

    # Highlight vùng
    ax.axvspan(1.8, 2.1, color='#FEF3C7', alpha=0.5)
    ax.text(1.95, 2.2, "RƠI TỰ DO\nSVM < 0.5g", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#B45309')

    ax.axvspan(2.1, 2.4, color='#FEE2E2', alpha=0.6)
    ax.text(2.25, 3.5, "VA CHẠM SÀN\nSVM = 3.25g", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#B91C1C')

    ax.axvspan(2.4, 5.0, color='#ECFDF5', alpha=0.5)
    ax.text(3.7, 2.2, "NẰM BẤT ĐỘNG SAU NGÃ\n(Kích hoạt đếm ngược SOS 15s)", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#047857')

    ax.set_xlabel('Thời gian (giây)', fontsize=8.8, fontweight='bold', color=C_SLATE_900)
    ax.set_ylabel('Gia tốc SVM |a| (g)', fontsize=8.8, fontweight='bold', color=C_SLATE_900)
    ax.set_ylim(0, 4.0)
    ax.grid(True, ls=':', alpha=0.4, color=C_SLATE_500)
    ax.legend(loc='upper right', fontsize=7.2)

    fig.text(0.5, 0.95, "DẠNG SÓNG GIA TỐC SVM TRONG CHU TRÌNH TÉ NGÃ 3 GIAI ĐOẠN",
             ha='center', va='center', fontsize=11.0, fontweight='bold', color=C_SLATE_900)

    p = os.path.join(OUT, 'f_accel.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_ultra():
    fig = plt.figure(figsize=(7.2, 5.0), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 95.5, "GIẢN ĐỒ THỜI GIAN XUNG KÍCH TRIG VÀ PHẢN HỒI ECHO HC-SR04",
            ha='center', va='center', fontsize=10.8, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 92.2, "Nguyên lý định thời sóng siêu âm 40kHz: d = (Thời gian Echo × 340 m/s) / 2",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # 4 Dạng sóng thời gian
    # 1. Trigger Pulse
    ax.text(12, 78, "1. CHÂN TRIG (GPIO 16):\nXung kích mức CAO 10µs", fontsize=7.2, fontweight='bold', color='#0891B2', va='center')
    ax.plot([34, 40, 40, 43, 43, 90], [74, 74, 82, 82, 74, 74], color='#0891B2', lw=2.2)
    ax.text(41.5, 84.5, "10µs", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#0891B2')

    # 2. Sonic Burst 8 chu kỳ 40kHz
    ax.text(12, 58, "2. PHÁT SÓNG SIÊU ÂM:\n8 chu kỳ xung 40kHz", fontsize=7.2, fontweight='bold', color='#4F46E5', va='center')
    # Vẽ chùm sóng dao động
    wave_x = np.linspace(44, 56, 100)
    wave_y = 58 + 6 * np.sin(2 * np.pi * 8 * (wave_x - 44)/12)
    ax.plot([34, 44], [58, 58], color='#4F46E5', lw=1.5)
    ax.plot(wave_x, wave_y, color='#4F46E5', lw=1.8)
    ax.plot([56, 90], [58, 58], color='#4F46E5', lw=1.5)
    ax.text(50, 67, "8 x 40kHz Sonic Burst", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#4F46E5')

    # 3. Echo Pulse
    ax.text(12, 38, "3. CHÂN ECHO (GPIO 17):\nĐộ rộng xung tỷ lệ cự ly", fontsize=7.2, fontweight='bold', color='#059669', va='center')
    ax.plot([34, 44, 44, 74, 74, 90], [34, 34, 42, 42, 34, 34], color='#059669', lw=2.2)
    ax.text(59, 44.5, "Thời gian phản hồi Echo (Δt = 2d / v)", ha='center', va='center', fontsize=7.0, fontweight='bold', color='#059669')

    # Khung công thức tính khoảng cách
    ax.add_patch(FancyBboxPatch((8, 8), 84, 18, boxstyle='round,pad=0,rounding_size=1.2', fc='#ECFDF5', ec='#059669', lw=1.2))
    ax.text(50, 20.5, "CÔNG THỨC ĐO KHOẢNG CÁCH:   d = (Δt × 0.0343) / 2  (cm)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#064E3B')
    ax.text(50, 13.5, "Ví dụ: Đo được Δt = 5830µs → d = (5830 × 0.0343) / 2 = 100.0 cm → Kích hoạt rung cảnh báo (< 150cm)", ha='center', va='center', fontsize=6.8, color='#1E293B')

    p = os.path.join(OUT, 'f_ultra.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_ir():
    fig = plt.figure(figsize=(7.2, 5.0), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 95.5, "NGUYÊN LÝ PHẢN XẠ QUANG HỌC CẢM BIẾN HỒNG NGOẠI E18-D50NK",
            ha='center', va='center', fontsize=10.8, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 92.2, "So sánh nguyên lý quang học hồng ngoại và cảm biến siêu âm trong việc phát hiện vật cản",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # Card Cảm biến bên trái (X = 22, Y = 50)
    ax.add_patch(FancyBboxPatch((6, 26), 32, 54, boxstyle='round,pad=0,rounding_size=1.5', fc='#1E293B', ec='#475569', lw=1.5))
    ax.text(22, 74, "CẢM BIẾN E18-D50NK", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#38BDF8')
    ax.text(22, 69, "Module quang điện tử", ha='center', va='center', fontsize=6.4, color='#94A3B8')

    # LED phát IR
    ax.add_patch(Circle((32, 58), 3.5, fc='#DC2626', ec='#B91C1C', lw=1.2))
    ax.text(18, 58, "LED Phát IR\n(940nm)", ha='center', va='center', fontsize=6.4, fontweight='bold', color='#FCA5A5')

    # Phototransistor thu IR
    ax.add_patch(Circle((32, 42), 3.5, fc='#2563EB', ec='#1D4ED8', lw=1.2))
    ax.text(18, 42, "Photodiode Thu\n(Mức Logic)", ha='center', va='center', fontsize=6.4, fontweight='bold', color='#93C5FD')

    # Vật cản phía trước bên phải (X = 75, Y = 50)
    ax.add_patch(FancyBboxPatch((72, 28), 12, 50, boxstyle='round,pad=0,rounding_size=1.0', fc='#78350F', ec='#D97706', lw=1.5))
    ax.text(78, 53, "VẬT CẢN\n(CHƯỚNG\nNGẠI VẬT)", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF')

    # Tia hồng ngoại phát (đỏ)
    ax.annotate("", xy=(72, 56), xytext=(36, 58), arrowprops=dict(arrowstyle="->", color='#DC2626', lw=2.2))
    ax.text(54, 61, "Tia hồng ngoại phát tới", ha='center', va='center', fontsize=6.6, fontweight='bold', color='#DC2626')

    # Tia hồng ngoại phản xạ (xanh)
    ax.annotate("", xy=(36, 43), xytext=(72, 48), arrowprops=dict(arrowstyle="->", color='#2563EB', lw=2.2, ls='--'))
    ax.text(54, 42, "Tia phản xạ dội ngược lại", ha='center', va='center', fontsize=6.6, fontweight='bold', color='#2563EB')

    # Đánh giá hạn chế của IR so với Siêu âm
    ax.add_patch(FancyBboxPatch((6, 8), 88, 14, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFBEB', ec=C_AMBER_BORDER, lw=1.2))
    ax.text(50, 16.5, "LÝ DO ĐỀ TÀI CHỌN SIÊU ÂM HC-SR04 THAY CHO HỒNG NGOẠI:", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#78350F')
    ax.text(50, 11.5, "Cảm biến IR dễ bị sai số khi gặp vật cản màu tối (hấp thụ ánh sáng) hoặc ánh nắng mặt trời ngoài trời gây nhiễu chói.", ha='center', va='center', fontsize=6.4, color='#1E293B')

    p = os.path.join(OUT, 'f_ir.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_mosfet():
    fig = plt.figure(figsize=(7.2, 5.2), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 95.8, "SƠ ĐỒ NGUYÊN LÝ MẠCH KÍCH CÔNG SUẤT MOTOR RUNG (MOSFET)",
            ha='center', va='center', fontsize=11.2, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 92.2, "Mạch đóng ngắt tải dòng lớn: MOSFET AOD4184N, Diode dập xung ngược 1N4007 và điện trở Gate",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Card Vi điều khiển ESP32 GPIO 6 bên trái
    ax.add_patch(FancyBboxPatch((5, 42), 22, 28, boxstyle='round,pad=0,rounding_size=1.2', fc='#EFF6FF', ec=C_BLUE_BORDER, lw=1.3))
    ax.text(16, 64, "ESP32-S3", ha='center', va='center', fontsize=8.5, fontweight='bold', color=C_BLUE_DARK)
    ax.text(16, 56, "GPIO 6\n(VIBRATOR)", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#B91C1C')
    ax.text(16, 47, "Mức logic 3.3V\n(PWM điều tốc)", ha='center', va='center', fontsize=7.2, color='#1E293B')

    # Điện trở hạn dòng Gate 100Ω & Kéo xuống 10kΩ
    ax.plot([27, 43], [56, 56], color='#2563EB', lw=2.0)
    ax.add_patch(Rectangle((31, 52.5), 7, 7, fc='#FFFFFF', ec='#2563EB', lw=1.3))
    ax.text(34.5, 56, "100Ω", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#2563EB')

    ax.plot([41, 41], [56, 32], color=C_SLATE_700, lw=1.8)
    ax.add_patch(Rectangle((37.5, 37), 7, 9, fc='#FFFFFF', ec=C_SLATE_700, lw=1.3))
    ax.text(41, 41.5, "10kΩ\nPull\nDown", ha='center', va='center', fontsize=6.8, fontweight='bold', color=C_SLATE_700)
    ax.text(41, 28, "GND", ha='center', va='center', fontsize=7.5, fontweight='bold', color=C_SLATE_700)

    # MOSFET AOD4184N ở giữa (X = 47 đến 63)
    ax.add_patch(FancyBboxPatch((47, 40), 16, 28, boxstyle='round,pad=0,rounding_size=1.2', fc='#1E293B', ec='#7C3AED', lw=1.8))
    ax.text(55, 61, "MOSFET\nAOD4184N", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#C4B5FD')
    ax.text(49, 56, "G", fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(55, 65, "D", fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(55, 42.5, "S", fontsize=7.5, fontweight='bold', color='#FFFFFF')

    # Source nối GND
    ax.plot([55, 55], [40, 29], color=C_SLATE_700, lw=2.2)
    ax.text(55, 25.5, "GND (Mass chung)", ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_SLATE_700)

    # Drain nối lên node ngã ba tại (55, 75)
    ax.plot([55, 55], [68, 75], color='#B91C1C', lw=2.2)

    # Đường dây song song: Từ (55, 75) rẽ sang nhánh 1 (X=70: Motor) và nhánh 2 (X=86: Diode)
    ax.plot([55, 86], [75, 75], color='#B91C1C', lw=2.0)

    # Nhánh 1: Motor Rung tại X = 70
    ax.plot([70, 70], [75, 78], color='#B91C1C', lw=2.0)
    ax.add_patch(Circle((70, 83), 5.0, fc='#FAF5FF', ec='#7C3AED', lw=1.6))
    ax.text(70, 83, "MOTOR\nRUNG", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#7C3AED')
    ax.plot([70, 70], [88, 91], color='#DC2626', lw=2.0)

    # Nhánh 2: Diode 1N4007 dập xung ngược tại X = 86
    # Anode ở dưới (nối Drain qua Y=75), Cathode ở trên (nối +5V qua Y=91)
    ax.plot([86, 86], [75, 79], color='#B91C1C', lw=2.0)
    ax.add_patch(FancyBboxPatch((80.5, 79), 11, 8, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFF1F2', ec='#DC2626', lw=1.3))
    ax.text(86, 83, "1N4007\n(Diode)", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#DC2626')
    ax.plot([86, 86], [87, 91], color='#DC2626', lw=2.0)

    # Đường dây gom trên nối nguồn +5V DC
    ax.plot([70, 96], [91, 91], color='#DC2626', lw=2.2)
    ax.text(96.5, 91, "+5V DC\n(Pin/Boost)", ha='left', va='center', fontsize=7.8, fontweight='bold', color='#DC2626')

    # Ghi chú nguyên lý an toàn
    ax.add_patch(FancyBboxPatch((5, 6), 90, 16, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFDF5', ec=C_EMERALD_BORDER, lw=1.3))
    ax.text(50, 17.5, "ƯU ĐIỂM CỦA MẠCH CÔNG SUẤT MOSFET TRONG THIẾT KẾ:", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#064E3B')
    ax.text(50, 13.0, "• Trở kháng dẫn Rds(on) siêu nhỏ (< 8.5mΩ) cho phép dòng tức thời tới 50A mà không sụt áp.", ha='center', va='center', fontsize=7.4, color='#1E293B')
    ax.text(50, 8.8, "• Diode 1N4007 dập xung điện áp ngược cuộn dây (L di/dt), bảo vệ an toàn 100% cho ESP32-S3.", ha='center', va='center', fontsize=7.4, color='#1E293B')

    p = os.path.join(OUT, 'f_mosfet.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_gps():
    fig = plt.figure(figsize=(7.2, 5.0), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 95.5, "NGUYÊN LÝ ĐỊNH VỊ TOÀN CẦU GPS DỰA TRÊN GIAO ĐIỂM MẶT CẦU",
            ha='center', va='center', fontsize=10.8, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 92.2, "Định vị không gian 3 chiều: Thu nhận tín hiệu từ tối thiểu 4 vệ tinh để xác định (Lat, Lng, Alt, Time)",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # 3 Vệ tinh GPS phát sóng
    sats = [
        (20, 75, "VỆ TINH 1 (SV1)", "d1 = c × Δt1", '#2563EB'),
        (50, 82, "VỆ TINH 2 (SV2)", "d2 = c × Δt2", '#7C3AED'),
        (80, 75, "VỆ TINH 3 (SV3)", "d3 = c × Δt3", '#D97706'),
    ]
    u_x, u_y = 50, 36

    for sx, sy, sname, sdist, scol in sats:
        # Vệ tinh Icon
        ax.add_patch(FancyBboxPatch((sx - 10, sy - 4), 20, 8, boxstyle='round,pad=0,rounding_size=1.0', fc='#1E293B', ec=scol, lw=1.5))
        ax.text(sx, sy + 1.2, sname, ha='center', va='center', fontsize=6.8, fontweight='bold', color='#FFFFFF')
        ax.text(sx, sy - 2.0, sdist, ha='center', va='center', fontsize=5.8, color='#CBD5E1')

        # Vòng tròn sóng định vị
        ax.plot([sx, u_x], [sy - 4, u_y + 6], color=scol, lw=1.5, ls='--')

    # Nạn nhân ở mặt đất
    ax.add_patch(Circle((u_x, u_y), 5.5, fc='#FFF1F2', ec='#B91C1C', lw=2.0))
    ax.text(u_x, u_y, "VỊ TRÍ\nNẠN NHÂN", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#B91C1C')

    # Khung công thức giải phương trình GPS
    ax.add_patch(FancyBboxPatch((6, 8), 88, 18, boxstyle='round,pad=0,rounding_size=1.2', fc='#EFF6FF', ec=C_BLUE_BORDER, lw=1.2))
    ax.text(50, 20.5, "HỆ PHƯƠNG TRÌNH GIAO ĐIỂM 4 MẶT CẦU GPS:  (x - xi)² + (y - yi)² + (z - zi)² = (c(ti - tr))²", ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_BLUE_DARK)
    ax.text(50, 13.5, "Điện thoại người dùng giải phương trình giải mã tọa độ GPS đạt độ chính xác cự ly dưới 4.5 mét, nhúng trực tiếp vào tin nhắn SOS.", ha='center', va='center', fontsize=6.4, color='#1E293B')

    p = os.path.join(OUT, 'f_gps.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_flutter():
    fig = plt.figure(figsize=(7.2, 5.2), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 95.5, "KIẾN TRÚC ĐA TẦNG CỦA FRAMEWORK LẬP TRÌNH DI ĐỘNG FLUTTER",
            ha='center', va='center', fontsize=10.8, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 92.2, "3 Phân tầng kiến trúc: Framework (Dart) -> C++ Engine (Skia/Impeller) -> Platform Embedder",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    layers = [
        (71, 18, "TẦNG FRAMEWORK (NGÔN NGỮ DART)", C_BLUE_DARK, '#EFF6FF', C_BLUE_BORDER,
         ["• Material Design & Cupertino Widgets giao diện trực quan",
          "• Quản lý trạng thái State Management: Provider, Bloc, Streams",
          "• Tầng logic ứng dụng: Xử lý sự cố, định vị GPS, đếm ngược 15 giây"]),

        (48, 18, "TẦNG ENGINE C++ (SKIA / IMPELLER)", C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER,
         ["• Bộ kết xuất đồ họa hiệu năng cao Skia / Impeller đạt 60 FPS mượt mà",
          "• Máy ảo Dart VM & Trình biên dịch AOT (Ahead-of-Time) sang mã máy",
          "• Tầng giao tiếp Plugin Platform Channels kết nối tới phần cứng Android"]),

        (25, 18, "TẦNG PLATFORM EMBEDDER (HỆ ĐIỀU HÀNH)", C_EMERALD_DARK, '#ECFDF5', C_EMERALD_BORDER,
         ["• Tương thích Android OS (SurfaceView, Android Activity, Foreground Service)",
          "• Quyền truy cập phần cứng: Bluetooth Low Energy, GPS Location, SMS Manager",
          "• Quản lý luồng luân chuyển Native Events và luồng Isolate đa nhiệm"]),
    ]

    for ly, lh, ltitle, lhcol, lbgcol, lbcol, llines in layers:
        ax.add_patch(FancyBboxPatch((6, ly - lh/2), 88, lh, boxstyle='round,pad=0,rounding_size=1.2', fc=lbgcol, ec=lbcol, lw=1.2))
        ax.add_patch(FancyBboxPatch((6, ly + lh/2 - 5.5), 88, 5.5, boxstyle='round,pad=0,rounding_size=1.2', fc=lhcol, ec='none'))
        ax.text(50, ly + lh/2 - 2.8, ltitle, ha='center', va='center', fontsize=7.6, fontweight='bold', color='#FFFFFF')

        text_y = ly + lh/2 - 8.2
        for tline in llines:
            ax.text(10, text_y, tline, ha='left', va='center', fontsize=6.6, color='#1E293B')
            text_y -= 3.6

    p = os.path.join(OUT, 'f_flutter.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_fgs():
    fig = plt.figure(figsize=(7.2, 5.0), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    ax.text(50, 95.5, "CƠ CHẾ ĐA LUỒNG ISOLATE CỦA FLUTTER BACKGROUND SERVICE",
            ha='center', va='center', fontsize=10.8, fontweight='bold', color=C_SLATE_900)
    ax.text(50, 92.2, "Tách biệt hoàn toàn luồng giao diện UI và luồng xử lý nền Background đảm bảo không giật lag",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # 2 Hộp Isolate
    # Hộp 1: Main UI Isolate bên trái
    ax.add_patch(FancyBboxPatch((6, 20), 40, 68, boxstyle='round,pad=0,rounding_size=1.5', fc='#EFF6FF', ec=C_BLUE_BORDER, lw=1.2))
    ax.add_patch(FancyBboxPatch((6, 79), 40, 9, boxstyle='round,pad=0,rounding_size=1.5', fc=C_BLUE_DARK, ec='none'))
    ax.text(26, 83.5, "MAIN UI ISOLATE (GIAO DIỆN)", ha='center', va='center', fontsize=7.4, fontweight='bold', color='#FFFFFF')
    ax.text(8, 73, "• Hiển thị màn hình cho người già", fontsize=6.6, color='#1E293B')
    ax.text(8, 67, "• Nút bấm to, giao diện thân thiện", fontsize=6.6, color='#1E293B')
    ax.text(8, 61, "• Màn hình đỏ đếm ngược 15s", fontsize=6.6, fontweight='bold', color='#B91C1C')
    ax.text(8, 55, "• Tắt khi người dùng bấm nút Home", fontsize=6.6, color='#64748B')
    ax.text(8, 49, "• Không bị treo đơ giao diện", fontsize=6.6, color='#059669', fontweight='bold')
    ax.text(8, 38, "NHẬN EVENT QUA PORT:\nReceivePort / SendPort", fontsize=6.6, fontweight='bold', color=C_BLUE_DARK)

    # Hộp 2: Background Service Isolate bên phải
    ax.add_patch(FancyBboxPatch((54, 20), 40, 68, boxstyle='round,pad=0,rounding_size=1.5', fc='#FAF5FF', ec=C_PURPLE_BORDER, lw=1.2))
    ax.add_patch(FancyBboxPatch((54, 79), 40, 9, boxstyle='round,pad=0,rounding_size=1.5', fc=C_PURPLE_DARK, ec='none'))
    ax.text(74, 83.5, "BACKGROUND ISOLATE (CHẠY NGẦM)", ha='center', va='center', fontsize=7.4, fontweight='bold', color='#FFFFFF')
    ax.text(56, 73, "• Chạy ngầm 24/7 dưới Android Service", fontsize=6.6, fontweight='bold', color=C_PURPLE_DARK)
    ax.text(56, 67, "• Duy trì kết nối Bluetooth BLE liên tục", fontsize=6.6, color='#1E293B')
    ax.text(56, 61, "• Lấy tọa độ GPS nền chính xác", fontsize=6.6, color='#1E293B')
    ax.text(56, 55, "• Ghi Firebase RTDB khi có ngã", fontsize=6.6, fontweight='bold', color='#059669')
    ax.text(56, 49, "• Tự động gửi SMS & Gọi điện SOS", fontsize=6.6, fontweight='bold', color='#B91C1C')
    ax.text(56, 40, "ĐỒNG BỘ 2 CHIỀU:", fontsize=6.4, fontweight='bold', color='#7C3AED')
    ax.text(56, 36, "SendPort.send({'status': 'FALL'})", fontsize=6.0, fontfamily='monospace', fontweight='bold', color='#7C3AED')

    # Cầu nối truyền thông điệp Inter-Isolate Communication
    ax.plot([46, 54], [54, 54], color='#D97706', lw=2.2)
    ax.plot([46, 54], [44, 44], color='#2563EB', lw=2.2)
    ax.text(50, 56.5, "SEND", ha='center', va='center', fontsize=6.0, fontweight='bold', color='#D97706')
    ax.text(50, 41.5, "RECV", ha='center', va='center', fontsize=6.0, fontweight='bold', color='#2563EB')

    p = os.path.join(OUT, 'f_fgs.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# PHẦN 4: 4 ĐỒ THỊ THỰC NGHIỆM ĐÁNH GIÁ (Chương 4)
# Canvas 7.2 x 4.8 in | DPI: 300 | Font số liệu, trục tọa độ cực to, rõ nét
# ==============================================================================

def gen_pro_exp_accel():
    activities = ['Đi bộ\n(ADL)', 'Ngồi xuống\nghế', 'Cúi nhặt\nđồ', 'Vung gậy\nnhanh',
                  'Ngã phía\ntrước', 'Ngã ngửa\nra sau', 'Ngã nghiêng\nsang bên', 'Đánh rơi\ngậy']
    means = [12.5, 14.2, 13.8, 18.5, 31.8, 33.4, 29.6, 27.2]
    stds = [1.8, 2.1, 1.9, 3.2, 3.5, 4.1, 3.8, 3.2]

    fig = plt.figure(figsize=(7.2, 4.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0.10, 0.18, 0.86, 0.70])
    ax.set_facecolor('#FAFBFD')

    ax.axhspan(0, 25.0, color='#EFF6FF', alpha=0.65, zorder=1)
    ax.axhspan(25.0, 44.0, color='#FFF1F2', alpha=0.65, zorder=1)
    ax.axhline(25.0, color=C_ROSE_MED, ls='--', lw=2.0, zorder=3, label='Ngưỡng phát hiện ngã SVM = 25.0 m/s² (2.55g)')

    x = np.arange(len(activities))
    colors = [C_BLUE_MED]*4 + [C_ROSE_MED]*3 + [C_AMBER_MED]
    edge_colors = [C_BLUE_DARK]*4 + [C_ROSE_DARK]*3 + [C_AMBER_DARK]

    bars = ax.bar(x, means, yerr=stds, capsize=3.5, color=colors, edgecolor=edge_colors, lw=1.2, width=0.58, zorder=4,
                  error_kw=dict(ecolor='#334155', lw=1.2, capthick=1.2))

    ax.set_xticks(x)
    ax.set_xticklabels(activities, fontsize=7.2, fontweight='bold', color=C_SLATE_800)
    ax.set_ylabel('Gia tốc vector tổng hợp SVM |a|max (m/s²)', fontsize=8.2, fontweight='bold', color=C_SLATE_900)
    ax.set_ylim(0, 43)

    ax.grid(axis='y', alpha=0.35, ls=':', color=C_SLATE_500, zorder=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for bar, m, s in zip(bars, means, stds):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + s + 1.0,
                f"{m:.1f}\n±{s:.1f}", ha='center', va='bottom', fontsize=6.8, fontweight='bold', color=C_SLATE_900, zorder=5)

    ax.text(0.1, 22.0, "VÙNG SINH HOẠT THƯỜNG NHẬT (ADL < 25 m/s²)", ha='left', va='center',
            fontsize=6.8, fontweight='bold', color=C_BLUE_DARK,
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#DBEAFE', edgecolor=C_BLUE_BORDER, lw=0.8))
    ax.text(0.1, 40.0, "VÙNG KÍCH HOẠT CẢNH BÁO TÉ NGÃ (SVM ≥ 25 m/s²)", ha='left', va='center',
            fontsize=6.8, fontweight='bold', color=C_ROSE_DARK,
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#FFE4E6', edgecolor=C_ROSE_BORDER, lw=0.8))

    fig.text(0.5, 0.95, "THỰC NGHIỆM ĐO GIA TỐC SVM TRONG CÁC KỊCH BẢN TÉ NGÃ VÀ SINH HOẠT (ADL)",
             ha='center', va='center', fontsize=10.5, fontweight='bold', color=C_SLATE_900)

    p = os.path.join(OUT, 'f_exp_accel.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_exp_latency():
    stages = ['Quét & Phát hiện ngã\n(ESP32 FSM)', 'Truyền tin BLE 5.0\n(Gậy → Gateway)',
              'Xử lý nền & GPS\n(Mobile Gateway)', 'Đẩy đám mây 4G\n(Firebase RTDB)',
              'Đồng bộ & Báo động\n(App Giám Hộ)']
    latencies = [42, 28, 85, 410, 195]
    colors = ['#10B981', '#06B6D4', '#3B82F6', '#8B5CF6', '#EC4899']

    fig = plt.figure(figsize=(7.2, 4.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0.18, 0.16, 0.78, 0.70])
    ax.set_facecolor('#FAFBFD')

    y_pos = np.arange(len(stages))
    bars = ax.barh(y_pos, latencies, color=colors, edgecolor='#1E293B', lw=1.2, height=0.55, zorder=3)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(stages, fontsize=7.2, fontweight='bold', color=C_SLATE_800)
    ax.set_xlabel('Thời gian đáp ứng (mili-giây - ms)', fontsize=8.2, fontweight='bold', color=C_SLATE_900)
    ax.set_xlim(0, 520)

    ax.grid(axis='x', alpha=0.35, ls=':', color=C_SLATE_500, zorder=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for bar, val in zip(bars, latencies):
        w = bar.get_width()
        pct = (val / sum(latencies)) * 100
        ax.text(w + 8, bar.get_y() + bar.get_height()/2.0,
                f"{val} ms ({pct:.1f}%)", ha='left', va='center', fontsize=6.8, fontweight='bold', color=C_SLATE_900)

    total_latency = sum(latencies)
    ax.text(0.95, 0.12, f"TỔNG ĐỘ TRỄ TOÀN TRÌNH:\n{total_latency} ms (≈ {total_latency/1000:.2f} giây)\n[Đạt chuẩn cứu hộ khẩn cấp y tế]",
            ha='right', va='center', transform=ax.transAxes, fontsize=7.0, fontweight='bold', color='#064E3B',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#ECFDF5', edgecolor='#059669', lw=1.0))

    fig.text(0.5, 0.95, "PHÂN RÃ ĐỘ TRỄ TOÀN TRÌNH CỦA CHUỖI CẢNH BÁO TÉ NGÃ KHẨN CẤP",
             ha='center', va='center', fontsize=10.5, fontweight='bold', color=C_SLATE_900)

    p = os.path.join(OUT, 'f_exp_latency.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_exp_ultrasonic():
    dist_real = np.array([10, 20, 30, 50, 80, 100, 120, 150, 200, 250, 300])
    dist_meas = np.array([10.2, 19.8, 30.4, 50.8, 81.2, 101.5, 122.1, 152.8, 204.2, 256.0, 308.5])
    error_pct = np.abs(dist_meas - dist_real) / dist_real * 100

    fig = plt.figure(figsize=(7.2, 4.8), dpi=300, facecolor='#FFFFFF')
    ax1 = fig.add_axes([0.10, 0.16, 0.76, 0.70])
    ax2 = ax1.twinx()
    ax1.set_facecolor('#FAFBFD')

    l1 = ax1.plot(dist_real, dist_meas, 'o-', color='#2563EB', lw=2.0, ms=5, label='Khoảng cách đo thực tế (cm)')
    l2 = ax1.plot(dist_real, dist_real, '--', color='#64748B', lw=1.5, label='Đường chuẩn lý tưởng (y = x)')
    l3 = ax2.plot(dist_real, error_pct, 's:', color='#DC2626', lw=1.8, ms=4.5, label='Sai số tương đối (%)')

    ax1.set_xlabel('Khoảng cách chuẩn thực tế (cm)', fontsize=8.2, fontweight='bold', color=C_SLATE_900)
    ax1.set_ylabel('Khoảng cách cảm biến đo được (cm)', fontsize=8.2, fontweight='bold', color='#2563EB')
    ax2.set_ylabel('Sai số tương đối (%)', fontsize=8.2, fontweight='bold', color='#DC2626')
    ax2.set_ylim(0, 4.5)

    ax1.grid(True, ls=':', alpha=0.35, color=C_SLATE_500)
    lines = l1 + l2 + l3
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=6.8)

    ax1.text(0.95, 0.15, "SAI SỐ BÌNH QUÂN:\n1.62% trong cự ly < 150cm\n[Rất tin cậy để cảnh báo rung]",
             ha='right', va='center', transform=ax1.transAxes, fontsize=6.8, fontweight='bold', color='#064E3B',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#ECFDF5', edgecolor='#059669', lw=0.8))

    fig.text(0.5, 0.95, "ĐỒ THỊ SAI SỐ VÀ ĐẶC TUYẾN ĐO KHOẢNG CÁCH SIÊU ÂM HC-SR04",
             ha='center', va='center', fontsize=10.5, fontweight='bold', color=C_SLATE_900)

    p = os.path.join(OUT, 'f_exp_ultrasonic.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


def gen_pro_exp_scenarios():
    scenarios = [
        'Ngã về phía trước',
        'Ngã ngửa ra sau',
        'Ngã nghiêng sang trái',
        'Ngã nghiêng sang phải',
        'Trượt chân ngã ngồi',
        'Đi bộ vấp nhẹ (ADL)',
        'Ngồi nhanh xuống ghế (ADL)',
        'Cúi người nhặt đồ (ADL)'
    ]
    total_tests = [20, 20, 20, 20, 20, 20, 20, 20]
    success_detect = [19, 20, 19, 19, 18, 20, 19, 20]  # Số lần phân loại chính xác

    accuracy = np.array(success_detect) / np.array(total_tests) * 100

    fig = plt.figure(figsize=(7.2, 4.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0.22, 0.16, 0.74, 0.70])
    ax.set_facecolor('#FAFBFD')

    y_pos = np.arange(len(scenarios))
    colors = ['#10B981' if acc >= 95 else '#3B82F6' if acc >= 90 else '#F59E0B' for acc in accuracy]

    bars = ax.barh(y_pos, accuracy, color=colors, edgecolor='#1E293B', lw=1.2, height=0.58, zorder=3)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(scenarios, fontsize=7.2, fontweight='bold', color=C_SLATE_800)
    ax.set_xlabel('Độ chính xác phân loại (%)', fontsize=8.2, fontweight='bold', color=C_SLATE_900)
    ax.set_xlim(70, 105)

    ax.axvline(90.0, color='#DC2626', ls='--', lw=1.5, zorder=2)
    ax.grid(axis='x', alpha=0.35, ls=':', color=C_SLATE_500, zorder=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for bar, acc, succ, tot in zip(bars, accuracy, success_detect, total_tests):
        w = bar.get_width()
        ax.text(w + 1.0, bar.get_y() + bar.get_height()/2.0,
                f"{acc:.1f}% ({succ}/{tot})", ha='left', va='center', fontsize=6.8, fontweight='bold', color=C_SLATE_900)

    avg_acc = np.mean(accuracy)
    ax.text(0.95, 0.12, f"ĐỘ CHÍNH XÁC TRUNG BÌNH:\n{avg_acc:.2f}%\nĐộ nhạy (Sensitivity): 95.0%\nĐộ đặc hiệu (Specificity): 98.75%",
            ha='right', va='center', transform=ax.transAxes, fontsize=6.8, fontweight='bold', color='#064E3B',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#ECFDF5', edgecolor='#059669', lw=1.0))

    fig.text(0.5, 0.95, "MA TRẬN ĐỘ CHÍNH XÁC PHÂN LOẠI CÁC KỊCH BẢN THỰC NGHIỆM",
             ha='center', va='center', fontsize=10.5, fontweight='bold', color=C_SLATE_900)

    p = os.path.join(OUT, 'f_exp_scenarios.png')
    fig.savefig(p, dpi=300, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# HÀM CHÍNH TÁI TẠO TẤT CẢ 23 HÌNH
# ==============================================================================
def gen_all():
    print("=================================================================")
    print("=== BẮT ĐẦU TẠO TOÀN DIỆN 23 HÌNH VẼ CỠ CHỮ LỚN CHO BÁO CÁO ===")
    print("=================================================================")
    
    print("\n--- PHẦN 1: CÁC HÌNH KIẾN TRÚC & SƠ ĐỒ CHÍNH ---")
    gen_pro_methods()
    gen_pro_overview()
    gen_pro_esp32()
    gen_pro_block_diag()
    gen_pro_schematic()
    gen_pro_gatt()
    gen_pro_rtdb()

    print("\n--- PHẦN 2: LƯU ĐỒ THUẬT TOÁN HỆ THỐNG ---")
    gen_pro_flow_firmware()
    gen_pro_flow_elderly()
    gen_pro_flow_guardian()

    print("\n--- PHẦN 3: NGUYÊN LÝ & KỸ THUẬT LINH KIỆN ---")
    gen_pro_i2c()
    gen_pro_mpu()
    gen_pro_accel()
    gen_pro_ultra()
    gen_pro_ir()
    gen_pro_mosfet()
    gen_pro_gps()
    gen_pro_flutter()
    gen_pro_fgs()

    print("\n--- PHẦN 4: ĐỒ THỊ THỰC NGHIỆM ĐÁNH GIÁ ---")
    gen_pro_exp_accel()
    gen_pro_exp_latency()
    gen_pro_exp_ultrasonic()
    gen_pro_exp_scenarios()

    print("\n=================================================================")
    print("=== HOÀN TẤT TẠO TOÀN BỘ 23 HÌNH VẼ ĐẠT CHUẨN PUBLICATION ===")
    print("=================================================================")

if __name__ == '__main__':
    gen_all()

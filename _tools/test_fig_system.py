# -*- coding: utf-8 -*-
"""
test_fig_system.py
Thực nghiệm chuẩn hóa kích thước Typography và Canvas cho toàn bộ sơ đồ đồ án.
Mục tiêu: Đảm bảo chữ to, đậm, rõ ràng, không bị tràn viền và cực kỳ sắc nét khi chèn vào Word.
"""
import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
from matplotlib import font_manager

for f in ['C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/segoeuib.ttf', 'C:/Windows/Fonts/arial.ttf', 'C:/Windows/Fonts/arialbd.ttf']:
    if os.path.exists(f):
        font_manager.fontManager.addfont(f)

plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

OUT = r'd:\doan\_tools\fig'
os.makedirs(OUT, exist_ok=True)

# Bảng màu chuẩn
C_SLATE_900 = '#0F172A'
C_SLATE_800 = '#1E293B'
C_SLATE_700 = '#334155'
C_SLATE_500 = '#64748B'
C_SLATE_200 = '#E2E8F0'

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

C_CYAN_MED   = '#0891B2'
C_CYAN_LIGHT = '#ECFEFF'
C_CYAN_BORDER= '#67E8F9'


def draw_card_pro(ax, x, y, w, h, title='', badge=None,
                  header_color=C_SLATE_800, bg_color='#FFFFFF', border_color=C_SLATE_200,
                  rx=1.8, shadow=True, hh=6.8, title_fs=8.2, badge_fs=6.2):
    """Card chuẩn đồ họa cao cấp 2 tầng tiêu đề: Badge phía trên, Title phía dưới."""
    x0, y0 = x - w / 2, y - h / 2

    if shadow:
        ax.add_patch(FancyBboxPatch((x0 + 0.35, y0 - 0.35), w, h,
                                   boxstyle=f'round,pad=0,rounding_size={rx}',
                                   fc='#0F172A', ec='none', alpha=0.08, zorder=1))

    card = FancyBboxPatch((x0, y0), w, h,
                          boxstyle=f'round,pad=0,rounding_size={rx}',
                          fc=bg_color, ec=border_color, lw=1.3, zorder=2)
    ax.add_patch(card)

    if title:
        ax.add_patch(FancyBboxPatch((x0, y0 + h - hh), w, hh,
                                   boxstyle=f'round,pad=0,rounding_size={rx}',
                                   fc=header_color, ec='none', zorder=3))
        ax.add_patch(Rectangle((x0, y0 + h - hh), w, rx, fc=header_color, ec='none', zorder=3))

        if badge:
            bw = len(badge) * 0.72 + 2.4
            ax.add_patch(FancyBboxPatch((x - bw / 2, y0 + h - 2.2 - 1.8 / 2), bw, 1.8,
                                       boxstyle='round,pad=0,rounding_size=0.9',
                                       fc='#FFFFFF', ec='none', alpha=0.22, zorder=4))
            ax.text(x, y0 + h - 2.2, badge, ha='center', va='center',
                    fontsize=badge_fs, fontweight='bold', color='#FFFFFF', zorder=5)
            ax.text(x, y0 + h - 4.8, title, ha='center', va='center',
                    fontsize=title_fs, fontweight='bold', color='#FFFFFF', zorder=5)
        else:
            ax.text(x, y0 + h - hh / 2, title, ha='center', va='center',
                    fontsize=title_fs + 0.6, fontweight='bold', color='#FFFFFF', zorder=5)

    return card


# ==============================================================================
# HÌNH 1.1: SƠ ĐỒ PHÂN LOẠI CÁC PHƯƠNG PHÁP PHÁT HIỆN TÉ NGÃ
# ==============================================================================
def gen_f_methods():
    w, h = 13.0, 9.8
    fig = plt.figure(figsize=(w, h), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 98)
    ax.axis('off')

    ax.text(65, 94.0, 'SƠ ĐỒ PHÂN LOẠI CÁC PHƯƠNG PHÁP PHÁT HIỆN VÀ CẢNH BÁO TÉ NGÃ',
            ha='center', va='center', fontsize=13.5, fontweight='bold', color=C_SLATE_900)
    ax.text(65, 90.5, 'So sánh các hướng tiếp cận công nghệ và tính ưu việt của giải pháp Gậy thông minh IoT',
            ha='center', va='center', fontsize=9.2, color=C_SLATE_500, fontstyle='italic')

    # Root button
    ax.add_patch(FancyBboxPatch((25, 81.5), 80, 6.5, boxstyle='round,pad=0,rounding_size=2.0', fc=C_SLATE_900, ec='none', zorder=3))
    ax.text(65, 84.75, 'CÁC PHƯƠNG PHÁP PHÁT HIỆN & CẢNH BÁO TÉ NGÃ Ở NGƯỜI CAO TUỔI',
            ha='center', va='center', fontsize=9.6, fontweight='bold', color='#FFFFFF', zorder=4)

    # 4 Traditional Cards
    t_cards = [
        (17.5, 'THIẾT BỊ ĐEO TAY', 'SMARTWATCH / VÒNG ĐEO', C_AMBER_DARK, '#FFFDF5', C_AMBER_BORDER,
         ['• Cảm biến gia tốc đeo tay', '• Nhỏ gọn, hiển thị giờ', '[-] Nhược điểm chính:', '  • Người già hay quên đeo', '  • Phải sạc pin mỗi 1-2 ngày', '  • Thao tác cảm ứng khó khăn']),
        (49.0, 'CAMERA THỊ GIÁC', 'COMPUTER VISION AI', C_BLUE_DARK, '#F8FAFC', C_BLUE_BORDER,
         ['• Camera nhận diện qua AI', '• Độ chính xác nhận dạng cao', '[-] Nhược điểm chính:', '  • Xâm phạm quyền riêng tư', '  • Góc chết (phòng tắm, ngủ)', '  • Chi phí lắp đặt rất đắt']),
        (81.0, 'CẢM BIẾN MÔI TRƯỜNG', 'ÂM THANH / RUNG SÀN', C_CYAN_MED, '#F0FDFA', C_CYAN_BORDER,
         ['• Micro mảng, sàn áp điện', '• Không cần đeo trên người', '[-] Nhược điểm chính:', '  • Dễ báo động giả do tạp âm', '  • Đồ vật rơi gây nhiễu sai', '  • Giới hạn trong căn phòng']),
        (112.5, 'RADAR KHÔNG DÂY', 'mmWAVE / UWB RADAR', C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER,
         ['• Quét sóng phản xạ radar', '• Không dùng camera ghi hình', '[-] Nhược điểm chính:', '  • Giá linh kiện rất đắt đỏ', '  • Bị che chắn bởi đồ đạc', '  • Lắp đặt cố định tại chỗ']),
    ]

    for cx, title, badge, hcol, bgcol, bcol, lines in t_cards:
        ax.plot([65, cx], [81.5, 75.0], color=hcol, lw=1.8, zorder=2)
        draw_card_pro(ax, cx, 57.5, 28.5, 35.0, title=title, badge=badge,
                      header_color=hcol, bg_color=bgcol, border_color=bcol, hh=7.0, title_fs=8.5, badge_fs=6.2)
        
        ly = 69.5
        for l in lines:
            is_bad = '[-]' in l or '  •' in l
            col = '#DC2626' if is_bad else (hcol if '• Cảm' in l or '• Micro' in l or '• Quét' in l or '• Camera' in l else C_SLATE_800)
            fwt = 'bold' if is_bad or '[-]' in l else 'normal'
            ax.text(cx - 12.8, ly, l, ha='left', va='center', fontsize=7.8, fontweight=fwt, color=col, zorder=5)
            ly -= 3.7

    # HERO CARD: GẬY THÔNG MINH IOT
    hx, hy, hw, hh = 65, 20.0, 123.5, 33.0
    hx0, hy0 = hx - hw/2, hy - hh/2
    ax.add_patch(FancyBboxPatch((hx0+0.5, hy0-0.5), hw, hh, boxstyle='round,pad=0,rounding_size=2.5', fc='#0F172A', alpha=0.1, zorder=2))
    ax.add_patch(FancyBboxPatch((hx0, hy0), hw, hh, boxstyle='round,pad=0,rounding_size=2.5', fc='#F0FDF4', ec='#059669', lw=2.0, zorder=3))
    
    head_h = 7.5
    ax.add_patch(FancyBboxPatch((hx0, hy0+hh-head_h), hw, head_h, boxstyle='round,pad=0,rounding_size=2.5', fc='#064E3B', ec='none', zorder=4))
    ax.add_patch(Rectangle((hx0, hy0+hh-head_h), hw, 2.5, fc='#064E3B', ec='none', zorder=4))
    ax.text(hx0 + 3.0, hy0 + hh - head_h/2, 'GIẢI PHÁP ĐỀ TÀI: GẬY THÔNG MINH IoT (SMART CANE)', ha='left', va='center', fontsize=10.5, fontweight='bold', color='#FFFFFF', zorder=5)
    ax.text(hx0 + hw - 3.0, hy0 + hh - head_h/2, '[+] KHẮC PHỤC HOÀN TOÀN CÁC NHƯỢC ĐIỂM TRÊN', ha='right', va='center', fontsize=8.6, fontweight='bold', color='#A7F3D0', zorder=5)

    fbox_w = 28.5
    fbox_h = 21.0
    fboxes = [
        (hx0 + 2.0 + fbox_w/2, 'CẢM BIẾN & XỬ LÝ', [
            '• ESP32-S3 Dual-Core',
            '• MPU-6050 phát hiện ngã',
            '• Thuật toán vector SVM',
            '• HC-SR04 quét vật cản',
        ]),
        (hx0 + 32.5 + fbox_w/2, 'VẬT DỤNG THỰC DỤNG', [
            '• Gậy là vật bất ly thân',
            '• Luôn mang theo khi đi lại',
            '• Không lo quên như vòng đeo',
            '• Pin sạc Type-C tiện lợi',
        ]),
        (hx0 + 63.0 + fbox_w/2, '100% RIÊNG TƯ', [
            '• Không dùng Camera giám sát',
            '• Hoạt động cả trong toilet',
            '• Tuyệt đối bảo mật đời tư',
            '• Người già an tâm sử dụng',
        ]),
        (hx0 + 93.5 + fbox_w/2, 'CẢNH BÁO ĐA KÊNH', [
            '• Còi hú 85dB + Rung tại chỗ',
            '• Cloud Firebase thời gian thực',
            '• SMS link Google Maps',
            '• Tự động gọi điện SOS',
        ]),
    ]

    for bx, btitle, blines in fboxes:
        bx0, by0 = bx - fbox_w/2, hy0 + 2.2
        ax.add_patch(FancyBboxPatch((bx0, by0), fbox_w, fbox_h, boxstyle='round,pad=0,rounding_size=1.5', fc='#FFFFFF', ec='#A7F3D0', lw=1.2, zorder=5))
        ax.add_patch(FancyBboxPatch((bx0, by0+fbox_h-5.0), fbox_w, 5.0, boxstyle='round,pad=0,rounding_size=1.5', fc='#ECFDF5', ec='none', zorder=6))
        ax.add_patch(Rectangle((bx0, by0+fbox_h-5.0), fbox_w, 1.5, fc='#ECFDF5', ec='none', zorder=6))
        ax.text(bx, by0+fbox_h-2.5, btitle, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#065F46', zorder=7)
        
        bly = by0 + fbox_h - 7.5
        for bl in blines:
            ax.text(bx0 + 2.0, bly, bl, ha='left', va='center', fontsize=8.2, fontweight='bold', color='#0F172A', zorder=7)
            bly -= 3.8

    ax.text(65, 1.5, 'Hình 1.1: Sơ đồ phân loại các phương pháp phát hiện và cảnh báo té ngã hiện nay', ha='center', va='center', fontsize=9.0, color='#334155', fontweight='bold')

    p = os.path.join(OUT, 'f_methods.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã cập nhật f_methods chuẩn nét: {p}")
    return p


# ==============================================================================
# HÌNH 1.2: MÔ HÌNH KIẾN TRÚC TỔNG THỂ HỆ THỐNG GẬY THÔNG MINH
# ==============================================================================
def gen_f_overview():
    w, h = 11.5, 7.2
    fig = plt.figure(figsize=(w, h), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 115)
    ax.set_ylim(0, 72)
    ax.axis('off')

    ax.text(57.5, 68.5, 'MÔ HÌNH KIẾN TRÚC TỔNG THỂ HỆ THỐNG GẬY THÔNG MINH (SMART CANE IoT)',
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#0F172A')
    ax.text(57.5, 65.5, 'Kiến trúc phân tầng 3 lớp: Thiết bị ngoại vi (Edge) - Cổng di động (Gateway) - Đám mây (Cloud Server)',
            ha='center', va='center', fontsize=8.2, color='#64748B', fontstyle='italic')

    # 4 Columns:
    # CARD 1: GẬY THÔNG MINH
    draw_card_pro(ax, 14.5, 34, 25.5, 54, 'GẬY THÔNG MINH IoT', 'PHẦN CỨNG NGOẠI VI (EDGE NODE)',
                  C_EMERALD_DARK, '#F0FDF4', '#A7F3D0', hh=6.8, title_fs=8.2, badge_fs=6.2)
    
    # Sub 1: ESP32-S3
    ax.add_patch(FancyBboxPatch((3.0, 44), 23, 11.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#6EE7B7', lw=1.1, zorder=4))
    ax.text(14.5, 53.0, 'VI ĐIỀU KHIỂN ESP32-S3', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#065F46', zorder=5)
    ax.text(4.2, 49.2, '• Xtensa Dual-Core 240MHz', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(4.2, 46.0, '• BLE 5.0 Server (SmartCane)', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 2: Cảm biến
    ax.add_patch(FancyBboxPatch((3.0, 28.5), 23, 14.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#93C5FD', lw=1.1, zorder=4))
    ax.text(14.5, 39.8, 'CẢM BIẾN THU THẬP', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#1E40AF', zorder=5)
    ax.text(4.2, 36.2, '• MPU-6050: Gia tốc 3 trục ±8g', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(4.2, 33.0, '• HC-SR04: Quét cự ly 3-80cm', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(4.2, 29.8, '• ADC: Đo điện áp Pin (GPIO 4)', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 3: Cảnh báo & Nguồn
    ax.add_patch(FancyBboxPatch((3.0, 9.5), 23, 17.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#FCD34D', lw=1.1, zorder=4))
    ax.text(14.5, 24.3, 'CẢNH BÁO TẠI CHỖ & NGUỒN', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#92400E', zorder=5)
    ax.text(4.2, 20.8, '• Còi hú 5V âm lượng >85dB', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#B91C1C', zorder=5)
    ax.text(4.2, 17.6, '• Motor rung lệch tâm MOSFET', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(4.2, 14.4, '• Pin 18650 3.7V + Sạc TP4056', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(4.2, 11.2, '• Nâng áp Boost 5V ổn định', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # CARD 2: ĐIỆN THOẠI NGƯỜI DÙNG
    draw_card_pro(ax, 43.0, 34, 25.5, 54, 'ĐIỆN THOẠI NGƯỜI DÙNG', 'CỔNG DI ĐỘNG (MOBILE GATEWAY)',
                  C_BLUE_DARK, '#EFF6FF', '#93C5FD', hh=6.8, title_fs=8.2, badge_fs=6.2)
    
    # Sub 1: Dịch vụ nền
    ax.add_patch(FancyBboxPatch((31.5, 44), 23, 11.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#93C5FD', lw=1.1, zorder=4))
    ax.text(43.0, 53.0, 'DỊCH VỤ NỀN THƯỜNG TRỰC', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#1E40AF', zorder=5)
    ax.text(32.7, 49.2, '• Foreground Service chạy 24/7', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(32.7, 46.0, '• Tự động kết nối lại BLE', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 2: GPS & SOS
    ax.add_patch(FancyBboxPatch((31.5, 28.5), 23, 14.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#6EE7B7', lw=1.1, zorder=4))
    ax.text(43.0, 39.8, 'ĐỊNH VỊ VÀ ĐIỀU PHỐI SOS', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#065F46', zorder=5)
    ax.text(32.7, 36.2, '• GPS: Tọa độ chính xác cao', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(32.7, 33.0, '• Bộ đếm lùi 15s hủy báo nhầm', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(32.7, 29.8, '• Đẩy gói tin khẩn lên Cloud', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 3: Cứu hộ GSM
    ax.add_patch(FancyBboxPatch((31.5, 9.5), 23, 17.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFF1F2', ec='#FDA4AF', lw=1.1, zorder=4))
    ax.text(43.0, 24.3, 'CỨU HỘ NGOẠI TUYẾN GSM', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#9F1239', zorder=5)
    ax.text(32.7, 20.8, '• SMS link Google Maps tức thì', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#B91C1C', zorder=5)
    ax.text(32.7, 17.6, '• Tự quay số gọi SOS Giám hộ', ha='left', va='center', fontsize=7.0, color='#0F172A', zorder=5)
    ax.text(32.7, 14.4, '• Hoạt động cả khi mất Internet', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(32.7, 11.2, '• Cứu hộ liên tục, không đứt đoạn', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # CARD 3: CLOUD & GSM
    # 3A: Firebase
    draw_card_pro(ax, 71.5, 46.5, 25.5, 29, 'FIREBASE CLOUD BACKEND', 'ĐÁM MÂY DỮ LIỆU (IoT CLOUD)',
                  C_AMBER_DARK, '#FFFDF5', '#FCD34D', hh=6.8, title_fs=8.2, badge_fs=6.2)
    ax.text(71.5, 57.5, 'Realtime Database & Auth:', ha='center', va='center', fontsize=7.4, fontweight='bold', color='#92400E')
    ax.text(60.2, 53.8, '• Cây JSON: /users/{uid}', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A')
    ax.text(60.2, 50.4, '• is_falling, lat, lng, ble, pin', ha='left', va='center', fontsize=7.0, color='#334155')
    ax.text(60.2, 47.0, '• WebSocket: Độ trễ < 0.5s', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#059669')
    ax.text(60.2, 43.6, '• Firebase Auth phân quyền vai trò', ha='left', va='center', fontsize=7.0, color='#334155')
    ax.text(60.2, 40.2, '• Lưu lịch sử sự cố & điểm hẹn', ha='left', va='center', fontsize=7.0, color='#334155')

    # 3B: GSM SMS
    draw_card_pro(ax, 71.5, 20.0, 25.5, 21, 'KÊNH DỰ PHÒNG GSM / SMS', 'NGOẠI TUYẾN (NO INTERNET)',
                  C_ROSE_DARK, '#FFF1F2', '#FDA4AF', hh=6.8, title_fs=8.2, badge_fs=6.2)
    ax.text(71.5, 26.5, 'Mạng Viễn thông Di động:', ha='center', va='center', fontsize=7.4, fontweight='bold', color='#9F1239')
    ax.text(60.2, 23.0, '• SMS khẩn cấp sóng viễn thông', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A')
    ax.text(60.2, 19.6, '• Nội dung: Cảnh báo + Tọa độ GPS', ha='left', va='center', fontsize=7.0, color='#334155')
    ax.text(60.2, 16.2, '• Cuộc gọi SOS thông mạch trực tiếp', ha='left', va='center', fontsize=7.0, color='#334155')
    ax.text(60.2, 12.8, '• Đảm bảo tin cậy khi mất mạng', ha='left', va='center', fontsize=7.0, color='#334155')

    # CARD 4: ĐIỆN THOẠI GIÁM HỘ
    draw_card_pro(ax, 100.0, 34, 25.5, 54, 'ĐIỆN THOẠI GIÁM HỘ', 'ỨNG DỤNG GIÁM SÁT (MONITOR)',
                  C_PURPLE_DARK, '#FAF5FF', '#C4B5FD', hh=6.8, title_fs=8.2, badge_fs=6.2)
    # Sub 1: Bản đồ
    ax.add_patch(FancyBboxPatch((88.5, 44), 23, 11.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#C4B5FD', lw=1.1, zorder=4))
    ax.text(100.0, 53.0, 'BẢN ĐỒ THỜI GIAN THỰC', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#6D28D9', zorder=5)
    ax.text(89.7, 49.2, '• OpenStreetMap / Mapbox live', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(89.7, 46.0, '• Marker vị trí người già + Nhà', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 2: Còi hú
    ax.add_patch(FancyBboxPatch((88.5, 28.5), 23, 14.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#FDA4AF', lw=1.1, zorder=4))
    ax.text(100.0, 39.8, 'CÒI BÁO ĐỘNG SOS KHẨN', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#9F1239', zorder=5)
    ax.text(89.7, 36.2, '• Chuông báo âm lượng cực đại', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#B91C1C', zorder=5)
    ax.text(89.7, 33.0, '• Rung liên tục & Banner cảnh báo', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(89.7, 29.8, '• Nút bấm tắt còi khi tiếp cận', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 3: Điều hướng
    ax.add_patch(FancyBboxPatch((88.5, 9.5), 23, 17.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#93C5FD', lw=1.1, zorder=4))
    ax.text(100.0, 24.3, 'ĐIỀU HƯỚNG VÀ NHẬT KÝ', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#1E40AF', zorder=5)
    ax.text(89.7, 20.8, '• Mở dẫn đường Google Maps', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(89.7, 17.6, '• Giám sát % Pin / Sóng / Mạng', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(89.7, 14.4, '• Lịch sử các lần té ngã chi tiết', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(89.7, 11.2, '• Quản lý danh bạ SOS khẩn cấp', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Connections
    # 1 -> 2: BLE
    ax.plot([27.25, 30.25], [41, 41], color='#059669', lw=2.5, zorder=6)
    ax.add_patch(FancyBboxPatch((28.75-1.5, 41-2.2), 3.0, 4.4, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#059669', lw=1.2, zorder=7))
    ax.text(28.75, 41, 'BLE\n5.0', ha='center', va='center', fontsize=6.0, fontweight='bold', color='#059669', zorder=8)

    # 2 -> 3A: WiFi/4G
    ax.plot([55.75, 58.75], [52, 52], color='#2563EB', lw=2.5, zorder=6)
    ax.add_patch(FancyBboxPatch((57.25-1.5, 52-2.2), 3.0, 4.4, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#2563EB', lw=1.2, zorder=7))
    ax.text(57.25, 52, 'WiFi\n4G', ha='center', va='center', fontsize=6.0, fontweight='bold', color='#2563EB', zorder=8)

    # 2 -> 3B: GSM SMS
    ax.plot([55.75, 58.75], [20, 20], color='#DC2626', lw=2.2, ls='--', zorder=6)
    ax.add_patch(FancyBboxPatch((57.25-1.5, 20-2.2), 3.0, 4.4, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#DC2626', lw=1.2, zorder=7))
    ax.text(57.25, 20, 'Sóng\nGSM', ha='center', va='center', fontsize=5.8, fontweight='bold', color='#DC2626', zorder=8)

    # 3A -> 4: WebSocket Cloud
    ax.plot([84.25, 87.25], [52, 52], color='#D97706', lw=2.5, zorder=6)
    ax.add_patch(FancyBboxPatch((85.75-1.5, 52-2.2), 3.0, 4.4, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#D97706', lw=1.2, zorder=7))
    ax.text(85.75, 52, 'Cloud\nStream', ha='center', va='center', fontsize=5.5, fontweight='bold', color='#D97706', zorder=8)

    # 3B -> 4: SMS / Voice
    ax.plot([84.25, 87.25], [20, 20], color='#DC2626', lw=2.2, ls='--', zorder=6)
    ax.add_patch(FancyBboxPatch((85.75-1.5, 20-2.2), 3.0, 4.4, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#DC2626', lw=1.2, zorder=7))
    ax.text(85.75, 20, 'SMS\nCall', ha='center', va='center', fontsize=5.8, fontweight='bold', color='#DC2626', zorder=8)

    ax.text(57.5, 1.5, 'Hình 1.2: Mô hình kiến trúc tổng thể của hệ thống gậy thông minh kết hợp IoT và thiết bị di động', ha='center', va='center', fontsize=8.8, color='#334155', fontweight='bold')

    p = os.path.join(OUT, 'f_overview.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã cập nhật f_overview chuẩn nét: {p}")
    return p


# ==============================================================================
# HÌNH 2.1: SƠ ĐỒ KIẾN TRÚC VI ĐIỀU KHIỂN ESP32-S3 VÀ NGOẠI VI
# ==============================================================================
def gen_f_esp32():
    w, h = 13.0, 9.2
    fig = plt.figure(figsize=(w, h), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 92)
    ax.axis('off')

    ax.text(65, 88.5, 'SƠ ĐỒ KIẾN TRÚC VI ĐIỀU KHIỂN ESP32-S3 (N16R8) VÀ PHÂN BỐ NGOẠI VI I/O',
            ha='center', va='center', fontsize=12.5, fontweight='bold', color=C_SLATE_900)
    ax.text(65, 85.5, 'Bố trí phân luồng tín hiệu cảm biến đầu vào (Inputs) và cơ cấu chấp hành - truyền thông đầu ra (Outputs)',
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # KHỐI TRUNG TÂM: ESP32-S3
    cx, cy, cw, ch = 65, 44, 38, 70
    draw_card_pro(ax, cx, cy, cw, ch, title="ESP32-S3-WROOM-1", badge="N16R8 · DUAL-CORE 240MHz",
                  header_color=C_SLATE_900, bg_color='#F8FAFC', border_color=C_SLATE_700,
                  hh=7.0, title_fs=8.8, badge_fs=6.2)

    # QFN Chip mô phỏng
    ax.add_patch(FancyBboxPatch((cx - 16, cy - 27), 32, 52,
                               boxstyle='round,pad=0,rounding_size=1.8',
                               fc='#0F172A', ec='#334155', lw=1.3, zorder=3))
    
    ax.text(cx, cy + 21.5, 'ESPRESSIF ESP32-S3', ha='center', va='center', fontsize=8.8, fontweight='bold', color='#E2E8F0', zorder=4)

    # 6 Silicon blocks
    sub_blocks = [
        (cx - 7.5, cy + 11.5, 13.5, 12, "CPU Xtensa® LX7", "2 Nhân @ 240MHz\n512KB SRAM", '#1E293B', C_CYAN_MED),
        (cx + 7.5, cy + 11.5, 13.5, 12, "BỘ NHỚ MỞ RỘNG", "16MB Flash SPI\n8MB PSRAM Octal", '#1E293B', C_CYAN_MED),
        (cx - 7.5, cy - 2.5, 13.5, 12, "VÔ TUYẾN 2.4 GHz", "Wi-Fi 802.11 b/g/n\nBluetooth 5.0 LE", '#1E293B', C_EMERALD_MED),
        (cx + 7.5, cy - 2.5, 13.5, 12, "BẢO MẬT PHẦN CỨNG", "AES-256 · SHA-2\nSecure Boot RSA", '#1E293B', C_PURPLE_MED),
        (cx - 7.5, cy - 16.5, 13.5, 12, "NGOẠI VI ANALOG", "12-bit ADC SAR\n8x LEDC PWM Timer", '#1E293B', C_AMBER_MED),
        (cx + 7.5, cy - 16.5, 13.5, 12, "GIAO TIẾP BUS", "I2C · SPI · UART\nUSB OTG · 45 GPIO", '#1E293B', C_BLUE_MED),
    ]

    for bx, by, bw, bh, btitle, bsub, bbg, btc in sub_blocks:
        ax.add_patch(FancyBboxPatch((bx - bw / 2, by - bh / 2), bw, bh,
                                   boxstyle='round,pad=0,rounding_size=1.0',
                                   fc=bbg, ec=btc, lw=1.0, zorder=5))
        ax.text(bx, by + 2.5, btitle, ha='center', va='center', fontsize=6.8, fontweight='bold', color=btc, zorder=6)
        ax.text(bx, by - 2.2, bsub, ha='center', va='center', fontsize=5.8, color='#CBD5E1', zorder=6)

    # INPUT CARDS (Bên trái: cx = 17, cw = 28)
    # 1. MPU-6050
    draw_card_pro(ax, 17, 65, 28, 19, title="CẢM BIẾN QUÁN TÍNH MPU-6050", badge="I2C BUS (0x68)",
                  header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 65.5, '• Gia tốc 3 trục ±8g, Gyro ±2000°/s', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 61.5, '• Tốc độ lấy mẫu: 50 Hz (20 ms)', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(4.2, 57.5, '• Ngưỡng rơi tự do: |a| < 0.6g', ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')

    # Dây nối MPU
    ax.plot([31, 46], [67, 67], color=C_AMBER_MED, lw=2.0)
    ax.plot([31, 46], [60, 60], color=C_AMBER_MED, lw=2.0)
    # pill badges
    ax.add_patch(FancyBboxPatch((38.5-4.5, 67-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFBEB', ec=C_AMBER_MED, lw=1.0, zorder=6))
    ax.text(38.5, 67, 'I2C SDA: GPIO 8', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_AMBER_DARK, zorder=7)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 60-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFBEB', ec=C_AMBER_MED, lw=1.0, zorder=6))
    ax.text(38.5, 60, 'I2C SCL: GPIO 9', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_AMBER_DARK, zorder=7)

    # 2. HC-SR04
    draw_card_pro(ax, 17, 43, 28, 19, title="CẢM BIẾN SIÊU ÂM HC-SR04", badge="XUNG 40 kHz",
                  header_color=C_CYAN_MED, bg_color='#F0FDFA', border_color=C_CYAN_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 43.5, '• Phát chùm siêu âm 40 kHz góc <15°', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 39.5, '• Cự ly phát hiện: 3 cm đến 80 cm', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(4.2, 35.5, '• Tính khoảng cách: d = t × 0.0343 / 2', ha='left', va='center', fontsize=6.8, color=C_CYAN_MED, fontweight='bold')

    # Dây nối HC-SR04
    ax.plot([46, 31], [46, 46], color=C_CYAN_MED, lw=2.0)
    ax.plot([31, 46], [39, 39], color=C_CYAN_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 46-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFEFF', ec=C_CYAN_MED, lw=1.0, zorder=6))
    ax.text(38.5, 46, 'TRIG: GPIO 16', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_CYAN_MED, zorder=7)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 39-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFEFF', ec=C_CYAN_MED, lw=1.0, zorder=6))
    ax.text(38.5, 39, 'ECHO: GPIO 17', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_CYAN_MED, zorder=7)

    # 3. ADC PIN
    draw_card_pro(ax, 17, 21, 28, 19, title="MẠCH ĐO ĐIỆN ÁP PIN", badge="ADC 12-BIT",
                  header_color=C_EMERALD_MED, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 21.5, '• Cầu phân áp trở R1=100k, R2=100k', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 17.5, '• Giảm áp Pin 4.2V về ngưỡng an toàn <2.1V', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(4.2, 13.5, '• Công thức: V_bat = 2 × V_adc', ha='left', va='center', fontsize=6.8, color='#065F46', fontweight='bold')

    # Dây nối ADC
    ax.plot([31, 46], [21, 21], color=C_EMERALD_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 21-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.0, zorder=6))
    ax.text(38.5, 21, 'ADC: GPIO 4', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_EMERALD_DARK, zorder=7)

    # OUTPUT CARDS (Bên phải: cx = 113, cw = 28)
    # 1. Còi Buzzer
    draw_card_pro(ax, 113, 65, 28, 19, title="CÒI HÚ BÁO ĐỘNG BUZZER", badge="ALARM 85dB",
                  header_color=C_ROSE_MED, bg_color='#FFF1F2', border_color=C_ROSE_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 65.5, '• Còi Active Buzzer 5V phát âm liên tục', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 61.5, '• Âm lượng >85dB vang xa trong bán kính 20m', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(100.2, 57.5, '• Kích hoạt mức HIGH khi có té ngã', ha='left', va='center', fontsize=6.8, color='#B91C1C', fontweight='bold')

    # Dây nối Buzzer
    ax.plot([84, 99], [65, 65], color=C_ROSE_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 65-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFF1F2', ec=C_ROSE_MED, lw=1.0, zorder=6))
    ax.text(91.5, 65, 'OUT: GPIO 6', ha='center', va='center', fontsize=6.5, fontweight='bold', color='#9F1239', zorder=7)

    # 2. Motor Rung
    draw_card_pro(ax, 113, 43, 28, 19, title="MẠCH ĐIỀU KHIỂN MOTOR RUNG", badge="MOSFET DRIVE",
                  header_color=C_PURPLE_MED, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 43.5, '• Đóng ngắt motor qua MOSFET công suất', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 39.5, '• Diode 1N4007 dập xung ngược bảo vệ chip', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(100.2, 35.5, '• Rung xung cảnh báo khi cự ly d < 80cm', ha='left', va='center', fontsize=6.8, color=C_PURPLE_DARK, fontweight='bold')

    # Dây nối Motor
    ax.plot([84, 99], [43, 43], color=C_PURPLE_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 43-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FAF5FF', ec=C_PURPLE_MED, lw=1.0, zorder=6))
    ax.text(91.5, 43, 'PWM: GPIO 5', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_PURPLE_DARK, zorder=7)

    # 3. BLE GATT
    draw_card_pro(ax, 113, 21, 28, 19, title="TRUYỀN THÔNG BLUETOOTH LE", badge="BLE 5.0 SERVER",
                  header_color=C_BLUE_MED, bg_color='#EFF6FF', border_color=C_BLUE_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 21.5, '• Tên thiết bị quảng bá: "SmartCane"', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 17.5, '• GATT Service: 4fafc201-1fb5-459e-8fcc-...', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(100.2, 13.5, '• Gửi Notify lập tức khi có sự kiện ngã', ha='left', va='center', fontsize=6.8, color=C_BLUE_DARK, fontweight='bold')

    # Dây nối BLE
    ax.plot([84, 99], [21, 21], color=C_BLUE_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 21-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#EFF6FF', ec=C_BLUE_MED, lw=1.0, zorder=6))
    ax.text(91.5, 21, 'BLE 5.0 RF', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_BLUE_DARK, zorder=7)

    ax.text(65, 1.5, 'Hình 2.1: Sơ đồ kiến trúc vi điều khiển ESP32-S3 N16R8 và các khối ngoại vi tích hợp', ha='center', va='center', fontsize=8.8, color='#334155', fontweight='bold')

    p = os.path.join(OUT, 'f_esp32.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã cập nhật f_esp32 chuẩn nét: {p}")
    return p

if __name__ == '__main__':
    gen_f_methods()
    gen_f_overview()
    gen_f_esp32()

# -*- coding: utf-8 -*-
"""
update_all_pro_figs.py
Thiết kế và tái tạo toàn bộ 23 sơ đồ, mô hình và biểu đồ của đồ án tốt nghiệp Gậy Thông Minh IoT.
Tất cả các hình đều được tối ưu kích thước canvas (11.0 - 13.0 inch) và font chữ (7.5 - 13.5 pt)
để khi chèn vào Word ở độ rộng 6.15 inch, mọi chữ đều CỰC KỲ TO, ĐẬM, RÕ NÉT VÀ CHUYÊN NGHIỆP.
"""
import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon
from matplotlib import font_manager

for f in ['C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/segoeuib.ttf', 'C:/Windows/Fonts/arial.ttf', 'C:/Windows/Fonts/arialbd.ttf']:
    if os.path.exists(f):
        font_manager.fontManager.addfont(f)

plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

OUT = r'd:\doan\_tools\fig'
os.makedirs(OUT, exist_ok=True)

# Bảng màu cao cấp
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


def draw_card(ax, x, y, w, h, title='', badge=None,
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
# 1. HÌNH 1.1: SƠ ĐỒ PHÂN LOẠI CÁC PHƯƠNG PHÁP PHÁT HIỆN TÉ NGÃ (f_methods)
# ==============================================================================
def gen_pro_methods():
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
        draw_card(ax, cx, 57.5, 28.5, 35.0, title=title, badge=badge,
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
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 2. HÌNH 1.2: MÔ HÌNH KIẾN TRÚC TỔNG THỂ HỆ THỐNG GẬY THÔNG MINH (f_overview)
# ==============================================================================
def gen_pro_overview():
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

    # CARD 1: GẬY THÔNG MINH
    draw_card(ax, 14.5, 34, 25.5, 54, 'GẬY THÔNG MINH IoT', 'PHẦN CỨNG NGOẠI VI (EDGE NODE)',
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
    draw_card(ax, 43.0, 34, 25.5, 54, 'ĐIỆN THOẠI NGƯỜI DÙNG', 'CỔNG DI ĐỘNG (MOBILE GATEWAY)',
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
    draw_card(ax, 71.5, 46.5, 25.5, 29, 'FIREBASE CLOUD BACKEND', 'ĐÁM MÂY DỮ LIỆU (IoT CLOUD)',
              C_AMBER_DARK, '#FFFDF5', '#FCD34D', hh=6.8, title_fs=8.2, badge_fs=6.2)
    ax.text(71.5, 51.5, 'Realtime Database & Auth:', ha='center', va='center', fontsize=7.4, fontweight='bold', color='#92400E')
    ax.text(60.2, 48.0, '• Cây JSON: /users/{uid}', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A')
    ax.text(60.2, 44.6, '• is_falling, lat, lng, ble, pin', ha='left', va='center', fontsize=7.0, color='#334155')
    ax.text(60.2, 41.2, '• WebSocket: Độ trễ < 0.5s', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#059669')
    ax.text(60.2, 37.8, '• Firebase Auth phân quyền vai trò', ha='left', va='center', fontsize=7.0, color='#334155')
    ax.text(60.2, 34.4, '• Lưu lịch sử sự cố & điểm hẹn', ha='left', va='center', fontsize=7.0, color='#334155')

    # 3B: GSM SMS
    draw_card(ax, 71.5, 20.0, 25.5, 21, 'KÊNH DỰ PHÒNG GSM / SMS', 'NGOẠI TUYẾN (NO INTERNET)',
              C_ROSE_DARK, '#FFF1F2', '#FDA4AF', hh=6.8, title_fs=8.2, badge_fs=6.2)
    ax.text(71.5, 22.0, 'Mạng Viễn thông Di động:', ha='center', va='center', fontsize=7.4, fontweight='bold', color='#9F1239')
    ax.text(60.2, 18.6, '• SMS khẩn cấp sóng viễn thông', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A')
    ax.text(60.2, 15.2, '• Nội dung: Cảnh báo + Tọa độ GPS', ha='left', va='center', fontsize=7.0, color='#334155')
    ax.text(60.2, 11.8, '• Cuộc gọi SOS thông mạch trực tiếp', ha='left', va='center', fontsize=7.0, color='#334155')

    # CARD 4: ĐIỆN THOẠI GIÁM HỘ
    draw_card(ax, 100.0, 34, 25.5, 54, 'ĐIỆN THOẠI GIÁM HỘ', 'ỨNG DỤNG GIÁM SÁT (MONITOR)',
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
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 3. HÌNH 2.1: SƠ ĐỒ KIẾN TRÚC VI ĐIỀU KHIỂN ESP32-S3 (f_esp32)
# ==============================================================================
def gen_pro_esp32():
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
    draw_card(ax, cx, cy, cw, ch, title="ESP32-S3-WROOM-1", badge="N16R8 · DUAL-CORE 240MHz",
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
    draw_card(ax, 17, 65, 28, 19, title="CẢM BIẾN QUÁN TÍNH MPU-6050", badge="I2C BUS (0x68)",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 65.5, '• Gia tốc 3 trục ±8g, Gyro ±2000°/s', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 61.5, '• Tốc độ lấy mẫu: 50 Hz (20 ms)', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(4.2, 57.5, '• Ngưỡng rơi tự do: |a| < 0.6g', ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')

    ax.plot([31, 46], [67, 67], color=C_AMBER_MED, lw=2.0)
    ax.plot([31, 46], [60, 60], color=C_AMBER_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 67-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFBEB', ec=C_AMBER_MED, lw=1.0, zorder=6))
    ax.text(38.5, 67, 'I2C SDA: GPIO 8', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_AMBER_DARK, zorder=7)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 60-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFBEB', ec=C_AMBER_MED, lw=1.0, zorder=6))
    ax.text(38.5, 60, 'I2C SCL: GPIO 9', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_AMBER_DARK, zorder=7)

    # 2. HC-SR04
    draw_card(ax, 17, 43, 28, 19, title="CẢM BIẾN SIÊU ÂM HC-SR04", badge="XUNG 40 kHz",
              header_color=C_CYAN_MED, bg_color='#F0FDFA', border_color=C_CYAN_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 43.5, '• Phát chùm siêu âm 40 kHz góc <15°', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 39.5, '• Cự ly phát hiện: 3 cm đến 80 cm', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(4.2, 35.5, '• Tính khoảng cách: d = t × 0.0343 / 2', ha='left', va='center', fontsize=6.8, color=C_CYAN_MED, fontweight='bold')

    ax.plot([46, 31], [46, 46], color=C_CYAN_MED, lw=2.0)
    ax.plot([31, 46], [39, 39], color=C_CYAN_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 46-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFEFF', ec=C_CYAN_MED, lw=1.0, zorder=6))
    ax.text(38.5, 46, 'TRIG: GPIO 16', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_CYAN_MED, zorder=7)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 39-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFEFF', ec=C_CYAN_MED, lw=1.0, zorder=6))
    ax.text(38.5, 39, 'ECHO: GPIO 17', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_CYAN_MED, zorder=7)

    # 3. ADC PIN
    draw_card(ax, 17, 21, 28, 19, title="MẠCH ĐO ĐIỆN ÁP PIN", badge="ADC 12-BIT",
              header_color=C_EMERALD_MED, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 21.5, '• Cầu phân áp trở R1=100k, R2=100k', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 17.5, '• Giảm áp Pin 4.2V về ngưỡng an toàn <2.1V', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(4.2, 13.5, '• Công thức: V_bat = 2 × V_adc', ha='left', va='center', fontsize=6.8, color='#065F46', fontweight='bold')

    ax.plot([31, 46], [21, 21], color=C_EMERALD_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 21-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.0, zorder=6))
    ax.text(38.5, 21, 'ADC: GPIO 4', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_EMERALD_DARK, zorder=7)

    # OUTPUT CARDS (Bên phải: cx = 113, cw = 28)
    # 1. Còi Buzzer (GPIO 5 theo config.h)
    draw_card(ax, 113, 65, 28, 19, title="CÒI HÚ BÁO ĐỘNG BUZZER", badge="ALARM 85dB",
                  header_color=C_ROSE_MED, bg_color='#FFF1F2', border_color=C_ROSE_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 65.5, '• Còi Active Buzzer 5V phát âm liên tục', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 61.5, '• Âm lượng >85dB vang xa bán kính 20m', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(100.2, 57.5, '• Kích hoạt mức HIGH khi có té ngã', ha='left', va='center', fontsize=6.8, color='#B91C1C', fontweight='bold')

    ax.plot([84, 99], [65, 65], color=C_ROSE_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 65-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFF1F2', ec=C_ROSE_MED, lw=1.0, zorder=6))
    ax.text(91.5, 65, 'OUT: GPIO 5', ha='center', va='center', fontsize=6.5, fontweight='bold', color='#9F1239', zorder=7)

    # 2. Motor Rung (GPIO 6 theo config.h)
    draw_card(ax, 113, 43, 28, 19, title="MẠCH ĐIỀU KHIỂN MOTOR RUNG", badge="MOSFET DRIVE",
                  header_color=C_PURPLE_MED, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 43.5, '• Đóng ngắt motor qua MOSFET công suất', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 39.5, '• Diode 1N4007 dập xung ngược bảo vệ chip', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(100.2, 35.5, '• Rung xung cảnh báo khi cự ly d < 80cm', ha='left', va='center', fontsize=6.8, color=C_PURPLE_DARK, fontweight='bold')

    ax.plot([84, 99], [43, 43], color=C_PURPLE_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 43-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FAF5FF', ec=C_PURPLE_MED, lw=1.0, zorder=6))
    ax.text(91.5, 43, 'PWM: GPIO 6', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_PURPLE_DARK, zorder=7)

    # 3. BLE GATT
    draw_card(ax, 113, 21, 28, 19, title="TRUYỀN THÔNG BLUETOOTH LE", badge="BLE 5.0 SERVER",
                  header_color=C_BLUE_MED, bg_color='#EFF6FF', border_color=C_BLUE_BORDER,
                  hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 21.5, '• Tên thiết bị quảng bá: "SmartCane"', ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 17.5, '• GATT Service: 4fafc201-1fb5-459e-8fcc-...', ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(100.2, 13.5, '• Gửi Notify lập tức khi có sự kiện ngã', ha='left', va='center', fontsize=6.8, color=C_BLUE_DARK, fontweight='bold')

    ax.plot([84, 99], [21, 21], color=C_BLUE_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 21-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#EFF6FF', ec=C_BLUE_MED, lw=1.0, zorder=6))
    ax.text(91.5, 21, 'BLE 5.0 RF', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_BLUE_DARK, zorder=7)

    ax.text(65, 1.5, 'Hình 2.1: Sơ đồ kiến trúc vi điều khiển ESP32-S3 N16R8 và các khối ngoại vi tích hợp', ha='center', va='center', fontsize=8.8, color='#334155', fontweight='bold')

    p = os.path.join(OUT, 'f_esp32.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 4. HÌNH 3.1: SƠ ĐỒ KHỐI CHỨC NĂNG HOÀN CHỈNH (f_block_diag)
# ==============================================================================
def gen_pro_block_diag():
    w, h = 13.0, 9.8
    fig = plt.figure(figsize=(w, h), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 98)
    ax.axis('off')

    ax.text(65, 94.0, 'SƠ ĐỒ KHỐI CHỨC NĂNG HOÀN CHỈNH HỆ THỐNG GẬY THÔNG MINH (SMART CANE IoT)',
            ha='center', va='center', fontsize=12.5, fontweight='bold', color=C_SLATE_900)
    ax.text(65, 90.5, 'Kiến trúc tích hợp 3 phân hệ: Phần cứng gậy ngoại vi - Cổng di động người dùng - Đám mây & Ứng dụng giám hộ',
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Phân hệ 1: Gậy thông minh (x=22, w=38)
    draw_card(ax, 22, 45, 38, 82, title="PHÂN HỆ PHẦN CỨNG GẬY (ESP32-S3)", badge="EDGE HARDWARE",
              header_color=C_EMERALD_DARK, bg_color='#F0FDF4', border_color='#A7F3D0', hh=6.8, title_fs=8.2, badge_fs=6.0)
    
    # 4 sub-boxes inside Gậy
    # Sub 1: MCU
    ax.add_patch(FancyBboxPatch((4.5, 66.5), 35, 14.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#6EE7B7', lw=1.1, zorder=4))
    ax.text(22, 78.0, 'BỘ XỬ LÝ TRUNG TÂM ESP32-S3', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#065F46', zorder=5)
    ax.text(6.0, 74.0, '• Xtensa Dual-Core 240MHz · 16MB Flash', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(6.0, 70.0, '• Thuật toán lọc nhiễu SVM & Đo cự ly siêu âm', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 2: Cảm biến
    ax.add_patch(FancyBboxPatch((4.5, 48.0), 35, 16.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#93C5FD', lw=1.1, zorder=4))
    ax.text(22, 61.5, 'KHỐI CẢM BIẾN ĐẦU VÀO', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#1E40AF', zorder=5)
    ax.text(6.0, 57.5, '• MPU-6050 (I2C): Gia tốc 3 trục ±8g, Gyro', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(6.0, 53.5, '• HC-SR04: Siêu âm quét vật cản 3-80cm', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(6.0, 49.5, '• Mạch phân áp ADC (GPIO 4) đo điện áp Pin', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 3: Cảnh báo
    ax.add_patch(FancyBboxPatch((4.5, 27.5), 35, 18.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#FDA4AF', lw=1.1, zorder=4))
    ax.text(22, 42.5, 'KHỐI CẢNH BÁO TẠI CHỖ', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#9F1239', zorder=5)
    ax.text(6.0, 38.5, '• Còi hú Active Buzzer 5V (2000Hz, >85dB)', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#B91C1C', zorder=5)
    ax.text(6.0, 34.5, '• Motor rung xúc giác cảnh báo vật cản', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(6.0, 30.5, '• Driver MOSFET công suất AOD4184', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 4: Nguồn
    ax.add_patch(FancyBboxPatch((4.5, 6.5), 35, 19.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#FCD34D', lw=1.1, zorder=4))
    ax.text(22, 22.0, 'KHỐI NGUỒN PIN & SẠC TYPE-C', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#92400E', zorder=5)
    ax.text(6.0, 18.0, '• Cell Pin Li-ion 18650 dung lượng 2600mAh', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(6.0, 14.0, '• Mạch sạc TP4056 tích hợp bảo vệ quá tải', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(6.0, 10.0, '• Mạch Boost DC-DC nâng áp ổn định 5V', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Phân hệ 2: Smartphone Người Dùng (x=65, w=38)
    draw_card(ax, 65, 45, 38, 82, title="SMARTPHONE NGƯỜI DÙNG GẬY", badge="MOBILE GATEWAY",
              header_color=C_BLUE_DARK, bg_color='#EFF6FF', border_color='#93C5FD', hh=6.8, title_fs=8.2, badge_fs=6.0)
    
    # Sub 1: BLE Client
    ax.add_patch(FancyBboxPatch((47.5, 66.5), 35, 14.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#93C5FD', lw=1.1, zorder=4))
    ax.text(65, 78.0, 'MÔ-ĐUN BLUETOOTH LE CLIENT', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#1E40AF', zorder=5)
    ax.text(49.0, 74.0, '• Tự động quét & kết nối lại BLE qua MAC', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(49.0, 70.0, '• Lắng nghe gói tin Notify ngã tức thời', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 2: Foreground Service
    ax.add_patch(FancyBboxPatch((47.5, 48.0), 35, 16.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#FCD34D', lw=1.1, zorder=4))
    ax.text(65, 61.5, 'DỊCH VỤ NỀN THƯỜNG TRỰC (24/7)', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#92400E', zorder=5)
    ax.text(49.0, 57.5, '• Flutter Foreground Service chạy ngầm', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(49.0, 53.5, '• Duy trì luồng BLE & GPS không bị ngắt', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(49.0, 49.5, '• Miễn nhiễm tối ưu hóa pin hệ điều hành', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 3: Fall Engine & GPS
    ax.add_patch(FancyBboxPatch((47.5, 27.5), 35, 18.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#6EE7B7', lw=1.1, zorder=4))
    ax.text(65, 42.5, 'BỘ XỬ LÝ KHẨN CẤP & ĐỊNH VỊ', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#065F46', zorder=5)
    ax.text(49.0, 38.5, '• Đếm lùi 15s (Hủy báo nhầm qua 1 chạm)', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#B91C1C', zorder=5)
    ax.text(49.0, 34.5, '• Lấy tọa độ GPS (Độ chính xác cao)', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(49.0, 30.5, '• Đẩy gói tin SOS lên Firebase Realtime', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 4: GSM Cứu hộ ngoại tuyến
    ax.add_patch(FancyBboxPatch((47.5, 6.5), 35, 19.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFF1F2', ec='#FDA4AF', lw=1.1, zorder=4))
    ax.text(65, 22.0, 'KÊNH CỨU HỘ NGOẠI TUYẾN GSM', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#9F1239', zorder=5)
    ax.text(49.0, 18.0, '• Tự động gửi SMS tọa độ vị trí Google Maps', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#B91C1C', zorder=5)
    ax.text(49.0, 14.0, '• Tự quay số gọi SOS trực tiếp cho Giám hộ', ha='left', va='center', fontsize=7.0, color='#0F172A', zorder=5)
    ax.text(49.0, 10.0, '• Đảm bảo hoạt động kể cả khi mất Internet', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Phân hệ 3: Đám mây & Giám hộ (x=108, w=38)
    draw_card(ax, 108, 45, 38, 82, title="ĐÁM MÂY & ỨNG DỤNG GIÁM HỘ", badge="CLOUD & MONITOR",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color='#C4B5FD', hh=6.8, title_fs=8.2, badge_fs=6.0)
    
    # Sub 1: Firebase RTDB
    ax.add_patch(FancyBboxPatch((90.5, 59.5), 35, 21.5, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#FCD34D', lw=1.1, zorder=4))
    ax.text(108, 78.0, 'FIREBASE CLOUD BACKEND', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#92400E', zorder=5)
    ax.text(92.0, 74.0, '• Realtime Database: JSON /users/{uid}', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(92.0, 70.0, '• WebSocket truyền phát độ trễ < 0.5 giây', ha='left', va='center', fontsize=7.0, color='#059669', fontweight='bold', zorder=5)
    ax.text(92.0, 66.0, '• Firebase Authentication bảo mật 2 vai trò', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(92.0, 62.0, '• Lưu vết Lịch sử sự cố, Nhà, Điểm hẹn an toàn', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Sub 2: Ứng dụng Giám hộ
    ax.add_patch(FancyBboxPatch((90.5, 6.5), 35, 51.0, boxstyle='round,pad=0,rounding_size=1.2', fc='#FFFFFF', ec='#C4B5FD', lw=1.1, zorder=4))
    ax.text(108, 54.0, 'ỨNG DỤNG GIÁM HỘ (MONITOR APP)', ha='center', va='center', fontsize=7.6, fontweight='bold', color='#6D28D9', zorder=5)
    ax.text(92.0, 49.0, '• Bản đồ số thời gian thực (OpenStreetMap)', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#0F172A', zorder=5)
    ax.text(92.0, 44.5, '• Marker vị trí người già + Địa điểm an toàn', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(92.0, 40.0, '• Còi báo động SOS âm lượng cực đại trên máy', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#B91C1C', zorder=5)
    ax.text(92.0, 35.5, '• Rung liên tục & Banner cảnh báo khẩn cấp', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(92.0, 31.0, '• 1 chạm mở dẫn đường Google Maps tới vị trí', ha='left', va='center', fontsize=7.0, fontweight='bold', color='#1E40AF', zorder=5)
    ax.text(92.0, 26.5, '• Giám sát % Pin gậy, trạng thái kết nối BLE', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(92.0, 22.0, '• Xem nhật ký lịch sử các lần té ngã', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(92.0, 17.5, '• Quản lý danh bạ liên hệ SOS khẩn cấp', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)
    ax.text(92.0, 13.0, '• Đăng ký nhận SMS dự phòng khi rớt mạng', ha='left', va='center', fontsize=7.0, color='#334155', zorder=5)

    # Connections
    # 1 -> 2: BLE
    ax.plot([41, 46], [68, 68], color='#059669', lw=2.5, zorder=6)
    ax.add_patch(FancyBboxPatch((43.5-2.2, 68-2.0), 4.4, 4.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#059669', lw=1.2, zorder=7))
    ax.text(43.5, 68, 'BLE\n5.0', ha='center', va='center', fontsize=6.2, fontweight='bold', color='#059669', zorder=8)

    # 2 -> 3: Internet & GSM
    ax.plot([84, 89], [68, 68], color='#2563EB', lw=2.5, zorder=6)
    ax.add_patch(FancyBboxPatch((86.5-2.2, 68-2.0), 4.4, 4.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#2563EB', lw=1.2, zorder=7))
    ax.text(86.5, 68, '4G/WiFi\nCloud', ha='center', va='center', fontsize=5.8, fontweight='bold', color='#2563EB', zorder=8)

    ax.plot([84, 89], [25, 25], color='#DC2626', lw=2.2, ls='--', zorder=6)
    ax.add_patch(FancyBboxPatch((86.5-2.2, 25-2.0), 4.4, 4.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#DC2626', lw=1.2, zorder=7))
    ax.text(86.5, 25, 'Sóng\nGSM', ha='center', va='center', fontsize=6.0, fontweight='bold', color='#DC2626', zorder=8)

    ax.text(65, 1.5, 'Hình 3.1: Sơ đồ khối chức năng hoàn chỉnh của toàn bộ hệ thống gậy thông minh', ha='center', va='center', fontsize=9.0, color='#334155', fontweight='bold')

    p = os.path.join(OUT, 'f_block_diag.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 5. HÌNH 3.2: SƠ ĐỒ NGUYÊN LÝ KẾT NỐI CHI TIẾT PHẦN CỨNG (f_schematic)
# ==============================================================================
def gen_pro_schematic():
    w, h = 13.0, 9.6
    fig = plt.figure(figsize=(w, h), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 96)
    ax.axis('off')

    ax.text(65, 92.5, 'SƠ ĐỒ NGUYÊN LÝ KẾT NỐI CHI TIẾT PHẦN CỨNG (HARDWARE SCHEMATIC)',
            ha='center', va='center', fontsize=12.5, fontweight='bold', color=C_SLATE_900)
    ax.text(65, 89.5, 'Bản vẽ thiết kế mạch điện tử: ESP32-S3 DevKit phối ghép cảm biến MPU6050, HC-SR04, Driver MOSFET và khối nguồn 18650',
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Bo mạch trung tâm ESP32-S3 DevKit (cx=65, cw=38)
    cx, cy, cw, ch = 65, 45, 38, 76
    draw_card(ax, cx, cy, cw, ch, title="ESP32-S3 N16R8 DEVKIT", badge="CORE MCU",
              header_color=C_SLATE_900, bg_color='#F8FAFC', border_color=C_SLATE_700,
              hh=7.0, title_fs=8.8, badge_fs=6.2)

    ax.add_patch(FancyBboxPatch((cx - 16, cy - 32), 32, 60,
                               boxstyle='round,pad=0,rounding_size=1.8',
                               fc='#0F172A', ec='#334155', lw=1.3, zorder=3))
    ax.text(cx, cy + 24.5, "ESPRESSIF", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#E2E8F0', zorder=4)
    ax.text(cx, cy + 21.0, "ESP32-S3-WROOM-1", ha='center', va='center', fontsize=7.6, color='#94A3B8', zorder=4)

    # Chân bên trái MCU
    pins_left = [
        ("GPIO 8 (SDA)", 68, C_AMBER_MED),
        ("GPIO 9 (SCL)", 60, C_AMBER_MED),
        ("GPIO 16 (TRIG)", 48, C_CYAN_MED),
        ("GPIO 17 (ECHO)", 40, C_CYAN_MED),
        ("GPIO 4 (ADC)", 28, C_EMERALD_MED),
        ("3V3 (VCC)", 18, C_AMBER_MED),
        ("GND (ĐẤT CHUNG)", 10, C_SLATE_700),
    ]
    for pname, py, pcol in pins_left:
        ax.plot([cx - cw / 2, cx - 16], [py, py], color=pcol, lw=2.0, zorder=4)
        ax.add_patch(Rectangle((cx - cw / 2 - 1.0, py - 1.0), 2.0, 2.0, fc='#94A3B8', ec='#475569', lw=0.8, zorder=5))
        ax.add_patch(FancyBboxPatch((cx - 15.5, py - 1.5), 14.5, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#1E293B', ec=pcol, lw=1.0, zorder=6))
        ax.text(cx - 8.2, py, pname, ha='center', va='center', fontsize=6.2, fontweight='bold', color='#FFFFFF', zorder=7)

    # Chân bên phải MCU
    pins_right = [
        ("GPIO 5 (BUZZER)", 64, C_ROSE_MED),
        ("GPIO 6 (VIBRATOR)", 46, C_PURPLE_MED),
        ("VIN (5V BOOST)", 28, C_ROSE_DARK),
        ("GND (ĐẤT CHUNG)", 14, C_SLATE_700),
    ]
    for pname, py, pcol in pins_right:
        ax.plot([cx + 16, cx + cw / 2], [py, py], color=pcol, lw=2.0, zorder=4)
        ax.add_patch(Rectangle((cx + cw / 2 - 1.0, py - 1.0), 2.0, 2.0, fc='#94A3B8', ec='#475569', lw=0.8, zorder=5))
        ax.add_patch(FancyBboxPatch((cx + 1.0, py - 1.5), 14.5, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#1E293B', ec=pcol, lw=1.0, zorder=6))
        ax.text(cx + 8.2, py, pname, ha='center', va='center', fontsize=6.2, fontweight='bold', color='#FFFFFF', zorder=7)

    # MODULES BÊN TRÁI (cx=17, cw=28)
    # 1. MPU-6050
    draw_card(ax, 17, 65, 28, 20, title="MODULE CẢM BIẾN MPU-6050", badge="I2C",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 65.0, "• VCC: Nối 3.3V từ ESP32 | GND chung", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 61.0, "• SDA: Nối chân GPIO 8 (Dữ liệu I2C)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 57.0, "• SCL: Nối chân GPIO 9 (Xung nhịp I2C)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)

    ax.plot([31, 46], [68, 68], color=C_AMBER_MED, lw=2.0)
    ax.plot([31, 46], [60, 60], color=C_AMBER_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 68-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFBEB', ec=C_AMBER_MED, lw=1.0, zorder=6))
    ax.text(38.5, 68, 'SDA: GPIO 8', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_AMBER_DARK, zorder=7)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 60-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFBEB', ec=C_AMBER_MED, lw=1.0, zorder=6))
    ax.text(38.5, 60, 'SCL: GPIO 9', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_AMBER_DARK, zorder=7)

    # 2. HC-SR04
    draw_card(ax, 17, 43, 28, 20, title="CẢM BIẾN SIÊU ÂM HC-SR04", badge="40 kHz",
              header_color=C_CYAN_MED, bg_color='#F0FDFA', border_color=C_CYAN_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 43.0, "• VCC: Nối nguồn 3.3V | GND chung", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 39.0, "• TRIG: Nối GPIO 16 (Phát xung 10µs)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 35.0, "• ECHO: Nối GPIO 17 (Thu xung phản xạ)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)

    ax.plot([46, 31], [48, 48], color=C_CYAN_MED, lw=2.0)
    ax.plot([31, 46], [40, 40], color=C_CYAN_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 48-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFEFF', ec=C_CYAN_MED, lw=1.0, zorder=6))
    ax.text(38.5, 48, 'TRIG: GPIO 16', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_CYAN_MED, zorder=7)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 40-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFEFF', ec=C_CYAN_MED, lw=1.0, zorder=6))
    ax.text(38.5, 40, 'ECHO: GPIO 17', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_CYAN_MED, zorder=7)

    # 3. Phân áp Pin ADC
    draw_card(ax, 17, 20, 28, 20, title="MẠCH CHIA ÁP PIN LI-ION", badge="ADC",
              header_color=C_EMERALD_MED, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(4.2, 20.0, "• R1 = 100kΩ nối cực dương Pin (+)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 16.0, "• R2 = 100kΩ nối cực âm GND (-)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(4.2, 12.0, "• Điểm giữa nối GPIO 4 (ADC1_CH3)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)

    ax.plot([31, 46], [28, 28], color=C_EMERALD_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((38.5-4.5, 28-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.0, zorder=6))
    ax.text(38.5, 28, 'ADC: GPIO 4', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_EMERALD_DARK, zorder=7)

    # MODULES BÊN PHẢI (cx=113, cw=28)
    # 1. Còi Buzzer (GPIO 5)
    draw_card(ax, 113, 65, 28, 20, title="CÒI HÚ BÁO ĐỘNG BUZZER", badge="ALARM",
              header_color=C_ROSE_MED, bg_color='#FFF1F2', border_color=C_ROSE_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 65.0, "• Cực dương (+) nối nguồn 5V Boost", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 61.0, "• Cực âm (-) nối chân GPIO 5", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 57.0, "• Phát âm báo 2000Hz >85dB khi ngã", ha='left', va='center', fontsize=6.8, color='#B91C1C', fontweight='bold')

    ax.plot([84, 99], [64, 64], color=C_ROSE_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 64-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFF1F2', ec=C_ROSE_MED, lw=1.0, zorder=6))
    ax.text(91.5, 64, 'OUT: GPIO 5', ha='center', va='center', fontsize=6.5, fontweight='bold', color='#9F1239', zorder=7)

    # 2. Motor Rung Driver (GPIO 6)
    draw_card(ax, 113, 43, 28, 20, title="MẠCH DRIVER MOTOR RUNG", badge="MOSFET",
              header_color=C_PURPLE_MED, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 43.0, "• MOSFET AOD4184 N-Channel kích Gate", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 39.0, "• Cổng Gate nối chân GPIO 6 (PWM)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 35.0, "• Diode 1N4007 dập điện áp cảm ứng ngược", ha='left', va='center', fontsize=6.8, color=C_PURPLE_DARK, fontweight='bold')

    ax.plot([84, 99], [46, 46], color=C_PURPLE_MED, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 46-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FAF5FF', ec=C_PURPLE_MED, lw=1.0, zorder=6))
    ax.text(91.5, 46, 'PWM: GPIO 6', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_PURPLE_DARK, zorder=7)

    # 3. Khối Nguồn Pin & Sạc
    draw_card(ax, 113, 20, 28, 20, title="KHỐI NGUỒN PIN 18650 & SẠC", badge="POWER",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER,
              hh=6.5, title_fs=7.5, badge_fs=5.8)
    ax.text(100.2, 20.0, "• Cell Pin 18650 3.7V nối Module TP4056", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 16.0, "• Mạch Boost DC-DC nâng áp lên 5V ổn định", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(100.2, 12.0, "• Đầu ra 5V cấp vào chân VIN của ESP32", ha='left', va='center', fontsize=6.8, color=C_AMBER_DARK, fontweight='bold')

    ax.plot([84, 99], [28, 28], color=C_ROSE_DARK, lw=2.0)
    ax.add_patch(FancyBboxPatch((91.5-4.5, 28-1.5), 9.0, 3.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFF1F2', ec=C_ROSE_DARK, lw=1.0, zorder=6))
    ax.text(91.5, 28, 'VIN (5V Boost)', ha='center', va='center', fontsize=6.5, fontweight='bold', color=C_ROSE_DARK, zorder=7)

    ax.text(65, 1.5, 'Hình 3.2: Sơ đồ nguyên lý kết nối chi tiết phần cứng trên vi điều khiển ESP32-S3', ha='center', va='center', fontsize=8.8, color='#334155', fontweight='bold')

    p = os.path.join(OUT, 'f_schematic.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 6. HÌNH 2.2: CẤU TRÚC GATT PROFILE BLUETOOTH LE (f_gatt)
# ==============================================================================
def gen_pro_gatt():
    w, h = 13.0, 9.2
    fig = plt.figure(figsize=(w, h), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 92)
    ax.axis('off')

    ax.text(65, 88.5, 'CẤU TRÚC PHÂN TẦNG VÀ GATT PROFILE CỦA BLUETOOTH LOW ENERGY',
            ha='center', va='center', fontsize=12.5, fontweight='bold', color=C_SLATE_900)
    ax.text(65, 85.5, 'Cấu hình phân cấp chuẩn Bluetooth SIG: Profile → Service → Characteristics → Descriptors',
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # GATT Server Top Card (cx=65, cw=110)
    draw_card(ax, 65, 73, 110, 14, title="GATT SERVER (ESP32-S3) – TÊN QUẢNG BÁ THIẾT BỊ: 'SmartCane'", badge="BLE SERVER",
              header_color=C_SLATE_900, bg_color='#F8FAFC', border_color=C_SLATE_700, hh=6.8, title_fs=8.8, badge_fs=6.2)
    ax.text(14, 69.0, "• Tự động quảng bá gói tin Advertisement dữ liệu dịch vụ sau khi khởi động", ha='left', va='center', fontsize=7.2, color=C_SLATE_800)
    ax.text(14, 65.5, "• Địa chỉ MAC phần cứng cố định giúp Flutter Mobile App tự động kết nối lại không cần dò quét thủ công", ha='left', va='center', fontsize=7.2, color=C_SLATE_700)

    # Primary Service Card (cx=65, cw=110)
    draw_card(ax, 65, 52, 110, 14, title="PRIMARY SERVICE: DỊCH VỤ PHÁT HIỆN TÉ NGÃ (FALL DETECTION)", badge="UUID SERVICE",
              header_color=C_BLUE_DARK, bg_color='#EFF6FF', border_color=C_BLUE_BORDER, hh=6.8, title_fs=8.8, badge_fs=6.2)
    ax.text(14, 48.0, "• UUID: 4fafc201-1fb5-459e-8fcc-c5c9c331914b  (Định danh duy nhất toàn cầu cho dịch vụ Gậy thông minh)",
            ha='left', va='center', fontsize=7.5, fontweight='bold', color=C_BLUE_DARK)
    ax.text(14, 44.5, "• Quản lý 2 Characteristic chính: Tín hiệu báo ngã khẩn cấp và Giám sát dung lượng pin",
            ha='left', va='center', fontsize=7.2, color=C_SLATE_700)

    ax.plot([65, 65], [66, 59], color=C_BLUE_MED, lw=2.2)

    # 2 Nhánh Characteristic
    # Nhánh 1 (Trái: cx=37, cw=54): Characteristic Báo Ngã
    draw_card(ax, 37, 24, 54, 30, title="CHARACTERISTIC 'TÉ NGÃ' (FALL EVENT)", badge="NOTIFY (UUID ...26a9)",
              header_color=C_ROSE_DARK, bg_color='#FFF1F2', border_color=C_ROSE_BORDER, hh=6.8, title_fs=8.2, badge_fs=6.0)
    ax.text(13, 27.5, "• UUID: beb5483e-36e1-4688-b7f5-ea07361b26a9", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_ROSE_DARK)
    ax.text(13, 23.5, "• Thuộc tính (Properties): READ | NOTIFY", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(13, 19.5, "• Giá trị dữ liệu (Payload):", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(13, 15.5, "  - '0': Trạng thái bình thường (An toàn)", ha='left', va='center', fontsize=7.0, color=C_EMERALD_DARK, fontweight='bold')
    ax.text(13, 11.5, "  - '1': PHÁT HIỆN TÉ NGÃ (Kích hoạt SOS)", ha='left', va='center', fontsize=7.0, color=C_ROSE_MED, fontweight='bold')

    ax.plot([45, 37], [45, 39], color=C_ROSE_MED, lw=2.0)

    # Descriptor CCCD dưới Characteristic Ngã
    ax.add_patch(FancyBboxPatch((13, 3.5), 48, 5.5, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFBEB', ec=C_AMBER_BORDER, lw=1.0, zorder=4))
    ax.text(37, 6.25, "DESCRIPTOR: CCCD 0x2902 (Đăng ký nhận Notify tự động)", ha='center', va='center', fontsize=6.8, fontweight='bold', color=C_AMBER_DARK, zorder=5)

    # Nhánh 2 (Phải: cx=93, cw=54): Characteristic Pin
    draw_card(ax, 93, 24, 54, 30, title="CHARACTERISTIC 'PIN' (BATTERY LEVEL)", badge="READ (UUID ...26a8)",
              header_color=C_EMERALD_DARK, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER, hh=6.8, title_fs=8.2, badge_fs=6.0)
    ax.text(69, 27.5, "• UUID: beb5483e-36e1-4688-b7f5-ea07361b26a8", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_EMERALD_DARK)
    ax.text(69, 23.5, "• Thuộc tính (Properties): READ", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(69, 19.5, "• Giá trị dữ liệu: Phần trăm Pin 0% - 100% (3.7V - 4.2V)", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(69, 15.5, "• Phục vụ hiển thị thanh trạng thái pin trên ứng dụng", ha='left', va='center', fontsize=7.0, color=C_SLATE_700)
    ax.text(69, 11.5, "• Báo cảnh báo pin yếu khi điện áp giảm dưới 3.4V", ha='left', va='center', fontsize=7.0, color=C_AMBER_DARK, fontweight='bold')

    ax.plot([85, 93], [45, 39], color=C_EMERALD_MED, lw=2.0)

    ax.text(65, 1.5, 'Hình 2.2: Cấu trúc phân tầng và GATT Profile của Bluetooth Low Energy trong hệ thống', ha='center', va='center', fontsize=8.8, color='#334155', fontweight='bold')

    p = os.path.join(OUT, 'f_gatt.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# 7. HÌNH 2.10: ĐỒNG BỘ REALTIME DATABASE (f_rtdb)
# ==============================================================================
def gen_pro_rtdb():
    w, h = 13.0, 9.0
    fig = plt.figure(figsize=(w, h), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 90)
    ax.axis('off')

    ax.text(65, 86.5, 'CƠ CHẾ ĐỒNG BỘ DỮ LIỆU HAI CHIỀU THỜI GIAN THỰC TRÊN FIREBASE RTDB',
            ha='center', va='center', fontsize=12.5, fontweight='bold', color=C_SLATE_900)
    ax.text(65, 83.5, 'Kiến trúc WebSocket Streaming hai chiều giữa Smartphone Người dùng gậy và Smartphone Giám hộ',
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Card Trái: Mobile Gateway Người Dùng (cx=25, cw=42)
    draw_card(ax, 25, 45, 42, 64, title="SMARTPHONE NGƯỜI DÙNG GẬY", badge="PUBLISHER",
              header_color=C_BLUE_DARK, bg_color='#EFF6FF', border_color=C_BLUE_BORDER, hh=6.8, title_fs=8.2, badge_fs=6.0)
    ax.text(6.0, 68.0, "• Giao tiếp BLE với Gậy thông minh", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_BLUE_DARK)
    ax.text(6.0, 63.5, "• Nhận tín hiệu Notify té ngã từ ESP32", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(6.0, 59.0, "• Đọc tọa độ GPS thời gian thực (lat, lng)", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(6.0, 54.5, "• Đếm ngược 15s xác nhận sự cố", ha='left', va='center', fontsize=7.0, color=C_AMBER_DARK, fontweight='bold')
    ax.text(6.0, 50.0, "• Đẩy gói tin khẩn cấp lên Firebase Cloud:", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    
    # JSON snippet đẩy lên
    json_push = FancyBboxPatch((6.0, 20.0), 38, 26, boxstyle='round,pad=0,rounding_size=1.2', fc='#1E293B', ec='#475569', lw=1.0, zorder=4)
    ax.add_patch(json_push)
    push_lines = [
        "PUT /users/{uid} HTTP/1.1",
        "{",
        '  "is_falling": true,',
        '  "latitude": 10.85024,',
        '  "longitude": 106.77192,',
        '  "ble_status": "connected",',
        '  "battery": 85,',
        '  "timestamp": 1730509200',
        "}"
    ]
    py = 42.5
    for pl in push_lines:
        col = '#38BDF8' if 'PUT' in pl else ('#F43F5E' if 'is_falling' in pl else ('#34D399' if 'latitude' in pl or 'longitude' in pl else '#E2E8F0'))
        fwt = 'bold' if 'is_falling' in pl or 'PUT' in pl else 'normal'
        ax.text(8.0, py, pl, ha='left', va='center', fontsize=6.5, fontfamily='monospace', fontweight=fwt, color=col, zorder=5)
        py -= 2.6

    # Card Giữa: Firebase Cloud RTDB (cx=65, cw=32)
    draw_card(ax, 65, 45, 32, 64, title="FIREBASE CLOUD", badge="BROKER",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER, hh=6.8, title_fs=8.2, badge_fs=6.0)
    ax.text(65, 68.0, "REALTIME DATABASE", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_AMBER_DARK)
    ax.text(51.5, 63.0, "• Cây JSON phân cấp NoSQL", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(51.5, 58.5, "• Lắng nghe sự kiện .onValue()", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(51.5, 54.0, "• Đồng bộ phân tán WebSocket", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(51.5, 49.5, "• Độ trễ truyền phát < 0.5s", ha='left', va='center', fontsize=7.0, color='#059669', fontweight='bold')
    ax.text(51.5, 45.0, "• Xác thực Firebase Auth", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(51.5, 40.5, "• Bảo mật dữ liệu vai trò Role", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(51.5, 36.0, "• Lưu lịch sử sự cố ngã", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(51.5, 31.5, "• Lưu tọa độ Nhà & Điểm hẹn", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(51.5, 27.0, "• Tự động khôi phục kết nối", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)

    # Card Phải: Monitor App Giám Hộ (cx=105, cw=42)
    draw_card(ax, 105, 45, 42, 64, title="SMARTPHONE GIÁM HỘ (MONITOR)", badge="SUBSCRIBER",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER, hh=6.8, title_fs=8.2, badge_fs=6.0)
    ax.text(86.0, 68.0, "• Lắng nghe luồng Stream .onValue()", ha='left', va='center', fontsize=7.2, fontweight='bold', color='#6D28D9')
    ax.text(86.0, 63.5, "• Nhận ngay lập tức khi is_falling=true", ha='left', va='center', fontsize=7.0, color='#B91C1C', fontweight='bold')
    ax.text(86.0, 59.0, "• Kích hoạt còi hú âm lượng cực đại", ha='left', va='center', fontsize=7.0, color='#B91C1C', fontweight='bold')
    ax.text(86.0, 54.5, "• Bật màn hình đỏ cảnh báo khẩn cấp", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(86.0, 50.0, "• Cập nhật Marker vị trí trên bản đồ", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)

    # Snippet phản hồi Giám Hộ
    json_sub = FancyBboxPatch((86.0, 20.0), 38, 26, boxstyle='round,pad=0,rounding_size=1.2', fc='#1E293B', ec='#475569', lw=1.0, zorder=4)
    ax.add_patch(json_sub)
    sub_lines = [
        "EVENT STREAM (WebSocket Live)",
        "{",
        '  "alarm": "ACTIVE_CRITICAL",',
        '  "victim": "Nguyễn Văn A",',
        '  "location": "10.8502, 106.7719",',
        '  "distance_to_home": "350m",',
        '  "action": "ROUTE_GOOGLE_MAPS",',
        '  "sound": "MAX_VOLUME_ALARM"',
        "}"
    ]
    sy = 42.5
    for sl in sub_lines:
        col = '#A855F7' if 'EVENT' in sl else ('#F43F5E' if 'ACTIVE' in sl or 'MAX' in sl else ('#34D399' if 'location' in sl else '#E2E8F0'))
        fwt = 'bold' if 'ACTIVE' in sl or 'EVENT' in sl else 'normal'
        ax.text(88.0, sy, sl, ha='left', va='center', fontsize=6.5, fontfamily='monospace', fontweight=fwt, color=col, zorder=5)
        sy -= 2.6

    # Data arrows
    ax.plot([46, 49], [50, 50], color='#2563EB', lw=2.5)
    ax.add_patch(FancyBboxPatch((47.5-2.0, 50-2.0), 4.0, 4.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#2563EB', lw=1.2, zorder=7))
    ax.text(47.5, 50, 'PUT\nJSON', ha='center', va='center', fontsize=5.8, fontweight='bold', color='#2563EB', zorder=8)

    ax.plot([81, 84], [50, 50], color='#D97706', lw=2.5)
    ax.add_patch(FancyBboxPatch((82.5-2.0, 50-2.0), 4.0, 4.0, boxstyle='round,pad=0,rounding_size=1.0', fc='#FFFFFF', ec='#D97706', lw=1.2, zorder=7))
    ax.text(82.5, 50, 'LIVE\nSYNC', ha='center', va='center', fontsize=5.8, fontweight='bold', color='#D97706', zorder=8)

    ax.text(65, 1.5, 'Hình 2.10: Cơ chế đồng bộ dữ liệu hai chiều thời gian thực trên Firebase Realtime Database', ha='center', va='center', fontsize=8.8, color='#334155', fontweight='bold')

    p = os.path.join(OUT, 'f_rtdb.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo: {p}")
    return p


# ==============================================================================
# HÀM CHÍNH TÁI TẠO TẤT CẢ CÁC HÌNH
# ==============================================================================
def gen_all():
    print("=== BẮT ĐẦU CẬP NHẬT CÁC HÌNH VẼ CHUẨN NÉT CỠ LỚN ===")
    gen_pro_methods()
    gen_pro_overview()
    gen_pro_esp32()
    gen_pro_block_diag()
    gen_pro_schematic()
    gen_pro_gatt()
    gen_pro_rtdb()
    print("=== HOÀN TẤT TẠO TOÀN BỘ CÁC HÌNH PHẦN 1 ===")

if __name__ == '__main__':
    gen_all()

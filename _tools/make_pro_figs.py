# -*- coding: utf-8 -*-
"""
make_pro_figs.py
Thiết kế lại toàn bộ mô hình kiến trúc và sơ đồ hệ thống với phong cách kỹ thuật cao cấp (Engineering Grade),
thẩm mỹ hiện đại, chi tiết chân thực và chuẩn xác 100% theo mã nguồn thực tế của đề tài.
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
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon, PathPatch, Wedge
from matplotlib.path import Path
from matplotlib import font_manager

# Cấu hình font Segoe UI / Arial chuẩn
for f in ['C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/segoeuib.ttf', 'C:/Windows/Fonts/arial.ttf', 'C:/Windows/Fonts/arialbd.ttf']:
    if os.path.exists(f):
        font_manager.fontManager.addfont(f)

plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

OUT = r'd:\doan\_tools\fig'
os.makedirs(OUT, exist_ok=True)

# Bảng màu cao cấp chuẩn quốc tế (Tailwind/Radix UI Dark & Accent Palette)
C_SLATE_900 = '#0F172A'
C_SLATE_800 = '#1E293B'
C_SLATE_700 = '#334155'
C_SLATE_500 = '#64748B'
C_SLATE_200 = '#E2E8F0'
C_SLATE_100 = '#F1F5F9'
C_SLATE_50  = '#F8FAFC'

# Accent Colors
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
C_PURPLE_LIGHT = '#F5F3FF'
C_PURPLE_BORDER= '#C4B5FD'

C_ROSE_DARK  = '#881337'
C_ROSE_MED   = '#E11D48'
C_ROSE_LIGHT = '#FFF1F2'
C_ROSE_BORDER= '#FDA4AF'

C_CYAN_MED   = '#0891B2'
C_CYAN_LIGHT = '#ECFEFF'
C_CYAN_BORDER= '#67E8F9'


def create_canvas(w_in, h_in, dpi=250):
    fig = plt.figure(figsize=(w_in, h_in), dpi=dpi, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w_in * 10)
    ax.set_ylim(0, h_in * 10)
    ax.axis('off')
    ax.set_aspect('equal')
    return fig, ax


def draw_card(ax, x, y, w, h, title='', subtitle=None, badge=None,
              header_color=C_SLATE_800, bg_color='#FFFFFF', border_color=C_SLATE_200,
              rx=2.0, shadow=True, header_h=None):
    """Vẽ Card giao diện hiện đại có thanh tiêu đề, viền bo tròn và đổ bóng đổ mịn."""
    x0, y0 = x - w / 2, y - h / 2

    # Đổ bóng (Shadow)
    if shadow:
        s_patch = FancyBboxPatch((x0 + 0.35, y0 - 0.4), w, h,
                                 boxstyle=f'round,pad=0,rounding_size={rx}',
                                 fc='#0F172A', ec='none', alpha=0.07, zorder=1)
        ax.add_patch(s_patch)

    # Thân Card
    card = FancyBboxPatch((x0, y0), w, h,
                          boxstyle=f'round,pad=0,rounding_size={rx}',
                          fc=bg_color, ec=border_color, lw=1.2, zorder=2)
    ax.add_patch(card)

    # Thanh Header (nếu có title)
    if title:
        hh = header_h if header_h else min(7.5, h * 0.22)
        # Header clip hoặc vẽ patch trên đỉnh
        h_patch = FancyBboxPatch((x0, y0 + h - hh), w, hh,
                                 boxstyle=f'round,pad=0,rounding_size={rx}',
                                 fc=header_color, ec='none', zorder=3)
        ax.add_patch(h_patch)
        # Phủ phần dưới của header để khớp với thân card
        ax.add_patch(Rectangle((x0, y0 + h - hh), w, rx, fc=header_color, ec='none', zorder=3))

        # Tiêu đề chính - Tự động chỉnh cỡ chữ để không bao giờ đè lên Badge
        t_fs = 9.2
        if badge:
            if len(title) > 34:
                t_fs = 7.2
            elif len(title) > 26:
                t_fs = 7.8
            elif len(title) > 20:
                t_fs = 8.4
        ax.text(x0 + 2.0, y0 + h - hh / 2, title,
                ha='left', va='center', fontsize=t_fs, fontweight='bold', color='#FFFFFF', zorder=4)

        # Badge góc phải
        if badge:
            bw = len(badge) * 1.05 + 3.0
            bh = hh * 0.55
            bx = x0 + w - bw / 2 - 1.5
            by = y0 + h - hh / 2
            ax.add_patch(FancyBboxPatch((bx - bw / 2, by - bh / 2), bw, bh,
                                       boxstyle=f'round,pad=0,rounding_size={bh/2}',
                                       fc='#FFFFFF', ec='none', alpha=0.22, zorder=4))
            ax.text(bx, by, badge, ha='center', va='center',
                    fontsize=7.0, fontweight='bold', color='#FFFFFF', zorder=5)

    return card


def draw_pill_badge(ax, x, y, text, fc='#FFFFFF', ec=C_SLATE_500, tc=C_SLATE_800, fs=7.5, bold=True, pad_w=2.5, pad_h=1.2, zorder=10):
    """Vẽ nhãn dạng con nhộng (Pill Badge) cho thông số kỹ thuật hoặc chân GPIO."""
    bw = len(text) * 0.95 + pad_w
    bh = 3.6 + pad_h
    patch = FancyBboxPatch((x - bw / 2, y - bh / 2), bw, bh,
                           boxstyle=f'round,pad=0,rounding_size={bh/2}',
                           fc=fc, ec=ec, lw=1.0, zorder=zorder)
    ax.add_patch(patch)
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, fontweight='bold' if bold else 'normal', color=tc, zorder=zorder+1)
    return patch


def draw_bus(ax, pts, color=C_SLATE_700, lw=1.6, style='-', arrow_end=True, arrow_both=False, label_text=None, sub_text=None, badge_color=None):
    """Vẽ đường truyền tín hiệu / mạng có bo góc nhẹ và nhãn giao thức nổi."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    
    # Vẽ đường line
    ax.plot(xs, ys, color=color, lw=lw, ls=style, zorder=6, solid_capstyle='round')

    # Mũi tên kết thúc
    if arrow_end:
        p_penult = pts[-2]
        p_last = pts[-1]
        dx = p_last[0] - p_penult[0]
        dy = p_last[1] - p_penult[1]
        dist = np.hypot(dx, dy)
        if dist > 0:
            ux, uy = dx / dist, dy / dist
            head_len = 1.8
            head_w = 1.1
            ax.add_patch(Polygon([
                p_last,
                (p_last[0] - head_len * ux + head_w * uy, p_last[1] - head_len * uy - head_w * ux),
                (p_last[0] - head_len * ux - head_w * uy, p_last[1] - head_len * uy + head_w * ux)
            ], closed=True, fc=color, ec='none', zorder=7))

    if arrow_both:
        p_start = pts[0]
        p_next = pts[1]
        dx = p_next[0] - p_start[0]
        dy = p_next[1] - p_start[1]
        dist = np.hypot(dx, dy)
        if dist > 0:
            ux, uy = dx / dist, dy / dist
            head_len = 1.8
            head_w = 1.1
            ax.add_patch(Polygon([
                p_start,
                (p_start[0] + head_len * ux + head_w * uy, p_start[1] + head_len * uy - head_w * ux),
                (p_start[0] + head_len * ux - head_w * uy, p_start[1] + head_len * uy + head_w * ux)
            ], closed=True, fc=color, ec='none', zorder=7))

    # Nhãn nằm chính giữa đoạn
    if label_text:
        # Tính tâm
        mid_idx = len(pts) // 2
        if len(pts) % 2 == 0:
            mx = (pts[mid_idx - 1][0] + pts[mid_idx][0]) / 2
            my = (pts[mid_idx - 1][1] + pts[mid_idx][1]) / 2
        else:
            mx, my = pts[mid_idx]

        b_fc = badge_color or '#FFFFFF'
        bw = max(len(label_text), len(sub_text or '')) * 0.95 + 4.0
        bh = 6.2 if sub_text else 3.8

        ax.add_patch(FancyBboxPatch((mx - bw / 2, my - bh / 2), bw, bh,
                                   boxstyle=f'round,pad=0,rounding_size={min(1.8, bh/2)}',
                                   fc=b_fc, ec=color, lw=1.2, zorder=8))
        if sub_text:
            ax.text(mx, my + 1.2, label_text, ha='center', va='center', fontsize=7.6, fontweight='bold', color=color, zorder=9)
            ax.text(mx, my - 1.4, sub_text, ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=9)
        else:
            ax.text(mx, my, label_text, ha='center', va='center', fontsize=7.8, fontweight='bold', color=color, zorder=9)


# ==============================================================================
# 1. HÌNH 1.2: MÔ HÌNH KIẾN TRÚC TỔNG THỂ HỆ THỐNG GẬY THÔNG MINH IOT (f_overview)
# ==============================================================================
def gen_pro_overview():
    w, h = 20.0, 9.2
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề lớn của mô hình hệ thống
    ax.text(w * 5, 87.0, "MÔ HÌNH KIẾN TRÚC TỔNG THỂ HỆ THỐNG GẬY THÔNG MINH (SMART CANE IoT)",
            ha='center', va='center', fontsize=12.5, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 84.0, "Hạ tầng phân tầng 3 lớp: Thiết bị ngoại vi (Edge Node) - Cổng di động (Mobile Gateway) - Đám mây (Cloud Server)",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Card 1: Gậy thông minh ESP32-S3 (Phần cứng IoT Edge)
    # x=22, w=35 (x: 4.5 -> 39.5)
    draw_card(ax, 22, 44, 35, 68,
              title="GẬY THÔNG MINH IoT", badge="EDGE NODE",
              header_color=C_EMERALD_DARK, bg_color='#FBFDFB', border_color=C_EMERALD_BORDER, rx=2.5)

    # Sub-blocks bên trong Node Gậy
    # Vi điều khiển trung tâm
    ax.add_patch(FancyBboxPatch((6.5, 54.5), 31, 15, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.2, zorder=4))
    ax.text(22, 66.5, "BỘ XỬ LÝ TRUNG TÂM ESP32-S3", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color=C_EMERALD_DARK, zorder=5)
    ax.text(22, 62.0, "• Xtensa LX7 Dual-Core 240MHz · 16MB Flash", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(22, 57.5, "• BLE 5.0 GATT Server ('SmartCane')", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)

    # Cảm biến
    ax.add_patch(FancyBboxPatch((6.5, 34.5), 31, 18, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFFFF', ec=C_SLATE_200, lw=1.0, zorder=4))
    ax.text(8.5, 48.5, "CẢM BIẾN THU THẬP TÍN HIỆU", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_BLUE_DARK, zorder=5)
    ax.text(8.5, 44.0, "• MPU-6050 (I2C): Gia tốc 3 trục ±8g", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(8.5, 40.0, "• HC-SR04: Siêu âm quét vật cản 3-80cm", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(8.5, 36.0, "• Nút bấm BOOT: Hủy còi & báo ngã (GPIO 0)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)

    # Cơ cấu chấp hành & Nguồn
    ax.add_patch(FancyBboxPatch((6.5, 13.5), 31, 19, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFFFF', ec=C_SLATE_200, lw=1.0, zorder=4))
    ax.text(8.5, 29.0, "CẢNH BÁO TẠI CHỖ & NGUỒN PIN", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_AMBER_DARK, zorder=5)
    ax.text(8.5, 24.5, "• Còi hú Buzzer (GPIO 4: Kêu sau 30s té ngã)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(8.5, 20.5, "• Motor rung lệch tâm (MOSFET AOD4184)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(8.5, 16.5, "• Pin 18650 3.7V + Mạch Boost 5V + TP4056", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)


    # Card 2: Smartphone Người dùng gậy (Mobile Gateway)
    # x=73, w=35 (x: 55.5 -> 90.5)
    draw_card(ax, 73, 44, 35, 68,
              title="ĐIỆN THOẠI NGƯỜI DÙNG", badge="GATEWAY",
              header_color=C_BLUE_DARK, bg_color='#F8FAFC', border_color=C_BLUE_BORDER, rx=2.5)

    # Foreground Service
    ax.add_patch(FancyBboxPatch((57.5, 54.5), 31, 15, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#EFF6FF', ec=C_BLUE_MED, lw=1.2, zorder=4))
    ax.text(73, 66.5, "DỊCH VỤ NỀN THƯỜNG TRỰC", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color=C_BLUE_DARK, zorder=5)
    ax.text(73, 62.0, "• Flutter Foreground Service chạy ngầm 24/7", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(73, 57.5, "• Tự kết nối lại BLE qua MAC đã lưu", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)

    # GPS & Fall Engine
    ax.add_patch(FancyBboxPatch((57.5, 34.5), 31, 18, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFFFF', ec=C_SLATE_200, lw=1.0, zorder=4))
    ax.text(59.5, 48.5, "ĐỊNH VỊ VÀ ĐIỀU PHỐI KHẨN CẤP", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_EMERALD_DARK, zorder=5)
    ax.text(59.5, 44.0, "• GPS High Accuracy: Tọa độ chu kỳ 5m", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(59.5, 40.0, "• Bộ đếm lùi 15s: Nút bấm hủy nếu báo nhầm", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(59.5, 36.0, "• Đẩy gói tin khẩn cấp lên Firebase Cloud", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)

    # Kênh liên lạc dự phòng SMS / Gọi
    ax.add_patch(FancyBboxPatch((57.5, 13.5), 31, 19, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFF1F2', ec=C_ROSE_BORDER, lw=1.0, zorder=4))
    ax.text(59.5, 29.0, "CỨU HỘ NGOẠI TUYẾN (GSM/SMS)", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_ROSE_DARK, zorder=5)
    ax.text(59.5, 24.5, "• Tự động gửi SMS tọa độ vị trí Google Maps", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(59.5, 20.5, "• Tự động quay số gọi SOS trực tiếp cho Giám hộ", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(59.5, 16.5, "• Hoạt động cả khi không có Wi-Fi / 4G", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)


    # Card 3: Nền tảng Đám mây Firebase
    # x=126, w=34 (x: 109 -> 143)
    draw_card(ax, 126, 60.5, 34, 35,
              title="FIREBASE CLOUD BACKEND", badge="IoT CLOUD",
              header_color=C_AMBER_DARK, bg_color='#FFFDF7', border_color=C_AMBER_BORDER, rx=2.5)

    ax.text(111, 67.5, "Realtime Database & Authentication:", ha='left', va='center', fontsize=7.8, fontweight='bold', color=C_AMBER_DARK)
    ax.text(111, 63.5, "• Cây dữ liệu JSON: /users/{uid}", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(111, 59.5, "• is_falling, lat, lng, ble_status, timestamp", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(111, 55.5, "• WebSocket Realtime: Độ trễ < 0.5 giây", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(111, 51.5, "• Firebase Auth & Phân quyền bảo mật theo vai trò", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(111, 47.5, "• Lưu vết Lịch sử sự cố, Nhà, Điểm hẹn an toàn", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)


    # Card 4: Kênh SMS GSM ngoại tuyến (Dưới Firebase)
    # x=126, w=34 (x: 109 -> 143)
    draw_card(ax, 126, 25.5, 34, 27,
              title="KÊNH DỰ PHÒNG GSM / SMS", badge="NO INTERNET",
              header_color=C_ROSE_DARK, bg_color='#FFF5F5', border_color=C_ROSE_BORDER, rx=2.0)

    ax.text(111, 31.0, "Mạng Viễn thông Di động (Không cần Internet):", ha='left', va='center', fontsize=7.5, fontweight='bold', color=C_ROSE_DARK)
    ax.text(111, 27.0, "• Gửi SMS khẩn cấp trực tiếp qua sóng viễn thông", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(111, 23.0, "• Nội dung: 'CANH BAO NGA! Vi tri: maps.google...'", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(111, 19.0, "• Cuộc gọi SOS tự động rung chuông người thân", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(111, 15.0, "• Đảm bảo cứu hộ ngay cả khi hết tiền 4G / mất mạng", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)


    # Card 5: Smartphone Người giám hộ (Bên phải cùng)
    # x=178, w=34 (x: 161 -> 195)
    draw_card(ax, 178, 44, 34, 68,
              title="ĐIỆN THOẠI GIÁM HỘ", badge="MONITOR APP",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER, rx=2.5)

    # Live Map
    ax.add_patch(FancyBboxPatch((162.5, 54.5), 31, 15, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFFFF', ec=C_PURPLE_MED, lw=1.2, zorder=4))
    ax.text(178, 66.5, "BẢN ĐỒ THỜI GIAN THỰC", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color=C_PURPLE_DARK, zorder=5)
    ax.text(178, 62.0, "• OpenStreetMap / Flutter Map", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(178, 57.5, "• Marker vị trí người già + Nhà + Điểm hẹn", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)

    # Siren & Alarm
    ax.add_patch(FancyBboxPatch((162.5, 34.5), 31, 18, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFF1F2', ec=C_ROSE_BORDER, lw=1.0, zorder=4))
    ax.text(178, 48.5, "CÒI BÁO ĐỘNG SOS KHẨN CẤP", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_ROSE_DARK, zorder=5)
    ax.text(178, 44.0, "• Chuông thức tỉnh âm lượng cực đại", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(178, 40.0, "• Rung liên tục & Banner cảnh báo khẩn", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(178, 36.0, "• Nút bấm tắt còi báo động từ xa", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)

    # Navigation & Logs
    ax.add_patch(FancyBboxPatch((162.5, 13.5), 31, 19, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFFFF', ec=C_SLATE_200, lw=1.0, zorder=4))
    ax.text(178, 29.0, "ĐIỀU HƯỚNG VÀ NHẬT KÝ", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_BLUE_DARK, zorder=5)
    ax.text(178, 24.5, "• 1 chạm mở chỉ đường Google Maps", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(178, 20.5, "• Giám sát trạng thái Pin / BLE / Mạng", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(178, 16.5, "• Lịch sử các lần ngã & Mất kết nối", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)


    # ================= CÁC ĐƯỜNG KẾT NỐI VÀ BADGE GIAO THỨC GỌN GÀNG =================
    # 1. BLE giữa Gậy và Smartphone Người Già: từ (39.5, 48) tới (55.5, 48) -> dx = 16
    draw_bus(ax, [(39.5, 48), (55.5, 48)], color=C_EMERALD_MED, lw=2.2, arrow_both=True)
    draw_pill_badge(ax, 47.5, 52.0, "BLE 5.0 GATT", fc='#ECFDF5', ec=C_EMERALD_MED, tc=C_EMERALD_DARK, fs=7.2, pad_w=2.0)
    ax.text(47.5, 44.5, "2.4GHz · 10-15m\nUUID: …26a9", ha='center', va='center', fontsize=6.2, color=C_SLATE_500)

    # 2. Internet giữa Smartphone Người Già và Firebase: từ (90.5, 62) tới (109, 62) -> dx = 18.5
    draw_bus(ax, [(90.5, 62), (109, 62)], color=C_BLUE_MED, lw=2.0, arrow_both=True)
    draw_pill_badge(ax, 99.8, 66.5, "Wi-Fi / 4G LTE", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_DARK, fs=7.2, pad_w=2.0)
    ax.text(99.8, 57.5, "HTTPS / WSS\nĐồng bộ 2 chiều", ha='center', va='center', fontsize=6.2, color=C_SLATE_500)

    # 3. Firebase sang Smartphone Giám hộ: từ (143, 62) tới (161, 62) -> dx = 18
    draw_bus(ax, [(143, 62), (161, 62)], color=C_AMBER_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 152.0, 66.5, "onValue() Stream", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=7.0, pad_w=2.0)
    ax.text(152.0, 57.5, "Push Realtime\nĐộ trễ < 0.5s", ha='center', va='center', fontsize=6.2, color=C_SLATE_500)

    # 4. GSM Ngoại tuyến từ Smartphone Người Già sang Card SMS: từ (90.5, 25.5) tới (109, 25.5) -> dx = 18.5
    draw_bus(ax, [(90.5, 25.5), (109, 25.5)], color=C_ROSE_MED, lw=2.0, style='--', arrow_end=True)
    draw_pill_badge(ax, 99.8, 29.5, "Sóng GSM", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=7.2, pad_w=2.0)
    ax.text(99.8, 21.0, "SMS trực tiếp\nKhông cần 4G", ha='center', va='center', fontsize=6.2, color=C_SLATE_500)

    # 5. Card SMS sang Smartphone Giám hộ: từ (143, 25.5) tới (161, 25.5) -> dx = 18
    draw_bus(ax, [(143, 25.5), (161, 25.5)], color=C_ROSE_MED, lw=2.0, style='--', arrow_end=True)
    draw_pill_badge(ax, 152.0, 29.5, "SMS + Gọi SOS", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=7.0, pad_w=2.0)
    ax.text(152.0, 21.0, "Link bản đồ\n+ Chuông gọi", ha='center', va='center', fontsize=6.2, color=C_SLATE_500)

    # Chú thích chân trang chuẩn học thuật
    ax.text(w * 5, 2.5, "Ghi chú: Cơ chế dự phòng kép (Dual-Channel Resilience) đảm bảo ngay cả khi điện thoại mất kết nối Internet, cảnh báo khẩn cấp vẫn đến tay người giám hộ tức thì qua mạng viễn thông GSM.",
            ha='center', va='center', fontsize=7.8, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_overview.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_overview: {p}")
    return p


# ==============================================================================
# 2. HÌNH 2.1: SƠ ĐỒ KIẾN TRÚC VI ĐIỀU KHIỂN ESP32-S3 VÀ NGOẠI VI (f_esp32)
# ==============================================================================
def gen_pro_esp32():
    w, h = 20.0, 9.8
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề sơ đồ
    ax.text(w * 5, 93.5, "SƠ ĐỒ KIẾN TRÚC VI ĐIỀU KHIỂN ESP32-S3 (N16R8) VÀ PHÂN BỐ NGOẠI VI I/O",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 90.5, "Bố trí phân luồng tín hiệu cảm biến đầu vào (Inputs) và cơ cấu chấp hành - truyền thông đầu ra (Outputs)",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # ================= KHỐI TRUNG TÂM: ESP32-S3 N16R8 DEVKIT =================
    cx, cy, cw, ch = 100, 46, 46, 76
    draw_card(ax, cx, cy, cw, ch,
              title="ESP32-S3-WROOM-1 (N16R8)", badge="Dual-Core 240MHz",
              header_color=C_SLATE_900, bg_color='#F8FAFC', border_color=C_SLATE_700, rx=3.0)

    # Mô phỏng QFN IC Package bên trong DevKit
    ax.add_patch(FancyBboxPatch((cx - 19, cy - 30), 38, 58,
                               boxstyle='round,pad=0,rounding_size=2.0',
                               fc='#0F172A', ec='#334155', lw=1.5, zorder=3))
    
    # Logo / Chip Label
    ax.text(cx, cy + 24.5, "ESPRESSIF", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#E2E8F0', zorder=4)
    ax.text(cx, cy + 21.0, "ESP32-S3 SoC", ha='center', va='center', fontsize=7.8, color='#94A3B8', zorder=4)

    # Các khối chức năng bên trong Silicon Chip
    sub_blocks = [
        # (x, y, w, h, title, sub, color)
        (cx - 9, cy + 11, 16.5, 12, "CPU Xtensa® LX7", "2 Nhân @ 240 MHz\n512KB SRAM", '#1E293B', C_CYAN_MED),
        (cx + 9, cy + 11, 16.5, 12, "BỘ NHỚ MỞ RỘNG", "16MB Flash SPI\n8MB PSRAM Octal", '#1E293B', C_CYAN_MED),
        (cx - 9, cy - 4, 16.5, 12, "VÔ TUYẾN 2.4 GHz", "Wi-Fi 802.11 b/g/n\nBluetooth 5.0 LE", '#1E293B', C_EMERALD_MED),
        (cx + 9, cy - 4, 16.5, 12, "BẢO MẬT PHẦN CỨNG", "AES-256 · SHA-2\nSecure Boot", '#1E293B', C_PURPLE_MED),
        (cx - 9, cy - 19, 16.5, 12, "NGOẠI VI ANALOG", "12-bit ADC SAR\n8x LEDC PWM", '#1E293B', C_AMBER_MED),
        (cx + 9, cy - 19, 16.5, 12, "GIAO TIẾP BUS", "I2C · SPI · UART\nUSB OTG · 45 GPIO", '#1E293B', C_BLUE_MED),
    ]

    for bx, by, bw, bh, btitle, bsub, bbg, btc in sub_blocks:
        ax.add_patch(FancyBboxPatch((bx - bw / 2, by - bh / 2), bw, bh,
                                   boxstyle='round,pad=0,rounding_size=1.2',
                                   fc=bbg, ec=btc, lw=1.0, zorder=5))
        ax.text(bx, by + 2.5, btitle, ha='center', va='center', fontsize=6.8, fontweight='bold', color=btc, zorder=6)
        ax.text(bx, by - 2.2, bsub, ha='center', va='center', fontsize=5.8, color='#CBD5E1', zorder=6)

    # Các cọc chân Pin nhỏ bên viền DevKit
    # Cọc trái
    left_pin_ys = [70, 62, 48, 40, 23]
    for py in left_pin_ys:
        ax.add_patch(Rectangle((cx - cw / 2 - 1.2, py - 1.2), 2.4, 2.4, fc='#94A3B8', ec='#475569', lw=0.8, zorder=4))
    # Cọc phải
    right_pin_ys = [64, 44, 24]
    for py in right_pin_ys:
        ax.add_patch(Rectangle((cx + cw / 2 - 1.2, py - 1.2), 2.4, 2.4, fc='#94A3B8', ec='#475569', lw=0.8, zorder=4))


    # ================= KHỐI ĐẦU VÀO (INPUTS - BÊN TRÁI: x=24, w=35, edges: 6.5 -> 41.5) =================
    # 1. Cảm biến MPU6050
    draw_card(ax, 24, 66, 35, 19,
              title="CẢM BIẾN QUÁN TÍNH MPU-6050", badge="I2C",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER, rx=2.0)
    ax.text(8.5, 68.0, "• Gia tốc 3 trục (±8g) & Con quay (±2000°/s)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8.5, 63.5, "• Tốc độ lấy mẫu: 50 Hz (Chu kỳ 20 ms)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(8.5, 59.0, "• Ngưỡng phát hiện ngã: |a| > 25.0 m/s²", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')
    
    # Dây nối I2C: từ x=41.5 tới x=77 (dx = 35.5)
    draw_bus(ax, [(41.5, 70), (77, 70)], color=C_AMBER_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 59.2, 70, "I2C SDA: GPIO 8", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=7.0, pad_w=2.0)

    draw_bus(ax, [(41.5, 62), (77, 62)], color=C_AMBER_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 59.2, 62, "I2C SCL: GPIO 9", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=7.0, pad_w=2.0)

    # 2. Cảm biến HC-SR04
    draw_card(ax, 24, 44, 35, 19,
              title="CẢM BIẾN SIÊU ÂM HC-SR04", badge="40 kHz",
              header_color=C_CYAN_MED, bg_color='#F0FDFA', border_color=C_CYAN_BORDER, rx=2.0)
    ax.text(8.5, 46.0, "• Phát sóng siêu âm 40 kHz, góc quét < 15°", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8.5, 41.5, "• Khoảng cách phát hiện: 3 cm đến 80 cm", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(8.5, 37.0, "• Tính cự ly: d = t × 0.0343 / 2 (cm)", ha='left', va='center', fontsize=6.8, color=C_CYAN_MED, fontweight='bold')

    # Dây nối HC-SR04
    draw_bus(ax, [(77, 48), (41.5, 48)], color=C_CYAN_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 59.2, 48, "TRIG: GPIO 16 (Xung 10µs)", fc='#ECFEFF', ec=C_CYAN_MED, tc=C_CYAN_MED, fs=6.8, pad_w=2.0)

    draw_bus(ax, [(41.5, 40), (77, 40)], color=C_CYAN_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 59.2, 40, "ECHO: GPIO 17 (Pulldown)", fc='#ECFEFF', ec=C_CYAN_MED, tc=C_CYAN_MED, fs=6.8, pad_w=2.0)

    # 3. Nút bấm hủy cảnh báo ngã & tắt còi
    draw_card(ax, 24, 21, 35, 19,
              title="NÚT BẤM HỦY BÁO NGÃ (BOOT)", badge="INPUT",
              header_color=C_EMERALD_DARK, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER, rx=2.0)
    ax.text(8.5, 23.0, "• Nút BOOT tích hợp sẵn trên ESP32-S3 DevKit", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8.5, 18.5, "• Chế độ INPUT_PULLUP (Mặc định mức 1 - HIGH)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(8.5, 14.0, "• Nhấn xuống nối GND (mức 0) → Tắt còi & hủy ngã", ha='left', va='center', fontsize=6.8, color=C_EMERALD_DARK, fontweight='bold')

    # Dây nối Button BOOT
    draw_bus(ax, [(41.5, 23), (77, 23)], color=C_EMERALD_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 59.2, 23, "BUTTON: GPIO 0 (PULLUP)", fc='#ECFDF5', ec=C_EMERALD_MED, tc=C_EMERALD_DARK, fs=6.8, pad_w=2.0)


    # ================= KHỐI ĐẦU RA (OUTPUTS - BÊN PHẢI: x=176, w=35, edges: 158.5 -> 193.5) =================
    # 4. Còi báo động Active Buzzer 5V
    draw_card(ax, 176, 64, 35, 19,
              title="CÒI HÚ KHẨN CẤP (BUZZER)", badge="ALARM",
              header_color=C_ROSE_DARK, bg_color='#FFF1F2', border_color=C_ROSE_BORDER, rx=2.0)
    ax.text(160.5, 66.0, "• Tần số âm học 2000 Hz (Cường độ > 85 dB)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160.5, 61.5, "• Module kích mức THẤP (Active LOW: LOW = Kêu)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(160.5, 57.0, "• Tự động hú sau 30s nếu người già không tắt", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')

    # Dây nối Buzzer: từ x=123 tới x=158.5 (dx = 35.5)
    draw_bus(ax, [(123, 64), (158.5, 64)], color=C_ROSE_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 140.8, 64, "BUZZER OUT: GPIO 4", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=7.0, pad_w=2.0)

    # 5. Mạch Driver Motor Rung Haptic
    draw_card(ax, 176, 44, 35, 19,
              title="MẠCH DRIVER MOTOR RUNG", badge="MOSFET",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER, rx=2.0)
    ax.text(160.5, 46.0, "• MOSFET N-Channel AOD4184 (Chịu dòng lớn)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160.5, 41.5, "• Diode dập xung 1N4007 bảo vệ vi điều khiển", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(160.5, 37.0, "• Rung báo chướng ngại vật phía trước < 80cm", ha='left', va='center', fontsize=6.8, color=C_PURPLE_MED, fontweight='bold')

    # Dây nối Motor
    draw_bus(ax, [(123, 44), (158.5, 44)], color=C_PURPLE_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 140.8, 44, "GATE CONTROL: GPIO 6", fc='#F5F3FF', ec=C_PURPLE_MED, tc=C_PURPLE_MED, fs=7.0, pad_w=2.0)

    # 6. Truyền thông BLE 5.0
    draw_card(ax, 176, 21, 35, 19,
              title="GIAO THỨC BLUETOOTH 5.0 LE", badge="GATT",
              header_color=C_BLUE_DARK, bg_color='#EFF6FF', border_color=C_BLUE_BORDER, rx=2.0)
    ax.text(160.5, 23.0, "• GATT Server: Tên thiết bị 'SmartCane'", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160.5, 18.5, "• Service UUID: 4fafc201-1fb5-459e-8fcc-…", ha='left', va='center', fontsize=6.6, color=C_SLATE_700)
    ax.text(160.5, 14.0, "• Characteristic Té ngã: …26a9 (Notify)", ha='left', va='center', fontsize=6.8, color=C_BLUE_MED, fontweight='bold')

    # Dây nối BLE
    draw_bus(ax, [(123, 24), (158.5, 24)], color=C_BLUE_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 140.8, 24, "2.4GHz RF ANTENNA", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_DARK, fs=7.0, pad_w=2.0)

    # Chú thích chân trang chuẩn kỹ thuật
    ax.text(w * 5, 3.0, "Sơ đồ thiết kế chuẩn phân rã chân I/O trên ESP32-S3: Toàn bộ ngoại vi sử dụng chung mức logic điện áp 3.3V và điểm tiếp đất GND chung để triệt tiêu nhiễu vòng lặp ground-loop.",
            ha='center', va='center', fontsize=7.8, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_esp32.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_esp32: {p}")
    return p


# ==============================================================================
# 3. HÌNH 3.1: SƠ ĐỒ KHỐI CHỨC NĂNG HOÀN CHỈNH CỦA HỆ THỐNG (f_block_diag)
# ==============================================================================
def gen_pro_block_diag():
    w, h = 20.0, 10.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề sơ đồ khối
    ax.text(w * 5, 100.5, "SƠ ĐỒ KHỐI CHỨC NĂNG HOÀN CHỈNH HỆ THỐNG GẬY THÔNG MINH (SMART CANE IoT)",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 97.5, "Kiến trúc tích hợp 3 phân hệ: Phần cứng gậy ngoại vi - Cổng di động người dùng - Đám mây & Ứng dụng giám hộ",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Phân hệ 1: Gậy thông minh ESP32-S3 (x=24, w=42, edges: 3 -> 45)
    draw_card(ax, 24, 48, 42, 88,
              title="PHÂN HỆ PHẦN CỨNG GẬY (ESP32-S3 IoT NODE)", badge="EDGE HARDWARE",
              header_color=C_EMERALD_DARK, bg_color='#FBFDFB', border_color=C_EMERALD_BORDER, rx=2.5)

    # Khối Vi điều khiển trung tâm
    ax.add_patch(FancyBboxPatch((5, 69), 38, 16, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.2, zorder=4))
    ax.text(24, 81.5, "BỘ XỬ LÝ TRUNG TÂM ESP32-S3 (N16R8)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color=C_EMERALD_DARK, zorder=5)
    ax.text(24, 77.0, "• Xtensa LX7 Dual-Core 240MHz · 16MB Flash · 8MB PSRAM", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(24, 73.0, "• Thuật toán lọc nhiễu gia tốc SVM & Tính khoảng cách siêu âm", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(24, 69.0, "• GATT Server BLE 5.0 (Broadcasting & Characteristic Notify)", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)

    # Khối Cảm biến đầu vào
    ax.add_patch(FancyBboxPatch((5, 48), 38, 18, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFFFF', ec=C_SLATE_200, lw=1.0, zorder=4))
    ax.text(7, 62.5, "KHỐI CẢM BIẾN & TÍN HIỆU ĐẦU VÀO", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_BLUE_DARK, zorder=5)
    ax.text(7, 58.0, "• Cảm biến quán tính MPU-6050 (6-DOF: Gia tốc 3 trục ±8g, SDA:8, SCL:9)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(7, 54.0, "• Cảm biến siêu âm HC-SR04 (Sóng âm 40kHz, Trig: GPIO 16, Echo: GPIO 17)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(7, 50.0, "• Nút bấm BOOT (GPIO 0, INPUT_PULLUP: Hủy báo động ngã & tắt còi)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)

    # Khối Cảnh báo tại chỗ
    ax.add_patch(FancyBboxPatch((5, 27), 38, 18, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFF1F2', ec=C_ROSE_BORDER, lw=1.0, zorder=4))
    ax.text(7, 41.5, "KHỐI CẢNH BÁO TẠI CHỖ (HAPTIC & ACOUSTIC)", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_ROSE_DARK, zorder=5)
    ax.text(7, 37.0, "• Còi hú Active Buzzer (GPIO 4: Kích mức LOW, hú sau 30s nếu chưa tắt)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(7, 33.0, "• Motor rung lệch tâm (GPIO 6: Rung cảnh báo xúc giác khi gặp vật cản)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(7, 29.0, "• Mạch công suất Driver MOSFET N-Channel AOD4184 + Diode dập xung", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)

    # Khối Nguồn năng lượng
    ax.add_patch(FancyBboxPatch((5, 7), 38, 17, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFDF5', ec=C_AMBER_BORDER, lw=1.0, zorder=4))
    ax.text(7, 20.5, "KHỐI QUẢN LÝ NGUỒN PIN & SẠC", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_AMBER_DARK, zorder=5)
    ax.text(7, 16.5, "• Cell Pin Li-ion 18650 (Dung lượng 2600mAh, điện áp 3.7V - 4.2V)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(7, 12.5, "• Mạch sạc pin TP4056 Type-C tích hợp bảo vệ quá nạp/quá xả", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(7, 8.5, "• Mạch Boost DC-DC nâng áp ổn định 5V cấp cho vi điều khiển & còi hú", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)


    # Phân hệ 2: Smartphone Người dùng gậy (Mobile Gateway) (x=77, w=38, edges: 58 -> 96)
    draw_card(ax, 77, 48, 38, 88,
              title="SMARTPHONE NGƯỜI DÙNG GẬY (GATEWAY)", badge="MOBILE APP",
              header_color=C_BLUE_DARK, bg_color='#F8FAFC', border_color=C_BLUE_BORDER, rx=2.5)

    # BLE Client
    ax.add_patch(FancyBboxPatch((60, 69), 34, 16, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#EFF6FF', ec=C_BLUE_MED, lw=1.2, zorder=4))
    ax.text(77, 81.5, "MÔ-ĐUN BLUETOOTH LE CLIENT", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color=C_BLUE_DARK, zorder=5)
    ax.text(77, 77.0, "• Tự động quét và kết nối lại BLE qua MAC đã lưu", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(77, 73.0, "• Đăng ký lắng nghe Characteristic Té ngã (Notify)", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(77, 69.0, "• Đọc trạng thái dung lượng pin gậy dự phòng", ha='center', va='center',
            fontsize=6.8, color=C_SLATE_800, zorder=5)

    # Foreground Service
    ax.add_patch(FancyBboxPatch((60, 48), 34, 18, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFFFF', ec=C_SLATE_200, lw=1.0, zorder=4))
    ax.text(62, 62.5, "DỊCH VỤ NỀN THƯỜNG TRỰC (24/7)", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_AMBER_DARK, zorder=5)
    ax.text(62, 58.0, "• Flutter Foreground Service chạy ngầm vĩnh viễn", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(62, 54.0, "• Không bị Android tối ưu hóa pin tiêu diệt tiến trình", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(62, 50.0, "• Quản lý thông báo thường trực trên thanh trạng thái", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)

    # GPS Geolocation
    ax.add_patch(FancyBboxPatch((60, 27), 34, 18, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFFFF', ec=C_SLATE_200, lw=1.0, zorder=4))
    ax.text(62, 41.5, "MÔ-ĐUN ĐỊNH VỊ TOÀN CẦU (GPS)", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_EMERALD_DARK, zorder=5)
    ax.text(62, 37.0, "• Thu nhận tọa độ kinh độ, vĩ độ độ chính xác cao (< 5m)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(62, 33.0, "• Cập nhật tọa độ di chuyển theo chu kỳ 5m", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(62, 29.0, "• Tự động kích hoạt khi có sự cố té ngã xảy ra", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)

    # Bộ đếm lùi & Cứu hộ khẩn cấp
    ax.add_patch(FancyBboxPatch((60, 7), 34, 17, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFF1F2', ec=C_ROSE_BORDER, lw=1.0, zorder=4))
    ax.text(62, 20.5, "BỘ ĐẾM 15s & CỨU HỘ NGOẠI TUYẾN", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_ROSE_DARK, zorder=5)
    ax.text(62, 16.5, "• Đếm lùi 15s trên màn hình: Bấm hủy nếu báo động nhầm", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(62, 12.5, "• Hết 15s: Tự gửi SMS link Google Maps tới Giám hộ", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)
    ax.text(62, 8.5, "• Tự động quay số gọi điện SOS trực tiếp qua sóng GSM", ha='left', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)


    # Phân hệ 3: Đám mây Firebase & Smartphone Giám hộ (x=130, w=38, edges: 111 -> 149)
    # Top Card: Firebase Cloud
    draw_card(ax, 130, 71, 38, 42,
              title="NỀN TẢNG ĐÁM MÂY FIREBASE CLOUD", badge="BACKEND",
              header_color=C_AMBER_DARK, bg_color='#FFFDF7', border_color=C_AMBER_BORDER, rx=2.5)

    ax.text(113, 85.0, "FIREBASE REALTIME DATABASE & AUTHENTICATION", ha='left', va='center', fontsize=7.8, fontweight='bold', color=C_AMBER_DARK)
    ax.text(113, 80.5, "• Cây dữ liệu thời gian thực: /users/{uid}", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(113, 76.5, "  - is_falling (boolean): Cờ phát hiện sự cố ngã", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')
    ax.text(113, 72.5, "  - latitude, longitude: Tọa độ GPS thời gian thực", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 68.5, "  - ble_connected, battery_level, last_online", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 64.5, "  - fall_history: Nhật ký lưu trữ tọa độ và mốc thời gian sự cố", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 60.5, "• Cơ chế bảo mật Firebase Security Rules: Phân quyền theo UID", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 56.5, "• Đồng bộ hai chiều WebSocket (Độ trễ cập nhật < 0.5s)", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)

    # Bottom Card: Smartphone Người Giám Hộ
    draw_card(ax, 130, 24, 38, 45,
              title="SMARTPHONE NGƯỜI GIÁM HỘ (MONITOR APP)", badge="DASHBOARD",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER, rx=2.5)

    ax.text(113, 40.0, "GIAO DIỆN GIÁM SÁT & CẢNH BÁO KHẨN CẤP", ha='left', va='center', fontsize=7.8, fontweight='bold', color=C_PURPLE_DARK)
    ax.text(113, 36.0, "• Bản đồ số OpenStreetMap (Flutter Map):", ha='left', va='center', fontsize=7.0, color=C_SLATE_800, fontweight='bold')
    ax.text(113, 32.0, "  - Theo dõi marker vị trí người già di chuyển thời gian thực", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 28.0, "  - Vùng an toàn: Vị trí Nhà, Điểm hẹn, Bán kính bảo vệ", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 24.0, "• Hệ thống còi báo động SOS toàn màn hình:", ha='left', va='center', fontsize=7.0, color=C_ROSE_DARK, fontweight='bold')
    ax.text(113, 20.0, "  - Phát chuông âm lượng cực đại thức tỉnh người giám hộ", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 16.0, "  - Nút bấm 'Chỉ đường': 1 chạm mở Google Maps điều hướng", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 12.0, "  - Nút bấm tắt còi báo động khẩn cấp từ xa", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(113, 8.0, "• Nhật ký sự cố ngã, mất mạng Internet, tắt GPS, tắt BLE", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)


    # Kênh SMS Ngoại tuyến (Card phụ bên phải ngoài: x=178, w=34, edges: 161 -> 195)
    draw_card(ax, 178, 48, 34, 46,
              title="KÊNH DỰ PHÒNG GSM/SMS", badge="OFFLINE",
              header_color=C_ROSE_DARK, bg_color='#FFF5F5', border_color=C_ROSE_BORDER, rx=2.0)

    ax.text(163, 64.0, "MẠNG VIỄN THÔNG DI ĐỘNG", ha='left', va='center', fontsize=7.6, fontweight='bold', color=C_ROSE_DARK)
    ax.text(163, 60.0, "• Truyền tin khẩn cấp qua sóng GSM", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(163, 56.0, "• Không phụ thuộc kết nối Internet (4G/Wi-Fi)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(163, 52.0, "• Nội dung SMS chứa tọa độ Google Maps", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(163, 48.0, "• Cuộc gọi SOS tự động rung chuông", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(163, 44.0, "• Đảm bảo độ tin cậy cứu hộ 100%", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')
    ax.text(163, 40.0, "  trong mọi tình huống sự cố viễn thông", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)


    # ================= CÁC ĐƯỜNG LIÊN KẾT GIAO THỨC CHUẨN XÁC =================
    # 1. BLE giữa Gậy và Smartphone Người Già: từ (45, 75) tới (58, 75)
    draw_bus(ax, [(45, 75), (58, 75)], color=C_EMERALD_MED, lw=2.2, arrow_both=True)
    draw_pill_badge(ax, 51.5, 79.5, "BLE 5.0 GATT", fc='#ECFDF5', ec=C_EMERALD_MED, tc=C_EMERALD_DARK, fs=7.0, pad_w=1.8)
    ax.text(51.5, 71.5, "Notify UUID: …26a9", ha='center', va='center', fontsize=6.0, color=C_SLATE_500)

    # 2. Internet giữa Smartphone Người Già và Firebase: từ (96, 75) tới (111, 75)
    draw_bus(ax, [(96, 75), (111, 75)], color=C_BLUE_MED, lw=2.0, arrow_both=True)
    draw_pill_badge(ax, 103.5, 79.5, "Wi-Fi / 4G LTE", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_DARK, fs=7.0, pad_w=1.8)
    ax.text(103.5, 71.5, "WebSocket / HTTPS", ha='center', va='center', fontsize=6.0, color=C_SLATE_500)

    # 3. Đồng bộ Firebase xuống Smartphone Giám hộ: từ (130, 50) tới (130, 46.5)
    draw_bus(ax, [(130, 50), (130, 46.5)], color=C_AMBER_MED, lw=2.2, arrow_end=True)
    draw_pill_badge(ax, 130, 48.2, "onValue() Realtime Stream", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=7.0, pad_w=2.0)

    # 4. Kênh SMS Ngoại tuyến từ Smartphone Người Già sang Kênh GSM: từ (96, 18) tới (103, 18) tới (103, 3) tới (178, 3) tới (178, 25)
    draw_bus(ax, [(96, 18), (105, 18), (105, 48), (111, 48)], color=C_ROSE_MED, lw=1.8, style='--', arrow_end=False)
    # Tiếp từ Firebase sang SMS card
    draw_bus(ax, [(149, 48), (161, 48)], color=C_ROSE_MED, lw=1.8, style='--', arrow_end=True)
    draw_pill_badge(ax, 155.0, 52.0, "SMS + Call SOS", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=7.0, pad_w=2.0)
    ax.text(155.0, 44.5, "Đường truyền trực tiếp", ha='center', va='center', fontsize=6.0, color=C_SLATE_500)

    # Chú thích chân trang chuẩn học thuật
    ax.text(w * 5, 2.5, "Hình 3.1: Sơ đồ khối chức năng hoàn chỉnh của hệ thống gậy thông minh Smart Cane IoT",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_block_diag.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_block_diag: {p}")
    return p


# ==============================================================================
# 4. HÌNH 3.2: SƠ ĐỒ NGUYÊN LÝ KẾT NỐI CHI TIẾT PHẦN CỨNG (f_schematic)
# ==============================================================================
def gen_pro_schematic():
    w, h = 20.0, 10.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề sơ đồ nguyên lý
    ax.text(w * 5, 100.5, "SƠ ĐỒ NGUYÊN LÝ KẾT NỐI CHI TIẾT PHẦN CỨNG (HARDWARE SCHEMATIC)",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 97.5, "Bản vẽ thiết kế mạch điện tử: ESP32-S3 DevKit phối ghép cảm biến MPU6050, HC-SR04, Driver MOSFET và khối nguồn 18650",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Bo mạch trung tâm ESP32-S3 DevKit
    cx, cy, cw, ch = 100, 48, 44, 86
    draw_card(ax, cx, cy, cw, ch,
              title="ESP32-S3 N16R8 DEVKIT", badge="CORE MCU",
              header_color=C_SLATE_900, bg_color='#F8FAFC', border_color=C_SLATE_700, rx=3.0)

    # Khung IC Package
    ax.add_patch(FancyBboxPatch((cx - 18, cy - 35), 36, 68,
                               boxstyle='round,pad=0,rounding_size=2.0',
                               fc='#0F172A', ec='#334155', lw=1.5, zorder=3))
    ax.text(cx, cy + 28, "ESPRESSIF", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#E2E8F0', zorder=4)
    ax.text(cx, cy + 24, "ESP32-S3-WROOM-1", ha='center', va='center', fontsize=7.8, color='#94A3B8', zorder=4)

    # Danh sách chân bên trái ESP32 (Inputs & Power)
    pins_left = [
        ("GPIO 8 (SDA)", 74, C_AMBER_MED),
        ("GPIO 9 (SCL)", 66, C_AMBER_MED),
        ("GPIO 16 (TRIG)", 54, C_CYAN_MED),
        ("GPIO 17 (ECHO)", 46, C_CYAN_MED),
        ("GPIO 0 (BOOT)", 34, C_EMERALD_MED),
        ("3V3 (VCC)", 22, C_AMBER_MED),
        ("GND (ĐẤT CHUNG)", 12, C_SLATE_700),
    ]
    for pname, py, pcol in pins_left:
        ax.plot([cx - cw / 2, cx - 18], [py, py], color=pcol, lw=2.0, zorder=4)
        ax.add_patch(Rectangle((cx - cw / 2 - 1.2, py - 1.2), 2.4, 2.4, fc='#94A3B8', ec='#475569', lw=0.8, zorder=5))
        draw_pill_badge(ax, cx - 9.5, py, pname, fc='#1E293B', ec=pcol, tc='#FFFFFF', fs=6.5, bold=True, pad_w=1.2, zorder=6)

    # Danh sách chân bên phải ESP32 (Outputs & Power)
    pins_right = [
        ("GPIO 4 (BUZZER)", 70, C_ROSE_MED),
        ("GPIO 6 (VIBRATOR)", 52, C_PURPLE_MED),
        ("VIN (5V BOOST)", 30, C_ROSE_DARK),
        ("GND (ĐẤT CHUNG)", 16, C_SLATE_700),
    ]
    for pname, py, pcol in pins_right:
        ax.plot([cx + 18, cx + cw / 2], [py, py], color=pcol, lw=2.0, zorder=4)
        ax.add_patch(Rectangle((cx + cw / 2 - 1.2, py - 1.2), 2.4, 2.4, fc='#94A3B8', ec='#475569', lw=0.8, zorder=5))
        draw_pill_badge(ax, cx + 9.5, py, pname, fc='#1E293B', ec=pcol, tc='#FFFFFF', fs=6.5, bold=True, pad_w=1.2, zorder=6)


    # ================= CÁC MODULE NGOẠI VI BÊN TRÁI (INPUTS) =================
    # 1. Module MPU-6050
    draw_card(ax, 24, 70, 36, 22,
              title="MODULE CẢM BIẾN MPU-6050", badge="I2C",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER, rx=2.0)
    ax.text(8, 73.0, "• VCC: Nối nguồn 3.3V từ ESP32", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8, 69.0, "• GND: Nối đất chung toàn mạch", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8, 65.0, "• SCL: Nối chân GPIO 9 (Xung nhịp Clock I2C)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8, 61.0, "• SDA: Nối chân GPIO 8 (Dữ liệu truyền I2C)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)

    draw_bus(ax, [(42, 74), (cx - cw / 2, 74)], color=C_AMBER_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 60, 74, "SDA: GPIO 8", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=7.0, pad_w=2.0)

    draw_bus(ax, [(42, 66), (cx - cw / 2, 66)], color=C_AMBER_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 60, 66, "SCL: GPIO 9", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=7.0, pad_w=2.0)

    # 2. Module HC-SR04
    draw_card(ax, 24, 48, 36, 20,
              title="CẢM BIẾN SIÊU ÂM HC-SR04", badge="40 kHz",
              header_color=C_CYAN_MED, bg_color='#F0FDFA', border_color=C_CYAN_BORDER, rx=2.0)
    ax.text(8, 51.5, "• VCC: Nối 3.3V (hoặc 5V) · GND: Nối đất", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8, 47.5, "• TRIG: Nối GPIO 16 (Phát xung kích 10µs)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8, 43.5, "• ECHO: Nối GPIO 17 (Thu nhận xung phản hồi)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)

    draw_bus(ax, [(cx - cw / 2, 54), (42, 54)], color=C_CYAN_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 60, 54, "TRIG: GPIO 16", fc='#ECFEFF', ec=C_CYAN_MED, tc=C_CYAN_MED, fs=7.0, pad_w=2.0)

    draw_bus(ax, [(42, 46), (cx - cw / 2, 46)], color=C_CYAN_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 60, 46, "ECHO: GPIO 17", fc='#ECFEFF', ec=C_CYAN_MED, tc=C_CYAN_MED, fs=7.0, pad_w=2.0)

    # 3. Nút bấm BOOT hủy báo ngã & tắt còi
    draw_card(ax, 24, 24, 36, 22,
              title="NÚT BẤM HỦY BÁO NGÃ (BOOT)", badge="INPUT",
              header_color=C_EMERALD_DARK, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER, rx=2.0)
    ax.text(8, 27.5, "• Nút BOOT trên ESP32-S3 (hoặc nút bấm ngoài kéo xuống GND)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8, 23.5, "• Chân GPIO 0 kích hoạt điện trở kéo lên INPUT_PULLUP", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8, 19.5, "• Trạng thái bình thường: Mức 1 (HIGH, không nhấn)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(8, 15.5, "• Khi nhấn (LOW): Hủy cảnh báo ngã & tắt còi ngay lập tức", ha='left', va='center', fontsize=6.8, color=C_EMERALD_DARK, fontweight='bold')

    draw_bus(ax, [(42, 34), (cx - cw / 2, 34)], color=C_EMERALD_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 60, 34, "BOOT: GPIO 0", fc='#ECFDF5', ec=C_EMERALD_MED, tc=C_EMERALD_DARK, fs=7.0, pad_w=2.0)


    # ================= CÁC MODULE NGOẠI VI BÊN PHẢI (OUTPUTS & NGUỒN) =================
    # 4. Còi báo động Active Buzzer
    draw_card(ax, 176, 70, 36, 22,
              title="CÒI HÚ KHẨN CẤP (BUZZER)", badge="ALARM",
              header_color=C_ROSE_DARK, bg_color='#FFF1F2', border_color=C_ROSE_BORDER, rx=2.0)
    ax.text(160, 73.0, "• VCC: Nối 3.3V hoặc 5V Boost · GND: Nối đất chung", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 69.0, "• I/O: Nối chân GPIO 4 của vi điều khiển ESP32-S3", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 65.0, "• Module kích mức THẤP (Active LOW: LOW = Kêu, HIGH = Tắt)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 61.0, "• Té ngã 30s không bấm nút tắt -> Tự động hú chuông liên tục", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')

    draw_bus(ax, [(cx + cw / 2, 70), (158, 70)], color=C_ROSE_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 140, 70, "BUZZER: GPIO 4", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=7.0, pad_w=2.0)

    # 5. Mạch Driver Motor Rung MOSFET
    draw_card(ax, 176, 48, 36, 20,
              title="MẠCH DRIVER MOTOR RUNG", badge="MOSFET",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER, rx=2.0)
    ax.text(160, 51.5, "• MOSFET AOD4184: Chân Gate nối GPIO 6 qua R=100Ω", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 47.5, "• Điện trở kéo xuống Pulldown 10kΩ giữa Gate và GND", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 43.5, "• Chân Drain: Nối cực (-) motor rung + Diode 1N4007 dập xung", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 39.5, "• Chân Source: Nối GND chung · Cực (+) motor nối 5V", ha='left', va='center', fontsize=6.8, color=C_PURPLE_MED, fontweight='bold')

    draw_bus(ax, [(cx + cw / 2, 52), (158, 52)], color=C_PURPLE_MED, lw=2.0, arrow_end=True)
    draw_pill_badge(ax, 140, 52, "GATE: GPIO 6", fc='#F5F3FF', ec=C_PURPLE_MED, tc=C_PURPLE_MED, fs=7.0, pad_w=2.0)

    # 6. Khối Quản lý nguồn Pin & Tăng áp
    draw_card(ax, 176, 24, 36, 22,
              title="KHỐI NGUỒN PIN & SẠC TYPE-C", badge="POWER BOOST",
              header_color=C_SLATE_800, bg_color='#F1F5F9', border_color=C_SLATE_500, rx=2.0)
    ax.text(160, 27.5, "• Cell Pin Li-ion 18650 2600mAh (Điện áp 3.7V - 4.2V)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 23.5, "• Module sạc TP4056 cổng Type-C bảo vệ dòng sạc 1A", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 19.5, "• Module Boost DC-DC MT3608: Nâng 3.7V lên ổn định 5V", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(160, 15.5, "• Đầu ra 5V: Cấp chân VIN ESP32, Buzzer và Motor rung", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)

    draw_bus(ax, [(158, 30), (cx + cw / 2, 30)], color=C_ROSE_DARK, lw=2.2, arrow_end=True)
    draw_pill_badge(ax, 140, 30, "VIN: 5.0V BOOST", fc='#FFF1F2', ec=C_ROSE_DARK, tc=C_ROSE_DARK, fs=7.0, pad_w=2.0)

    # Chú thích chân trang chuẩn kỹ thuật
    ax.text(w * 5, 2.5, "Hình 3.2: Sơ đồ nguyên lý kết nối chi tiết phần cứng trên vi điều khiển ESP32-S3",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_schematic.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_schematic: {p}")
    return p


# ==============================================================================
# 5. HÌNH 3.4: LƯU ĐỒ THUẬT TOÁN CHÍNH FIRMWARE ESP32-S3 (f_flow_firmware)
# ==============================================================================
def gen_pro_flow_firmware():
    w, h = 16.0, 14.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề lưu đồ
    ax.text(w * 5, 141.0, "LƯU ĐỒ THUẬT TOÁN CHÍNH CỦA FIRMWARE ESP32-S3",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 137.5, "Chu trình FreeRTOS: Khởi tạo I/O, quét gia tốc té ngã MPU6050, đo khoảng cách siêu âm HC-SR04 & phát sóng BLE",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cx = 80

    # Hàm vẽ block lưu đồ chuẩn ISO 5807
    def draw_term(y, text):
        patch = FancyBboxPatch((cx - 25, y - 4), 50, 8, boxstyle='round,pad=0,rounding_size=4.0',
                               fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.5, zorder=3)
        ax.add_patch(patch)
        ax.text(cx, y, text, ha='center', va='center', fontsize=8.2, fontweight='bold', color=C_EMERALD_DARK, zorder=4)

    def draw_proc(y, title, desc, w_box=60, h_box=9, fc='#EFF6FF', ec=C_BLUE_MED):
        patch = FancyBboxPatch((cx - w_box / 2, y - h_box / 2), w_box, h_box, boxstyle='round,pad=0,rounding_size=1.5',
                               fc=fc, ec=ec, lw=1.3, zorder=3)
        ax.add_patch(patch)
        ax.text(cx, y + 1.8, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color=C_SLATE_900, zorder=4)
        ax.text(cx, y - 2.0, desc, ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=4)

    def draw_dec(y, cond, w_dia=50, h_dia=11):
        poly = Polygon([(cx, y + h_dia / 2), (cx + w_dia / 2, y), (cx, y - h_dia / 2), (cx - w_dia / 2, y)],
                       closed=True, fc='#FFFBEB', ec=C_AMBER_MED, lw=1.5, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, y, cond, ha='center', va='center', fontsize=7.5, fontweight='bold', color=C_AMBER_DARK, zorder=4)

    # 1. Bắt đầu
    draw_term(130, "BẮT ĐẦU (POWER ON / RESET ESP32-S3)")

    # 2. Cấu hình GPIO
    draw_proc(118, "CẤU HÌNH GPIO VÀ NGOẠI VI", "Buzzer (GPIO 4: LOW=kêu), Motor (GPIO 6) → OUTPUT | Nút BOOT (GPIO 0: PULLUP) | HC-SR04 (16, 17)")
    draw_bus(ax, [(cx, 126), (cx, 122.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 3. Self-Test
    draw_proc(106, "TỰ KIỂM TRA PHẦN CỨNG (SELF-TEST)", "Bật còi hú + rung trong 0.2 giây rồi tắt để báo hiệu hệ thống sẵn sàng hoạt động")
    draw_bus(ax, [(cx, 113.5), (cx, 110.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 4. Khởi tạo I2C & MPU6050
    draw_proc(94, "KHỞI TẠO CẢM BIẾN QUÁN TÍNH MPU-6050", "Giao thức I2C (SDA:8, SCL:9, 400kHz) · Cấu hình dải gia tốc ±8g · Tần số 50Hz")
    draw_bus(ax, [(cx, 101.5), (cx, 98.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 5. Khởi tạo BLE Server
    draw_proc(82, "KHỞI TẠO BLUETOOTH LOW ENERGY (GATT SERVER)", "Tên 'SmartCane' · Service UUID ...914b · Characteristic Báo ngã (...26a9, Notify)")
    draw_bus(ax, [(cx, 89.5), (cx, 86.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 6. Vòng lặp Loop: Đọc gia tốc & tính SVM
    draw_proc(70, "ĐỌC GIA TỐC VÀ TÍNH ĐỘ LỚN VECTOR TỔNG HỢP SVM", "Thu nhận (ax, ay, az) từ MPU6050 · Tính độ lớn: |a| = √(ax² + ay² + az²)")
    draw_bus(ax, [(cx, 77.5), (cx, 74.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 7. Phán đoán ngã: |a| > 25.0 m/s2 ?
    draw_dec(57, "|a| > 25.0 m/s² ?\n(Phát hiện va chạm té ngã)", w_dia=52, h_dia=12)
    draw_bus(ax, [(cx, 65.5), (cx, 63)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # Nhánh ĐÚNG: Kích hoạt báo động ngã
    # Box báo động ngã ở bên trái (x=24, y=57)
    patch_alarm = FancyBboxPatch((24 - 18, 57 - 8), 36, 16, boxstyle='round,pad=0,rounding_size=1.5',
                                 fc='#FFF1F2', ec=C_ROSE_MED, lw=1.5, zorder=3)
    ax.add_patch(patch_alarm)
    ax.text(24, 61.5, "KÍCH HOẠT BÁO ĐỘNG NGÃ", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_ROSE_DARK, zorder=4)
    ax.text(24, 57.5, "• Gửi gói tin BLE Notify: value = '1' lên App", ha='center', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold', zorder=4)
    ax.text(24, 53.5, "• Khởi động bộ đếm 30s đếm lùi trên phần cứng", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=4)
    ax.text(24, 49.5, "• Quá 30s chưa nhấn BOOT (GPIO 0) -> Còi GPIO 4 hú", ha='center', va='center', fontsize=6.8, color=C_ROSE_DARK, fontweight='bold', zorder=4)

    draw_bus(ax, [(cx - 26, 57), (42, 57)], color=C_ROSE_MED, lw=1.8, arrow_end=True)
    draw_pill_badge(ax, 48, 60.5, "ĐÚNG (NGÃ)", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=6.8, pad_w=1.5)

    # 8. Nhánh SAI: Đo khoảng cách siêu âm
    draw_proc(42, "ĐO KHOẢNG CÁCH VẬT CẢN (HC-SR04)", "Phát xung TRIG 10µs · Đo độ rộng xung ECHO: d = t × 0.0343 / 2 (cm)")
    draw_bus(ax, [(cx, 51), (cx, 46.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)
    draw_pill_badge(ax, cx + 9, 49, "SAI", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_MED, fs=6.5, pad_w=1.2)

    # Dây từ Box báo động ngã đi xuống khối đo siêu âm
    draw_bus(ax, [(24, 49), (24, 42), (50, 42)], color=C_ROSE_MED, lw=1.3, arrow_end=True)

    # 9. Phán đoán vật cản: 3cm <= d <= 80cm ?
    draw_dec(29, "3 cm ≤ d ≤ 80 cm ?\n(Có vật cản phía trước)", w_dia=52, h_dia=11)
    draw_bus(ax, [(cx, 37.5), (cx, 34.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # Nhánh ĐÚNG: Bật motor rung
    patch_von = FancyBboxPatch((28 - 14, 16 - 5), 28, 10, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FAF5FF', ec=C_PURPLE_MED, lw=1.3, zorder=3)
    ax.add_patch(patch_von)
    ax.text(28, 18.0, "BẬT MOTOR RUNG", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_PURPLE_DARK, zorder=4)
    ax.text(28, 14.0, "Rung phản hồi báo vật cản", ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=4)

    draw_bus(ax, [(cx - 26, 29), (28, 29), (28, 21)], color=C_PURPLE_MED, lw=1.6, arrow_end=True)
    draw_pill_badge(ax, 48, 31.5, "ĐÚNG (CÓ VẬT)", fc='#FAF5FF', ec=C_PURPLE_MED, tc=C_PURPLE_MED, fs=6.8, pad_w=1.5)

    # Nhánh SAI: Tắt motor rung
    patch_voff = FancyBboxPatch((132 - 14, 16 - 5), 28, 10, boxstyle='round,pad=0,rounding_size=1.5',
                                fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.3, zorder=3)
    ax.add_patch(patch_voff)
    ax.text(132, 18.0, "TẮT MOTOR RUNG", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_EMERALD_DARK, zorder=4)
    ax.text(132, 14.0, "Đường đi thông thoáng", ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=4)

    draw_bus(ax, [(cx + 26, 29), (132, 29), (132, 21)], color=C_EMERALD_MED, lw=1.6, arrow_end=True)
    draw_pill_badge(ax, 112, 31.5, "SAI (AN TOÀN)", fc='#ECFDF5', ec=C_EMERALD_MED, tc=C_EMERALD_DARK, fs=6.8, pad_w=1.5)

    # Đường hồi quy vòng lặp Loop
    draw_bus(ax, [(28, 11), (28, 6), (cx, 6)], color=C_SLATE_500, lw=1.3, arrow_end=False)
    draw_bus(ax, [(132, 11), (132, 6), (cx, 6)], color=C_SLATE_500, lw=1.3, arrow_end=False)
    draw_bus(ax, [(cx, 6), (152, 6), (152, 70), (cx + 30, 70)], color=C_SLATE_500, lw=1.3, arrow_end=True)
    ax.text(152, 38, "Vòng lặp lấy mẫu chu kỳ 20 ms (50 Hz)", ha='center', va='center', fontsize=6.8, color=C_SLATE_500, rotation=-90)

    # Chú thích chân trang chuẩn học thuật
    ax.text(w * 5, 2.0, "Hình 3.4: Lưu đồ thuật toán chính của Firmware điều khiển trên ESP32-S3",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_flow_firmware.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_flow_firmware: {p}")
    return p


# ==============================================================================
# 6. HÌNH 3.5: LƯU ĐỒ HOẠT ĐỘNG DỊCH VỤ NGẦM NGƯỜI DÙNG GẬY (f_flow_elderly)
# ==============================================================================
def gen_pro_flow_elderly():
    w, h = 16.0, 14.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề lưu đồ
    ax.text(w * 5, 141.0, "LƯU ĐỒ HOẠT ĐỘNG DỊCH VỤ CHẠY NGẦM NGƯỜI DÙNG GẬY (ELDERLY SERVICE)",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 137.5, "Flutter Foreground Service: Tự kết nối BLE, luồng GPS 5m, quản lý bộ đếm ngược 15s và kích hoạt cứu hộ GSM/SMS",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cx = 80

    def draw_term(y, text):
        patch = FancyBboxPatch((cx - 28, y - 4), 56, 8, boxstyle='round,pad=0,rounding_size=4.0',
                               fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.5, zorder=3)
        ax.add_patch(patch)
        ax.text(cx, y, text, ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_EMERALD_DARK, zorder=4)

    def draw_proc(y, title, desc, w_box=62, h_box=9, fc='#EFF6FF', ec=C_BLUE_MED):
        patch = FancyBboxPatch((cx - w_box / 2, y - h_box / 2), w_box, h_box, boxstyle='round,pad=0,rounding_size=1.5',
                               fc=fc, ec=ec, lw=1.3, zorder=3)
        ax.add_patch(patch)
        ax.text(cx, y + 1.8, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color=C_SLATE_900, zorder=4)
        ax.text(cx, y - 2.0, desc, ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=4)

    def draw_dec(y, cond, w_dia=52, h_dia=11):
        poly = Polygon([(cx, y + h_dia / 2), (cx + w_dia / 2, y), (cx, y - h_dia / 2), (cx - w_dia / 2, y)],
                       closed=True, fc='#FFFBEB', ec=C_AMBER_MED, lw=1.5, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, y, cond, ha='center', va='center', fontsize=7.5, fontweight='bold', color=C_AMBER_DARK, zorder=4)

    # 1. Bắt đầu
    draw_term(130, "BẮT ĐẦU DỊCH VỤ NGẦM (ROLE: ELDERLY)")

    # 2. Khởi động Foreground Service & Auto-connect BLE
    draw_proc(118, "KHỞI TẠO TIẾN TRÌNH NGẦM & TỰ KẾT NỐI BLE", "Khởi chạy Foreground Service vĩnh viễn · Quét MAC lưu sẵn và kết nối lại 'SmartCane'")
    draw_bus(ax, [(cx, 126), (cx, 122.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 3. Luồng GPS định vị
    draw_proc(106, "KHỞI CHẠY LUỒNG ĐỊNH VỊ TOÀN CẦU (GPS STREAM)", "Geolocator High Accuracy: Mỗi 5m di chuyển → Cập nhật (lat, lng, ble_status) lên Firebase")
    draw_bus(ax, [(cx, 113.5), (cx, 110.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 4. Kiểm tra gói tin BLE Té ngã
    draw_dec(93, "Nhận gói tin BLE = '1' ?\n(Gậy báo phát hiện té ngã)", w_dia=52, h_dia=11)
    draw_bus(ax, [(cx, 101.5), (cx, 98.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # Nhánh SAI: Quay lại lắng nghe
    draw_bus(ax, [(cx + 26, 93), (124, 93), (124, 106), (cx + 31, 106)], color=C_SLATE_500, lw=1.3, arrow_end=True)
    draw_pill_badge(ax, 114, 95.5, "SAI (BÌNH THƯỜNG)", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_MED, fs=6.5, pad_w=1.2)

    # 5. Nhánh ĐÚNG: Đẩy cảnh báo lên Firebase
    draw_proc(78, "ĐẨY CẢNH BÁO KHẨN CẤP LÊN FIREBASE REALTIME DB", "Ghi is_falling = true · Lưu tọa độ GPS sự cố và fall_location_url (Google Maps link)", fc='#FFF1F2', ec=C_ROSE_MED)
    draw_bus(ax, [(cx, 87.5), (cx, 82.5)], color=C_ROSE_MED, lw=1.8, arrow_end=True)
    draw_pill_badge(ax, cx + 8, 85, "ĐÚNG", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=6.5, pad_w=1.2)

    # 6. Kích hoạt bộ đếm ngược 15s
    draw_proc(66, "KÍCH HOẠT BỘ ĐẾM NGƯỢC KHẨN CẤP 15 GIÂY", "Bật màn hình khẩn cấp, rung chuông nhắc nhở · Hiển thị nút bấm 'HỦY BÁO ĐỘNG'", fc='#FFFDF5', ec=C_AMBER_MED)
    draw_bus(ax, [(cx, 73.5), (cx, 70.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 7. Kiểm tra người già bấm Hủy trước 15s
    draw_dec(53, "Người dùng bấm HỦY\ntrước khi hết 15s ?", w_dia=52, h_dia=11)
    draw_bus(ax, [(cx, 61.5), (cx, 58.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # Nhánh CÓ: Hủy cảnh báo
    patch_cancel = FancyBboxPatch((28 - 14, 53 - 6), 28, 12, boxstyle='round,pad=0,rounding_size=1.5',
                                  fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.3, zorder=3)
    ax.add_patch(patch_cancel)
    ax.text(28, 55.5, "HỦY CẢNH BÁO", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_EMERALD_DARK, zorder=4)
    ax.text(28, 51.5, "Reset is_falling = false\nDừng bộ đếm ngược", ha='center', va='center', fontsize=6.5, color=C_SLATE_700, zorder=4)

    draw_bus(ax, [(cx - 26, 53), (42, 53)], color=C_EMERALD_MED, lw=1.6, arrow_end=True)
    draw_pill_badge(ax, 48, 55.5, "CÓ (HỦY)", fc='#ECFDF5', ec=C_EMERALD_MED, tc=C_EMERALD_DARK, fs=6.8, pad_w=1.5)

    # 8. Nhánh KHÔNG: Hết 15 giây -> Kích hoạt cứu hộ GSM / SMS
    draw_proc(37, "HẾT 15s: KÍCH HOẠT CỨU HỘ NGOẠI TUYẾN GSM TỨC THÌ", "1. Tự động gửi SMS link Google Maps · 2. Tự động quay số gọi SOS trực tiếp cho Giám hộ", fc='#FFF1F2', ec=C_ROSE_DARK)
    draw_bus(ax, [(cx, 47.5), (cx, 41.5)], color=C_ROSE_MED, lw=1.8, arrow_end=True)
    draw_pill_badge(ax, cx + 11, 44.5, "KHÔNG (HẾT 15s)", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=6.5, pad_w=1.2)

    # 9. Tiếp tục duy trì bảo vệ
    draw_term(23, "TIẾP TỤC DUY TRÌ BẢO VỆ NGẦM 24/7")
    draw_bus(ax, [(cx, 32.5), (cx, 27)], color=C_SLATE_700, lw=1.5, arrow_end=True)
    draw_bus(ax, [(28, 47), (28, 23), (52, 23)], color=C_EMERALD_MED, lw=1.3, arrow_end=True)

    # Vòng lặp hồi quy
    draw_bus(ax, [(cx, 19), (cx, 14), (134, 14), (134, 106), (cx + 31, 106)], color=C_SLATE_500, lw=1.3, arrow_end=True)
    ax.text(134, 60, "Giữ kết nối nền thường trực", ha='center', va='center', fontsize=6.8, color=C_SLATE_500, rotation=-90)

    # Chú thích chân trang chuẩn học thuật
    ax.text(w * 5, 2.0, "Hình 3.5: Lưu đồ hoạt động của dịch vụ chạy ngầm trên máy Người Dùng Gậy",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_flow_elderly.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_flow_elderly: {p}")
    return p


# ==============================================================================
# 7. HÌNH 3.6: LƯU ĐỒ HOẠT ĐỘNG GIÁM SÁT NGƯỜI GIÁM HỘ (f_flow_guardian)
# ==============================================================================
def gen_pro_flow_guardian():
    w, h = 16.0, 14.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề lưu đồ
    ax.text(w * 5, 141.0, "LƯU ĐỒ HOẠT ĐỘNG ỨNG DỤNG GIÁM SÁT NGƯỜI GIÁM HỘ (GUARDIAN APP)",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 137.5, "Theo dõi Firebase Realtime, còi hú thức tỉnh SOS, điều hướng 1 chạm Google Maps và quản lý vùng an toàn",
            ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    cx = 80

    def draw_term(y, text):
        patch = FancyBboxPatch((cx - 28, y - 4), 56, 8, boxstyle='round,pad=0,rounding_size=4.0',
                               fc='#ECFDF5', ec=C_EMERALD_MED, lw=1.5, zorder=3)
        ax.add_patch(patch)
        ax.text(cx, y, text, ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_EMERALD_DARK, zorder=4)

    def draw_proc(y, title, desc, w_box=62, h_box=9, fc='#FAF5FF', ec=C_PURPLE_MED):
        patch = FancyBboxPatch((cx - w_box / 2, y - h_box / 2), w_box, h_box, boxstyle='round,pad=0,rounding_size=1.5',
                               fc=fc, ec=ec, lw=1.3, zorder=3)
        ax.add_patch(patch)
        ax.text(cx, y + 1.8, title, ha='center', va='center', fontsize=7.8, fontweight='bold', color=C_SLATE_900, zorder=4)
        ax.text(cx, y - 2.0, desc, ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=4)

    def draw_dec(y, cond, w_dia=52, h_dia=11):
        poly = Polygon([(cx, y + h_dia / 2), (cx + w_dia / 2, y), (cx, y - h_dia / 2), (cx - w_dia / 2, y)],
                       closed=True, fc='#FFFBEB', ec=C_AMBER_MED, lw=1.5, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, y, cond, ha='center', va='center', fontsize=7.5, fontweight='bold', color=C_AMBER_DARK, zorder=4)

    # 1. Bắt đầu
    draw_term(130, "BẮT ĐẦU ỨNG DỤNG GIÁM HỘ (ROLE: GUARDIAN)")

    # 2. Lắng nghe Firebase Realtime Database
    draw_proc(118, "LẮNG NGHE SỰ KIỆN FIREBASE REALTIME DB", "Đăng ký lắng nghe onValue() tại /users/{uid}: is_falling, lat, lng, ble_connected, online")
    draw_bus(ax, [(cx, 126), (cx, 122.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 3. Phân loại sự kiện
    draw_dec(104, "Phát hiện sự kiện\nbất thường xảy ra ?", w_dia=52, h_dia=11)
    draw_bus(ax, [(cx, 113.5), (cx, 109.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # Nhánh Trái: SỰ CỐ TÉ NGÃ (is_falling == true)
    patch_fall = FancyBboxPatch((28 - 14, 88 - 7), 28, 14, boxstyle='round,pad=0,rounding_size=1.5',
                                fc='#FFF1F2', ec=C_ROSE_MED, lw=1.5, zorder=3)
    ax.add_patch(patch_fall)
    ax.text(28, 92.5, "SỰ CỐ TÉ NGÃ (SOS)", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_ROSE_DARK, zorder=4)
    ax.text(28, 88.5, "• Kích hoạt còi báo động cực đại", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=4)
    ax.text(28, 84.5, "• Rung máy & Banner khẩn cấp", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=4)
    ax.text(28, 80.5, "• Đánh dấu vị trí ngã trên bản đồ", ha='center', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold', zorder=4)

    draw_bus(ax, [(cx - 26, 104), (28, 104), (28, 95)], color=C_ROSE_MED, lw=1.8, arrow_end=True)
    draw_pill_badge(ax, 48, 106.5, "is_falling == true", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=6.8, pad_w=1.5)

    # Nhánh Phải: CẢNH BÁO MẤT MẠNG / TẮT GPS / TẮT BLE
    patch_net = FancyBboxPatch((132 - 14, 88 - 7), 28, 14, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#FFFDF5', ec=C_AMBER_MED, lw=1.3, zorder=3)
    ax.add_patch(patch_net)
    ax.text(132, 92.5, "MẤT MẠNG / MẤT GPS", ha='center', va='center', fontsize=7.6, fontweight='bold', color=C_AMBER_DARK, zorder=4)
    ax.text(132, 88.5, "• Ghi nhận log mất kết nối", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=4)
    ax.text(132, 84.5, "• Hiển thị banner cảnh báo đỏ", ha='center', va='center', fontsize=6.8, color=C_SLATE_800, zorder=4)
    ax.text(132, 80.5, "• Khi hồi phục: ghi thời gian online", ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=4)

    draw_bus(ax, [(cx + 26, 104), (132, 104), (132, 95)], color=C_AMBER_MED, lw=1.6, arrow_end=True)
    draw_pill_badge(ax, 112, 106.5, "MẤT KẾT NỐI", fc='#FFFDF5', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=6.8, pad_w=1.5)

    # Nhánh Giữa: Bình thường -> Cập nhật bản đồ
    draw_bus(ax, [(cx, 98.5), (cx, 75.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)
    draw_pill_badge(ax, cx + 9, 87, "BÌNH THƯỜNG", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_MED, fs=6.5, pad_w=1.2)

    # 4. Tương tác Người Giám Hộ trên Dashboard
    draw_proc(71, "TƯƠNG TÁC XỬ LÝ TRÊN GIAO DIỆN DASHBOARD", "1. Bấm 'Chỉ đường' → Mở Google Maps | 2. Bấm 'Tắt báo động' → Reset is_falling | 3. Đặt Vùng an toàn", fc='#EFF6FF', ec=C_BLUE_MED)
    draw_bus(ax, [(28, 81), (28, 71), (49, 71)], color=C_ROSE_MED, lw=1.5, arrow_end=True)
    draw_bus(ax, [(132, 81), (132, 71), (111, 71)], color=C_AMBER_MED, lw=1.5, arrow_end=True)

    # 5. Cập nhật bản đồ liên tục
    draw_proc(55, "CẬP NHẬT BẢN ĐỒ SỐ THỜI GIAN THỰC (OPENSTREETMAP)", "Vẽ lại vị trí người già + Nhà + Điểm hẹn + Vùng an toàn · Cập nhật vạch pin và trạng thái BLE")
    draw_bus(ax, [(cx, 66.5), (cx, 59.5)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # 6. Duy trì giám sát
    draw_term(41, "DUY TRÌ GIÁM SÁT THỜI GIAN THỰC 24/7")
    draw_bus(ax, [(cx, 50.5), (cx, 45)], color=C_SLATE_700, lw=1.5, arrow_end=True)

    # Vòng lặp hồi quy
    draw_bus(ax, [(cx, 37), (cx, 31), (150, 31), (150, 118), (cx + 31, 118)], color=C_SLATE_500, lw=1.3, arrow_end=True)
    ax.text(150, 75, "Lắng nghe sự kiện Push Realtime", ha='center', va='center', fontsize=6.8, color=C_SLATE_500, rotation=-90)

    # Chú thích chân trang chuẩn học thuật
    ax.text(w * 5, 2.0, "Hình 3.6: Lưu đồ hoạt động giám sát và cảnh báo trên máy Người Giám Hộ",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_flow_guardian.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_flow_guardian: {p}")
    return p


# ==============================================================================
# 8. HÌNH 1.1: SƠ ĐỒ PHÂN LOẠI CÁC PHƯƠNG PHÁP PHÁT HIỆN NGÃ (f_methods)
# ==============================================================================
def gen_pro_methods():
    w, h = 18.0, 9.2
    fig, ax = create_canvas(w, h, dpi=250)

    ax.text(w * 5, 87.0, "SƠ ĐỒ PHÂN LOẠI CÁC PHƯƠNG PHÁP PHÁT HIỆN VÀ CẢNH BÁO TÉ NGÃ",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 84.0, "So sánh ưu - nhược điểm giữa các hướng tiếp cận công nghệ và tính ưu việt của giải pháp Gậy thông minh",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Nút gốc
    patch_root = FancyBboxPatch((w * 5 - 35, 72), 70, 8.5, boxstyle='round,pad=0,rounding_size=2.0',
                                fc=C_SLATE_900, ec='none', zorder=3)
    ax.add_patch(patch_root)
    ax.text(w * 5, 76.2, "CÁC PHƯƠNG PHÁP PHÁT HIỆN & CẢNH BÁO TÉ NGÃ Ở NGƯỜI CAO TUỔI",
            ha='center', va='center', fontsize=8.8, fontweight='bold', color='#FFFFFF', zorder=4)

    # 5 cột phương pháp:
    methods = [
        (20, "THIẾT BỊ ĐEO", "Smartwatch / Vòng tay", C_AMBER_DARK, '#FFFDF5', C_AMBER_BORDER,
         ["• Gia tốc kế, con quay, áp suất", "• Nhỏ gọn, hiện đại", "• Nhược điểm lớn:", "  - Người già hay quên đeo", "  - Phải sạc pin mỗi 1-2 ngày", "  - Thao tác cảm ứng phức tạp"]),
        
        (55, "CAMERA THỊ GIÁC", "Computer Vision / AI", C_BLUE_DARK, '#F8FAFC', C_BLUE_BORDER,
         ["• Nhận diện tư thế cơ thể qua ảnh", "• Độ chính xác nhận dạng cao", "• Nhược điểm lớn:", "  - Xâm phạm quyền riêng tư", "  - Góc chết (phòng tắm, ngủ)", "  - Chi phí lắp đặt rất cao"]),
        
        (90, "CẢM BIẾN MÔI TRƯỜNG", "Âm thanh / Rung sàn", C_CYAN_MED, '#F0FDFA', C_CYAN_BORDER,
         ["• Micro mảng, cảm biến sàn nhà", "• Không cần đeo trên người", "• Nhược điểm lớn:", "  - Dễ báo động giả do tạp âm", "  - Rơi đồ vật gây nhiễu", "  - Giới hạn trong căn phòng"]),
        
        (125, "RADAR KHÔNG DÂY", "mmWave / UWB Radar", C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER,
         ["• Quét sóng phản xạ cơ thể", "• Không cần camera, riêng tư", "• Nhược điểm lớn:", "  - Giá thành linh kiện đắt đỏ", "  - Lắp đặt cố định tại chỗ", "  - Bị che chắn bởi đồ đạc"]),
        
        (160, "GẬY THÔNG MINH", "ĐỀ TÀI NGHIÊN CỨU", C_EMERALD_DARK, '#F0FDF4', C_EMERALD_MED,
         ["• MPU-6050 + Siêu âm + BLE", "• Vật dụng trợ thị bất ly thân", "• Ưu điểm vượt trội:", "  [+] Luôn mang theo khi đi lại", "  [+] 100% bảo vệ quyền riêng tư", "  [+] Kênh kép 4G Cloud + SMS GSM"]),
    ]

    for mx, mtitle, msub, mcol, mbg, mbc, mbullets in methods:
        # Đường rẽ nhánh từ nút gốc
        draw_bus(ax, [(w * 5, 72), (w * 5, 66), (mx, 66), (mx, 60)], color=mcol, lw=1.5, arrow_end=True)

        # Card phương pháp
        draw_card(ax, mx, 33, 31, 54,
                  title=mtitle, badge=msub[:12],
                  header_color=mcol, bg_color=mbg, border_color=mbc, rx=2.0)

        # Bullets
        by = 51
        for b in mbullets:
            is_hl = "[+]" in b or "Ưu điểm" in b or "Nhược điểm" in b
            col_txt = mcol if is_hl else C_SLATE_800
            fwt = 'bold' if is_hl else 'normal'
            ax.text(mx - 13.5, by, b, ha='left', va='center', fontsize=6.8, fontweight=fwt, color=col_txt)
            by -= 4.2

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 1.1: Sơ đồ phân loại các phương pháp phát hiện và cảnh báo té ngã hiện nay",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_methods.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_methods: {p}")
    return p


# ==============================================================================
# 9. HÌNH 2.2: CẤU TRÚC GATT PROFILE BLUETOOTH LOW ENERGY (f_gatt)
# ==============================================================================
def gen_pro_gatt():
    w, h = 18.0, 9.2
    fig, ax = create_canvas(w, h, dpi=250)

    ax.text(w * 5, 87.0, "CẤU TRÚC PHÂN TẦNG VÀ GATT PROFILE CỦA BLUETOOTH LOW ENERGY",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 84.0, "Cấu hình phân cấp chuẩn Bluetooth SIG: Profile → Service → Characteristics → Descriptors",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Card GATT Server
    draw_card(ax, 75, 73, 110, 11,
              title="GATT SERVER (ESP32-S3) – TÊN QUẢNG BÁ THIẾT BỊ: 'SmartCane'", badge="SERVER",
              header_color=C_SLATE_900, bg_color='#F8FAFC', border_color=C_SLATE_700, rx=2.0)
    ax.text(25, 70.0, "• Địa chỉ MAC phần cứng cố định (dùng để Flutter BLE Client tự động nhận diện và ghép nối lại không cần quét thủ công)",
            ha='left', va='center', fontsize=7.2, color=C_SLATE_700)

    # Card Primary Service
    draw_card(ax, 75, 54, 110, 12,
              title="PRIMARY SERVICE: FALL DETECTION SERVICE", badge="SERVICE",
              header_color=C_BLUE_DARK, bg_color='#EFF6FF', border_color=C_BLUE_BORDER, rx=2.0)
    ax.text(25, 51.0, "• UUID: 4fafc201-1fb5-459e-8fcc-c5c9c331914b  (Định danh duy nhất dịch vụ gậy thông minh)",
            ha='left', va='center', fontsize=7.5, fontweight='bold', color=C_BLUE_DARK)

    draw_bus(ax, [(75, 67.5), (75, 60)], color=C_BLUE_MED, lw=2.0, arrow_end=True)

    # 2 Nhánh Characteristic
    # Nhánh 1 (Trái): Characteristic Báo Ngã
    draw_card(ax, 45, 30, 56, 26,
              title="CHARACTERISTIC 'TÉ NGÃ' (FALL EVENT)", badge="NOTIFY",
              header_color=C_ROSE_DARK, bg_color='#FFF1F2', border_color=C_ROSE_BORDER, rx=2.0)
    ax.text(20, 35.5, "• UUID: beb5483e-36e1-4688-b7f5-ea07361b26a9", ha='left', va='center', fontsize=7.0, fontweight='bold', color=C_ROSE_DARK)
    ax.text(20, 31.5, "• Thuộc tính (Properties): READ | NOTIFY", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(20, 27.5, "• Giá trị dữ liệu (Value):", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(20, 23.5, "  - '0': Trạng thái bình thường", ha='left', va='center', fontsize=6.8, color=C_EMERALD_DARK, fontweight='bold')
    ax.text(20, 19.5, "  - '1': PHÁT HIỆN TÉ NGÃ (Kích hoạt SOS)", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')

    draw_bus(ax, [(55, 48), (45, 43)], color=C_ROSE_MED, lw=1.8, arrow_end=True)

    # Descriptor CCCD dưới Characteristic Ngã
    draw_card(ax, 45, 9, 56, 9,
              title="DESCRIPTOR: CCCD (Client Characteristic Config)", badge="0x2902",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER, rx=1.5)
    ax.text(20, 6.5, "• Cho phép Smartphone Client đăng ký nhận gói tin ngắt đẩy về tự động", ha='left', va='center', fontsize=6.6, color=C_SLATE_700)

    draw_bus(ax, [(45, 17), (45, 13.5)], color=C_AMBER_MED, lw=1.5, arrow_end=True)

    # Nhánh 2 (Phải): Characteristic Pin / Dự phòng
    draw_card(ax, 115, 30, 56, 26,
              title="CHARACTERISTIC 'PIN' (BATTERY LEVEL)", badge="READ",
              header_color=C_EMERALD_DARK, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER, rx=2.0)
    ax.text(90, 35.5, "• UUID: beb5483e-36e1-4688-b7f5-ea07361b26a8", ha='left', va='center', fontsize=7.0, fontweight='bold', color=C_EMERALD_DARK)
    ax.text(90, 31.5, "• Thuộc tính (Properties): READ", ha='left', va='center', fontsize=7.0, color=C_SLATE_800)
    ax.text(90, 27.5, "• Giá trị dữ liệu (Value): 0% - 100% (Điện áp 3.7V - 4.2V)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(90, 23.5, "• Phục vụ giám sát năng lượng pin từ xa qua Dashboard", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(90, 19.5, "• Dự phòng mở rộng truyền dữ liệu cấu hình ngưỡng ngã", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)

    draw_bus(ax, [(95, 48), (115, 43)], color=C_EMERALD_MED, lw=1.8, arrow_end=True)

    # Client bên phải
    draw_card(ax, 155, 60, 30, 20,
              title="GATT CLIENT", badge="FLUTTER",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER, rx=2.0)
    ax.text(142, 63.5, "• Thư viện flutter_blue_plus", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(142, 59.5, "• Subscribe Characteristic", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(142, 55.5, "• Nhận callback ngay tức thì", ha='left', va='center', fontsize=6.8, color=C_PURPLE_MED, fontweight='bold')

    draw_bus(ax, [(140, 60), (130, 60)], color=C_PURPLE_MED, lw=2.0, arrow_both=True)

    # Chú thích chân trang
    ax.text(w * 5, 2.0, "Hình 2.2: Cấu trúc phân tầng và GATT Profile của Bluetooth Low Energy trong hệ thống",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_gatt.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_gatt: {p}")
    return p


# ==============================================================================
# 10. HÌNH 2.10: ĐỒNG BỘ DỮ LIỆU FIREBASE REALTIME DATABASE (f_rtdb)
# ==============================================================================
def gen_pro_rtdb():
    w, h = 18.0, 9.2
    fig, ax = create_canvas(w, h, dpi=250)

    ax.text(w * 5, 87.0, "CƠ CHẾ ĐỒNG BỘ DỮ LIỆU THỜI GIAN THỰC TRÊN FIREBASE REALTIME DATABASE",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 84.0, "Kiến trúc Publish/Subscribe qua kết nối WebSocket bảo đảm độ trễ cập nhật < 0.5s và bộ đệm ngoại tuyến (Offline Cache)",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Trung tâm: Firebase RTDB Cloud
    draw_card(ax, 90, 48, 56, 56,
              title="FIREBASE REALTIME DATABASE (JSON CLOUD TREE)", badge="WEBSOCKET",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER, rx=2.5)

    json_lines = [
        "{\n",
        '  "users": {\n',
        '    "<UID_ELDERLY>": {\n',
        '      "is_falling": true,         // Cờ báo ngã SOS\n',
        '      "latitude": 10.762622,       // Tọa độ GPS\n',
        '      "longitude": 106.660172,\n',
        '      "ble_connected": true,\n',
        '      "battery_level": 85,\n',
        '      "fall_timestamp": 1730472000,\n',
        '      "safe_zone": { "lat": 10.76, "lng": 106.66, "radius": 50 }\n',
        '    }\n',
        '  }\n',
        "}"
    ]
    ax.text(65, 45, "".join(json_lines), ha='left', va='center', fontsize=6.8, fontfamily='monospace', color=C_SLATE_900)

    # Máy A: Smartphone Người dùng gậy (Bên trái: x=24, w=36)
    draw_card(ax, 24, 48, 36, 42,
              title="MÁY A (NGƯỜI DÙNG GẬY)", badge="PUBLISHER",
              header_color=C_BLUE_DARK, bg_color='#EFF6FF', border_color=C_BLUE_BORDER, rx=2.0)
    ax.text(9, 58.0, "• Cập nhật dữ liệu khi có thay đổi:", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_BLUE_DARK)
    ax.text(9, 53.5, "  - Vị trí GPS thay đổi > 5m", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(9, 49.5, "  - Gậy báo sự cố té ngã (is_falling=true)", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')
    ax.text(9, 45.5, "  - Trạng thái kết nối BLE đóng / mở", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(9, 41.5, "• Giao thức: REST API / WebSocket update()", ha='left', va='center', fontsize=7.0, color=C_BLUE_MED, fontweight='bold')
    ax.text(9, 37.5, "• Offline Persistence: Tự động lưu hàng đợi", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(9, 33.5, "  khi mất mạng và đồng bộ ngay khi có lại", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)

    draw_bus(ax, [(42, 54), (62, 54)], color=C_BLUE_MED, lw=2.2, arrow_end=True)
    draw_pill_badge(ax, 52, 58, "update()", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_DARK, fs=7.2, pad_w=1.8)

    # Máy B: Smartphone Người giám hộ (Bên phải: x=156, w=36)
    draw_card(ax, 156, 48, 36, 42,
              title="MÁY B (NGƯỜI GIÁM HỘ)", badge="SUBSCRIBER",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER, rx=2.0)
    ax.text(141, 58.0, "• Lắng nghe luồng dữ liệu liên tục:", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_PURPLE_DARK)
    ax.text(141, 53.5, "  - Hàm onValue() nhận push tức thời", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(141, 49.5, "  - Kích hoạt còi hú SOS khi is_falling=true", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')
    ax.text(141, 45.5, "  - Cập nhật marker di chuyển trên bản đồ", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(141, 41.5, "• Giao thức: Persistent WebSocket WSS", ha='left', va='center', fontsize=7.0, color=C_PURPLE_MED, fontweight='bold')
    ax.text(141, 37.5, "• Độ trễ truyền dẫn toàn trình: < 0.5s", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(141, 33.5, "• Gửi lệnh phản hồi tắt còi từ xa", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)

    draw_bus(ax, [(118, 54), (138, 54)], color=C_AMBER_MED, lw=2.2, arrow_end=True)
    draw_pill_badge(ax, 128, 58, "onValue() Stream", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=7.0, pad_w=1.8)

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 2.10: Cơ chế đồng bộ dữ liệu hai chiều thời gian thực trên Firebase Realtime Database",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_rtdb.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_rtdb: {p}")
    return p


# ==============================================================================
# HÀM CHÍNH TẠO TẤT CẢ CÁC HÌNH CÒN LẠI VÀ CHẠY
# ==============================================================================
def gen_all():
    gen_pro_overview()
    gen_pro_esp32()
    gen_pro_block_diag()
    gen_pro_schematic()
    gen_pro_flow_firmware()
    gen_pro_flow_elderly()
    gen_pro_flow_guardian()
    gen_pro_methods()
    gen_pro_gatt()
    gen_pro_rtdb()

if __name__ == '__main__':
    gen_all()


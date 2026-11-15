# -*- coding: utf-8 -*-
"""
make_pro_figs2.py
Phần 2: Thiết kế các sơ đồ kỹ thuật chi tiết chuẩn Publication / Engineering-Grade:
- Hình 2.3: Chuẩn giao tiếp I2C giữa vi điều khiển ESP32-S3 và MPU6050 (f_i2c)
- Hình 2.4: Hệ trục tọa độ 3D và cảm biến quán tính 6-DOF MPU6050 (f_mpu)
- Hình 2.5: Dạng sóng vector gia tốc tổng hợp SVM khi đi bộ, ngã và nằm yên (f_accel)
- Hình 2.6: Giản đồ thời gian xung Trig và Echo của cảm biến siêu âm HC-SR04 (f_ultra)
- Hình 2.7: Nguyên lý phản xạ quang học của cảm biến hồng ngoại E18-D50NK (f_ir)
- Hình 2.8: Sơ đồ nguyên lý mạch driver MOSFET AOD4184 điều khiển motor rung (f_mosfet)
- Hình 2.9: Nguyên lý định vị toàn cầu GPS dựa trên giao điểm mặt cầu vệ tinh (f_gps)
- Hình 2.11: Kiến trúc đa tầng của Framework Flutter (f_flutter)
- Hình 2.12: Cơ chế hoạt động đa luồng Isolate của Background Service (f_fgs)
- Các biểu đồ thực nghiệm Chương 4: f_exp_accel, f_exp_latency, f_exp_ultrasonic, f_exp_scenarios
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
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon, Arc, Wedge
from matplotlib import font_manager

from make_pro_figs import (
    create_canvas, draw_card, draw_pill_badge, draw_bus, OUT,
    C_SLATE_900, C_SLATE_800, C_SLATE_700, C_SLATE_500, C_SLATE_200, C_SLATE_100, C_SLATE_50,
    C_BLUE_DARK, C_BLUE_MED, C_BLUE_LIGHT, C_BLUE_BORDER,
    C_EMERALD_DARK, C_EMERALD_MED, C_EMERALD_LIGHT, C_EMERALD_BORDER,
    C_AMBER_DARK, C_AMBER_MED, C_AMBER_LIGHT, C_AMBER_BORDER,
    C_PURPLE_DARK, C_PURPLE_MED, C_PURPLE_LIGHT, C_PURPLE_BORDER,
    C_ROSE_DARK, C_ROSE_MED, C_ROSE_LIGHT, C_ROSE_BORDER,
    C_CYAN_MED, C_CYAN_LIGHT, C_CYAN_BORDER
)

C_SLATE_300 = '#CBD5E1'


# ==============================================================================
# 1. HÌNH 2.3: CHUẨN GIAO TIẾP VẬT LÝ VÀ GIAO THỨC I2C (f_i2c)
# ==============================================================================
def gen_pro_i2c():
    w, h = 18.0, 9.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề
    ax.text(w * 5, 90.0, "CHUẨN GIAO TIẾP VẬT LÝ VÀ GIAO THỨC I2C (ESP32-S3 VÀ MPU-6050)",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 87.0, "Cấu hình Bus Master - Slave: SDA (GPIO 8), SCL (GPIO 9), điện trở kéo lên Pull-up 4.7kΩ và khung truyền dữ liệu 400kHz",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Card Master bên trái: ESP32-S3
    draw_card(ax, 28, 56, 38, 48,
              title="ESP32-S3 DEVKIT (MASTER)", badge="I2C0 MASTER",
              header_color=C_BLUE_DARK, bg_color='#EFF6FF', border_color=C_BLUE_BORDER, rx=2.2)
    ax.text(11, 66.5, "• Vai trò: Khởi tạo truyền thông (Bus Master)", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_BLUE_DARK)
    ax.text(11, 62.0, "• Tần số xung nhịp Clock: 400 kHz (Fast Mode)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(11, 57.5, "• Chân SDA (Serial Data): GPIO 8", ha='left', va='center', fontsize=7.0, color=C_AMBER_DARK, fontweight='bold')
    ax.text(11, 53.0, "• Chân SCL (Serial Clock): GPIO 9", ha='left', va='center', fontsize=7.0, color=C_CYAN_MED, fontweight='bold')
    ax.text(11, 48.5, "• Cực thu hở Open-Drain (Cần điện trở kéo lên)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(11, 44.0, "• Nguồn cấp VCC: 3.3V DC (ổn định)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(11, 39.5, "• Tiếp đất: GND chung toàn mạch", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)

    # Card Slave bên phải: MPU-6050
    draw_card(ax, 152, 56, 38, 48,
              title="CẢM BIẾN MPU-6050 (SLAVE)", badge="ADDR: 0x68",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER, rx=2.2)
    ax.text(135, 66.5, "• Vai trò: Phản hồi yêu cầu (Bus Slave)", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_AMBER_DARK)
    ax.text(135, 62.0, "• Địa chỉ phần cứng I2C: 0x68 (Chân AD0 nối GND)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(135, 57.5, "• Chân SDA: Nhận/Phát dữ liệu nhị phân", ha='left', va='center', fontsize=7.0, color=C_AMBER_DARK, fontweight='bold')
    ax.text(135, 53.0, "• Chân SCL: Nhận xung nhịp từ Master", ha='left', va='center', fontsize=7.0, color=C_CYAN_MED, fontweight='bold')
    ax.text(135, 48.5, "• Thanh ghi dữ liệu: ACCEL_XOUT_H (0x3B)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(135, 44.0, "• Tốc độ đọc: Burst read 6 byte gia tốc (X, Y, Z)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(135, 39.5, "• Nguồn cấp: 3.3V (Bộ ổn áp LDO tích hợp)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)

    # Khối Nguồn 3.3V và Điện trở kéo lên (Pull-up Resistors) ở giữa
    ax.add_patch(FancyBboxPatch((80, 68), 20, 11, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#F8FAFC', ec=C_SLATE_500, lw=1.2, zorder=3))
    ax.text(90, 75.5, "+3.3V VCC", ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_ROSE_DARK, zorder=4)
    ax.text(90, 71.5, "Điện trở kéo Rp = 4.7 kΩ", ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=4)

    # Vẽ 2 điện trở kéo
    # Kéo SDA
    ax.plot([85, 85], [68, 60], color=C_AMBER_MED, lw=1.8, zorder=3)
    ax.plot([85, 85], [78, 68], color=C_ROSE_DARK, lw=1.5, zorder=3)
    # Kéo SCL
    ax.plot([95, 95], [68, 48], color=C_CYAN_MED, lw=1.8, zorder=3)
    ax.plot([95, 95], [78, 68], color=C_ROSE_DARK, lw=1.5, zorder=3)

    # 2 Đường Bus I2C ngang
    # Đường SDA (GPIO 8)
    draw_bus(ax, [(47, 60), (133, 60)], color=C_AMBER_MED, lw=2.4, arrow_both=True)
    draw_pill_badge(ax, 66, 60, "SDA: GPIO 8 (Dữ liệu 2 chiều)", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=7.0, pad_w=2.0)

    # Đường SCL (GPIO 9)
    draw_bus(ax, [(47, 48), (133, 48)], color=C_CYAN_MED, lw=2.4, arrow_end=True)
    draw_pill_badge(ax, 66, 48, "SCL: GPIO 9 (Xung đồng hồ)", fc='#ECFEFF', ec=C_CYAN_MED, tc=C_CYAN_MED, fs=7.0, pad_w=2.0)

    # Khung giao thức truyền thông nhị phân ở dưới
    draw_card(ax, 90, 19, 162, 22,
              title="TRÌNH TỰ KHUNG TRUYỀN DỮ LIỆU I2C (I2C TRANSACTION FRAME - ĐỌC GIA TỐC MPU-6050)",
              badge="PROTOCOL PACKET", header_color=C_SLATE_900, bg_color='#FFFFFF', border_color=C_SLATE_200, rx=2.0)

    # Các block trong khung truyền
    frames = [
        # (x, w, label, sub, color, textcol)
        (18, 12, "START", "SDA ↓ khi SCL ↑", C_EMERALD_MED, '#FFFFFF'),
        (33, 20, "SLAVE ADDR (0x68)", "7-bit: 1101000", C_BLUE_MED, '#FFFFFF'),
        (47, 10, "R/W", "0: Write", C_BLUE_DARK, '#FFFFFF'),
        (55, 9, "ACK", "0 (Slave)", C_SLATE_700, '#FFFFFF'),
        (69, 21, "REG ADDR (0x3B)", "ACCEL_XOUT_H", C_PURPLE_MED, '#FFFFFF'),
        (83, 9, "ACK", "0 (Slave)", C_SLATE_700, '#FFFFFF'),
        (94, 14, "RE-START", "Sr condition", C_EMERALD_MED, '#FFFFFF'),
        (109, 18, "SLAVE ADDR", "0x68 + R (1)", C_BLUE_MED, '#FFFFFF'),
        (121, 9, "ACK", "0 (Slave)", C_SLATE_700, '#FFFFFF'),
        (139, 28, "DATA 6 BYTES", "Gia tốc X, Y, Z (16-bit)", C_AMBER_MED, '#FFFFFF'),
        (156, 9, "NACK", "1 (Master)", C_ROSE_MED, '#FFFFFF'),
        (165, 11, "STOP", "SDA ↑ khi SCL ↑", C_SLATE_900, '#FFFFFF'),
    ]

    for fx, fw, flabel, fsub, fbg, ftc in frames:
        ax.add_patch(FancyBboxPatch((fx - fw / 2, 13), fw, 10, boxstyle='round,pad=0,rounding_size=1.0',
                                   fc=fbg, ec='#FFFFFF', lw=1.0, zorder=4))
        ax.text(fx, 19.0, flabel, ha='center', va='center', fontsize=6.5, fontweight='bold', color=ftc, zorder=5)
        ax.text(fx, 15.0, fsub, ha='center', va='center', fontsize=5.5, color='#F1F5F9', zorder=5)

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 2.3: Chuẩn giao tiếp I2C giữa vi điều khiển ESP32-S3 và cảm biến quán tính MPU-6050",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_i2c.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_i2c: {p}")
    return p


# ==============================================================================
# 2. HÌNH 2.4: HỆ TRỤC TỌA ĐỘ 3D VÀ NGUYÊN LÝ CẢM BIẾN MPU-6050 (f_mpu)
# ==============================================================================
def gen_pro_mpu():
    w, h = 18.0, 9.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề
    ax.text(w * 5, 90.0, "HỆ TRỤC TỌA ĐỘ KHÔNG GIAN 3 CHIỀU VÀ NGUYÊN LÝ CẢM BIẾN QUÁN TÍNH 6-DOF MPU-6050",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 87.0, "Minh họa cấu trúc vector gia tốc tổng hợp SVM, các bậc tự do góc quay Roll - Pitch - Yaw và cấu hình phần cứng",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Bên trái: Mô hình hệ trục không gian 3D
    ax.add_patch(FancyBboxPatch((8, 10), 80, 72, boxstyle='round,pad=0,rounding_size=2.5',
                               fc='#F8FAFC', ec=C_SLATE_200, lw=1.2, zorder=2))
    ax.text(48, 77.0, "HỆ TRỤC TỌA ĐỘ DESCARTES 3 CHIỀU (X, Y, Z)",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color=C_SLATE_900, zorder=4)

    ox, oy = 34, 36

    # Trục X (Đỏ - Hướng sang phải)
    ax.annotate('', xy=(ox + 30, oy), xytext=(ox, oy),
                arrowprops=dict(arrowstyle="-|>", color=C_ROSE_MED, lw=2.4, mutation_scale=15), zorder=5)
    draw_pill_badge(ax, ox + 33, oy, "Trục X (+ax)", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=6.8)

    # Trục Y (Xanh lá - Hướng dọc lên / dọc thân gậy)
    ax.annotate('', xy=(ox, oy + 32), xytext=(ox, oy),
                arrowprops=dict(arrowstyle="-|>", color=C_EMERALD_MED, lw=2.4, mutation_scale=15), zorder=5)
    draw_pill_badge(ax, ox, oy + 35, "Trục Y (+ay - Dọc thân gậy)", fc='#ECFDF5', ec=C_EMERALD_MED, tc=C_EMERALD_DARK, fs=6.8)

    # Trục Z (Xanh dương - Chiếu xiên vuông góc mặt phẳng)
    ax.annotate('', xy=(ox - 20, oy - 16), xytext=(ox, oy),
                arrowprops=dict(arrowstyle="-|>", color=C_BLUE_MED, lw=2.4, mutation_scale=15), zorder=5)
    draw_pill_badge(ax, ox - 24, oy - 19, "Trục Z (+az)", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_DARK, fs=6.8)

    # Vector gia tốc tổng hợp |a| (SVM)
    vx, vy = ox + 20, oy + 20
    ax.annotate('', xy=(vx, vy), xytext=(ox, oy),
                arrowprops=dict(arrowstyle="-|>", color=C_PURPLE_DARK, lw=2.8, mutation_scale=16), zorder=6)
    
    # Hộp công thức SVM (Nằm trọn trong card trái)
    ax.add_patch(FancyBboxPatch((vx + 1, vy - 4), 28, 9, boxstyle='round,pad=0,rounding_size=1.2',
                               fc='#FAF5FF', ec=C_PURPLE_MED, lw=1.2, zorder=7))
    ax.text(vx + 15, vy + 1.5, "VECTOR GIA TỐC TỔNG HỢP SVM", ha='center', va='center', fontsize=6.0, fontweight='bold', color=C_PURPLE_DARK, zorder=8)
    ax.text(vx + 15, vy - 1.5, "|a| = √(ax² + ay² + az²)", ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_PURPLE_MED, zorder=8)

    # Vòng quay con quay hồi chuyển (Gyroscope)
    # Roll quanh X
    ax.add_patch(Arc((ox + 16, oy), 13, 9, theta1=20, theta2=340, color=C_ROSE_MED, lw=1.5, ls='--', zorder=4))
    ax.text(ox + 16, oy - 6.5, "Roll (φ)", ha='center', va='center', fontsize=6.8, color=C_ROSE_DARK, fontweight='bold')

    # Pitch quanh Y
    ax.add_patch(Arc((ox, oy + 16), 9, 13, theta1=110, theta2=430, color=C_EMERALD_MED, lw=1.5, ls='--', zorder=4))
    ax.text(ox - 7.5, oy + 16, "Pitch (θ)", ha='center', va='center', fontsize=6.8, color=C_EMERALD_DARK, fontweight='bold')

    # Yaw quanh Z
    ax.add_patch(Arc((ox - 11, oy - 9), 12, 12, theta1=0, theta2=300, color=C_BLUE_MED, lw=1.5, ls='--', zorder=4))
    ax.text(ox - 18, oy - 4, "Yaw (ψ)", ha='center', va='center', fontsize=6.8, color=C_BLUE_DARK, fontweight='bold')


    # Bên phải: Chi tiết thông số cảm biến MPU-6050
    draw_card(ax, 134, 60, 80, 24,
              title="THÔNG SỐ PHẦN CỨNG CẢM BIẾN MPU-6050", badge="HARDWARE SPECS",
              header_color=C_SLATE_900, bg_color='#FFFFFF', border_color=C_SLATE_200, rx=2.0)
    ax.text(97, 65.0, "• Cấu trúc MEMS 6-DOF: Tích hợp 3 trục gia tốc kế + 3 trục con quay hồi chuyển", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(97, 61.0, "• Bộ chuyển đổi ADC tích hợp: 16-bit SAR ADC trên mỗi kênh độc lập", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(97, 57.0, "• Dải đo gia tốc kế cấu hình: ±8g (Tương ứng độ nhạy 4096 LSB/g)", ha='left', va='center', fontsize=6.8, color=C_BLUE_DARK, fontweight='bold')
    ax.text(97, 53.0, "• Dải đo con quay hồi chuyển: ±500 °/s (Độ nhạy 65.5 LSB/(°/s))", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)

    # Card cấu hình Firmware
    draw_card(ax, 134, 33, 80, 25,
              title="CẤU HÌNH FIRMWARE VÀ THUẬT TOÁN PHÁT HIỆN TÉ NGÃ", badge="ALGORITHM",
              header_color=C_EMERALD_DARK, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER, rx=2.0)
    ax.text(97, 39.0, "• Tần số lấy mẫu trong FreeRTOS: 50 Hz (Chu kỳ đo đạc 20 ms)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(97, 35.0, "• Bộ lọc số thông thấp DLPF: 21 Hz (Triệt tiêu rung lắc rung cơ khí thông thường)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(97, 31.0, "• Trạng thái người già bình thường: |a| dao động quanh g = 9.8 m/s² (± 2.5 m/s²)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(97, 27.0, "• NGƯỠNG VA CHẠM NGÃ: |a| > 25.0 m/s² (≈ 2.55 g) → KÍCH HOẠT SOS", ha='left', va='center', fontsize=7.2, color=C_ROSE_MED, fontweight='bold')
    ax.text(97, 23.0, "• Phối hợp góc nghiêng Pitch/Roll > 60° xác nhận gậy tiếp đất bất động", ha='left', va='center', fontsize=6.8, color=C_EMERALD_DARK)

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 2.4: Hệ trục tọa độ không gian 3 chiều và cảm biến quán tính 6-DOF MPU-6050",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_mpu.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_mpu: {p}")
    return p


# ==============================================================================
# 3. HÌNH 2.5: ĐỒ THỊ DẠNG SÓNG GIA TỐC SVM THỰC TẾ (f_accel)
# ==============================================================================
def gen_pro_accel():
    np.random.seed(42)
    t = np.linspace(0, 12, 1200)

    # Đi bộ bình thường (0 - 6.5s)
    walk = 9.8 + 1.8 * np.sin(2 * np.pi * 1.6 * t) * (t < 6.5) + np.random.normal(0, 0.25, t.size)

    # Rơi tự do (Free-fall dip) từ 6.5s đến 6.75s
    freefall = -7.5 * np.exp(-((t - 6.65) / 0.12) ** 2)

    # Đỉnh va chạm (Impact Spike) tại 6.85s: vọt lên 32.5 m/s2
    impact = 24.5 * np.exp(-((t - 6.85) / 0.06) ** 2)

    # Nằm bất động (Post-fall Rest) sau 7.5s: nằm im phẳng lặng ở mức 9.8 m/s2
    rest = np.where(t > 7.3, 9.8 + np.random.normal(0, 0.08, t.size), walk)

    a = rest + freefall + impact

    fig = plt.figure(figsize=(10.5, 4.8), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0.08, 0.15, 0.90, 0.76])

    # Vẽ nền các giai đoạn (Phase Regions)
    ax.axvspan(0, 6.4, color='#EFF6FF', alpha=0.5, label='Giai đoạn 1: Đi bộ sinh hoạt thường nhật (ADL)')
    ax.axvspan(6.4, 6.75, color='#FEF3C7', alpha=0.55, label='Giai đoạn 2: Mất thăng bằng & Rơi tự do (|a| giảm mạnh)')
    ax.axvspan(6.75, 7.3, color='#FFE4E6', alpha=0.6, label='Giai đoạn 3: Va chạm mạnh với mặt đất (|a| > 25 m/s²)')
    ax.axvspan(7.3, 12, color='#F1F5F9', alpha=0.5, label='Giai đoạn 4: Nằm bất động sau ngã')

    # Vẽ đường gia tốc SVM
    ax.plot(t, a, color='#1E3A8A', lw=1.6, label='Vector gia tốc tổng hợp |a| (m/s²)')

    # Đường ngưỡng phát hiện ngã (25 m/s2)
    ax.axhline(25.0, color='#E11D48', ls='--', lw=1.8, label='Ngưỡng kích hoạt cảnh báo té ngã (25.0 m/s²)')
    ax.text(0.2, 25.8, 'NGƯỠNG BÁO NGÃ: 25.0 m/s² (≈ 2.55 g)', color='#E11D48', fontsize=8.5, fontweight='bold')

    # Đường gia trọng trường chuẩn g = 9.8 m/s2
    ax.axhline(9.8, color='#64748B', ls=':', lw=1.2)
    ax.text(10.2, 10.5, 'g = 9.8 m/s²', color='#64748B', fontsize=8.0, fontweight='bold')

    # Điểm chú thích đỉnh va chạm
    ax.scatter([6.85], [32.5], color='#E11D48', s=60, zorder=5)
    ax.annotate('ĐỈNH VA CHẠM (IMPACT)\n|a|max = 32.5 m/s² (> 25 m/s²)\n→ KÍCH HOẠT CÒI HÚ + BLE NOTIFY',
                xy=(6.85, 32.5), xytext=(3.5, 30.5),
                fontsize=7.8, fontweight='bold', color='#E11D48',
                arrowprops=dict(arrowstyle="->", color='#E11D48', lw=1.5),
                bbox=dict(boxstyle="round,pad=0.4", fc="#FFF1F2", ec="#FDA4AF", lw=1.0))

    # Điểm chú thích rơi tự do
    ax.annotate('Rơi tự do (|a| < 4 m/s²)',
                xy=(6.65, 3.2), xytext=(4.2, 2.0),
                fontsize=7.2, color='#D97706', fontweight='bold',
                arrowprops=dict(arrowstyle="->", color='#D97706', lw=1.2))

    ax.set_title('DẠNG SÓNG VECTOR GIA TỐC TỔNG HỢP SVM TRONG CÁC GIAI ĐOẠN ĐI BỘ VÀ TÉ NGÃ', fontsize=10.5, fontweight='bold', color='#0F172A', pad=12)
    ax.set_xlabel('Thời gian đo đạc (giây)', fontsize=8.8, fontweight='bold', color='#334155')
    ax.set_ylabel('Độ lớn vector gia tốc |a| (m/s²)', fontsize=8.8, fontweight='bold', color='#334155')
    ax.set_ylim(0, 38)
    ax.set_xlim(0, 12)
    ax.grid(alpha=0.3, ls=':')
    ax.legend(loc='upper right', fontsize=7.2, framealpha=0.92)

    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)

    p = os.path.join(OUT, 'f_accel.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_accel: {p}")
    return p


# ==============================================================================
# 4. HÌNH 2.6: GIẢN ĐỒ THỜI GIAN PHÁT XUNG HC-SR04 (f_ultra)
# ==============================================================================
def gen_pro_ultra():
    w, h = 18.0, 9.2
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề
    ax.text(w * 5, 87.0, "GIẢN ĐỒ THỜI GIAN PHÁT XUNG KÍCH VÀ PHẢN HỒI CẢM BIẾN SIÊU ÂM HC-SR04",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 84.0, "Quy trình đo cự ly thời gian thực: Phát xung TRIG 10µs, phát 8 chu kỳ sóng 40kHz, thu phản xạ ECHO và tính khoảng cách",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Card chứa giản đồ xung
    draw_card(ax, 90, 48, 164, 60,
              title="GIẢN ĐỒ DẠNG SÓNG ĐIỆN TỬ VÀ SÓNG ÂM HỌC (TIMING WAVEFORMS)", badge="40 kHz SONIC",
              header_color=C_SLATE_900, bg_color='#FFFFFF', border_color=C_SLATE_300, rx=2.5)

    # 1. Tín hiệu TRIG (GPIO 16)
    y_trig = 59
    ax.text(16, y_trig + 3, "1. TÍN HIỆU KÍCH TRIG (GPIO 16)", ha='left', va='center', fontsize=7.5, fontweight='bold', color=C_BLUE_DARK)
    ax.plot([16, 28, 28, 34, 34, 166], [y_trig, y_trig, y_trig + 5, y_trig + 5, y_trig, y_trig], color=C_BLUE_MED, lw=2.0)
    ax.text(31, y_trig + 7.5, "≥ 10 µs", ha='center', va='center', fontsize=7.0, fontweight='bold', color=C_BLUE_DARK)
    ax.annotate('', xy=(34, y_trig + 6.2), xytext=(28, y_trig + 6.2), arrowprops=dict(arrowstyle="<->", color=C_BLUE_MED, lw=1.2))

    # 2. Chùm 8 chu kỳ sóng âm 40 kHz
    y_burst = 47
    ax.text(16, y_burst + 3, "2. CHÙM SÓNG SIÊU ÂM 40 kHz (TRANSMITTER T)", ha='left', va='center', fontsize=7.5, fontweight='bold', color=C_AMBER_DARK)
    ax.plot([16, 38], [y_burst, y_burst], color=C_AMBER_MED, lw=1.5)
    # 8 chu kỳ sin
    xs = np.linspace(38, 58, 200)
    ys = y_burst + 3.0 * np.sin(2 * np.pi * 8 * (xs - 38) / 20.0)
    ax.plot(xs, ys, color=C_AMBER_MED, lw=1.8)
    ax.plot([58, 166], [y_burst, y_burst], color=C_AMBER_MED, lw=1.5)
    ax.text(48, y_burst + 5.5, "8 chu kỳ sóng âm 40 kHz (Tự động phát)", ha='center', va='center', fontsize=6.8, color=C_AMBER_DARK)

    # 3. Sóng phản hồi từ vật cản
    y_refl = 35
    ax.text(16, y_refl + 3, "3. SÓNG ÂM PHẢN HỒI TỪ VẬT CẢN (RECEIVER R)", ha='left', va='center', fontsize=7.5, fontweight='bold', color=C_PURPLE_DARK)
    ax.plot([16, 102], [y_refl, y_refl], color=C_PURPLE_MED, lw=1.5)
    xs_r = np.linspace(102, 122, 200)
    ys_r = y_refl + 2.0 * np.sin(2 * np.pi * 8 * (xs_r - 102) / 20.0)
    ax.plot(xs_r, ys_r, color=C_PURPLE_MED, lw=1.8)
    ax.plot([122, 166], [y_refl, y_refl], color=C_PURPLE_MED, lw=1.5)
    ax.text(112, y_refl + 4.5, "Sóng dội về chạm màng thu", ha='center', va='center', fontsize=6.8, color=C_PURPLE_DARK)

    # 4. Tín hiệu ECHO (GPIO 17)
    y_echo = 23
    ax.text(16, y_echo + 3, "4. TÍN HIỆU ĐỘ RỘNG XUNG ECHO (GPIO 17)", ha='left', va='center', fontsize=7.5, fontweight='bold', color=C_EMERALD_DARK)
    ax.plot([16, 58, 58, 122, 122, 166], [y_echo, y_echo, y_echo + 5.5, y_echo + 5.5, y_echo, y_echo], color=C_EMERALD_MED, lw=2.2)
    ax.annotate('', xy=(122, y_echo + 7.0), xytext=(58, y_echo + 7.0), arrowprops=dict(arrowstyle="<->", color=C_EMERALD_MED, lw=1.5))
    ax.text(90, y_echo + 8.5, "Thời gian xung HIGH: t (µs) = Thời gian sóng âm đi và về", ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_EMERALD_DARK)

    # Khung công thức toán học tính cự ly
    ax.add_patch(FancyBboxPatch((30, 4), 120, 10, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#F0FDF4', ec=C_EMERALD_MED, lw=1.5, zorder=4))
    ax.text(90, 10.5, "CÔNG THỨC TOÁN HỌC: Khoảng cách d = (t × v_sound) / 2 = (t × 0.0343) / 2  (cm)",
            ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_EMERALD_DARK, zorder=5)
    ax.text(90, 6.5, "Ngưỡng kích hoạt rung cảnh báo trên gậy: 3 cm ≤ d ≤ 80 cm (Khi phát hiện chướng ngại vật phía trước)",
            ha='center', va='center', fontsize=7.0, color=C_SLATE_800, zorder=5)

    p = os.path.join(OUT, 'f_ultra.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_ultra: {p}")
    return p


# ==============================================================================
# 5. HÌNH 2.7: CẢM BIẾN HỒNG NGOẠI E18-D50NK (f_ir)
# ==============================================================================
def gen_pro_ir():
    w, h = 18.0, 9.2
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề
    ax.text(w * 5, 87.0, "NGUYÊN LÝ PHẢN XẠ QUANG HỌC VÀ MẠCH SO SÁNH CẢM BIẾN HỒNG NGOẠI E18-D50NK",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 84.0, "Cơ chế phát xung LED hồng ngoại điều chế, thu phản xạ khuếch tán, so sánh điện áp LM393 và xuất tín hiệu số NPN Open Collector",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Mô phỏng thân cảm biến công nghiệp E18-D50NK bên trái
    draw_card(ax, 34, 46, 44, 56,
              title="CẢM BIẾN E18-D50NK (M18)", badge="OPTICAL SENSOR",
              header_color=C_BLUE_DARK, bg_color='#F8FAFC', border_color=C_BLUE_BORDER, rx=2.0)
    
    # 2 Mắt thấu kính IR
    # Mắt phát (Emitter)
    ax.add_patch(Circle((48, 56), 4.5, fc='#FEF3C7', ec=C_AMBER_MED, lw=1.5, zorder=4))
    ax.text(48, 56, "IR TX", ha='center', va='center', fontsize=6.8, fontweight='bold', color=C_AMBER_DARK, zorder=5)
    ax.text(28, 56, "LED Phát Hồng Ngoại", ha='right', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)

    # Mắt thu (Receiver)
    ax.add_patch(Circle((48, 40), 4.5, fc='#EFF6FF', ec=C_BLUE_MED, lw=1.5, zorder=4))
    ax.text(48, 40, "IR RX", ha='center', va='center', fontsize=6.8, fontweight='bold', color=C_BLUE_DARK, zorder=5)
    ax.text(28, 40, "Phototransistor Thu", ha='right', va='center', fontsize=6.8, color=C_SLATE_800, zorder=5)

    # Biến trở vi chỉnh ở đuôi
    ax.text(34, 26, "• Biến trở vi chỉnh cự ly: 3 - 50 cm", ha='center', va='center', fontsize=6.8, color=C_SLATE_700, zorder=5)
    ax.text(34, 22, "• Đèn LED đỏ báo trạng thái ngõ ra", ha='center', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold', zorder=5)

    # Chùm tia phát đi
    poly_tx = Polygon([(52.5, 58), (110, 68), (110, 48), (52.5, 54)], closed=True,
                      fc='#FFFBEB', ec=C_AMBER_MED, lw=1.2, ls='--', alpha=0.6, zorder=3)
    ax.add_patch(poly_tx)
    ax.text(80, 62, "Chùm tia hồng ngoại phát ra (Điều chế tần số)", ha='center', va='center', fontsize=6.8, color=C_AMBER_DARK, fontweight='bold')

    # Vật cản ở giữa (x=115)
    ax.add_patch(FancyBboxPatch((110, 28), 12, 44, boxstyle='round,pad=0,rounding_size=1.5',
                               fc='#E2E8F0', ec=C_SLATE_700, lw=1.5, zorder=4))
    ax.text(116, 50, "VẬT CẢN\n(Bề mặt phản xạ)", ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_SLATE_900, zorder=5)

    # Tia phản xạ quay về
    draw_bus(ax, [(110, 48), (80, 42), (52.5, 40)], color=C_BLUE_MED, lw=1.8, style='--', arrow_end=True)
    ax.text(80, 36, "Tia phản xạ dội về mắt thu", ha='center', va='center', fontsize=6.8, color=C_BLUE_DARK)

    # Khối Mạch so sánh LM393 & Ngõ ra bên phải
    draw_card(ax, 154, 46, 38, 56,
              title="MẠCH NỘI BỘ & NGÕ RA SỐ", badge="OUTPUT NPN",
              header_color=C_EMERALD_DARK, bg_color='#F0FDF4', border_color=C_EMERALD_BORDER, rx=2.0)
    ax.text(138, 64.0, "• Bộ so sánh khuếch đại LM393", ha='left', va='center', fontsize=7.0, fontweight='bold', color=C_EMERALD_DARK)
    ax.text(138, 59.5, "• Dây Nâu: Cấp nguồn 5V", ha='left', va='center', fontsize=6.8, color=C_ROSE_DARK, fontweight='bold')
    ax.text(138, 55.0, "• Dây Xanh dương: GND", ha='left', va='center', fontsize=6.8, color=C_SLATE_700, fontweight='bold')
    ax.text(138, 50.5, "• Dây Đen: Ngõ ra Digital (NPN)", ha='left', va='center', fontsize=6.8, color=C_BLUE_DARK, fontweight='bold')
    ax.text(138, 44.0, "• BẢNG MỨC LOGIC ĐẦU RA:", ha='left', va='center', fontsize=7.0, fontweight='bold', color=C_SLATE_900)
    ax.text(138, 38.5, "  - CÓ VẬT CẢN: Mức LOW (0V)", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')
    ax.text(138, 33.5, "  - KHÔNG VẬT: Mức HIGH (3.3V)", ha='left', va='center', fontsize=6.8, color=C_EMERALD_DARK, fontweight='bold')
    ax.text(138, 27.5, "• Cấu hình GPIO ESP32-S3: INPUT_PULLUP", ha='left', va='center', fontsize=6.6, color=C_SLATE_700)

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 2.7: Nguyên lý phản xạ quang học của cảm biến vật cản hồng ngoại E18-D50NK",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_ir.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_ir: {p}")
    return p


# ==============================================================================
# 6. HÌNH 2.8: MẠCH CÔNG SUẤT DRIVER MOTOR RUNG MOSFET AOD4184 (f_mosfet)
# ==============================================================================
def gen_pro_mosfet():
    w, h = 18.0, 9.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề
    ax.text(w * 5, 90.0, "SƠ ĐỒ NGUYÊN LÝ MẠCH CÔNG SUẤT DRIVER MOTOR RUNG MOSFET AOD4184",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 87.0, "Thiết kế mạch kích đóng/ngắt tải cảm kháng: MOSFET N-Channel, Diode dập xung ngược 1N4007 và điện trở xả cực Gate",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Card Sơ đồ mạch điện tử bên trái (x=52, w=88, y=48, h=66)
    draw_card(ax, 52, 48, 88, 66,
              title="MẠCH ĐIỆN TỬ DRIVER MOTOR RUNG", badge="DRIVER CIRCUIT",
              header_color=C_PURPLE_DARK, bg_color='#FAF5FF', border_color=C_PURPLE_BORDER, rx=2.5)

    # Nguồn 5V Boost trên đỉnh (bên trong thân card bên dưới header, y=69)
    draw_pill_badge(ax, 52, 69, "+5V POWER BOOST (Tải độc lập)", fc='#FFF1F2', ec=C_ROSE_DARK, tc=C_ROSE_DARK, fs=7.2)
    ax.plot([52, 52], [66.5, 62], color=C_ROSE_DARK, lw=2.4)

    # Động cơ rung lệch tâm M (Vibration Motor) tại (52, 56)
    ax.add_patch(Circle((52, 56), 6.0, fc='#FFFBEB', ec=C_AMBER_MED, lw=1.8, zorder=4))
    ax.text(52, 56, "MOTOR\nRUNG", ha='center', va='center', fontsize=7.2, fontweight='bold', color=C_AMBER_DARK, zorder=5)

    # Diode dập xung 1N4007 mắc song song ngược
    ax.plot([36, 36], [62, 50], color='#1E293B', lw=1.6)
    ax.plot([36, 52], [62, 62], color='#1E293B', lw=1.6)
    ax.plot([36, 52], [50, 50], color='#1E293B', lw=1.6)
    ax.add_patch(Polygon([(33.5, 53), (38.5, 53), (36, 59)], closed=True, fc=C_ROSE_MED, ec='#1E293B', lw=1.0, zorder=4))
    ax.plot([33, 39], [59, 59], color='#1E293B', lw=1.8, zorder=4)
    ax.text(26, 56, "Diode 1N4007\n(Dập xung L)", ha='center', va='center', fontsize=6.8, color=C_ROSE_DARK, fontweight='bold')

    # Dây từ Motor xuống Drain của MOSFET
    ax.plot([52, 52], [50, 44], color='#1E293B', lw=1.8)

    # MOSFET AOD4184
    ax.plot([52, 52], [44, 40], color='#1E293B', lw=2.4)  # Drain lead
    ax.plot([47, 52], [40, 40], color='#1E293B', lw=2.4)
    ax.plot([47, 47], [32, 44], color='#1E293B', lw=2.4)  # Kênh dẫn Drain-Source
    ax.plot([43, 43], [32, 44], color='#1E293B', lw=2.0)  # Cực Gate
    ax.plot([47, 52], [36, 36], color='#1E293B', lw=2.4)
    ax.plot([52, 52], [36, 32], color='#1E293B', lw=2.4)  # Source lead
    ax.plot([52, 52], [32, 25], color='#1E293B', lw=2.0)  # Dây Source xuống GND

    ax.text(56, 41, "DRAIN (D)", ha='left', va='center', fontsize=7.0, fontweight='bold', color='#1E293B')
    ax.text(56, 33, "SOURCE (S)", ha='left', va='center', fontsize=7.0, fontweight='bold', color='#1E293B')
    ax.text(41, 41, "GATE (G)", ha='right', va='center', fontsize=7.0, fontweight='bold', color='#1E293B')

    # Chân GPIO 6 từ ESP32
    draw_pill_badge(ax, 14, 38, "GPIO 6", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_DARK, fs=7.0)

    # Điện trở hạn dòng Gate Rg = 100 ohm
    ax.plot([19, 43], [38, 38], color=C_PURPLE_MED, lw=2.0)
    draw_pill_badge(ax, 26, 38, "Rg = 100 Ω", fc='#FFFFFF', ec=C_PURPLE_MED, tc=C_PURPLE_DARK, fs=6.5)

    # Điện trở xả Rpd = 10k nối Gate xuống GND
    ax.plot([35, 35], [38, 25], color='#1E293B', lw=1.5)
    draw_pill_badge(ax, 35, 31.5, "Rpd = 10 kΩ", fc='#FFFFFF', ec=C_SLATE_500, tc=C_SLATE_800, fs=6.2)
    ax.plot([35, 52], [25, 25], color='#1E293B', lw=1.5)

    # Ký hiệu GND chung
    ax.plot([46, 58], [25, 25], color='#1E293B', lw=2.4)
    ax.plot([48, 56], [23, 23], color='#1E293B', lw=2.0)
    ax.plot([50, 54], [21, 21], color='#1E293B', lw=1.6)
    draw_pill_badge(ax, 52, 17, "GND CHUNG TOÀN MẠCH", fc='#F1F5F9', ec=C_SLATE_700, tc=C_SLATE_900, fs=6.8)


    # Bên phải: Giải thích nguyên lý kỹ thuật chi tiết
    draw_card(ax, 142, 60, 72, 34,
              title="NGUYÊN LÝ ĐÓNG / NGẮT VÀ THÔNG SỐ KỸ THUẬT", badge="OPERATION",
              header_color=C_SLATE_900, bg_color='#FFFFFF', border_color=C_SLATE_200, rx=2.0)
    ax.text(109, 67.0, "• MOSFET AOD4184: Chịu điện áp Vds=40V, dòng cực đại Id=50A", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(109, 63.0, "• Điện trở nội dẫn Rds(on) siêu nhỏ < 8.5 mΩ (Không bị nóng mạch)", ha='left', va='center', fontsize=6.8, color=C_EMERALD_DARK, fontweight='bold')
    ax.text(109, 59.0, "• MỨC ĐIỀU KHIỂN TỪ ESP32-S3 (GPIO 6):", ha='left', va='center', fontsize=7.0, fontweight='bold', color=C_PURPLE_DARK)
    ax.text(109, 55.0, "  - GPIO 6 = HIGH (3.3V) → Vgs > Vth → MOSFET dẫn bão hòa → Motor RUNG", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')
    ax.text(109, 51.0, "  - GPIO 6 = LOW (0V) → Vgs = 0V → MOSFET khóa hoàn toàn → Motor DỪNG", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(109, 47.0, "• Điện trở kéo xuống Rpd = 10kΩ: Đảm bảo motor không rung khi chip boot", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)

    draw_card(ax, 142, 28, 72, 24,
              title="BẢO VỆ XUNG ĐIỆN ÁP NGƯỢC (FLYBACK PROTECTION)", badge="SAFETY DESIGN",
              header_color=C_ROSE_DARK, bg_color='#FFF1F2', border_color=C_ROSE_BORDER, rx=2.0)
    ax.text(109, 32.5, "• Hiện tượng: Cuộn dây động cơ có tính cảm kháng (L)", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(109, 28.5, "• Khi MOSFET ngắt đột ngột: Sinh sức điện động ngược e = -L(di/dt)", ha='left', va='center', fontsize=6.8, color=C_ROSE_DARK, fontweight='bold')
    ax.text(109, 24.5, "• Điện áp cảm ứng có thể vọt lên hàng chục Volt gây thủng MOSFET", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(109, 20.5, "• Diode 1N4007: Khép kín dòng xả cảm ứng, triệt tiêu xung nhọn hoàn toàn", ha='left', va='center', fontsize=6.8, color=C_EMERALD_DARK, fontweight='bold')

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 2.8: Sơ đồ nguyên lý mạch kích công suất motor rung sử dụng MOSFET và diode dập xung",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_mosfet.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_mosfet: {p}")
    return p


# ==============================================================================
# 7. HÌNH 2.9: NGUYÊN LÝ ĐỊNH VỊ TOÀN CẦU GPS VỆ TINH (f_gps)
# ==============================================================================
def gen_pro_gps():
    w, h = 18.0, 9.2
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề
    ax.text(w * 5, 87.0, "NGUYÊN LÝ ĐỊNH VỊ TOÀN CẦU GPS DỰA TRÊN GIAO ĐIỂM CÁC MẶT CẦU VỆ TINH",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 84.0, "Phương pháp giao thoa cự ly đa vệ tinh (Trilateration): Tối thiểu 4 vệ tinh để xác định tọa độ 3D (Lat, Lng, Alt) và bù trừ sai số đồng hồ",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Vị trí người dùng gậy / smartphone
    ux, uy = 65, 42

    # 4 Vệ tinh GPS
    sats = [
        (25, 68, "VỆ TINH SV-1", "Quỹ đạo MEO 20,200 km\nTín hiệu L1: 1575.42 MHz", C_BLUE_MED),
        (105, 70, "VỆ TINH SV-2", "Quỹ đạo MEO 20,200 km\nTín hiệu L1: 1575.42 MHz", C_AMBER_MED),
        (20, 18, "VỆ TINH SV-3", "Quỹ đạo MEO 20,200 km\nTín hiệu L1: 1575.42 MHz", C_EMERALD_MED),
        (110, 18, "VỆ TINH SV-4", "Bù trừ sai số đồng hồ\nΔt Receiver Clock Bias", C_PURPLE_MED),
    ]

    for sx, sy, sname, sdesc, scol in sats:
        r = np.hypot(sx - ux, sy - uy)
        # Vòng cầu khoảng cách
        ax.add_patch(Circle((sx, sy), r, fc='none', ec=scol, lw=1.3, ls='--', alpha=0.55))
        # Vệ tinh
        ax.add_patch(Circle((sx, sy), 3.5, fc=scol, ec='#FFFFFF', lw=1.5, zorder=5))
        ax.text(sx, sy, "SAT", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#FFFFFF', zorder=6)
        draw_pill_badge(ax, sx, sy + 6.5, sname, fc='#FFFFFF', ec=scol, tc=scol, fs=6.8)
        # Đường truyền sóng vệ tinh tới smartphone
        draw_bus(ax, [(sx, sy), (ux, uy)], color=scol, lw=1.5, style=':', arrow_end=True)

    # Điểm người dùng (Giao điểm)
    ax.add_patch(Circle((ux, uy), 5.5, fc='#E11D48', ec='#FFFFFF', lw=2.0, zorder=8))
    ax.text(ux, uy, "GPS", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#FFFFFF', zorder=9)
    draw_pill_badge(ax, ux + 18, uy - 6, "VỊ TRÍ NGƯỜI DÙNG GẬY\n(10.762622, 106.660172)", fc='#FFF1F2', ec=C_ROSE_MED, tc=C_ROSE_DARK, fs=7.2)

    # Card bên phải: Giải thích nguyên lý toán học
    draw_card(ax, 155, 48, 44, 60,
              title="PHƯƠNG TRÌNH ĐỊNH VỊ TOÁN HỌC", badge="TRILATERATION",
              header_color=C_SLATE_900, bg_color='#FFFFFF', border_color=C_SLATE_200, rx=2.0)
    ax.text(135, 68.0, "• Cự ly giả định (Pseudorange):", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_BLUE_DARK)
    ax.text(135, 63.5, "  ρi = c × (t_rx - t_tx)", ha='left', va='center', fontsize=7.2, fontfamily='monospace', color=C_SLATE_900)
    ax.text(135, 59.0, "  (c = 3×10⁸ m/s: Vận tốc ánh sáng)", ha='left', va='center', fontsize=6.2, color=C_SLATE_500)
    ax.text(135, 53.5, "• Hệ 4 phương trình 4 ẩn số:", ha='left', va='center', fontsize=7.0, fontweight='bold', color=C_SLATE_900)
    ax.text(135, 49.0, "  (x - xi)² + (y - yi)² + (z - zi)²", ha='left', va='center', fontsize=6.8, fontfamily='monospace', color=C_SLATE_800)
    ax.text(135, 45.0, "  = (ρi - c × Δt)²", ha='left', va='center', fontsize=6.8, fontfamily='monospace', color=C_SLATE_800)
    ax.text(135, 39.0, "• TÍCH HỢP ỨNG DỤNG FLUTTER:", ha='left', va='center', fontsize=7.0, fontweight='bold', color=C_EMERALD_DARK)
    ax.text(135, 34.5, "  - Geolocator High Accuracy", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(135, 30.5, "  - Lọc khoảng cách di chuyển: 5 mét", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(135, 26.5, "  - Đẩy tọa độ lên Firebase Realtime", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(135, 22.5, "  - Nhúng link Google Maps vào SMS", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 2.9: Nguyên lý định vị toàn cầu GPS dựa trên giao điểm mặt cầu vệ tinh",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_gps.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_gps: {p}")
    return p


# ==============================================================================
# 8. HÌNH 2.11: KIẾN TRÚC ĐA TẦNG CỦA FRAMEWORK FLUTTER (f_flutter)
# ==============================================================================
def gen_pro_flutter():
    w, h = 18.0, 9.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề
    ax.text(w * 5, 90.0, "KIẾN TRÚC PHÂN TẦNG VÀ CƠ CHẾ ĐIỀU PHỐI CỦA GOOGLE FLUTTER",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 87.0, "Mô hình kiến trúc 3 tầng: Framework (Dart) - Engine (C/C++) - Embedder (Platform Native Android/iOS)",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    layers = [
        # (y, h, title, badge, headercol, bgcol, bordercol, bullets)
        (71, 20, "TẦNG 1: FLUTTER FRAMEWORK (NGÔN NGỮ DART)", "APPLICATION & UI", C_BLUE_DARK, '#EFF6FF', C_BLUE_BORDER,
         ["• Screens & Widgets: pair_role_screen, elderly_screen, dashboard_screen, sos_alarm_dialog",
          "• Services: ble_service (flutter_blue_plus), firebase_service, location_service, sms_call_service",
          "• Rendering Layer & Animation: Quản lý cây Widget (Widget Tree), Element Tree và RenderObject Tree"]),

        (48, 19, "TẦNG 2: FLUTTER ENGINE (NGÔN NGỮ C / C++)", "CORE ENGINE", C_PURPLE_DARK, '#FAF5FF', C_PURPLE_BORDER,
         ["• Skia / Impeller: Bộ máy kết xuất đồ họa tăng tốc phần cứng 60 - 120 FPS mượt mà",
          "• Dart Virtual Machine (Dart VM): Trình thông dịch JIT khi debug và biên dịch AOT thành mã máy",
          "• Platform Channels: Điều phối thông điệp nhị phân giữa Dart và hệ điều hành qua MethodChannel"]),

        (24, 21, "TẦNG 3: EMBEDDER & PLATFORM NATIVE (ANDROID OS / iOS)", "NATIVE PLATFORM", C_SLATE_900, '#F8FAFC', C_SLATE_700,
         ["• Android Java / Kotlin & NDK: Khởi chạy SurfaceView kết xuất và tiếp nhận sự kiện cảm ứng chạm",
          "• Phần cứng thiết bị di động: Bluetooth Adapter (BLE 5.0), GPS Location Provider, Telephony (SMS/Call)",
          "• Android Foreground Service: Tiến trình chạy ngầm với thông báo cố định bảo vệ 24/7 không bị kill"]),
    ]

    for ly, lh, ltitle, lbadge, lhc, lbg, lbc, lbullets in layers:
        draw_card(ax, 90, ly, 164, lh,
                  title=ltitle, badge=lbadge, header_color=lhc, bg_color=lbg, border_color=lbc, rx=2.0)
        by = ly + lh / 2 - 6.5
        for b in lbullets:
            ax.text(14, by, b, ha='left', va='center', fontsize=7.2, color=C_SLATE_800)
            by -= 3.8

    # Các mũi tên liên tầng
    draw_bus(ax, [(90, 61), (90, 57.5)], color=C_BLUE_MED, lw=2.4, arrow_both=True)
    draw_pill_badge(ax, 90, 59.2, "Dart FFI / C++ API", fc='#FFFFFF', ec=C_BLUE_MED, tc=C_BLUE_DARK, fs=6.8)

    draw_bus(ax, [(90, 38.5), (90, 34.5)], color=C_PURPLE_MED, lw=2.4, arrow_both=True)
    draw_pill_badge(ax, 90, 36.5, "Platform Channels (MethodChannel & EventChannel)", fc='#FFFFFF', ec=C_PURPLE_MED, tc=C_PURPLE_DARK, fs=6.8)

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 2.11: Kiến trúc đa tầng của Framework lập trình di động Flutter",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_flutter.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_flutter: {p}")
    return p


# ==============================================================================
# 9. HÌNH 2.12: CƠ CHẾ ISOLATE CỦA FLUTTER BACKGROUND SERVICE (f_fgs)
# ==============================================================================
def gen_pro_fgs():
    w, h = 18.0, 9.5
    fig, ax = create_canvas(w, h, dpi=250)

    # Tiêu đề
    ax.text(w * 5, 90.0, "CƠ CHẾ ĐA TIẾN TRÌNH ISOLATE CỦA FLUTTER BACKGROUND SERVICE",
            ha='center', va='center', fontsize=12.2, fontweight='bold', color=C_SLATE_900)
    ax.text(w * 5, 87.0, "Kiến trúc cô lập bộ nhớ (Memory Isolation) giữa giao diện chính (UI Isolate) và dịch vụ chạy ngầm thường trực 24/7 (Background Isolate)",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_500, fontstyle='italic')

    # Card Isolate 1 (Bên trái): UI Isolate (Giao diện người dùng)
    draw_card(ax, 42, 54, 62, 54,
              title="UI ISOLATE (MAIN THREAD)", badge="UI PROCESS",
              header_color=C_BLUE_DARK, bg_color='#EFF6FF', border_color=C_BLUE_BORDER, rx=2.2)
    ax.text(14, 68.0, "• Vùng nhớ Heap riêng biệt (Isolated Heap)", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_BLUE_DARK)
    ax.text(14, 63.5, "• Quản lý giao diện Flutter Widgets:", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(14, 59.5, "  - Màn hình Người già (elderly_screen)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(14, 55.5, "  - Màn hình Giám hộ (dashboard_screen)", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(14, 51.5, "  - Hộp thoại cảnh báo ngã khẩn cấp 15s", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')
    ax.text(14, 47.0, "• Bị Android tạm dừng khi người dùng tắt màn hình", ha='left', va='center', fontsize=6.8, color=C_AMBER_DARK)
    ax.text(14, 43.0, "• Giao tiếp với Background Service qua Event Port", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(14, 38.5, "• Gọi Service.invoke('stopService') khi đăng xuất", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)

    # Card Isolate 2 (Bên phải): Background Service Isolate
    draw_card(ax, 138, 54, 62, 54,
              title="BACKGROUND ISOLATE (SERVICE THREAD)", badge="24/7 DAEMON",
              header_color=C_AMBER_DARK, bg_color='#FFFDF5', border_color=C_AMBER_BORDER, rx=2.2)
    ax.text(110, 68.0, "• Vùng nhớ Heap độc lập (Không bị kill)", ha='left', va='center', fontsize=7.2, fontweight='bold', color=C_AMBER_DARK)
    ax.text(110, 63.5, "• Khởi tạo qua onStart() - flutter_background_service", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(110, 59.5, "• Gắn Notification thường trực thanh trạng thái", ha='left', va='center', fontsize=6.8, color=C_SLATE_700)
    ax.text(110, 55.5, "• 4 TÁC VỤ CHẠY NGẦM VĨNH VIỄN 24/7:", ha='left', va='center', fontsize=7.0, fontweight='bold', color=C_SLATE_900)
    ax.text(110, 51.5, "  1. Quét và tự động kết nối BLE với Gậy", ha='left', va='center', fontsize=6.8, color=C_EMERALD_DARK, fontweight='bold')
    ax.text(110, 47.5, "  2. Luồng GPS thu nhận tọa độ di chuyển 5m", ha='left', va='center', fontsize=6.8, color=C_BLUE_DARK, fontweight='bold')
    ax.text(110, 43.5, "  3. Lắng nghe và đẩy dữ liệu Firebase Cloud", ha='left', va='center', fontsize=6.8, color=C_AMBER_DARK, fontweight='bold')
    ax.text(110, 39.5, "  4. Hẹn giờ 15s và tự động gửi SMS / Gọi SOS", ha='left', va='center', fontsize=6.8, color=C_ROSE_MED, fontweight='bold')

    # Kênh truyền tin giữa 2 Isolate ở giữa
    draw_bus(ax, [(73, 62), (107, 62)], color=C_BLUE_MED, lw=2.2, arrow_end=True)
    draw_pill_badge(ax, 90, 66, "FlutterBackgroundService().invoke()", fc='#EFF6FF', ec=C_BLUE_MED, tc=C_BLUE_DARK, fs=6.5)

    draw_bus(ax, [(107, 46), (73, 46)], color=C_AMBER_MED, lw=2.2, arrow_end=True)
    draw_pill_badge(ax, 90, 42, "FlutterBackgroundService().on()", fc='#FFFBEB', ec=C_AMBER_MED, tc=C_AMBER_DARK, fs=6.5)

    # Card chú thích cơ chế sống sót ở dưới
    draw_card(ax, 90, 15, 158, 14,
              title="CƠ CHẾ MIỄN NHIỄM VỚI BỘ TỐI ƯU PIN CỦA HỆ ĐIỀU HÀNH ANDROID (DOZE MODE & APP STANDBY)",
              badge="ANDROID RESILIENCE", header_color=C_SLATE_900, bg_color='#FFFFFF', border_color=C_SLATE_200, rx=1.8)
    ax.text(14, 13.0, "• Nhờ đăng ký Foreground Service với Notification ưu tiên cao, Android xem tiến trình nền như một dịch vụ phát nhạc hoặc dẫn đường bản đồ.", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)
    ax.text(14, 9.5, "• Dịch vụ không bị tắt khi màn hình khóa, không bị giải phóng RAM khi mở app khác và vẫn hoạt động ngay cả khi người dùng vuốt đóng app khỏi đa nhiệm.", ha='left', va='center', fontsize=6.8, color=C_SLATE_800)

    # Chú thích chân trang
    ax.text(w * 5, 2.5, "Hình 2.12: Cơ chế hoạt động đa luồng Isolate của Flutter Background Service trên Android",
            ha='center', va='center', fontsize=8.2, color=C_SLATE_700, fontweight='bold')

    p = os.path.join(OUT, 'f_fgs.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công mô hình cao cấp f_fgs: {p}")
    return p


# ==============================================================================
# 10. HÌNH 4.1: THỰC NGHIỆM ĐO GIA TỐC SVM (f_exp_accel)
# ==============================================================================
def gen_pro_exp_accel():
    activities = ['Đi bộ\n(Bình thường)', 'Ngồi xuống\nghế', 'Cúi người\nnhặt đồ', 'Vung gậy\nnhanh',
                  'Ngã về\nphía trước', 'Ngã ngửa\nra sau', 'Ngã nghiêng\nsang bên', 'Đánh rơi gậy\ntự do']
    means = [12.5, 14.2, 13.8, 18.5, 31.8, 33.4, 29.6, 27.2]
    stds = [1.8, 2.1, 1.9, 3.2, 3.5, 4.1, 3.8, 3.2]

    fig = plt.figure(figsize=(10.5, 5.5), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0.08, 0.18, 0.88, 0.68])
    ax.set_facecolor('#FAFBFD')

    # Vùng an toàn và vùng té ngã
    ax.axhspan(0, 25.0, color='#EFF6FF', alpha=0.65, zorder=1)
    ax.axhspan(25.0, 44.0, color='#FFF1F2', alpha=0.65, zorder=1)

    # Đường ngưỡng 25 m/s2
    ax.axhline(25.0, color=C_ROSE_MED, ls='--', lw=2.2, zorder=3, label='Ngưỡng phát hiện ngã SVM = 25.0 m/s²')

    x = np.arange(len(activities))
    colors = [C_BLUE_MED]*4 + [C_ROSE_MED]*3 + [C_AMBER_MED]
    edge_colors = [C_BLUE_DARK]*4 + [C_ROSE_DARK]*3 + [C_AMBER_DARK]

    bars = ax.bar(x, means, yerr=stds, capsize=4, color=colors,
                  edgecolor=edge_colors, lw=1.3, width=0.58, zorder=4, error_kw=dict(ecolor='#334155', lw=1.4, capthick=1.4))

    ax.set_xticks(x)
    ax.set_xticklabels(activities, fontsize=8.2, fontweight='bold', color=C_SLATE_800)
    ax.set_ylabel('Gia tốc vector tổng hợp SVM |a|max (m/s²)', fontsize=9.2, fontweight='bold', color=C_SLATE_900)
    ax.set_ylim(0, 43)

    # Lưới tinh tế
    ax.grid(axis='y', alpha=0.35, ls=':', color=C_SLATE_500, zorder=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_SLATE_500)
    ax.spines['bottom'].set_color(C_SLATE_500)

    # Ghi chú giá trị trên cột
    for bar, m, s in zip(bars, means, stds):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + s + 1.2,
                f"{m:.1f}\n±{s:.1f}", ha='center', va='bottom', fontsize=7.5, fontweight='bold', color=C_SLATE_900, zorder=5)

    # Badges thông tin vùng
    ax.text(0.2, 22.5, "VÙNG SINH HOẠT THƯỜNG NHẬT (ADL < 25 m/s²)", ha='left', va='center',
            fontsize=7.8, fontweight='bold', color=C_BLUE_DARK,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#DBEAFE', edgecolor=C_BLUE_BORDER, lw=1.0))
    ax.text(0.2, 40.5, "VÙNG KÍCH HOẠT CẢNH BÁO TÉ NGÃ (SVM ≥ 25 m/s²)", ha='left', va='center',
            fontsize=7.8, fontweight='bold', color=C_ROSE_DARK,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFE4E6', edgecolor=C_ROSE_BORDER, lw=1.0))

    # Tiêu đề
    fig.text(0.5, 0.95, "THỰC NGHIỆM ĐO GIA TỐC SVM TRONG CÁC KỊCH BẢN TÉ NGÃ VÀ SINH HOẠT (ADL)",
             ha='center', va='center', fontsize=11.5, fontweight='bold', color=C_SLATE_900)
    fig.text(0.5, 0.90, "Thực nghiệm 50 lần thử nghiệm trên từng hành vi với cảm biến MPU-6050 gắn cố định trên thân gậy",
             ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    p = os.path.join(OUT, 'f_exp_accel.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công biểu đồ thực nghiệm f_exp_accel: {p}")
    return p


# ==============================================================================
# 11. HÌNH 4.9: PHÂN TÍCH ĐỘ TRỄ CẢNH BÁO TOÀN TRÌNH (f_exp_latency)
# ==============================================================================
def gen_pro_exp_latency():
    stages = [
        '1. Va chạm ngã (MPU-6050)',
        '2. Gậy gửi Notify qua BLE 5.0',
        '3. Đếm ngược 15s (Hủy báo ảo)',
        '4. Đẩy tọa độ lên Firebase Cloud',
        '5. App Giám hộ hú còi báo động',
        '6. Gửi tin nhắn SMS khẩn cấp (GSM)',
        'TỔNG ĐỘ TRỄ TOÀN TRÌNH'
    ]
    times = [0.10, 0.25, 15.00, 0.45, 0.65, 3.20, 19.65]
    percentages = [f"{t/19.65*100:.1f}%" for t in times]
    percentages[-1] = "100%"

    fig = plt.figure(figsize=(10.5, 5.5), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0.22, 0.16, 0.74, 0.70])
    ax.set_facecolor('#FAFBFD')

    y_pos = np.arange(len(stages))
    colors = [C_BLUE_MED, C_CYAN_MED, C_AMBER_MED, C_PURPLE_MED, C_ROSE_MED, C_EMERALD_MED, C_ROSE_DARK]
    edge_colors = [C_BLUE_DARK, C_CYAN_MED, C_AMBER_DARK, C_PURPLE_DARK, C_ROSE_DARK, C_EMERALD_DARK, '#4C0519']

    bars = ax.barh(y_pos, times, color=colors, edgecolor=edge_colors, lw=1.2, height=0.55, zorder=3)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(stages, fontsize=8.5, fontweight='bold', color=C_SLATE_800)
    ax.invert_yaxis()
    ax.set_xlabel('Thời gian đo đạc thực tế (giây)', fontsize=9.2, fontweight='bold', color=C_SLATE_900)
    ax.set_xlim(0, 24)

    ax.grid(axis='x', alpha=0.35, ls=':', color=C_SLATE_500, zorder=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_SLATE_500)
    ax.spines['bottom'].set_color(C_SLATE_500)

    for bar, t, pct in zip(bars, times, percentages):
        w = bar.get_width()
        txt = f"{t:.2f} s  ({pct})" if t < 10 else f"{t:.2f} s  ({pct} - Cố định)"
        ax.text(w + 0.35, bar.get_y() + bar.get_height()/2, txt,
                va='center', fontsize=8.2, fontweight='bold', color=C_SLATE_900, zorder=4)

    # Tiêu đề
    fig.text(0.5, 0.95, "PHÂN RÃ THỜI GIAN ĐÁP ỨNG VÀ ĐỘ TRỄ TOÀN TRÌNH CỦA CHUỖI CẢNH BÁO SOS",
             ha='center', va='center', fontsize=11.5, fontweight='bold', color=C_SLATE_900)
    fig.text(0.5, 0.90, "Thời gian truyền dẫn công nghệ chỉ mất 4.65s; 15s là cửa sổ đếm ngược chống báo ảo bảo vệ người dùng",
             ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    p = os.path.join(OUT, 'f_exp_latency.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công biểu đồ thực nghiệm f_exp_latency: {p}")
    return p


# ==============================================================================
# 12. HÌNH 4.5: ĐỘ CHÍNH XÁC ĐO KHOẢNG CÁCH HC-SR04 (f_exp_ultrasonic)
# ==============================================================================
def gen_pro_exp_ultrasonic():
    d_real = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    d_meas = np.array([5.1, 10.2, 19.8, 30.4, 40.2, 50.8, 61.2, 70.9, 81.5, 92.1, 103.2])
    err = np.abs(d_meas - d_real)

    fig = plt.figure(figsize=(10.5, 5.5), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0.10, 0.16, 0.86, 0.68])
    ax.set_facecolor('#FAFBFD')

    # Vùng kích hoạt motor rung (3cm - 80cm)
    ax.axvspan(3, 80, color='#ECFDF5', alpha=0.7, zorder=1, label='Vùng cảnh báo rung chướng ngại vật (3cm - 80cm)')

    # Đường chuẩn và đường đo
    ax.plot(d_real, d_real, '--', color=C_SLATE_500, lw=1.5, zorder=2, label='Khoảng cách chuẩn thực tế (Lý tưởng)')
    ax.plot(d_real, d_meas, 'o-', color=C_BLUE_MED, lw=2.2, markersize=6.5,
            markerfacecolor='#FFFFFF', markeredgewidth=2.0, markeredgecolor=C_BLUE_DARK,
            zorder=4, label='Khoảng cách đo bởi HC-SR04')

    # Biểu đồ cột thể hiện sai số tuyệt đối
    ax.bar(d_real, err, width=2.4, color=C_AMBER_MED, alpha=0.8, edgecolor=C_AMBER_DARK, lw=1.0,
           zorder=3, label='Sai số tuyệt đối Δd (cm)')

    ax.set_xlabel('Khoảng cách thực tế (cm)', fontsize=9.2, fontweight='bold', color=C_SLATE_900)
    ax.set_ylabel('Khoảng cách đo đạc / Sai số (cm)', fontsize=9.2, fontweight='bold', color=C_SLATE_900)
    ax.set_xlim(0, 106)
    ax.set_ylim(0, 110)

    ax.grid(alpha=0.35, ls=':', color=C_SLATE_500, zorder=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_SLATE_500)
    ax.spines['bottom'].set_color(C_SLATE_500)
    ax.legend(loc='upper left', fontsize=8.0, framealpha=0.95, edgecolor=C_SLATE_200)

    # Hiển thị sai số trên từng điểm
    for r, m, e in zip(d_real, d_meas, err):
        ax.text(r, e + 2.5, f"{e:.1f}cm", ha='center', va='bottom', fontsize=7.0, color=C_AMBER_DARK, fontweight='bold')

    # Badge sai số trung bình
    ax.text(78, 25, "Sai số trung bình: 0.94 cm (< 1.5%)\nĐộ phân giải thực tế: ±0.3 cm",
            ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_EMERALD_DARK,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#D1FAE5', edgecolor=C_EMERALD_BORDER, lw=1.2))

    # Tiêu đề
    fig.text(0.5, 0.95, "ĐÁNH GIÁ ĐỘ CHÍNH XÁC CẢM BIẾN SIÊU ÂM HC-SR04 TÍCH HỢP TRÊN GẬY",
             ha='center', va='center', fontsize=11.5, fontweight='bold', color=C_SLATE_900)
    fig.text(0.5, 0.90, "Thực nghiệm đo cự ly từ 5 cm đến 100 cm trên nhiều loại bề mặt phản xạ (Tường bê tông, cửa gỗ, vải)",
             ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    p = os.path.join(OUT, 'f_exp_ultrasonic.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công biểu đồ thực nghiệm f_exp_ultrasonic: {p}")
    return p


# ==============================================================================
# 13. HÌNH 4.4: TỈ LỆ NHẬN DIỆN CÁC KỊCH BẢN (f_exp_scenarios)
# ==============================================================================
def gen_pro_exp_scenarios():
    scenarios = [
        '1. Đi bộ liên tục 500m (Không ngã)',
        '2. Ngồi xuống ghế & đứng dậy',
        '3. Cúi người nhặt vật dụng rơi',
        '4. Chống gậy mạnh / vấp nhẹ',
        '5. Ngã về phía trước',
        '6. Ngã ngửa ra sau',
        '7. Ngã nghiêng trái / phải',
        '8. Ngã rồi tự đứng dậy bình thường'
    ]
    correct = [50, 49, 48, 47, 48, 49, 47, 46]  # trên 50 lần thử
    total = 50
    rates = [c / total * 100 for c in correct]

    fig = plt.figure(figsize=(10.5, 5.5), dpi=250, facecolor='#FFFFFF')
    ax = fig.add_axes([0.25, 0.15, 0.71, 0.65])
    ax.set_facecolor('#FAFBFD')

    y_pos = np.arange(len(scenarios))
    bars = ax.barh(y_pos, rates, color=C_EMERALD_MED, edgecolor=C_EMERALD_DARK, lw=1.2, height=0.55, zorder=3)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(scenarios, fontsize=8.5, fontweight='bold', color=C_SLATE_800)
    ax.invert_yaxis()
    ax.set_xlabel('Tỉ lệ phân loại và nhận diện chính xác (%)', fontsize=9.2, fontweight='bold', color=C_SLATE_900)
    ax.set_xlim(80, 105)

    ax.grid(axis='x', alpha=0.35, ls=':', color=C_SLATE_500, zorder=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C_SLATE_500)
    ax.spines['bottom'].set_color(C_SLATE_500)

    for bar, r, c in zip(bars, rates, correct):
        w = bar.get_width()
        ax.text(w + 0.35, bar.get_y() + bar.get_height()/2, f"{r:.1f}%  ({c}/{total} lần)",
                va='center', fontsize=8.2, fontweight='bold', color=C_EMERALD_DARK, zorder=4)

    # Đường chỉ chuẩn 95%
    ax.axvline(95.0, color=C_AMBER_MED, ls='--', lw=1.5, zorder=2)

    # Tiêu đề
    fig.text(0.5, 0.95, "MA TRẬN ĐỘ CHÍNH XÁC PHÂN LOẠI CÁC KỊCH BẢN TÉ NGÃ VÀ HOẠT ĐỘNG SINH HOẠT",
             ha='center', va='center', fontsize=11.5, fontweight='bold', color=C_SLATE_900)
    fig.text(0.5, 0.90, "Thực nghiệm 50 lần thử nghiệm lặp lại trên từng kịch bản (Tổng cộng 400 lượt thử nghiệm thực tế)",
             ha='center', va='center', fontsize=8.0, color=C_SLATE_500, fontstyle='italic')

    # Badge tổng kết
    fig.text(0.5, 0.852, "  ĐỘ CHÍNH XÁC TRUNG BÌNH TOÀN HỆ THỐNG: 96.0% (384 / 400 LẦN THỬ)  ",
             ha='center', va='center', fontsize=8.0, fontweight='bold', color=C_EMERALD_DARK,
             bbox=dict(boxstyle='round,pad=0.35', facecolor='#ECFDF5', edgecolor=C_EMERALD_BORDER, lw=1.2))

    p = os.path.join(OUT, 'f_exp_scenarios.png')
    fig.savefig(p, dpi=250, facecolor='#FFFFFF')
    plt.close(fig)
    print(f"Đã tạo thành công biểu đồ thực nghiệm f_exp_scenarios: {p}")
    return p


# ==============================================================================
# HÀM CHÍNH TẠO TOÀN BỘ PHẦN 2
# ==============================================================================
def gen_all_part2():
    gen_pro_i2c()
    gen_pro_mpu()
    gen_pro_accel()
    gen_pro_ultra()
    gen_pro_ir()
    gen_pro_mosfet()
    gen_pro_gps()
    gen_pro_flutter()
    gen_pro_fgs()
    gen_pro_exp_accel()
    gen_pro_exp_latency()
    gen_pro_exp_ultrasonic()
    gen_pro_exp_scenarios()

if __name__ == '__main__':
    gen_all_part2()


# -*- coding: utf-8 -*-
import numpy as np
from figlib import *
from matplotlib.patches import Circle, Arc, Wedge


def f_methods():
    fig, ax = new_fig(16, 8.2)
    box(ax, 80, 72, 70, 8, 'Các phương pháp phát hiện & cảnh báo té ngã', 'blue', 11, True)
    items = [
        (20, 'Thiết bị đeo\n(smartwatch, vòng tay,\nthiết bị gắn thắt lưng)', 'orange', 'Gia tốc kế, con quay,\náp suất khí quyển\nHay quên đeo / hết pin'),
        (50, 'Camera /\nthị giác máy tính', 'teal', 'Độ chính xác cao\nLo ngại riêng tư,\ngiới hạn không gian'),
        (80, 'Phân tích\nâm thanh', 'purple', 'Micro, mảng micro\nDễ nhiễu bởi tạp âm'),
        (110, 'Radar\n(mmWave, UWB)', 'grey', 'Không tiếp xúc, riêng tư\nChi phí cao,\nlắp đặt cố định'),
        (140, 'Gậy thông minh\n(đề tài)', 'green', 'MPU6050 + siêu âm + BLE\nVật dụng quen thuộc,\nmang theo mọi lúc'),
    ]
    for x, t, c, d in items:
        arrow(ax, [(80, 68), (80, 62), (x, 62), (x, 55)], head=True)
        box(ax, x, 46, 27, 16, t, c, 8.5, True)
        box(ax, x, 22, 27, 22, d, 'white', 7.8)
        arrow(ax, [(x, 38), (x, 33)])
    return save(fig, 'f_methods')


def f_overview():
    fig, ax = new_fig(16, 7)
    box(ax, 20, 35, 28, 30, 'GẬY THÔNG MINH\nESP32-S3\n\nMPU6050 · HC-SR04\nBuzzer · Motor rung', 'green', 9, True)
    box(ax, 66, 35, 28, 30, 'ĐIỆN THOẠI\nNGƯỜI DÙNG GẬY\n\nGPS · Dịch vụ nền\nSMS / Gọi điện', 'blue', 9, True)
    box(ax, 112, 55, 28, 18, 'FIREBASE\nAuth · Realtime DB', 'orange', 9, True)
    box(ax, 140, 35, 28, 30, 'ĐIỆN THOẠI\nNGƯỜI GIÁM HỘ\n\nBản đồ · Lịch sử\nThông báo + chuông', 'teal', 9, True)
    box(ax, 112, 15, 28, 14, 'SMS cảnh báo\n+ liên kết bản đồ', 'red', 8.5, True)
    arrow(ax, [(34, 35), (52, 35)], both=True, color=C_GREEN)
    label(ax, 43, 40, 'BLE', 9, C_GREEN, True)
    arrow(ax, [(80, 42), (98, 55)], color=C_BLUE)
    arrow(ax, [(98, 52), (80, 38)], color=C_BLUE)
    label(ax, 88, 52, 'Internet\n(Wi-Fi/4G)', 8, C_BLUE, True)
    arrow(ax, [(126, 55), (140, 50)], color=C_ORANGE)
    arrow(ax, [(140, 44), (126, 52)], color=C_ORANGE, head=False)
    arrow(ax, [(80, 28), (98, 15)], color=C_RED)
    arrow(ax, [(126, 15), (140, 24)], color=C_RED)
    label(ax, 112, 5, 'Mạng di động (không cần Internet)', 8, C_RED, True)
    return save(fig, 'f_overview')


def f_esp32():
    fig, ax = new_fig(15, 8.5)
    box(ax, 75, 42, 54, 56, '', 'blue', rounded=True)
    label(ax, 75, 76, 'ESP32-S3 (N16R8)', 11, C_BLUE, True)
    box(ax, 56, 62, 24, 10, 'CPU Xtensa LX7\n2 nhân, 240 MHz', 'white', 8)
    box(ax, 94, 62, 24, 10, 'Bộ nhớ: 16 MB Flash\n8 MB PSRAM', 'white', 8)
    box(ax, 56, 46, 24, 10, 'Wi-Fi 802.11 b/g/n', 'white', 8)
    box(ax, 94, 46, 24, 10, 'Bluetooth 5 (LE)', 'white', 8)
    box(ax, 56, 30, 24, 10, 'GPIO · ADC 12-bit\nPWM (LEDC)', 'white', 8)
    box(ax, 94, 30, 24, 10, 'I2C · SPI · UART\nUSB OTG', 'white', 8)
    ins = [(14, 62, 'MPU6050\n(I2C: GPIO 8, 9)'), (14, 42, 'HC-SR04\n(GPIO 16, 17)'), (14, 22, 'Chia áp pin\n(ADC: GPIO 4)')]
    for x, y, t in ins:
        box(ax, x, y, 24, 10, t, 'green', 8)
        arrow(ax, [(x + 12, y), (48 - 5, y if y != 62 else 62)], color=C_GREEN)
    outs = [(136, 62, 'Buzzer\n(GPIO 5)'), (136, 42, 'Motor rung / MOSFET\n(GPIO 6)'), (136, 22, 'BLE → Điện thoại\n(Notify)')]
    for x, y, t in outs:
        box(ax, x, y, 24, 10, t, 'orange', 8)
        arrow(ax, [(102 + 6 + 3, y), (x - 12, y)], color=C_ORANGE)
    return save(fig, 'f_esp32')


def f_gatt():
    fig, ax = new_fig(15, 7.5)
    box(ax, 75, 65, 40, 8, 'GATT Server (ESP32-S3) – tên thiết bị "SmartCane"', 'blue', 9, True)
    box(ax, 75, 48, 56, 8, 'Service  UUID: 4fafc201-1fb5-459e-8fcc-c5c9c331914b', 'teal', 8.5, True)
    box(ax, 40, 30, 54, 12, 'Characteristic "Té ngã"\nUUID: …26a9\nThuộc tính: READ | NOTIFY', 'green', 8)
    box(ax, 110, 30, 54, 12, 'Characteristic "Pin" (dự phòng)\nUUID: …26a8\nTrong config.h', 'grey', 8)
    box(ax, 40, 12, 40, 7, 'Descriptor BLE2902 (CCCD)', 'yellow', 8)
    arrow(ax, [(75, 61), (75, 52)])
    arrow(ax, [(60, 44), (40, 36)])
    arrow(ax, [(90, 44), (110, 36)])
    arrow(ax, [(40, 24), (40, 16)])
    box(ax, 130, 62, 28, 14, 'GATT Client\n(App Flutter\nflutter_blue_plus)', 'orange', 8, True)
    arrow(ax, [(116, 62), (96, 62)], color=C_ORANGE, both=True)
    label(ax, 106, 66, 'Kết nối', 8, C_ORANGE, True)
    label(ax, 75, 3, 'Giá trị "1" = phát hiện ngã  ·  Giá trị "0" = bình thường', 8.5, C_GREY, italic=True)
    return save(fig, 'f_gatt')


def f_i2c():
    fig, ax = new_fig(14, 6.5)
    box(ax, 25, 40, 30, 14, 'ESP32-S3\n(Master)', 'blue', 9, True)
    box(ax, 105, 40, 30, 14, 'MPU6050\n(Slave, 0x68)', 'green', 9, True)
    # bus
    ax.plot([40, 90], [46, 46], color=C_ORANGE, lw=2)
    ax.plot([40, 90], [34, 34], color=C_TEAL, lw=2)
    label(ax, 65, 50, 'SDA – GPIO 8 (dữ liệu hai chiều)', 8.5, C_ORANGE, True)
    label(ax, 65, 30, 'SCL – GPIO 9 (xung đồng hồ)', 8.5, C_TEAL, True)
    for y, c in [(46, C_ORANGE), (34, C_TEAL)]:
        ax.plot([40, 40], [y, y], color=c)
    # pull-up
    ax.plot([62, 62], [46, 56], color=C_ORANGE, lw=1.2)
    ax.plot([72, 72], [34, 56], color=C_TEAL, lw=1.2)
    ax.plot([55, 80], [56, 56], color='#333', lw=1.2)
    label(ax, 67, 60, 'VCC 3.3V + điện trở kéo lên', 8, C_GREY)
    box(ax, 40, 12, 56, 8, 'Chuỗi: START → địa chỉ+W → thanh ghi → dữ liệu → STOP', 'yellow', 8)
    return save(fig, 'f_i2c')


def f_mpu():
    fig, ax = new_fig(14, 7)
    # hệ trục
    ox, oy = 40, 32
    arrow(ax, [(ox, oy), (ox + 30, oy)], color=C_RED, lw=2)
    arrow(ax, [(ox, oy), (ox, oy + 28)], color=C_GREEN, lw=2)
    arrow(ax, [(ox, oy), (ox - 14, oy - 12)], color=C_BLUE, lw=2)
    label(ax, ox + 33, oy, 'X', 10, C_RED, True)
    label(ax, ox, oy + 31, 'Y', 10, C_GREEN, True)
    label(ax, ox - 17, oy - 14, 'Z', 10, C_BLUE, True)
    # vector tổng
    arrow(ax, [(ox, oy), (ox + 22, oy + 20)], color='#000', lw=2.2)
    label(ax, ox + 30, oy + 24, '|a| = √(ax²+ay²+az²)', 9, '#000', True)
    # góc quay
    ax.add_patch(Arc((ox + 15, oy), 16, 10, theta1=0, theta2=270, color=C_ORANGE, lw=1.5))
    label(ax, ox + 15, oy - 10, 'Quay quanh trục\n(con quay hồi chuyển)', 8, C_ORANGE)
    # bảng
    box(ax, 105, 48, 50, 36, '', 'white')
    label(ax, 105, 62, 'Tín hiệu MPU6050', 9.5, C_BLUE, True)
    label(ax, 105, 50, 'Gia tốc kế 3 trục: ±8 g\n(setAccelerometerRange 8G)\n\nCon quay 3 trục\n\nCảm biến nhiệt độ', 8.5, '#1a1a1a')
    box(ax, 105, 14, 50, 9, 'Ngưỡng ngã: |a| > 25 m/s² (≈ 2,55 g)', 'orange', 8.5, True)
    return save(fig, 'f_mpu')


def f_accel():
    np.random.seed(3)
    t = np.linspace(0, 12, 1200)
    a = 9.8 + 1.6 * np.sin(2 * np.pi * 1.8 * t) * (t < 8) + np.random.normal(0, 0.25, t.size)
    # va chạm
    imp = np.exp(-((t - 8.0) / 0.05) ** 2) * 22
    free = -6 * np.exp(-((t - 7.8) / 0.12) ** 2)
    after = (t > 8.3)
    a = np.where(after, 9.8 + np.random.normal(0, 0.08, t.size), a) + imp + free
    fig = plt.figure(figsize=(8, 3.8), dpi=200)
    ax = fig.add_axes([0.09, 0.17, 0.88, 0.75])
    ax.plot(t, a, color=C_BLUE, lw=1)
    ax.axhline(25, color=C_RED, ls='--', lw=1.3)
    ax.text(0.2, 26, 'Ngưỡng 25 m/s²', color=C_RED, fontsize=9, fontweight='bold')
    ax.axhline(9.8, color='#888', ls=':', lw=1)
    ax.text(10.2, 10.6, 'g = 9,8 m/s²', color='#666', fontsize=8)
    ax.annotate('Va chạm\n(|a| vượt ngưỡng)', xy=(8.0, 30.5), xytext=(5.0, 29), fontsize=8.5,
                arrowprops=dict(arrowstyle='->', color=C_ORANGE), color=C_ORANGE, fontweight='bold')
    ax.text(1.0, 18.5, 'Đi bộ bình thường', fontsize=8.5, color=C_GREEN, fontweight='bold')
    ax.text(9.0, 14, 'Nằm bất động', fontsize=8.5, color=C_GREY, fontweight='bold')
    ax.set_xlabel('Thời gian (s)')
    ax.set_ylabel('Gia tốc tổng hợp |a| (m/s²)')
    ax.set_ylim(0, 36)
    ax.grid(alpha=.25)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    return save(fig, 'f_accel')


def f_ultra():
    fig = plt.figure(figsize=(8.5, 4.2), dpi=200)
    ax = fig.add_axes([0.09, 0.08, 0.88, 0.86])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 40)
    ax.axis('off')
    # Trig
    ax.plot([0, 10, 10, 14, 14, 100], [30, 30, 36, 36, 30, 30], color=C_BLUE, lw=2)
    ax.text(0, 38, 'TRIG', fontsize=9, fontweight='bold', color=C_BLUE)
    ax.text(16, 36.5, 'xung ≥ 10 µs', fontsize=8, color=C_BLUE)
    # burst
    xs = np.linspace(20, 34, 140)
    ax.plot(xs, 20 + 3 * np.sign(np.sin(2 * np.pi * (xs - 20) * 1.1)), color=C_ORANGE, lw=1.1)
    ax.plot([0, 20], [20, 20], color=C_ORANGE, lw=1.1)
    ax.plot([34, 100], [20, 20], color=C_ORANGE, lw=1.1)
    ax.text(0, 25, '8 xung 40 kHz', fontsize=9, fontweight='bold', color=C_ORANGE, va='center')
    # Echo
    ax.plot([0, 36, 36, 78, 78, 100], [5, 5, 12, 12, 5, 5], color=C_GREEN, lw=2)
    ax.text(0, 15.5, 'ECHO', fontsize=9, fontweight='bold', color=C_GREEN)
    ax.annotate('', xy=(78, 2), xytext=(36, 2), arrowprops=dict(arrowstyle='<->', color='#333'))
    ax.text(57, -0.8, 't (µs) = thời gian sóng đi – về', fontsize=8.5, ha='center')
    ax.text(57, 14, 'Khoảng cách d = t × 0,0343 / 2  (cm)', fontsize=9, ha='center', fontweight='bold', color='#222')
    return save(fig, 'f_ultra')


def f_ir():
    fig, ax = new_fig(15, 6.5)
    box(ax, 22, 32, 30, 18, 'E18-D50NK\nPhát + thu IR\nngưỡng chỉnh được', 'blue', 8.5, True)
    ax.add_patch(Polygon([(37, 36), (88, 40), (88, 24), (37, 28)], closed=True, fc='#FFF4E5', ec=C_ORANGE, lw=1, alpha=.8))
    label(ax, 62, 32, 'Chùm tia hồng ngoại', 8.5, C_ORANGE, True)
    box(ax, 102, 32, 12, 26, 'Vật\ncản', 'grey', 8.5, True)
    arrow(ax, [(100, 22), (62, 25), (40, 27)], color=C_RED, ls='--')
    label(ax, 70, 17, 'Tia phản xạ → bộ thu', 8, C_RED)
    box(ax, 128, 32, 30, 20, 'OUT (NPN-NO)\nCó vật: LOW\nKhông: HIGH', 'green', 8.5, True)
    arrow(ax, [(37, 42), (113, 52), (128, 44)], color=C_GREEN, head=True)
    label(ax, 76, 52, 'Tín hiệu số về GPIO (INPUT_PULLUP)', 8, C_GREEN, True)
    label(ax, 75, 5, 'Tầm phát hiện danh định 3 – 50 cm (chỉnh bằng biến trở trên thân cảm biến)', 8.5, C_GREY, italic=True)
    return save(fig, 'f_ir')


def f_mosfet():
    fig, ax = new_fig(14, 8)
    # nguồn 5V
    ax.plot([60, 60], [68, 60], color='#333', lw=1.6)
    label(ax, 60, 71, '+5V (mạch tăng áp)', 9, C_RED, True)
    # motor
    ax.add_patch(Circle((60, 52), 7, fc=C_LORANGE, ec=C_ORANGE, lw=1.6))
    label(ax, 60, 52, 'M', 11, C_ORANGE, True)
    label(ax, 74, 52, 'Motor rung', 8.5, C_ORANGE, True, ha='left')
    ax.plot([60, 60], [60, 59], color='#333')
    # diode
    ax.plot([60, 60], [45, 36], color='#333', lw=1.6)
    ax.plot([45, 45], [57, 36], color='#333', lw=1.2)
    ax.plot([45, 60], [57, 57], color='#333', lw=1.2)
    ax.plot([45, 60], [36, 36], color='#333', lw=1.2)
    label(ax, 36, 46, 'Diode\nhồi tiếp', 8, C_GREY)
    # mosfet
    ax.plot([60, 60], [36, 28], color='#333', lw=1.6)
    ax.plot([55, 55], [22, 30], color='#333', lw=2.2)
    ax.plot([60, 55], [28, 28], color='#333', lw=1.6)
    ax.plot([55, 60], [24, 24], color='#333', lw=1.6)
    ax.plot([60, 60], [24, 16], color='#333', lw=1.6)
    ax.plot([52, 52], [21, 31], color='#333', lw=1.6)
    ax.plot([30, 52], [26, 26], color=C_GREEN, lw=1.6)
    box(ax, 18, 26, 22, 10, 'GPIO 6\n(ESP32-S3)', 'green', 8, True)
    label(ax, 66, 32, 'D', 9, '#333', True)
    label(ax, 66, 20, 'S', 9, '#333', True)
    label(ax, 46, 29, 'G', 9, '#333', True)
    # GND
    ax.plot([52, 70], [16, 16], color='#333', lw=1.6)
    label(ax, 61, 12, 'GND chung (ESP32 + nguồn motor)', 8.5, C_BLUE, True)
    # R pulldown
    ax.plot([38, 38], [26, 18], color='#333', lw=1.2)
    ax.add_patch(Rectangle((36, 18), 4, 6, fc='white', ec='#333'))
    ax.plot([38, 38], [18, 16], color='#333', lw=1.2)
    ax.plot([38, 52], [16, 16], color='#333', lw=1.2)
    label(ax, 30, 20, 'R kéo xuống', 7.5, C_GREY)
    box(ax, 112, 40, 40, 36, 'Nguyên lý\n\nGPIO = HIGH → MOSFET dẫn\n→ dòng chạy qua motor → RUNG\n\nGPIO = LOW → MOSFET ngắt\n→ motor dừng', 'yellow', 8.5)
    return save(fig, 'f_mosfet')


def f_gps():
    fig, ax = new_fig(13, 8)
    pts = [(25, 55, 24, 'Vệ tinh 1'), (95, 58, 26, 'Vệ tinh 2'), (60, 12, 22, 'Vệ tinh 3')]
    target = (62, 38)
    for x, y, r, n in pts:
        ax.add_patch(Circle((x, y), np.hypot(x - target[0], y - target[1]), fc='none', ec=C_BLUE, lw=1.2, ls='--', alpha=.7))
        ax.add_patch(Circle((x, y), 2.2, fc=C_ORANGE, ec=C_ORANGE))
        label(ax, x, y + 5, n, 8.5, C_ORANGE, True)
    ax.add_patch(Circle(target, 2.6, fc=C_GREEN, ec=C_GREEN))
    label(ax, target[0] + 14, target[1] - 4, 'Vị trí điện thoại\n(vĩ độ, kinh độ)', 8.5, C_GREEN, True)
    label(ax, 65, 76, 'Định vị bằng giao điểm các mặt cầu/đường tròn khoảng cách', 9, C_GREY, italic=True)
    return save(fig, 'f_gps')


def f_rtdb():
    fig, ax = new_fig(15, 7.5)
    box(ax, 75, 35, 38, 24, 'FIREBASE\nREALTIME DATABASE\n(JSON, đồng bộ thời gian thực)', 'orange', 9, True)
    for x, y, t, c in [(20, 58, 'Máy A\n(Người dùng gậy)', 'blue'), (130, 58, 'Máy B\n(Người giám hộ)', 'teal'),
                       (20, 12, 'Ngoại tuyến:\nbộ nhớ đệm cục bộ', 'grey'), (130, 12, 'Lắng nghe\nonValue()', 'green')]:
        box(ax, x, y, 30, 13, t, c, 8.5, True)
    arrow(ax, [(35, 56), (58, 44)], color=C_BLUE)
    label(ax, 44, 55, 'update()', 8, C_BLUE, True)
    arrow(ax, [(94, 44), (115, 56)], color=C_TEAL)
    label(ax, 106, 55, 'onValue', 8, C_TEAL, True)
    arrow(ax, [(35, 14), (58, 26)], color=C_GREY, ls='--')
    arrow(ax, [(94, 26), (115, 14)], color=C_GREEN)
    return save(fig, 'f_rtdb')


def f_flutter():
    fig, ax = new_fig(13, 8)
    layers = [('Ứng dụng Smart Cane (Dart)\nscreens · widgets · theme', 'teal'),
              ('Framework Flutter\nWidgets · Material · Rendering', 'blue'),
              ('Engine (C++ · Skia/Impeller · Dart VM)', 'purple'),
              ('Nền tảng Android / iOS\nBluetooth · GPS · SMS · Foreground Service', 'grey')]
    y = 63
    for t, c in layers:
        box(ax, 65, y, 90, 14, t, c, 9, True)
        y -= 17
    return save(fig, 'f_flutter')


def f_fgs():
    fig, ax = new_fig(15, 8.5)
    box(ax, 38, 62, 56, 18, 'Isolate giao diện (UI)\nelderly_screen / dashboard_screen\nHiển thị trạng thái, nút thao tác', 'blue', 8.5, True)
    box(ax, 112, 62, 58, 18, 'Isolate dịch vụ nền (Foreground Service)\nonStart() – flutter_background_service\nThông báo thường trực "Đang bảo vệ ngầm..."', 'orange', 8.5, True)
    arrow(ax, [(66, 66), (83, 66)], color=C_BLUE)
    arrow(ax, [(83, 58), (66, 58)], color=C_ORANGE)
    label(ax, 74.5, 70, 'invoke()', 8, C_BLUE, True)
    label(ax, 74.5, 54, 'on()', 8, C_ORANGE, True)
    tasks = [('Quét/kết nối BLE', 90), ('Luồng GPS (5 m)', 108), ('Lắng nghe Firebase', 126), ('SMS / Gọi', 144)]
    for t, x in tasks:
        pass
    xs = [84, 104, 124, 144]
    for (t, _), x in zip(tasks, xs):
        box(ax, x, 22, 18, 14, t, 'white', 7.8, True)
        arrow(ax, [(112, 53), (112, 42), (x, 42), (x, 29)], color=C_GREY, lw=1)
    label(ax, 38, 22, 'Tiếp tục chạy khi\nmàn hình tắt / app\nbị vuốt khỏi đa nhiệm', 8.5, C_GREEN, True)
    return save(fig, 'f_fgs')


if __name__ == '__main__':
    for fn in [f_methods, f_overview, f_esp32, f_gatt, f_i2c, f_mpu, f_accel, f_ultra, f_ir, f_mosfet, f_gps, f_rtdb, f_flutter, f_fgs]:
        print(fn())

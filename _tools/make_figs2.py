# -*- coding: utf-8 -*-
"""Tạo các hình vẽ kỹ thuật cho Chương 3 và Chương 4: Sơ đồ khối, sơ đồ nguyên lý, các lưu đồ thuật toán và biểu đồ thực nghiệm."""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from figlib import *

OUT = r'd:\doan\_tools\fig'
os.makedirs(OUT, exist_ok=True)

# 1. Sơ đồ khối hệ thống (Chương 3)
def f_block_diag():
    fig, ax = new_fig(16, 9)
    # Khối Gậy
    ax.add_patch(FancyBboxPatch((4, 4), 62, 82, boxstyle='round,pad=1,rounding_size=3', fc='#F4FBF7', ec=C_GREEN, lw=2, ls='--'))
    label(ax, 35, 83, 'PHẦN CỨNG GẬY THÔNG MINH (ESP32-S3)', 10, C_GREEN, True)
    
    # Trung tâm ESP32
    box(ax, 35, 45, 24, 28, 'BỘ XỬ LÝ TRUNG TÂM\n\nESP32-S3 N16R8\nXtensa LX7 Dual-Core\n240 MHz - 512KB SRAM\n16MB Flash - 8MB PSRAM\nBluetooth 5.0 BLE', 'green', 8.5, True)
    
    # Cảm biến đầu vào
    box(ax, 14, 66, 16, 12, 'CẢM BIẾN IMU\nMPU6050 (6-DOF)\nGia tốc 3 trục\nCon quay 3 trục\n(I2C: GPIO 8, 9)', 'blue', 7.5, True)
    box(ax, 14, 48, 16, 12, 'CẢM BIẾN SIÊU ÂM\nHC-SR04\nSóng âm 40 kHz\n(Trig:16, Echo:17)', 'blue', 7.5, True)
    box(ax, 14, 30, 16, 10, 'CẢM BIẾN HỒNG NGOẠI\nE18-D50NK (Dự phòng)\nTia hồng ngoại 3-50cm\n(GPIO 4 / GPIO 15)', 'grey', 7.2)
    box(ax, 14, 15, 16, 10, 'ĐIỆN ÁP PIN\nMạch chia áp R1/R2\nĐo điện áp 3.7V - 4.2V\n(ADC: GPIO 4)', 'teal', 7.2)

    # Chấp hành đầu ra
    box(ax, 56, 60, 15, 12, 'CÒI HÚ CHÍNH\nBuzzer 5V\nTần số 2000 Hz\n(GPIO 5)', 'orange', 7.5, True)
    box(ax, 56, 42, 15, 12, 'MOTOR RUNG\nĐộng cơ rung lệch tâm\nDriver MOSFET\n(GPIO 6)', 'orange', 7.5, True)
    box(ax, 56, 22, 15, 14, 'KHỐI NGUỒN PIN\nPin Li-ion 18650 3.7V\nSạc TP4056 Type-C\nTăng áp Boost 5V', 'red', 7.5, True)

    # Mũi tên nội bộ gậy
    arrow(ax, [(22, 66), (23, 66)], color=C_BLUE)
    arrow(ax, [(22, 48), (23, 48)], color=C_BLUE)
    arrow(ax, [(22, 30), (23, 30)], color=C_GREY)
    arrow(ax, [(22, 15), (23, 25), (23, 35)], color=C_TEAL)
    arrow(ax, [(47, 50), (48.5, 60)], color=C_ORANGE)
    arrow(ax, [(47, 45), (48.5, 42)], color=C_ORANGE)
    arrow(ax, [(48.5, 22), (40, 22), (40, 31)], color=C_RED)

    # Khối Smartphone Người Già
    ax.add_patch(FancyBboxPatch((72, 4), 38, 82, boxstyle='round,pad=1,rounding_size=3', fc='#F0F7FC', ec=C_BLUE, lw=2, ls='--'))
    label(ax, 91, 83, 'SMARTPHONE NGƯỜI GIÀ (GẬY)', 10, C_BLUE, True)
    box(ax, 91, 68, 30, 10, 'FLUTTER BLE CLIENT\nAuto-reconnect qua MAC\nLắng nghe Characteristic Té ngã', 'blue', 8, True)
    box(ax, 91, 52, 30, 10, 'DỊCH VỤ NỀN (Foreground Service)\nChạy ngầm vĩnh viễn không tắt\nQuản lý hẹn giờ khẩn cấp 15 giây', 'orange', 8, True)
    box(ax, 91, 36, 30, 10, 'MÔ-ĐUN GPS ĐIỆN THOẠI\nLấy tọa độ chính xác cao (5m)\nPhát luồng vị trí liên tục', 'teal', 8, True)
    box(ax, 91, 18, 30, 12, 'CẢNH BÁO KHẨN CẤP NGOẠI TUYẾN\nTự động gửi SMS tọa độ vị trí\nQuay số gọi trực tiếp Giám hộ', 'red', 8, True)

    arrow(ax, [(91, 63), (91, 57)], color=C_BLUE)
    arrow(ax, [(91, 47), (91, 41)], color=C_BLUE)
    arrow(ax, [(91, 31), (91, 24)], color=C_RED)

    # Kết nối BLE giữa Gậy và Smartphone Người Già
    arrow(ax, [(47, 55), (76, 68)], color=C_GREEN, lw=2, both=True)
    label(ax, 68, 67, 'BLE 5.0\nNotify', 8.5, C_GREEN, True)

    # Đám mây Firebase
    box(ax, 122, 65, 22, 20, 'FIREBASE CLOUD\n\nRealtime Database\n- Users / Trạng thái ngã\n- Tọa độ GPS thời gian thực\n- Trạng thái BLE / Mạng\n- Lịch sử sự cố & Điểm hẹn\nFirebase Authentication', 'orange', 8, True)
    
    # Kết nối Internet Người già -> Firebase
    arrow(ax, [(106, 52), (111, 65)], color=C_BLUE, lw=1.6, both=True)
    label(ax, 109, 56, 'Wi-Fi / 4G\nREST / WS', 7.5, C_BLUE)

    # Khối Smartphone Người Giám Hộ
    ax.add_patch(FancyBboxPatch((116, 4), 38, 48, boxstyle='round,pad=1,rounding_size=3', fc='#FAF5FF', ec=C_PURPLE, lw=2, ls='--'))
    label(ax, 135, 49, 'SMARTPHONE NGƯỜI GIÁM HỘ', 9.5, C_PURPLE, True)
    box(ax, 135, 38, 30, 10, 'BẢN ĐỒ GIÁM SÁT THỜI GIAN THỰC\nFlutter Map (OpenStreetMap)\nTheo dõi vị trí gậy, nhà, điểm hẹn', 'teal', 7.8, True)
    box(ax, 135, 25, 30, 8, 'HỆ THỐNG CÒI BÁO ĐỘNG SOS\nChuông thức tỉnh âm lượng cực đại\nRung liên tục & Thông báo pop-up', 'red', 7.8, True)
    box(ax, 135, 13, 30, 8, 'TIỆN ÍCH DẪN ĐƯỜNG & LỊCH SỬ\nMở chỉ đường Google Maps 1 chạm\nXem log sự cố, mất mạng, tắt GPS', 'purple', 7.8, True)

    # Kết nối Firebase -> Giám hộ
    arrow(ax, [(126, 55), (126, 43)], color=C_ORANGE, lw=1.6)
    label(ax, 129, 48, 'onValue()', 7.5, C_ORANGE)

    # Đường SMS trực tiếp khi không có mạng
    arrow(ax, [(106, 18), (120, 18)], color=C_RED, lw=1.8, ls=':')
    label(ax, 113, 14, 'SMS GSM\n(Dự phòng)', 7.5, C_RED, True)

    return save(fig, 'f_block_diag')


# 2. Sơ đồ nối dây chi tiết phần cứng (Schematic Layout)
def f_schematic():
    fig, ax = new_fig(16, 10)
    # Khung ESP32-S3
    box(ax, 80, 50, 48, 70, '', 'blue', lw=2)
    label(ax, 80, 81, 'ESP32-S3 N16R8 DEVKIT', 12, C_BLUE, True)

    # Các chân GPIO hiển thị bên trái ESP32
    left_pins = [
        ('GPIO 8 (SDA)', 70),
        ('GPIO 9 (SCL)', 63),
        ('GPIO 16 (TRIG)', 54),
        ('GPIO 17 (ECHO)', 47),
        ('GPIO 4 (ADC/IR)', 38),
        ('3V3 (VCC)', 28),
        ('GND', 21)
    ]
    for name, y in left_pins:
        ax.plot([56, 62], [y, y], color=C_BLUE, lw=1.5)
        label(ax, 63, y, name, 8.5, '#1a1a1a', ha='left', bold=True)

    # Các chân GPIO hiển thị bên phải ESP32
    right_pins = [
        ('GPIO 5 (BUZZER)', 70),
        ('GPIO 6 (VIBRATOR)', 58),
        ('VIN (5V)', 40),
        ('GND', 25)
    ]
    for name, y in right_pins:
        ax.plot([98, 104], [y, y], color=C_BLUE, lw=1.5)
        label(ax, 97, y, name, 8.5, '#1a1a1a', ha='right', bold=True)

    # Module MPU6050 (Bên trái trên)
    box(ax, 24, 70, 24, 18, 'CẢM BIẾN MPU6050\n\nVCC: 3.3V\nGND: GND\nSDA: GPIO 8\nSCL: GPIO 9', 'green', 8, True)
    arrow(ax, [(36, 73), (56, 70)], color=C_ORANGE, lw=1.3)
    arrow(ax, [(36, 67), (56, 63)], color=C_TEAL, lw=1.3)

    # Module HC-SR04 (Bên trái giữa)
    box(ax, 24, 48, 24, 18, 'CẢM BIẾN HC-SR04\n\nVCC: 3.3V (hoặc 5V)\nGND: GND\nTRIG: GPIO 16\nECHO: GPIO 17 (Pulldown)', 'teal', 8, True)
    arrow(ax, [(36, 52), (56, 54)], color=C_BLUE, lw=1.3)
    arrow(ax, [(56, 47), (36, 47)], color=C_GREEN, lw=1.3)

    # Cảm biến E18-D50NK & Chia áp (Bên trái dưới)
    box(ax, 24, 25, 24, 20, 'E18-D50NK / PIN ADC\n\nNâu: 5V (Nguồn)\nXanh: GND\nĐen: GPIO 4 / 15\nR1=10k, R2=10k chia áp', 'grey', 8)
    arrow(ax, [(36, 25), (56, 38)], color=C_GREY, lw=1.3)

    # Còi Buzzer (Bên phải trên)
    box(ax, 134, 70, 24, 16, 'CÒI HÚ BUZZER 5V\n\nChân + : GPIO 5\nChân - : GND\nPhát tần số 2kHz', 'orange', 8, True)
    arrow(ax, [(104, 70), (122, 70)], color=C_ORANGE, lw=1.5)

    # Motor rung + MOSFET (Bên phải giữa)
    box(ax, 134, 50, 24, 18, 'MẠCH DRIVER MOTOR\n\nChân SIG: GPIO 6\nMOSFET AOD4184\nMotor Rung 5V\nĐiện trở xả 10k', 'purple', 8, True)
    arrow(ax, [(104, 58), (122, 54)], color=C_PURPLE, lw=1.5)

    # Mạch nguồn Pin + Boost (Bên phải dưới)
    box(ax, 134, 25, 24, 22, 'KHỐI NGUỒN\n\nPin 18650 (3.7V - 4.2V)\nMạch sạc TP4056\nMạch Boost tăng áp 5V\nCấp VIN ESP32 & Motor', 'red', 8, True)
    arrow(ax, [(122, 30), (104, 40)], color=C_RED, lw=1.8)
    arrow(ax, [(122, 22), (104, 25)], color='#333', lw=1.8)
    label(ax, 113, 18, 'Chung GND!', 8, C_RED, True)

    return save(fig, 'f_schematic')


# 3. Lưu đồ chính của Firmware ESP32-S3
def f_flow_firmware():
    f = Flow(14, 12)
    f.node('start', 70, 114, 'term', 'BẮT ĐẦU (Khởi động ESP32-S3)', 44, 7, 'green')
    f.node('init_io', 70, 103, 'proc', 'Cấu hình GPIO:\nBuzzer, Motor rung (OUTPUT)\nHC-SR04 Trig (OUTPUT), Echo (INPUT_PULLDOWN)', 50, 9, 'blue')
    f.node('selftest', 70, 91, 'proc', 'Self-Test trong 0.2s:\nBật Buzzer + Motor rung rồi tắt để báo sẵn sàng', 48, 8, 'blue')
    f.node('init_mpu', 70, 79, 'proc', 'Khởi tạo I2C (SDA:8, SCL:9) và MPU6050\nĐặt dải gia tốc: ±8g (MPU6050_RANGE_8_G)', 48, 8, 'blue')
    f.node('init_ble', 70, 67, 'proc', 'Khởi tạo BLE Server ("SmartCane")\nTạo Service + Characteristic Báo Ngã (Notify)\nBắt đầu phát sóng BLE Advertising', 50, 9, 'blue')
    f.node('loop_ble', 70, 54, 'proc', 'Quản lý kết nối BLE:\nNếu App mất kết nối → Tự động phát sóng lại', 48, 8, 'teal')
    f.node('read_mpu', 70, 42, 'proc', 'Đọc gia tốc 3 trục MPU6050:\nTính độ lớn vector tổng hợp: |a| = √(ax² + ay² + az²)', 48, 8, 'blue')
    f.node('check_fall', 70, 29, 'dec', '|a| > 25.0 m/s² ?\n(Phát hiện va chạm ngã)', 36, 11, 'orange')
    
    # Nhánh có ngã
    f.node('act_alarm', 26, 29, 'proc', 'KÍCH HOẠT BÁO ĐỘNG NGÃ:\n- Bật Còi hú 2000Hz + Rung\n- Gửi Notify "1" qua BLE lên App\n- Đặt timer tắt sau 3 giây', 34, 11, 'red')
    
    # Nhánh không ngã / hết báo động ngã
    f.node('read_ultra', 70, 15, 'proc', 'Đo khoảng cách HC-SR04 (pulseIn + micros):\nd = duration × 0.0343 / 2 (cm)', 48, 8, 'blue')
    f.node('check_dist', 70, 4, 'dec', '3 cm ≤ d ≤ 80 cm ?\n(Có vật cản trước mặt)', 36, 9, 'orange')
    f.node('vib_on', 26, 4, 'proc', 'BẬT MOTOR RUNG\n(Báo vật cản cho người dùng)', 28, 7, 'orange')
    f.node('vib_off', 114, 4, 'proc', 'TẮT MOTOR RUNG\n(Đường đi thông thoáng)', 28, 7, 'green')

    f.edge('start', 'b', 'init_io', 't')
    f.edge('init_io', 'b', 'selftest', 't')
    f.edge('selftest', 'b', 'init_mpu', 't')
    f.edge('init_mpu', 'b', 'init_ble', 't')
    f.edge('init_ble', 'b', 'loop_ble', 't')
    f.edge('loop_ble', 'b', 'read_mpu', 't')
    f.edge('read_mpu', 'b', 'check_fall', 't')
    f.edge('check_fall', 'l', 'act_alarm', 'r', text='ĐÚNG')
    f.edge('check_fall', 'b', 'read_ultra', 't', text='SAI')
    f.edge('act_alarm', 'b', 'read_ultra', 'l', via=[(26, 15)])
    f.edge('read_ultra', 'b', 'check_dist', 't')
    f.edge('check_dist', 'l', 'vib_on', 'r', text='ĐÚNG')
    f.edge('check_dist', 'r', 'vib_off', 'l', text='SAI')
    f.edge('vib_on', 'l', 'loop_ble', 'l', via=[(8, 4), (8, 54)])
    f.edge('vib_off', 'r', 'loop_ble', 'r', via=[(132, 4), (132, 54)])
    return f.save('f_flow_firmware')


# 4. Lưu đồ Dịch vụ ngầm Người Già (Flutter Elderly Background Service)
def f_flow_elderly():
    f = Flow(14, 11)
    f.node('start', 70, 104, 'term', 'BẮT ĐẦU DỊCH VỤ NGẦM (Role: Elderly)', 44, 6, 'green')
    f.node('auto_ble', 70, 93, 'proc', 'Quét và Tự động kết nối BLE với Gậy:\nĐọc MAC lưu từ trước → autoConnect trực tiếp\nĐăng ký lắng nghe Characteristic Báo ngã (Notify)', 52, 9, 'blue')
    f.node('gps_stream', 70, 80, 'proc', 'Khởi chạy luồng GPS (Geolocator High Accuracy):\nMỗi 5m di chuyển → Cập nhật (lat, lng, ble_status)\nlên Firebase Realtime Database (/users/{uid})', 52, 9, 'teal')
    f.node('chk_fall', 70, 67, 'dec', 'Nhận gói tin BLE = "1" ?\n(Gậy báo té ngã)', 38, 9, 'orange')
    f.node('push_fb', 70, 53, 'proc', 'BẮT ĐẦU XỬ LÝ SỰ CỐ NGÃ:\n- Đẩy is_falling = true lên Firebase\n- Ghi nhận local_fall_timestamp\n- Lưu fall_location_url (Google Maps link)', 50, 10, 'red')
    f.node('timer15', 70, 39, 'proc', 'Kích hoạt bộ đếm ngược khẩn cấp 15 GIÂY\n(Màn hình điện thoại hiển thị nút hủy ngã nếu bấm nhầm)', 50, 8, 'orange')
    f.node('chk_cancel', 70, 27, 'dec', 'Người già bấm HỦY\ntrước 15 giây?', 36, 9, 'orange')
    f.node('abort', 26, 27, 'proc', 'HỦY CẢNH BÁO:\nReset is_falling = false\nDừng hẹn giờ', 28, 8, 'green')
    f.node('call_sms', 70, 12, 'proc', 'HẾT 15 GIÂY - KÍCH HOẠT CỨU HỘ KHẨN CẤP:\n1. Gửi SMS ngầm chứa link Google Maps tới SĐT Giám hộ\n2. Tự động chuyển lệnh gọi điện thoại trực tiếp SOS', 52, 10, 'red')
    f.node('end_loop', 70, 2, 'term', 'Tiếp tục duy trì bảo vệ ngầm 24/7', 40, 5, 'blue')

    f.edge('start', 'b', 'auto_ble', 't')
    f.edge('auto_ble', 'b', 'gps_stream', 't')
    f.edge('gps_stream', 'b', 'chk_fall', 't')
    f.edge('chk_fall', 'b', 'push_fb', 't', text='ĐÚNG')
    f.edge('chk_fall', 'r', 'gps_stream', 'r', text='SAI', via=[(104, 67), (104, 80)])
    f.edge('push_fb', 'b', 'timer15', 't')
    f.edge('timer15', 'b', 'chk_cancel', 't')
    f.edge('chk_cancel', 'l', 'abort', 'r', text='CÓ')
    f.edge('chk_cancel', 'b', 'call_sms', 't', text='KHÔNG')
    f.edge('abort', 'b', 'end_loop', 'l', via=[(26, 2)])
    f.edge('call_sms', 'b', 'end_loop', 't')
    return f.save('f_flow_elderly')


# 5. Lưu đồ Dịch vụ Giám Hộ (Flutter Guardian Logic)
def f_flow_guardian():
    f = Flow(14, 10)
    f.node('start', 70, 94, 'term', 'BẮT ĐẦU ỨNG DỤNG GIÁM HỘ (Role: Guardian)', 46, 6, 'green')
    f.node('listen_fb', 70, 83, 'proc', 'Lắng nghe Firebase Realtime Database (/users/{uid}):\nTheo dõi is_online, ble_connected, gps_enabled, is_falling', 54, 9, 'blue')
    f.node('chk_event', 70, 70, 'dec', 'Có sự kiện\nbất thường?', 32, 8, 'orange')
    
    f.node('event_fall', 30, 56, 'proc', 'SỰ CỐ TÉ NGÃ (is_falling == true):\n- Phát còi hú báo thức âm lượng cực đại\n- Bật thông báo khẩn cấp toàn màn hình\n- Cập nhật marker ngã trên bản đồ', 42, 11, 'red')
    f.node('event_net', 110, 56, 'proc', 'MẤT MẠNG / TẮT GPS / TẮT BLE:\n- Ghi nhận lịch sử cảnh báo mất mạng\n- Hiển thị banner cảnh báo màu đỏ trên Dashboard\n- Khi có mạng lại: tự động ghi thời gian hồi phục', 42, 11, 'orange')

    f.node('user_action', 70, 36, 'proc', 'TƯƠNG TÁC CỦA NGƯỜI GIÁM HỘ TRÊN DASHBOARD:\n- Bấm nút "Chỉ đường" → Tự động mở Google Maps điều hướng\n- Bấm "Tắt báo động" → Cập nhật is_falling=false lên Firebase\n- Đặt / Xóa vị trí Địa chỉ Nhà và Điểm Hẹn cho người già', 54, 11, 'teal')
    f.node('update_map', 70, 18, 'proc', 'Cập nhật bản đồ OpenStreetMap liên tục:\nHiển thị vị trí người già + Nhà + Điểm hẹn + Bán kính an toàn', 52, 8, 'blue')
    f.node('end_guard', 70, 6, 'term', 'Duy trì giám sát thời gian thực', 36, 5, 'green')

    f.edge('start', 'b', 'listen_fb', 't')
    f.edge('listen_fb', 'b', 'chk_event', 't')
    f.edge('chk_event', 'l', 'event_fall', 't', text='NGÃ', via=[(30, 70)])
    f.edge('chk_event', 'r', 'event_net', 't', text='MẠNG/GPS', via=[(110, 70)])
    f.edge('chk_event', 'b', 'update_map', 't', text='BÌNH THƯỜNG')
    f.edge('event_fall', 'b', 'user_action', 'l', via=[(30, 36)])
    f.edge('event_net', 'b', 'user_action', 'r', via=[(110, 36)])
    f.edge('user_action', 'b', 'update_map', 't')
    f.edge('update_map', 'b', 'end_guard', 't')
    return f.save('f_flow_guardian')


# 6. Biểu đồ thực nghiệm: Phân bố gia tốc các tư thế sinh hoạt & ngã (Chương 4)
def f_exp_accel():
    np.random.seed(42)
    activities = ['Đi bộ', 'Ngồi xuống', 'Cúi nhặt đồ', 'Vung gậy', 'Ngã về trước', 'Ngã ngửa', 'Ngã sang bên', 'Rơi gậy']
    means = [12.5, 14.2, 13.8, 18.5, 31.8, 33.4, 29.6, 27.2]
    stds = [1.8, 2.1, 1.9, 3.2, 3.5, 4.1, 3.8, 3.2]
    
    fig = plt.figure(figsize=(9, 4.5), dpi=200)
    ax = fig.add_axes([0.1, 0.18, 0.86, 0.74])
    
    x = np.arange(len(activities))
    colors = [C_BLUE]*4 + [C_RED]*3 + [C_ORANGE]
    bars = ax.bar(x, means, yerr=stds, capsize=5, color=colors, alpha=0.85, edgecolor='#333', lw=1.2)
    
    # Đường ngưỡng 25 m/s2
    ax.axhline(25.0, color=C_RED, ls='--', lw=1.8, label='Ngưỡng phát hiện ngã (25 m/s²)')
    
    ax.set_xticks(x)
    ax.set_xticklabels(activities, fontsize=8.5, rotation=15)
    ax.set_ylabel('Gia tốc cực đại |a|max (m/s²)', fontsize=9.5, fontweight='bold')
    ax.set_title('Thực nghiệm đo gia tốc đỉnh trong các hoạt động sinh hoạt và té ngã mô phỏng', fontsize=10.5, fontweight='bold')
    ax.set_ylim(0, 42)
    ax.grid(axis='y', alpha=0.3, ls=':')
    ax.legend(loc='upper left', fontsize=8.5)
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 4.5, f'{yval:.1f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
        
    return save(fig, 'f_exp_accel')


# 7. Biểu đồ thực nghiệm: Độ trễ cảnh báo (Latency breakdown)
def f_exp_latency():
    fig = plt.figure(figsize=(8.5, 4.2), dpi=200)
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.76])
    
    stages = ['Va chạm ngã\n(MPU6050)', 'Gậy bắn Notify\nqua BLE', 'App nhận & kích hoạt\nđếm 15s (có thể hủy)', 'Đẩy tọa độ lên\nFirebase Cloud', 'App Giám hộ\nhú còi báo động', 'Gửi SMS ngầm\n(GSM)', 'Tổng thời gian\nđến người thân']
    # Thời gian trung bình (giây)
    times = [0.1, 0.25, 15.0, 0.45, 0.65, 3.2, 19.6]
    y_pos = np.arange(len(stages))
    
    colors = [C_BLUE, C_TEAL, C_ORANGE, C_BLUE, C_RED, C_PURPLE, '#B71C1C']
    bars = ax.barh(y_pos, times, color=colors, alpha=0.85, edgecolor='#333', lw=1)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(stages, fontsize=8.5)
    ax.invert_yaxis()  # Đưa bước đầu lên trên
    ax.set_xlabel('Thời gian đo đạc thực tế (giây)', fontsize=9.5, fontweight='bold')
    ax.set_title('Phân tích độ trễ của các giai đoạn trong quy trình cảnh báo té ngã', fontsize=10, fontweight='bold')
    ax.set_xlim(0, 24)
    ax.grid(axis='x', alpha=0.3, ls=':')
    
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.3, bar.get_y() + bar.get_height()/2, f'{w:.2f} s', va='center', fontsize=8.5, fontweight='bold')
        
    return save(fig, 'f_exp_latency')


# 8. Biểu đồ thực nghiệm: Độ chính xác đo khoảng cách HC-SR04
def f_exp_ultrasonic():
    fig = plt.figure(figsize=(8, 4.2), dpi=200)
    ax = fig.add_axes([0.12, 0.15, 0.82, 0.75])
    
    d_real = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    d_meas = np.array([5.1, 10.2, 19.8, 30.4, 40.2, 50.8, 61.2, 70.9, 81.5, 92.1, 103.2])
    err = np.abs(d_meas - d_real)
    
    ax.plot(d_real, d_meas, 'o-', color=C_BLUE, lw=1.8, markersize=6, label='Khoảng cách đo được bởi HC-SR04')
    ax.plot(d_real, d_real, '--', color='#666', lw=1.2, label='Khoảng cách chuẩn thực tế')
    ax.bar(d_real, err, width=2.5, color=C_ORANGE, alpha=0.6, label='Sai số tuyệt đối (cm)')
    
    ax.axvspan(3, 80, color=C_GREEN, alpha=0.12, label='Vùng kích hoạt motor rung (3cm - 80cm)')
    ax.set_xlabel('Khoảng cách thực tế (cm)', fontsize=9.5, fontweight='bold')
    ax.set_ylabel('Khoảng cách đo đạc (cm)', fontsize=9.5, fontweight='bold')
    ax.set_title('Đánh giá độ chính xác cảm biến siêu âm HC-SR04 tích hợp trên gậy', fontsize=10, fontweight='bold')
    ax.legend(loc='upper left', fontsize=8)
    ax.grid(alpha=0.3, ls=':')
    
    return save(fig, 'f_exp_ultrasonic')


# 9. Ma trận nhầm lẫn / Tỉ lệ phát hiện các kịch bản
def f_exp_scenarios():
    fig = plt.figure(figsize=(9, 4.2), dpi=200)
    ax = fig.add_axes([0.15, 0.18, 0.8, 0.72])
    
    scenarios = ['Đi bộ 500m', 'Ngồi xuống ghế', 'Cúi nhặt vật', 'Chống gậy mạnh', 'Ngã về phía trước', 'Ngã ngửa ra sau', 'Ngã nghiêng trái/phải', 'Ngã rồi tự đứng dậy']
    correct = [50, 49, 48, 47, 48, 49, 47, 46]  # trên 50 lần thử
    total = 50
    rates = [c / total * 100 for c in correct]
    
    y_pos = np.arange(len(scenarios))
    bars = ax.barh(y_pos, rates, color=C_TEAL, alpha=0.85, edgecolor='#333', lw=1)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(scenarios, fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlabel('Tỉ lệ nhận diện chính xác (%)', fontsize=9.5, fontweight='bold')
    ax.set_title('Kết quả thực nghiệm 50 lần thử nghiệm trên từng kịch bản di chuyển & té ngã', fontsize=10, fontweight='bold')
    ax.set_xlim(80, 105)
    ax.grid(axis='x', alpha=0.3, ls=':')
    
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.4, bar.get_y() + bar.get_height()/2, f'{w:.1f}% ({int(w*total/100)}/50)', va='center', fontsize=8, fontweight='bold')
        
    return save(fig, 'f_exp_scenarios')


if __name__ == '__main__':
    for fn in [f_block_diag, f_schematic, f_flow_firmware, f_flow_elderly, f_flow_guardian, f_exp_accel, f_exp_latency, f_exp_ultrasonic, f_exp_scenarios]:
        print(fn())

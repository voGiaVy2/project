# -*- coding: utf-8 -*-
"""Vẽ các màn hình giao diện ứng dụng Flutter Smart Cane cực kỳ chi tiết, chuẩn thiết kế Dark Theme của app."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
from figlib import new_fig, save, label, box, C_GREEN, C_RED, C_BLUE, C_ORANGE, C_GREY

OUT = r'd:\doan\_tools\fig'
os.makedirs(OUT, exist_ok=True)

# Khung điện thoại chuẩn tỉ lệ 9:18.5
def draw_phone_frame(ax, ox, oy, w, h, title=""):
    # Viền máy
    ax.add_patch(FancyBboxPatch((ox, oy), w, h, boxstyle='round,pad=0,rounding_size=4', fc='#1E1E1E', ec='#333333', lw=2.5))
    # Màn hình trong
    mw, mh = w - 2.5, h - 5
    mx, my = ox + 1.25, oy + 2.5
    ax.add_patch(FancyBboxPatch((mx, my), mw, mh, boxstyle='round,pad=0,rounding_size=2.5', fc='#121212', ec='none'))
    # Tai thỏ / camera nốt ruồi
    ax.add_patch(Circle((ox + w/2, oy + h - 1.8), 0.7, fc='#000000', ec='#222'))
    # Loa thoại
    ax.add_patch(FancyBboxPatch((ox + w/2 - 2, oy + h - 1), 4, 0.4, boxstyle='round,pad=0,rounding_size=0.2', fc='#333'))
    # Status bar
    label(ax, mx + 3.5, oy + h - 3.8, '09:41', 6.5, '#AAA', bold=True)
    label(ax, mx + mw - 4, oy + h - 3.8, '5G  100%', 6.5, '#AAA', bold=True)
    # App Bar
    ax.add_patch(Rectangle((mx, my + mh - 6.5), mw, 6.5, fc='#1A1A1A', ec='none'))
    label(ax, ox + w/2, my + mh - 3.5, title, 8, 'white', bold=True)
    return mx, my, mw, mh - 6.5

# 1. Màn hình chọn vai trò & Ghép nối (RoleSelectionScreen)
def f_ui_role():
    fig, ax = new_fig(15, 10)
    
    # Máy 1: Đăng nhập
    mx, my, mw, mh = draw_phone_frame(ax, 15, 5, 42, 88, 'ĐĂNG NHẬP / TẠO TÀI KHOẢN')
    ax.add_patch(Circle((mx + mw/2, my + mh - 14), 6, fc='#1E1E1E', ec=C_GREEN, lw=1.5))
    label(ax, mx + mw/2, my + mh - 14, '🦯', 16)
    label(ax, mx + mw/2, my + mh - 24, 'GẬY THÔNG MINH', 10, 'white', bold=True)
    label(ax, mx + mw/2, my + mh - 28, 'Bảo vệ an toàn cho người cao tuổi', 7, '#888')
    
    # Input Email
    ax.add_patch(FancyBboxPatch((mx + 4, my + mh - 42), mw - 8, 7, boxstyle='round,pad=0,rounding_size=1.5', fc='#1E1E1E', ec='#333'))
    label(ax, mx + 7, my + mh - 38.5, 'Email: giavylyson@gmail.com', 7, '#DDD', ha='left')
    # Input Pass
    ax.add_patch(FancyBboxPatch((mx + 4, my + mh - 52), mw - 8, 7, boxstyle='round,pad=0,rounding_size=1.5', fc='#1E1E1E', ec='#333'))
    label(ax, mx + 7, my + mh - 48.5, 'Mật khẩu: ••••••••••••', 7, '#DDD', ha='left')
    # Button Login
    ax.add_patch(FancyBboxPatch((mx + 4, my + mh - 64), mw - 8, 8, boxstyle='round,pad=0,rounding_size=2', fc=C_GREEN, ec='none'))
    label(ax, mx + mw/2, my + mh - 60, 'ĐĂNG NHẬP', 8.5, 'white', bold=True)
    label(ax, mx + mw/2, my + mh - 72, 'Quên mật khẩu?  |  Tạo tài khoản mới', 7, C_BLUE)

    # Máy 2: Ghép nối 2 thiết bị
    mx2, my2, mw2, mh2 = draw_phone_frame(ax, 75, 5, 42, 88, 'GHÉP NỐI THIẾT BỊ')
    label(ax, mx2 + mw2/2, my2 + mh2 - 8, 'HỆ THỐNG ĐỒNG BỘ 2 MÁY', 8.5, 'white', bold=True)
    label(ax, mx2 + mw2/2, my2 + mh2 - 13, 'Mỗi tài khoản kết nối đúng 1 máy Người Già & 1 máy Giám Hộ', 6.5, '#AAA')

    # Card 1: Người giám hộ
    ax.add_patch(FancyBboxPatch((mx2 + 4, my2 + mh2 - 38), mw2 - 8, 22, boxstyle='round,pad=0,rounding_size=2', fc='#1E1E1E', ec=C_BLUE, lw=1.5))
    label(ax, mx2 + 8, my2 + mh2 - 21, '🛡️  NGƯỜI GIÁM HỘ', 8.5, C_BLUE, bold=True, ha='left')
    label(ax, mx2 + 8, my2 + mh2 - 27, 'Theo dõi vị trí, lịch sử, nhận còi báo\nvà tự động mở chỉ đường Google Maps', 6.8, '#CCC', ha='left')
    ax.add_patch(FancyBboxPatch((mx2 + mw2 - 16, my2 + mh2 - 35), 10, 5, boxstyle='round,pad=0,rounding_size=1', fc=C_BLUE, ec='none'))
    label(ax, mx2 + mw2 - 11, my2 + mh2 - 32.5, 'CHỌN', 7, 'white', bold=True)

    # Card 2: Người dùng gậy
    ax.add_patch(FancyBboxPatch((mx2 + 4, my2 + mh2 - 64), mw2 - 8, 22, boxstyle='round,pad=0,rounding_size=2', fc='#1E1E1E', ec=C_GREEN, lw=1.5))
    label(ax, mx2 + 8, my2 + mh2 - 47, '👴  NGƯỜI DÙNG GẬY', 8.5, C_GREEN, bold=True, ha='left')
    label(ax, mx2 + 8, my2 + mh2 - 53, 'Tự động kết nối Bluetooth với Gậy,\nphát GPS liên tục và tự gọi điện/SMS SOS', 6.8, '#CCC', ha='left')
    ax.add_patch(FancyBboxPatch((mx2 + mw2 - 16, my2 + mh2 - 61), 10, 5, boxstyle='round,pad=0,rounding_size=1', fc=C_GREEN, ec='none'))
    label(ax, mx2 + mw2 - 11, my2 + mh2 - 58.5, 'CHỌN', 7, 'white', bold=True)

    label(ax, mx2 + mw2/2, my2 + mh2 - 73, 'Trạng thái: Đang chờ thiết bị thứ 2 đăng nhập...', 7, '#FFB300', italic=True)

    return save(fig, 'f_ui_role')


# 2. Màn hình Người Dùng Gậy (ElderlyScreen) - Bình thường & Báo ngã 15s
def f_ui_elderly():
    fig, ax = new_fig(15, 10)
    
    # Máy 1: Trạng thái bình thường
    mx, my, mw, mh = draw_phone_frame(ax, 15, 5, 42, 88, 'CHẾ ĐỘ NGƯỜI DÙNG GẬY')
    
    # Thanh trạng thái kết nối
    ax.add_patch(FancyBboxPatch((mx + 3, my + mh - 12), mw - 6, 10, boxstyle='round,pad=0,rounding_size=1.5', fc='#1E1E1E', ec='#333'))
    label(ax, mx + 5, my + mh - 6, '🔵 Bluetooth: Gậy đã kết nối (SmartCane)', 6.8, C_GREEN, ha='left', bold=True)
    label(ax, mx + 5, my + mh - 10, '🛰️ GPS: Đang phát vị trí thời gian thực', 6.8, C_BLUE, ha='left')

    # Khu vực bản đồ giả lập
    ax.add_patch(Rectangle((mx + 3, my + mh - 54), mw - 6, 40, fc='#1A262F', ec='#2A3D4D'))
    # Đường đi mô phỏng
    ax.plot([mx + 10, mx + 20, mx + 24, mx + 34], [my + mh - 48, my + mh - 38, my + mh - 30, my + mh - 22], color='#3498DB', lw=2)
    # Marker hiện tại
    ax.add_patch(Circle((mx + 24, my + mh - 30), 2.5, fc=C_BLUE, ec='white', lw=1.5))
    label(ax, mx + 24, my + mh - 25, 'Vị trí của bạn', 6.5, 'white', bold=True)
    # Marker Nhà
    ax.add_patch(Circle((mx + 34, my + mh - 22), 2.5, fc=C_GREEN, ec='white', lw=1.5))
    label(ax, mx + 34, my + mh - 18, 'Nhà', 6.5, C_GREEN, bold=True)

    # 2 Nút lớn Về nhà & Điểm hẹn
    ax.add_patch(FancyBboxPatch((mx + 4, my + mh - 66), (mw - 10)/2, 9, boxstyle='round,pad=0,rounding_size=2', fc=C_GREEN, ec='none'))
    label(ax, mx + 4 + (mw - 10)/4, my + mh - 61.5, '🏠 VỀ NHÀ', 7.5, 'white', bold=True)

    ax.add_patch(FancyBboxPatch((mx + 6 + (mw - 10)/2, my + mh - 66), (mw - 10)/2, 9, boxstyle='round,pad=0,rounding_size=2', fc=C_BLUE, ec='none'))
    label(ax, mx + 6 + 3*(mw - 10)/4, my + mh - 61.5, '📍 ĐIỂM HẸN', 7.5, 'white', bold=True)

    # Nút SOS thủ công
    ax.add_patch(FancyBboxPatch((mx + 4, my + mh - 76), mw - 8, 8, boxstyle='round,pad=0,rounding_size=2', fc=C_RED, ec='none'))
    label(ax, mx + mw/2, my + mh - 72, '🚨 GỌI KHẨN CẤP (SOS)', 8, 'white', bold=True)

    # Máy 2: Trạng thái PHÁT HIỆN TÉ NGÃ (Đếm ngược 15s)
    mx2, my2, mw2, mh2 = draw_phone_frame(ax, 75, 5, 42, 88, 'CẢNH BÁO TÉ NGÃ !')
    
    # Nền cảnh báo đỏ
    ax.add_patch(Rectangle((mx2, my2), mw2, mh2, fc='#330A0A', ec='none'))
    
    # Biểu tượng cảnh báo lớn
    ax.add_patch(Circle((mx2 + mw2/2, my2 + mh2 - 20), 12, fc=C_RED, ec='white', lw=2))
    label(ax, mx2 + mw2/2, my2 + mh2 - 20, '⚠️', 20)
    label(ax, mx2 + mw2/2, my2 + mh2 - 36, 'ĐÃ PHÁT HIỆN TÉ NGÃ!', 10, 'white', bold=True)
    label(ax, mx2 + mw2/2, my2 + mh2 - 42, 'Hệ thống chuẩn bị gọi cho người thân sau:', 7.5, '#FFCDD2')

    # Bộ đếm 15 giây
    ax.add_patch(Circle((mx2 + mw2/2, my2 + mh2 - 52), 6, fc='#5A1212', ec=C_RED, lw=1.5))
    label(ax, mx2 + mw2/2, my2 + mh2 - 52, '12s', 10, 'white', bold=True)

    # Nút HỦY nếu không sao
    ax.add_patch(FancyBboxPatch((mx2 + 5, my2 + mh2 - 67), mw2 - 10, 10, boxstyle='round,pad=0,rounding_size=2.5', fc='#2E7D32', ec='white', lw=1.5))
    label(ax, mx2 + mw2/2, my2 + mh2 - 62, 'TÔI ỔN - HỦY BÁO ĐỘNG', 8.5, 'white', bold=True)

    label(ax, mx2 + mw2/2, my2 + mh2 - 74, 'Nếu không bấm hủy, hệ thống sẽ tự động\ngửi tin nhắn SMS tọa độ và gọi khẩn cấp!', 6.5, '#FFCDD2')

    return save(fig, 'f_ui_elderly')


# 3. Màn hình Người Giám Hộ (DashboardScreen & AlertHistoryScreen)
def f_ui_guardian():
    fig, ax = new_fig(15, 10)
    
    # Máy 1: Dashboard giám sát bản đồ thời gian thực
    mx, my, mw, mh = draw_phone_frame(ax, 15, 5, 42, 88, 'GIÁM HỘ - THEO DÕI GẬY')
    
    # Banner cảnh báo trạng thái
    ax.add_patch(FancyBboxPatch((mx + 3, my + mh - 11), mw - 6, 9, boxstyle='round,pad=0,rounding_size=1.5', fc='#1E1E1E', ec=C_GREEN))
    label(ax, mx + 5, my + mh - 5, '🟢 Người già: TRỰC TUYẾN  |  Gậy: ĐÃ KẾT NỐI', 6.5, C_GREEN, ha='left', bold=True)
    label(ax, mx + 5, my + mh - 9, 'Tọa độ: 10.8275° N, 106.6789° E  (Cập nhật 2s trước)', 6.2, '#BBB', ha='left')

    # Bản đồ Flutter Map OpenStreetMap
    ax.add_patch(Rectangle((mx + 3, my + mh - 60), mw - 6, 47, fc='#1E2B37', ec='#324456'))
    # Lưới phố
    ax.plot([mx+5, mx+mw-5], [my+mh-35, my+mh-35], color='#2C3E50', lw=1.5)
    ax.plot([mx+5, mx+mw-5], [my+mh-45, my+mh-45], color='#2C3E50', lw=1.5)
    ax.plot([mx+15, mx+15], [my+mh-58, my+mh-15], color='#2C3E50', lw=1.5)
    ax.plot([mx+28, mx+28], [my+mh-58, my+mh-15], color='#2C3E50', lw=1.5)

    # Vị trí người già
    ax.add_patch(Circle((mx + 22, my + mh - 38), 3, fc=C_RED, ec='white', lw=1.5))
    label(ax, mx + 22, my + mh - 32, 'Vị trí Gậy', 6.5, C_RED, bold=True)

    # Vị trí Nhà
    ax.add_patch(Circle((mx + 32, my + mh - 25), 2.5, fc=C_GREEN, ec='white', lw=1.5))
    label(ax, mx + 32, my + mh - 20, 'Địa chỉ Nhà', 6.5, C_GREEN, bold=True)

    # Nút tiện ích chỉ đường 1 chạm
    ax.add_patch(FancyBboxPatch((mx + 4, my + mh - 70), (mw - 10)/2, 8, boxstyle='round,pad=0,rounding_size=1.5', fc='#0288D1', ec='none'))
    label(ax, mx + 4 + (mw - 10)/4, my + mh - 66, '🗺️ CHỈ ĐƯỜNG', 7.5, 'white', bold=True)

    ax.add_patch(FancyBboxPatch((mx + 6 + (mw - 10)/2, my + mh - 70), (mw - 10)/2, 8, boxstyle='round,pad=0,rounding_size=1.5', fc='#C2185B', ec='none'))
    label(ax, mx + 6 + 3*(mw - 10)/4, my + mh - 66, '🔔 CÒI BÁO ĐỘNG', 7.5, 'white', bold=True)

    label(ax, mx + mw/2, my + mh - 75, 'Bấm vào bản đồ để Cài Đặt Địa Chỉ Nhà hoặc Điểm Hẹn mới', 6, '#AAA')

    # Máy 2: Lịch sử cảnh báo (AlertHistoryScreen)
    mx2, my2, mw2, mh2 = draw_phone_frame(ax, 75, 5, 42, 88, 'LỊCH SỬ CẢNH BÁO')
    
    # Mục 1: Báo động ngã khẩn cấp
    ax.add_patch(FancyBboxPatch((mx2 + 3, my2 + mh2 - 20), mw2 - 6, 17, boxstyle='round,pad=0,rounding_size=1.5', fc='#1E1E1E', ec=C_RED, lw=1.2))
    label(ax, mx2 + 6, my2 + mh2 - 7, '🚨 PHÁT HIỆN TÉ NGÃ KHẨN CẤP!', 7.5, C_RED, bold=True, ha='left')
    label(ax, mx2 + 6, my2 + mh2 - 12, 'Thời gian: 08:35 - 14/10/2026', 6.5, '#AAA', ha='left')
    label(ax, mx2 + 6, my2 + mh2 - 16.5, 'Vị trí: 10.82753, 106.67891 (Đã gửi SMS)', 6.2, '#DDD', ha='left')
    ax.add_patch(FancyBboxPatch((mx2 + mw2 - 14, my2 + mh2 - 18), 9, 5, boxstyle='round,pad=0,rounding_size=1', fc=C_RED, ec='none'))
    label(ax, mx2 + mw2 - 9.5, my2 + mh2 - 15.5, 'Xem Maps', 5.5, 'white', bold=True)

    # Mục 2: Mất kết nối mạng & Khôi phục
    ax.add_patch(FancyBboxPatch((mx2 + 3, my2 + mh2 - 40), mw2 - 6, 17, boxstyle='round,pad=0,rounding_size=1.5', fc='#1E1E1E', ec=C_ORANGE, lw=1.2))
    label(ax, mx2 + 6, my2 + mh2 - 27, '⚠️ Sự cố Mạng (Đã kết nối lại)', 7.5, C_ORANGE, bold=True, ha='left')
    label(ax, mx2 + 6, my2 + mh2 - 32, 'Mất mạng lúc: 07:15  |  Khôi phục: 07:22', 6.5, '#AAA', ha='left')
    label(ax, mx2 + 6, my2 + mh2 - 36.5, 'Máy người già đã tự động đồng bộ lại vị trí', 6.2, C_GREEN, ha='left')

    # Mục 3: Mất kết nối Bluetooth Gậy
    ax.add_patch(FancyBboxPatch((mx2 + 3, my2 + mh2 - 60), mw2 - 6, 17, boxstyle='round,pad=0,rounding_size=1.5', fc='#1E1E1E', ec=C_BLUE, lw=1.2))
    label(ax, mx2 + 6, my2 + mh2 - 47, 'ℹ️ Thông tin: Gậy ĐÃ KẾT NỐI lại', 7.5, C_BLUE, bold=True, ha='left')
    label(ax, mx2 + 6, my2 + mh2 - 52, 'Thời gian: 06:40 - 14/10/2026', 6.5, '#AAA', ha='left')
    label(ax, mx2 + 6, my2 + mh2 - 56.5, 'Tự động quét MAC và kết nối thành công', 6.2, '#DDD', ha='left')

    # Nút xóa lịch sử
    ax.add_patch(FancyBboxPatch((mx2 + 10, my2 + mh2 - 74), mw2 - 20, 7, boxstyle='round,pad=0,rounding_size=1.5', fc='#333', ec='none'))
    label(ax, mx2 + mw2/2, my2 + mh2 - 70.5, 'Xóa toàn bộ lịch sử cảnh báo', 7, '#AAA')

    return save(fig, 'f_ui_guardian')


if __name__ == '__main__':
    for fn in [f_ui_role, f_ui_elderly, f_ui_guardian]:
        print(fn())

# Hướng Dẫn Nối Dây Cảm Biến E18-D50NK và Motor Rung với ESP32

## 1. Cảm Biến Vật Cản E18-D50NK (Loại NPN - NO)
- **Dây Nâu (VCC):** Nối vào chân **5V** của mạch tăng áp hoặc chân 5V / VIN trên mạch ESP32.
- **Dây Xanh dương (GND):** Nối vào chân âm (**GND**).
- **Dây Đen (Tín hiệu / OUT):** Cắm vào chân số **4** (`GPIO 4`) trên ESP32.

*(Lưu ý: Cảm biến này theo nhà sản xuất ghi 6-36V nhưng trên thực tế đa số vẫn chạy tốt khi cấp nguồn 5V, bạn cứ thử với 5V trước nhé).*

## 2. Cụm Motor Rung + Mạch Điều Khiển (MOSFET/Driver)
Vì ESP32 không đủ dòng điện để chạy motor trực tiếp, nên ta phải dùng mạch tăng áp và mạch driver. Cắm dây như sau:
- **Chân IN (hoặc SIG/PWM):** Nối vào chân số **5** (`GPIO 5`) của ESP32 (do bản ESP32-S3 không có chân 25).
- **Chân VCC (+):** Nối vào đầu ra **5V (Dương)** của mạch tăng áp.
- **Chân GND (-):** Nối vào đầu ra **GND (Âm)** của mạch tăng áp.
- ⚠️ **LƯU Ý CỰC QUAN TRỌNG:** Bạn BẮT BUỘC phải dùng 1 sợi dây nối chập chân GND của mạch tăng áp vào chân GND của ESP32. Nếu không có dây chung âm (GND) này, ESP32 sẽ không thể điều khiển được motor.

## 3. Cách chạy chương trình
1. Mở file `test_e18d50nk.ino` nằm trong cùng thư mục này bằng phần mềm Arduino IDE.
2. Cắm mạch ESP32 vào máy tính qua cáp USB.
3. Chọn đúng cổng COM và bấm nút mũi tên ngang (**Upload**) để nạp code.
4. Mở **Serial Monitor** (cài đặt tốc độ `115200` ở góc dưới cùng) để xem thông báo mỗi khi cảm biến phát hiện vật cản.

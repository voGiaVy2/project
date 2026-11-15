# -*- coding: utf-8 -*-
from doc_helpers import *
from docx.shared import Inches
import os

FIG_DIR = r'd:\doan\_tools\fig'

def build_ch2(doc):
    add_heading1(doc, "CƠ SỞ LÝ THUYẾT")

    # 2.1 ESP32-S3
    add_heading2(doc, "Tổng quan về vi điều khiển ESP32-S3:")
    add_heading3(doc, "Kiến trúc phần cứng và tập lệnh Xtensa 32-bit LX7 Dual-Core:")
    add_p(doc, "ESP32-S3 là dòng vi điều khiển System-on-Chip (SoC) hiệu năng cao thế hệ mới được phát triển bởi tập đoàn Espressif Systems, được thiết kế chuyên biệt cho các ứng dụng trí tuệ nhân tạo vạn vật (AIoT), xử lý tín hiệu số tại biên và các thiết bị đeo/cầm tay thông minh. Trái tim của ESP32-S3 là bộ vi xử lý lõi kép Xtensa 32-bit LX7, có khả năng hoạt động ở tần số xung nhịp lên đến 240 MHz. Kiến trúc đường ống 7 giai đoạn (7-stage pipeline) mang lại khả năng xử lý các phép tính số học và logic với thông lượng cực cao.")
    add_p(doc, "Đặc biệt, dòng chip LX7 trên ESP32-S3 được tích hợp thêm tập lệnh mở rộng xử lý vector (Vector Instructions) và bộ tăng tốc phần cứng cho các phép toán ma trận điểm tĩnh và dấu chấm động, giúp vi điều khiển có thể thực thi các phép nhân - cộng tích lũy (MAC) trong một chu kỳ xung nhịp. Điều này tạo điều kiện lý tưởng để triển khai các thuật toán lọc số (như bộ lọc thông thấp Butterworth, bộ lọc bù Complementary Filter hay bộ lọc Kalman) trực tiếp trên chip nhằm khử nhiễu tín hiệu cảm biến quán tính thời gian thực mà không làm nghẽn CPU.")

    add_heading3(doc, "Phân bố bộ nhớ và các ngoại vi trên chip:")
    add_p(doc, "Bản mạch vi điều khiển được nhóm nghiên cứu sử dụng trong đề tài là phiên bản cao cấp ESP32-S3 N16R8 (tích hợp 16 MB Flash ngoài qua giao tiếp Octal SPI và 8 MB PSRAM ngoài). Cấu trúc bộ nhớ của chip bao gồm:")
    add_p(doc, "• 512 KB bộ nhớ SRAM nội tại trên chip, chia thành SRAM0 (chứa mã lệnh), SRAM1 và SRAM2 (chứa dữ liệu tĩnh và heap động).")
    add_p(doc, "• 8 MB PSRAM tốc độ cao mở rộng: Cho phép lưu trữ các mảng dữ liệu lấy mẫu lớn, hàng đợi tin nhắn BLE và bộ đệm trạng thái cảm biến mà không lo ngại hiện tượng tràn bộ nhớ (stack overflow).")
    add_p(doc, "• 16 MB bộ nhớ Flash Quad/Octal SPI: Dùng để lưu trữ toàn bộ mã nguồn firmware nhúng, các bảng cấu hình tham số, dải địa chỉ MAC thiết bị ghép nối và vùng nhớ phân vùng NVS (Non-Volatile Storage).")
    add_p(doc, "ESP32-S3 cung cấp tới 45 chân vào/ra đa dụng (GPIO) có thể tái cấu hình linh hoạt thông qua ma trận IO Mux (Hình 2.1). Chip hỗ trợ đầy đủ các giao thức giao tiếp nối tiếp chuẩn công nghiệp: 2 bộ điều khiển bus I2C tốc độ chuẩn 100 kHz và Fast-mode 400 kHz; 3 bộ UART hỗ trợ cấu hình tốc độ baud tùy ý; 4 bộ SPI đa năng; 2 bộ chuyển đổi tín hiệu tương tự sang số (ADC) 12-bit độ phân giải cao với 20 kênh ngõ vào; và bộ điều khiển xung PWM chuyên dụng (LEDC) hỗ trợ phát các tần số âm thanh chính xác điều khiển còi báo động.")

    # Chèn hình 2.1
    add_fig(doc, os.path.join(FIG_DIR, 'f_esp32.png'), "Hình 2.1 Sơ đồ kiến trúc vi điều khiển ESP32-S3 N16R8 và các khối ngoại vi tích hợp")

    # Bảng 2.1 Thông số kỹ thuật ESP32-S3
    esp_specs = [
        ("Bộ xử lý trung tâm", "Xtensa 32-bit LX7 Dual-Core, xung nhịp 240 MHz"),
        ("Bộ nhớ nội (Internal RAM)", "512 KB SRAM + 384 KB ROM"),
        ("Bộ nhớ ngoài tích hợp", "16 MB SPI Flash (N16) + 8 MB Octal PSRAM (R8)"),
        ("Kết nối không dây", "Wi-Fi 802.11 b/g/n (2.4 GHz) + Bluetooth 5.0 (LE)"),
        ("Giao tiếp phần cứng", "45 GPIO, 2x I2C, 3x UART, 4x SPI, 14x Touch, 2x ADC 12-bit"),
        ("Điện áp hoạt động", "3.0 V đến 3.6 V (Điện áp logic chuẩn 3.3 V)"),
        ("Dòng tiêu thụ ở chế độ Active", "40 mA đến 95 mA (Tùy tần số CPU và bật/tắt radio)"),
        ("Dòng tiêu thụ ở chế độ Modem-sleep", "20 mA đến 25 mA (CPU chạy, tắt Wi-Fi/BLE)"),
        ("Dòng tiêu thụ ở chế độ Deep-sleep", "8 µA (Chỉ duy trì bộ nhớ RTC và ngắt thức tỉnh)")
    ]
    headers = ["Đặc tính kỹ thuật", "Giá trị / Mô tả chi tiết trên phiên bản ESP32-S3 N16R8"]
    col_w = [Inches(2.5), Inches(4.0)]
    add_table_data(doc, headers, esp_specs, col_w, "Bảng 2.1 Thông số kỹ thuật chi tiết của vi điều khiển ESP32-S3 N16R8")

    # 2.2 BLE
    add_heading2(doc, "Công nghệ truyền thông không dây Bluetooth Low Energy (BLE 5.0):")
    add_heading3(doc, "Khái niệm và ưu thế năng lượng của BLE so với Bluetooth Classic:")
    add_p(doc, "Bluetooth Low Energy (BLE), ban đầu được giới thiệu trong chuẩn Bluetooth 4.0 và được nâng cấp toàn diện trong Bluetooth 5.0, là một công nghệ mạng không dây cá nhân (PAN) được thiết kế chuyên biệt cho các thiết bị di động và nhúng đòi hỏi mức tiêu thụ năng lượng cực thấp.")
    add_p(doc, "Khác biệt căn bản giữa Bluetooth Classic (BR/EDR) và BLE nằm ở chu kỳ làm việc (Duty Cycle). Trong khi Bluetooth Classic duy trì một kênh truyền dữ liệu liên tục (thích hợp cho truyền âm thanh chất lượng cao, tai nghe không dây), dẫn đến tiêu tốn dòng điện lớn (từ 30 mA đến 50 mA liên tục), thì BLE được tối ưu hóa cho các giao dịch truyền nhận các gói dữ liệu nhỏ ngắt quãng theo từng chu kỳ. Sau khi phát hoặc nhận xong một gói tin, chip vô tuyến của BLE ngay lập tức chuyển về trạng thái ngủ sâu (sleep mode) với dòng tiêu thụ chỉ vài micro-ampe. Điều này cho phép một nút cảm biến dùng pin có thể hoạt động bền bỉ từ vài tháng đến vài năm mà không cần sạc lại.")

    add_heading3(doc, "Kiến trúc GATT Profile: Service, Characteristic và Descriptor:")
    add_p(doc, "Trong giao thức BLE, việc tổ chức và trao đổi dữ liệu giữa hai thiết bị được quy định bởi cấu trúc GATT (Generic Attribute Profile) như minh họa trên Hình 2.2:")
    add_p(doc, "• Vai trò thiết bị (Roles):")
    add_p(doc, "- GATT Server: Thiết bị nắm giữ cơ sở dữ liệu thuộc tính và phục vụ các yêu cầu đọc/ghi từ xa. Trong đề tài này, cây gậy thông minh ESP32-S3 đóng vai trò là GATT Server, quản lý dữ liệu cảm biến té ngã.")
    add_p(doc, "- GATT Client: Thiết bị khởi tạo kết nối và gửi các yêu cầu truy vấn hoặc nhận thông báo. Chiếc điện thoại thông minh của người cao tuổi đóng vai trò là GATT Client, chủ động kết nối tới gậy.")
    add_p(doc, "• Cấu trúc phân tầng dữ liệu (GATT Hierarchy):")
    add_p(doc, "- Profile: Tập hợp một hoặc nhiều Service định nghĩa một trường hợp sử dụng cụ thể.")
    add_p(doc, "- Service (Dịch vụ): Một khối logic nhóm các dữ liệu có liên quan lại với nhau, được định danh duy nhất bởi một mã UUID 128-bit (Universally Unique Identifier). Trong đề tài, nhóm nghiên cứu đã thiết lập một Service báo ngã tùy biến với UUID: 4fafc201-1fb5-459e-8fcc-c5c9c331914b.")
    add_p(doc, "- Characteristic (Đặc tính): Là phần tử dữ liệu cụ thể nằm trong một Service, bao gồm giá trị dữ liệu thực tế (Value) và các quyền truy cập (Properties: Read, Write, Notify, Indicate). Đặc tính cảnh báo té ngã trong đề tài có UUID: beb5483e-36e1-4688-b7f5-ea07361b26a9, được gán thuộc tính PROPERTY_READ và PROPERTY_NOTIFY.")
    add_p(doc, "- Descriptor: Bộ mô tả thuộc tính bổ sung cho Characteristic. Đặc biệt, bộ mô tả Client Characteristic Configuration Descriptor (CCCD với UUID chuẩn 0x2902) đóng vai trò cực kỳ quan trọng, cho phép phía Client (App di động) bật hoặc tắt quyền gửi tín hiệu Notify tự động từ Server mà không cần phải thăm dò (polling) liên tục.")

    # Chèn hình 2.2
    add_fig(doc, os.path.join(FIG_DIR, 'f_gatt.png'), "Hình 2.2 Cấu trúc phân tầng và GATT Profile của Bluetooth Low Energy trong hệ thống")

    # 2.3 MPU6050
    add_heading2(doc, "Cảm biến quán tính MPU6050 và thuật toán đo lường:")
    add_heading3(doc, "Cấu tạo và nguyên lý hoạt động của gia tốc kế và con quay hồi chuyển 6-DOF:")
    add_p(doc, "MPU6050 là cảm biến tích hợp nguyên khối công nghệ vi cơ điện tử (MEMS) hàng đầu của hãng InvenSense, bao gồm một gia tốc kế 3 trục (3-axis accelerometer) và một con quay hồi chuyển 3 trục (3-axis gyroscope) trên cùng một đế silicon có kích thước chỉ 4 x 4 x 0.9 mm.")
    add_p(doc, "• Nguyên lý gia tốc kế (Accelerometer): Hoạt động dựa trên định luật II Newton (F = m.a). Bên trong vi cấu trúc silicon của cảm biến có các khối lượng thử (proof mass) siêu nhỏ được treo bởi các thanh dầm đàn hồi. Khi cảm biến chịu tác động của gia tốc tuyến tính (hoặc trọng lực Trái Đất g = 9.8 m/s²), khối lượng thử dịch chuyển tương đối so với các điện cực cố định, làm thay đổi điện dung vi sai giữa các bản cực tụ điện. Mạch khuếch đại điện tích trên chip sẽ chuyển đổi sự thay đổi điện dung này thành điện áp, sau đó đưa qua bộ ADC 16-bit tích hợp để xuất ra giá trị gia tốc số học trên 3 trục tọa độ X, Y, Z.")
    add_p(doc, "• Nguyên lý con quay hồi chuyển (Gyroscope): Hoạt động dựa trên hiệu ứng lực quán tính Coriolis. Khi một cấu trúc vi cơ đang dao động cộng hưởng ở tần số cao bị quay quanh một trục vuông góc, lực Coriolis sẽ làm xuất hiện một dao động thứ cấp vuông góc với cả phương dao động ban đầu và trục quay. Biên độ của dao động thứ cấp tỷ lệ thuận với tốc độ góc quay (đơn vị: độ/giây - dps), được chuyển đổi qua bộ ADC 16-bit độc lập để cung cấp tốc độ quay quanh 3 trục Pitch, Roll, Yaw.")

    # Bảng 2.2 Thông số MPU6050
    mpu_specs = [
        ("Dải đo gia tốc (Accelerometer Ranges)", "±2g, ±4g, ±8g, ±16g (Lựa chọn dải ±8g cho đề tài)"),
        ("Độ phân giải bộ chuyển đổi ADC", "16-bit độc lập cho từng trục (Gia tốc và Con quay)"),
        ("Độ nhạy gia tốc kế ở dải ±8g", "4096 LSB/g"),
        ("Dải đo con quay hồi chuyển (Gyroscope)", "±250, ±500, ±1000, ±2000 dps (độ/giây)"),
        ("Chuẩn giao tiếp vi điều khiển", "I2C Fast-Mode (Tần số xung nhịp lên đến 400 kHz)"),
        ("Địa chỉ I2C mặc định", "0x68 (Chân AD0 nối GND) hoặc 0x69 (AD0 nối VCC)"),
        ("Tần số lấy mẫu dữ liệu ngõ ra (ODR)", "Tối đa 1000 Hz cho gia tốc kế, 8000 Hz cho con quay"),
        ("Dòng điện tiêu thụ hoạt động", "Khoảng 3.8 mA ở chế độ Full-Power")
    ]
    headers = ["Thông số kỹ thuật", "Chi tiết cấu hình trên cảm biến MPU6050"]
    col_w = [Inches(2.5), Inches(4.0)]
    add_table_data(doc, headers, mpu_specs, col_w, "Bảng 2.2 Thông số kỹ thuật của cảm biến quán tính 6-DOF MPU6050")

    add_heading3(doc, "Giao tiếp I2C và định dạng khung truyền:")
    add_p(doc, "Cảm biến MPU6050 giao tiếp với ESP32-S3 thông qua chuẩn bus nối tiếp đồng bộ I2C (Inter-Integrated Circuit) hai dây: chân SDA (Serial Data) dùng để truyền nhận dữ liệu hai chiều và chân SCL (Serial Clock) dùng để truyền xung đồng hồ định thời do ESP32-S3 phát ra (Hình 2.3). Do mạch ngõ ra của I2C là dạng cực máng hở (Open-Drain), cả hai đường SDA và SCL đều bắt buộc phải được kết nối với các điện trở kéo lên nguồn (Pull-up resistors, giá trị từ 2.2 kΩ đến 4.7 kΩ lên mức điện áp 3.3 V) để xác lập mức logic cao mặc định khi bus rảnh.")

    # Chèn hình 2.3 và 2.4
    add_fig(doc, os.path.join(FIG_DIR, 'f_i2c.png'), "Hình 2.3 Chuẩn giao tiếp I2C giữa vi điều khiển ESP32-S3 và cảm biến MPU6050")
    add_fig(doc, os.path.join(FIG_DIR, 'f_mpu.png'), "Hình 2.4 Hệ trục tọa độ không gian 3 chiều và cảm biến quán tính 6-DOF MPU6050")

    add_heading3(doc, "Thuật toán phát hiện té ngã dựa trên ngưỡng gia tốc tổng hợp (SVM):")
    add_p(doc, "Để nhận diện một cú té ngã độc lập với hướng rơi và góc đặt ban đầu của cây gậy trong không gian ba chiều, đại lượng gia tốc tổng hợp SVM (Signal Vector Magnitude) được sử dụng làm tham số động học cốt lõi. Độ lớn của vector gia tốc tổng hợp |a| tại thời điểm lấy mẫu t được tính theo công thức Euclid:")
    add_p(doc, "    |a| = √(ax² + ay² + az²)", style='Caption', align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(doc, "Trong đó ax, ay, az lần lượt là thành phần gia tốc tức thời đo được trên ba trục trực giao X, Y, Z (đơn vị: m/s²).")
    add_p(doc, "Quá trình một cú ngã thực tế diễn ra qua 3 giai đoạn động học phân biệt rõ rệt như biểu diễn trên Hình 2.5:")
    add_p(doc, "1. Giai đoạn rơi tự do (Free-fall): Thân người và cây gậy mất thăng bằng bắt đầu rơi nhanh xuống đất dưới tác dụng của trọng trường. Tại giai đoạn này, các gia tốc phản lực triệt tiêu, độ lớn vector gia tốc tổng hợp |a| giảm mạnh đột ngột, tiệm cận về mức 0 m/s² trong khoảng thời gian từ 100 ms đến 300 ms.")
    add_p(doc, "2. Giai đoạn va chạm với mặt sàn (Impact): Thân gậy và cơ thể va đập trực tiếp xuống sàn gạch hoặc bề mặt cứng. Quá trình hãm tốc diễn ra trong tích tắc tạo ra một xung gia tốc cực đại (Impact Acceleration Spike) với biên độ vượt trội, thường dao động trong khoảng từ 25 m/s² đến 40 m/s².")
    add_p(doc, "3. Giai đoạn nằm bất động (Rest / Immobility): Sau cú va đập, nếu người già bị chấn thương hoặc choáng ngất, cây gậy sẽ nằm cố định trên mặt đất. Khi đó, vector gia tốc tổng hợp sẽ nhanh chóng trở về giá trị tĩnh tương đương gia tốc trọng trường g ≈ 9.8 m/s², đồng thời độ lệch chuẩn dao động của gia tốc đạt mức gần như bằng 0 trong thời gian kéo dài nhiều giây.")

    # Chèn hình 2.5
    add_fig(doc, os.path.join(FIG_DIR, 'f_accel.png'), "Hình 2.5 Dạng sóng vector gia tốc tổng hợp SVM khi đi bộ, va chạm té ngã và nằm bất động")

    # 2.4 Cảm biến khoảng cách
    add_heading2(doc, "Cảm biến phát hiện khoảng cách vật cản (HC-SR04 & E18-D50NK):")
    add_heading3(doc, "Cảm biến siêu âm HC-SR04 và nguyên lý phản xạ sóng âm 40 kHz:")
    add_p(doc, "Cảm biến siêu âm HC-SR04 được sử dụng làm cảm biến phát hiện chướng ngại vật chính trên gậy thông minh. Cảm biến bao gồm một đầu phát sóng siêu âm (Transmitter) và một đầu thu sóng siêu âm (Receiver) bằng gốm áp điện (piezoelectric).")
    add_p(doc, "Nguyên lý hoạt động chi tiết (Hình 2.6):")
    add_p(doc, "• Bước 1: Vi điều khiển ESP32-S3 kích hoạt một xung điện áp mức cao (HIGH) có độ rộng tối thiểu 10 µs vào chân TRIG của cảm biến.")
    add_p(doc, "• Bước 2: Nhận được tín hiệu kích, mạch phát tích hợp trên HC-SR04 sẽ tự động phát ra một chùm 8 chu kỳ xung sóng âm có tần số chuẩn 40 kHz hướng về phía trước.")
    add_p(doc, "• Bước 3: Đồng thời, chân ECHO của cảm biến được kéo lên mức HIGH. Sóng siêu âm lan truyền trong không khí, khi gặp vật cản sẽ bị phản xạ ngược trở lại. Đầu thu sẽ chuyển đổi áp suất sóng âm phản xạ thành tín hiệu điện và kéo chân ECHO trở về mức LOW.")
    add_p(doc, "Khoảng cách từ cảm biến đến chướng ngại vật được tính toán chính xác dựa trên thời gian bay của sóng (Time-of-Flight - t tính bằng micro-giây) và vận tốc lan truyền của âm thanh trong không khí (v ≈ 343 m/s ở 20°C):")
    add_p(doc, "    Khoảng cách d = (t × 0.0343) / 2  (cm)", style='Caption', align=WD_ALIGN_PARAGRAPH.CENTER)

    # Chèn hình 2.6
    add_fig(doc, os.path.join(FIG_DIR, 'f_ultra.png'), "Hình 2.6 Giản đồ thời gian phát xung kích Trig và phản hồi Echo của cảm biến HC-SR04")

    add_heading3(doc, "Kỹ thuật đo xung pulseIn kết hợp micros() chống treo ESP32-S3:")
    add_p(doc, "Trong các hệ thống nhúng thông thường, hàm pulseIn(ECHO_PIN, HIGH) của Arduino framework thường được sử dụng để đo thời gian chân Echo giữ mức cao. Tuy nhiên, trên vi điều khiển lõi kép ESP32-S3 chạy hệ điều hành thời gian thực FreeRTOS, việc gọi pulseIn() đôi khi gặp hiện tượng trả về giá trị 0 ngẫu nhiên do bị bộ lập lịch (Scheduler) ngắt quãng hoặc xung bị méo dạng ở mức logic 3.3V.")
    add_p(doc, "Để khắc phục triệt để lỗi này, nhóm nghiên cứu đã thiết kế một giải pháp thuật toán đo lường chuyên sâu:")
    add_p(doc, "1. Sử dụng lệnh noInterrupts() và interrupts() bao bọc quá trình kích chân Trig (kéo LOW 5 µs, kéo HIGH 12 µs, kéo LOW) để đảm bảo xung kích tuyệt đối sạch sẽ, không bị chia sẻ thời gian với các tác vụ Wi-Fi hay BLE.")
    add_p(doc, "2. Cài đặt thời gian chờ (timeout) cho pulseIn là 40000 µs (tương đương phạm vi đo tối đa khoảng 6.8 mét).")
    add_p(doc, "3. Cơ chế dự phòng thông minh (Fallback mechanism): Nếu pulseIn trả về 0, chương trình ngay lập tức chuyển sang vòng lặp đo trực tiếp bằng bộ đếm thời gian phần cứng micros(). Vòng lặp liên tục kiểm tra trạng thái chân Echo, nếu sau 35 ms không có xung phản hồi sẽ trả về mã lỗi quy ước (-1 hoặc -2), ngăn chặn triệt để nguy cơ vi điều khiển bị treo vô hạn (Watchdog Timer crash).")

    add_heading3(doc, "Cảm biến quang hồng ngoại E18-D50NK dự phòng:")
    add_p(doc, "Để tăng cường độ tin cậy trong các môi trường đặc thù (như phát hiện các bề mặt nghiêng tán xạ sóng âm kém hoặc vật cản bằng vải dày hấp thụ âm thanh), hệ thống được thiết kế mở rộng hỗ trợ cảm biến quang hồng ngoại E18-D50NK (Hình 2.7). Cảm biến này tích hợp một diode phát hồng ngoại và một photodiode thu trong cùng một vỏ bọc kim loại hình trụ chắc chắn, có biến trở hiệu chỉnh cự ly phát hiện từ 3 cm đến 50 cm. Tín hiệu ngõ ra là cực thu hở NPN thường mở (Normally Open): khi có vật cản, ngõ ra kéo xuống mức LOW (0V); khi không có vật cản, chân OUT giữ mức HIGH thông qua điện trở kéo lên nội tại của ESP32 (INPUT_PULLUP).")

    # Chèn hình 2.7
    add_fig(doc, os.path.join(FIG_DIR, 'f_ir.png'), "Hình 2.7 Nguyên lý phản xạ quang học của cảm biến vật cản hồng ngoại E18-D50NK")

    # 2.5 Mạch kích công suất
    add_heading2(doc, "Mạch kích công suất và cơ chế cảnh báo xúc giác/âm thanh:")
    add_heading3(doc, "Mạch điều khiển động cơ rung lệch tâm (ERM) qua MOSFET AOD4184:")
    add_p(doc, "Động cơ rung lệch tâm (Eccentric Rotating Mass - ERM) hoạt động ở điện áp 5V, có dòng khởi động có thể lên tới 150 mA - 200 mA. Trong khi đó, dòng điện ngõ ra tối đa cho phép trên mỗi chân GPIO của ESP32-S3 chỉ giới hạn ở mức 20 mA - 40 mA. Việc nối trực tiếp động cơ vào chân GPIO sẽ gây sụt áp nghiêm trọng và làm cháy cổng vi điều khiển.")
    add_p(doc, "Giải pháp kỹ thuật được áp dụng là sử dụng mạch driver chuyển mạch công suất dùng Transistor hiệu ứng trường N-channel MOSFET logic level AOD4184 (Hình 2.8). MOSFET này có điện áp kích ngưỡng Vgs(th) rất thấp (1.7 V - 2.6 V), cho phép mở bão hòa hoàn toàn chỉ với điện áp điều khiển 3.3 V từ chân GPIO 6 của ESP32-S3. Nội trở dẫn Rds(on) siêu nhỏ (< 8.5 mΩ) giúp MOSFET hầu như không phát nhiệt khi dẫn dòng lớn.")
    add_p(doc, "Đặc biệt, do động cơ điện là tải có tính cảm ứng (Inductive load), khi ngắt dòng điện đột ngột, từ trường trong cuộn dây động cơ sụp đổ sẽ tạo ra một xung điện áp cảm ứng ngược (Back-EMF) lên tới hàng chục vôn theo định luật Faraday. Một diode chỉnh lưu hồi tiếp (Flyback diode 1N4007 hoặc SS34) được mắc song song ngược cực với hai đầu động cơ để dập tắt xung điện áp ngược này, bảo vệ an toàn tuyệt đối cho MOSFET và vi điều khiển.")

    # Chèn hình 2.8
    add_fig(doc, os.path.join(FIG_DIR, 'f_mosfet.png'), "Hình 2.8 Sơ đồ nguyên lý mạch kích công suất motor rung sử dụng MOSFET và diode dập xung")

    add_heading3(doc, "Còi hú báo động Buzzer và khối nguồn sạc Pin Li-ion 18650:")
    add_p(doc, "• Còi hú Buzzer 5V: Sử dụng còi điện từ chủ động (Active Buzzer) kết hợp phát xung tần số 2000 Hz bằng lệnh tone() của vi điều khiển. Âm lượng phát ra đạt mức 85 dB ở khoảng cách 1 mét, đủ lớn để thu hút sự chú ý tức thời của người thân ở các phòng lân cận hoặc người đi đường ngoài phố.")
    add_p(doc, "• Khối nguồn điện di động: Toàn bộ hệ thống phần cứng trên gậy được cấp nguồn từ một cell pin sạc Li-ion 18650 dung lượng 2500 mAh - 3000 mAh (điện áp danh định 3.7 V, đầy 4.2 V). Mạch sạc tích hợp TP4056 hỗ trợ cổng cắm Type-C hiện đại, có mạch bảo vệ chống quá nạp, chống quá xả (cắt nguồn khi điện áp tụt dưới 2.5 V) và bảo vệ ngắn mạch. Điện áp của pin sau đó được đưa qua mạch tăng áp DC-DC Boost converter hiệu suất cao để nâng lên mức 5.0 V ổn định, cung cấp đồng thời cho chân VIN của ESP32-S3, cảm biến siêu âm và cụm motor rung.")

    # 2.6 GPS
    add_heading2(doc, "Hệ thống định vị toàn cầu GPS và dịch vụ định vị di động:")
    add_heading3(doc, "Nguyên lý định vị vệ tinh GPS và giao thức NMEA 0183:")
    add_p(doc, "Hệ thống định vị toàn cầu GPS (Global Positioning System) hoạt động dựa trên chòm sao gồm tối thiểu 24 vệ tinh bay quanh quỹ đạo Trái Đất. Nguyên lý cốt lõi của định vị GPS là phương pháp giao điểm các mặt cầu khoảng cách (Trilateration) như mô tả trên Hình 2.9:")
    add_p(doc, "Mỗi vệ tinh liên tục phát tín hiệu vô tuyến mang thông tin về vị trí quỹ đạo (ephemeris) và thời điểm phát sóng chính xác tuyệt đối từ đồng hồ nguyên tử. Bộ thu GPS sẽ tính toán thời gian truyền sóng từ vệ tinh đến anten thu, từ đó nhân với vận tốc ánh sáng (c ≈ 300.000 km/s) để xác định khoảng cách cầu tới từng vệ tinh. Để xác định được tọa độ vị trí 3 chiều (Kinh độ, Vĩ độ, Độ cao) và bù trừ sai số đồng hồ nội tại của máy thu, thiết bị cần bắt được tín hiệu từ tối thiểu 4 vệ tinh đồng thời.")

    # Chèn hình 2.9
    add_fig(doc, os.path.join(FIG_DIR, 'f_gps.png'), "Hình 2.9 Nguyên lý định vị toàn cầu GPS dựa trên giao điểm mặt cầu vệ tinh")

    add_heading3(doc, "Dịch vụ định vị kết hợp (Fused Location Provider) và thư viện Geolocator:")
    add_p(doc, "Trong các mô hình gậy IoT truyền thống, việc gắn module phần cứng GPS rời (như u-blox NEO-6M) trực tiếp lên gậy bộc lộ nhiều nhược điểm nghiêm trọng: module rời tiêu thụ dòng điện rất lớn (45 mA - 60 mA liên tục), thời gian bắt tín hiệu nguội (Cold Start) ngoài trời kéo dài từ 30 đến 60 giây, và đặc biệt là hoàn toàn mất tín hiệu (GPS Blind) khi người già di chuyển vào trong nhà, chung cư hoặc khu vực có mái che dày đặc.")
    add_p(doc, "Để khắc phục triệt để rào cản này, đề tài đã áp dụng giải pháp dịch vụ định vị kết hợp (Fused Location Provider) thông qua thư viện chuyên dụng Geolocator trên nền tảng Flutter. Công nghệ này kết hợp thông minh dữ liệu từ 3 nguồn: chip thu GPS vệ tinh của điện thoại, mạng định vị trạm phát sóng di động GSM/4G (Cell-ID) và nhận dạng địa chỉ MAC của các mạng Wi-Fi lân cận (Wi-Fi Positioning). Nhờ đó, ngay cả khi người già ở trong phòng ngủ kín không có sóng vệ tinh, điện thoại vẫn xác định được tọa độ tương đối với sai số chấp nhận được. Tọa độ thu được theo hệ quy chiếu WGS84 được tự động chuyển thành liên kết Google Maps chuẩn mực dạng: https://maps.google.com/?q=lat,lng để gửi đi cứu hộ.")

    # 2.7 Firebase
    add_heading2(doc, "Nền tảng đám mây Firebase Cloud:")
    add_heading3(doc, "Cơ sở dữ liệu thời gian thực Firebase Realtime Database:")
    add_p(doc, "Firebase Realtime Database (RTDB) là giải pháp cơ sở dữ liệu NoSQL đám mây do Google phát triển, lưu trữ dữ liệu dưới dạng một cây đối tượng JSON (JSON Tree) phân cấp lớn. Khác với các cơ sở dữ liệu quan hệ truyền thống đòi hỏi câu lệnh SQL và cơ chế thăm dò HTTP request định kỳ, Firebase RTDB sử dụng giao thức kết nối liên tục WebSocket. Khi có bất kỳ một trường dữ liệu nào trong cây JSON thay đổi (ví dụ: cờ is_falling đổi từ false sang true), máy chủ Firebase sẽ chủ động 'đẩy' (Push) sự thay đổi đó xuống tất cả các thiết bị Client đang đăng ký lắng nghe (qua hàm onValue) trong thời gian tính bằng phần trăm giây mà không làm tốn tài nguyên mạng (Hình 2.10).")

    # Chèn hình 2.10
    add_fig(doc, os.path.join(FIG_DIR, 'f_rtdb.png'), "Hình 2.10 Cơ chế đồng bộ dữ liệu hai chiều thời gian thực trên Firebase Realtime Database")

    add_heading3(doc, "Cơ chế theo dõi trạng thái mạng (Presence System) qua .info/connected:")
    add_p(doc, "Một tính năng cực kỳ quan trọng được nhóm nghiên cứu khai thác là hệ thống nhận diện trạng thái kết nối mạng (Presence System) của Firebase. Thông qua đường dẫn đặc biệt .info/connected, ứng dụng trên máy người già có thể bắt chính xác khoảnh khắc kết nối mạng Internet bị đứt đoạn hoặc khôi phục.")
    add_p(doc, "Đặc biệt, lệnh onDisconnect().set(false) được thiết lập tại máy chủ: nếu chiếc điện thoại của người già bị hết pin đột ngột, tắt nguồn hoặc mất hẳn sóng 4G/Wi-Fi, máy chủ Firebase sẽ tự động phát hiện socket WebSocket bị đóng và cập nhật trường is_online = false. Nhờ đó, ứng dụng phía Người Giám Hộ sẽ ngay lập tức phát hiện trạng thái mất mạng của cha mẹ và kích hoạt banner cảnh báo màu đỏ trên giao diện.")

    # 2.8 Flutter
    add_heading2(doc, "Framework lập trình ứng dụng di động đa nền tảng Flutter:")
    add_heading3(doc, "Kiến trúc đa tầng của Framework Flutter:")
    add_p(doc, "Flutter là bộ công cụ phát triển phần mềm giao diện người dùng mã nguồn mở (UI SDK) do Google xây dựng, sử dụng ngôn ngữ lập trình Dart hiện đại. Kiến trúc của Flutter được chia thành 3 tầng chính (Hình 2.11):")
    add_p(doc, "1. Tầng Framework (Dart): Chứa hệ thống widget phong phú (Material Design và Cupertino), các bộ quản trị hoạt ảnh (Animation), điều hướng (Navigator) và cử chỉ (Gestures).")
    add_p(doc, "2. Tầng Engine (C++): Trái tim hiệu năng của Flutter, bao gồm bộ thư viện đồ họa phần cứng Impeller/Skia, máy ảo Dart VM thực thi mã bytecode cực nhanh, và hệ thống phân giải văn bản.")
    add_p(doc, "3. Tầng Platform (Nền tảng): Giao tiếp trực tiếp với hệ điều hành Android và iOS thông qua cơ chế Platform Channels (MethodChannel), cho phép mã Dart gọi các dịch vụ phần cứng bản địa của điện thoại như Bluetooth, GPS, SMS và Background Services.")

    # Chèn hình 2.11
    add_fig(doc, os.path.join(FIG_DIR, 'f_flutter.png'), "Hình 2.11 Kiến trúc đa tầng của Framework lập trình di động Flutter")

    add_heading3(doc, "Dịch vụ chạy ngầm liên tục (Flutter Background Service) trên Android:")
    add_p(doc, "Một rào cản kỹ thuật rất lớn trong các ứng dụng di động hiện đại là các cơ chế tiết kiệm pin nghiêm ngặt của hệ điều hành Android (như chế độ Doze Mode, App Standby). Nếu không có giải pháp chuyên biệt, khi người dùng tắt màn hình hoặc vuốt ứng dụng khỏi danh sách đa nhiệm, hệ điều hành Android sẽ tự động tiêu diệt (kill) tiến trình ứng dụng sau 5 đến 15 phút, khiến kết nối Bluetooth và GPS bị gián đoạn hoàn toàn.")
    add_p(doc, "Để giải quyết triệt để vấn đề sống còn này, nhóm nghiên cứu đã triển khai gói thư viện flutter_background_service để khởi tạo một Dịch vụ chạy ở tiền cảnh (Foreground Service) độc lập (Hình 2.12). Dịch vụ này chạy trên một Isolate Dart riêng biệt, duy trì một biểu tượng thông báo thường trực trên thanh trạng thái hệ thống ('Smart Cane - Đang bảo vệ ngầm...') với mức ưu tiên kênh PRIORITY_HIGH. Nhờ đó, hệ điều hành Android nhận diện đây là dịch vụ cốt lõi và không bao giờ tự ý dừng tiến trình. Dịch vụ ngầm này liên tục đảm nhận 4 nhiệm vụ song song 24/7:")
    add_p(doc, "• Quét và chủ động gửi lệnh kết nối lại Bluetooth trực tiếp (Direct Connect) với cây gậy mỗi khi gậy ở trong tầm phủ sóng.")
    add_p(doc, "• Lắng nghe Characteristic báo ngã từ gậy.")
    add_p(doc, "• Nhận luồng vị trí GPS từ phần cứng điện thoại và đồng bộ lên Firebase.")
    add_p(doc, "• Quản lý đồng hồ đếm ngược 15 giây và điều khiển cơ chế gửi tin nhắn SMS ngầm tự động cứu hộ.")

    # Chèn hình 2.12
    add_fig(doc, os.path.join(FIG_DIR, 'f_fgs.png'), "Hình 2.12 Cơ chế hoạt động đa luồng Isolate của Flutter Background Service trên Android")

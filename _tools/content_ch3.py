# -*- coding: utf-8 -*-
from doc_helpers import *
from docx.shared import Inches
import os

FIG_DIR = r'd:\doan\_tools\fig'
DH_DIR = r'd:\doan\DH'

def build_ch3(doc):
    add_heading1(doc, "PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG")

    # 3.1 Phân tích yêu cầu
    add_heading2(doc, "Phân tích yêu cầu thiết kế hệ thống:")
    add_heading3(doc, "Yêu cầu người dùng (User Requirements):")
    add_p(doc, "Để một thiết bị hỗ trợ sức khỏe có thể thực sự đi vào đời sống của người cao tuổi tại Việt Nam, sản phẩm phải được thiết kế xoay quanh chính các thói quen, tâm sinh lý và đặc thù sinh hoạt của đối tượng sử dụng:")
    add_p(doc, "1. Tính thân thiện và dễ sử dụng tối đa: Người cao tuổi thường gặp khó khăn với các thao tác công nghệ phức tạp. Do đó, toàn bộ phần cứng trên gậy phải hoạt động hoàn toàn tự động (Zero-Configuration). Người già chỉ cần cầm gậy lên đi lại bình thường như một cây gậy truyền thống, không cần bấm bất kỳ công tắc phức tạp nào. Mọi tiến trình kết nối Bluetooth, định vị và giám sát đều diễn ra âm thầm ở chế độ ngầm.")
    add_p(doc, "2. Cảnh báo xúc giác trực quan: Khi phát hiện có chướng ngại vật trước mặt ở cự ly nguy hiểm (3 cm - 80 cm), gậy phải lập tức rung mạnh vào lòng bàn tay để người dùng cảm nhận được ngay, đặc biệt hữu ích với những người già có thính lực kém hoặc mắt nhìn mờ.")
    add_p(doc, "3. Cơ chế chống báo nhầm thông minh: Người cao tuổi rất ngại làm phiền con cháu khi họ đang đi làm. Nếu cây gậy chẳng may bị tuột tay rơi xuống sàn hoặc va quẹt nhẹ mà đã vội vàng hú còi gọi điện thoại đến cơ quan của con cái thì sẽ gây tâm lý ức chế, dẫn đến việc người già vứt bỏ thiết bị. Do đó, hệ thống bắt buộc phải có cơ chế đếm ngược 15 giây với nút bấm to rõ 'Tôi ổn - Hủy báo động' trên màn hình điện thoại để người già có thể tự tay hủy bỏ cảnh báo nếu mình không sao.")
    add_p(doc, "4. Trực quan hóa phía người giám hộ: Ứng dụng phía người chăm sóc phải hiển thị bản đồ trực tiếp với các biểu tượng phân biệt rõ ràng (vị trí hiện tại của người già, vị trí ngôi nhà, các điểm hẹn gặp). Khi có sự cố, hệ thống phải cung cấp nút bấm dẫn đường Google Maps tức thời chỉ với một lần chạm.")

    add_heading3(doc, "Yêu cầu kỹ thuật (Technical Specifications):")
    add_p(doc, "Các chỉ tiêu kỹ thuật khắt khe được đặt ra cho toàn bộ hệ thống:")
    add_p(doc, "• Về phần cứng nhúng: Vi điều khiển phải có tốc độ lấy mẫu cảm biến IMU đạt tối thiểu 10 Hz (100 ms một lần), thuật toán đo khoảng cách siêu âm có độ trễ dưới 50 ms và không làm nghẽn tiến trình truyền thông BLE.")
    add_p(doc, "• Về độ trễ truyền thông: Thời gian từ khi MPU6050 phát hiện xung va chạm té ngã cho đến khi điện thoại nhận được gói tin Notify BLE phải nhỏ hơn 300 ms; thời gian đồng bộ dữ liệu sự cố lên Firebase Cloud phải nhỏ hơn 1 giây khi có kết nối mạng ổn định.")
    add_p(doc, "• Về cơ chế dự phòng ngoại tuyến (Offline Resiliency): Trong trường hợp người già đi lạc ra ngoài khu vực phủ sóng Wi-Fi hoặc tài khoản 4G hết dung lượng, hệ thống vẫn phải có khả năng tự động gửi tin nhắn SMS chứa tọa độ GPS cuối cùng đến thẳng số điện thoại của người giám hộ.")
    add_p(doc, "• Về nguồn điện: Cây gậy phải đảm bảo hoạt động liên tục tối thiểu 18 - 24 giờ sau mỗi lần sạc đầy, và sử dụng cổng sạc chuẩn USB Type-C phổ biến.")

    # 3.2 Sơ đồ khối
    add_heading2(doc, "Sơ đồ khối và kiến trúc hệ thống:")
    add_p(doc, "Hệ thống Gậy Thông Minh được thiết kế theo mô hình kiến trúc phân tán gồm 4 khối chức năng chính liên kết chặt chẽ với nhau như biểu diễn trên Hình 3.1:")

    # Chèn hình 3.1
    add_fig(doc, os.path.join(FIG_DIR, 'f_block_diag.png'), "Hình 3.1 Sơ đồ khối chức năng hoàn chỉnh của toàn bộ hệ thống gậy thông minh")

    add_heading3(doc, "Phân tích chức năng các khối trong hệ thống:")
    add_p(doc, "1. Khối Gậy Thông Minh (Hardware Node):")
    add_p(doc, "Là trung tâm thu thập dữ liệu sinh trắc học và tương tác cơ học trực tiếp với người cao tuổi:")
    add_p(doc, "• Cảm biến gia tốc MPU6050 liên tục đo đạc các vector chuyển động trong không gian 3 chiều.")
    add_p(doc, "• Cảm biến siêu âm HC-SR04 đóng vai trò quét không gian phía trước ở góc mở 15 độ, phát hiện sớm các chướng ngại vật (bậc tam cấp, bàn ghế, tường chắn) từ 3 cm đến 80 cm.")
    add_p(doc, "• Cụm chấp hành gồm Còi hú Buzzer phát âm thanh tần số cao 2000 Hz và Motor rung xúc giác ở tay cầm.")
    add_p(doc, "• Vi điều khiển trung tâm ESP32-S3 xử lý tín hiệu cảm biến thời gian thực, điều khiển cơ chế báo động tại chỗ và duy trì kênh kết nối vô tuyến BLE 5.0 đóng vai trò GATT Server.")

    add_p(doc, "2. Khối Smartphone Người Dùng Gậy (Elderly Gateway Node):")
    add_p(doc, "Đóng vai trò là trạm kết nối cổng (IoT Gateway) trung gian nhưng cực kỳ mạnh mẽ:")
    add_p(doc, "• Chạy Dịch vụ ngầm (Foreground Service) vĩnh viễn trên hệ điều hành Android, tự động kết nối lại Bluetooth với gậy mà không cần người dùng mở ứng dụng.")
    add_p(doc, "• Tận dụng chip thu GPS đa băng tần của điện thoại để cập nhật tọa độ liên tục mỗi khi người già di chuyển trên 5 mét.")
    add_p(doc, "• Đảm nhận khâu trung gian an toàn: Khi gậy phát lệnh té ngã, điện thoại phát âm thanh cảnh báo và kích hoạt bộ đếm ngược 15 giây cho phép hủy bỏ.")
    add_p(doc, "• Quản lý 2 kênh cứu nạn độc lập: Kênh Internet (đẩy dữ liệu lên Firebase) và Kênh viễn thông GSM (gửi tin nhắn SMS ngầm và quay số cuộc gọi SOS trực tiếp).")

    add_p(doc, "3. Khối Đám Mây Firebase Cloud (Cloud Backend Node):")
    add_p(doc, "• Đóng vai trò là trung tâm lưu trữ và cầu nối đồng bộ dữ liệu thời gian thực giữa hai thiết bị di động.")
    add_p(doc, "• Quản trị xác thực người dùng an toàn bằng Firebase Authentication.")
    add_p(doc, "• Lưu trữ trạng thái hoạt động tức thời của người già: cờ is_falling, trạng thái kết nối Bluetooth ble_connected, trạng thái bật tắt GPS gps_enabled, và trạng thái trực tuyến is_online.")
    add_p(doc, "• Lưu trữ lịch sử toàn bộ các sự cố ngã, các lần mất kết nối mạng và tọa độ các điểm hẹn an toàn.")

    add_p(doc, "4. Khối Smartphone Người Giám Hộ (Guardian Client Node):")
    add_p(doc, "• Cung cấp giao diện trực quan cho con cháu theo dõi tình trạng cha mẹ ở bất kỳ đâu.")
    add_p(doc, "• Hiển thị bản đồ số OpenStreetMap thời gian thực, tự động ghim vị trí của gậy và vị trí ngôi nhà.")
    add_p(doc, "• Kích hoạt còi hú báo thức âm lượng cực đại (Alarm Siren) và rung liên tục khi nhận được sự cố té ngã từ máy chủ Firebase, đảm bảo đánh thức người giám hộ ngay cả khi họ đang ngủ say.")
    add_p(doc, "• Cung cấp tính năng điều hướng 1 chạm: Mở ứng dụng Google Maps vẽ đường đi ngắn nhất đến vị trí tai nạn của người thân.")

    # 3.3 Sơ đồ nguyên lý
    add_heading2(doc, "Thiết kế phần cứng và sơ đồ nguyên lý kết nối chi tiết:")
    add_p(doc, "Sơ đồ nguyên lý kết nối chi tiết giữa vi điều khiển ESP32-S3 N16R8 và các module ngoại vi được biểu diễn trên Hình 3.2:")

    # Chèn hình 3.2
    add_fig(doc, os.path.join(FIG_DIR, 'f_schematic.png'), "Hình 3.2 Sơ đồ nguyên lý kết nối chi tiết phần cứng trên vi điều khiển ESP32-S3")

    add_heading3(doc, "Bảng phân bổ chân GPIO và tính toán linh kiện:")
    add_p(doc, "Dựa trên cấu trúc phần cứng của chip ESP32-S3, nhóm nghiên cứu đã lựa chọn và tối ưu hóa ma trận chân kết nối như trình bày trong Bảng 3.1. Các chân GPIO được bố trí nhằm tránh xung đột với các chân nạp nạp chương trình (strapping pins GPIO 0, GPIO 45, GPIO 46) và các chân kết nối bộ nhớ Flash/PSRAM ngoài (GPIO 26 đến GPIO 37):")

    # Bảng 3.1
    pin_table = [
        ("Cảm biến MPU6050", "SDA", "GPIO 8", "Giao tiếp dữ liệu I2C (Có trở kéo lên 3.3V)"),
        ("Cảm biến MPU6050", "SCL", "GPIO 9", "Xung đồng hồ I2C (Xung nhịp 400 kHz)"),
        ("Cảm biến siêu âm HC-SR04", "TRIG", "GPIO 16", "Ngõ ra kích xung siêu âm (Xung dương 12 µs)"),
        ("Cảm biến siêu âm HC-SR04", "ECHO", "GPIO 17", "Ngõ vào đo thời gian xung (INPUT_PULLDOWN)"),
        ("Cảm biến hồng ngoại E18", "OUT", "GPIO 4 / 15", "Ngõ vào số báo vật cản (NPN Open-Drain)"),
        ("Mạch đo điện áp Pin", "ADC_IN", "GPIO 4", "Ngõ vào tương tự ADC 12-bit (Cầu chia áp R1=R2=10k)"),
        ("Còi hú Buzzer 5V", "BUZZER_PIN", "GPIO 5", "Ngõ ra điều khiển âm thanh PWM (2000 Hz)"),
        ("Motor rung xúc giác", "VIBRATOR_PIN", "GPIO 6", "Ngõ ra kích mở cực cổng G của MOSFET AOD4184")
    ]
    headers = ["Khối linh kiện", "Tên chân module", "Chân kết nối ESP32", "Chức năng và đặc tính kỹ thuật"]
    col_w = [Inches(1.8), Inches(1.1), Inches(1.1), Inches(2.5)]
    add_table_data(doc, headers, pin_table, col_w, "Bảng 3.1 Bảng ánh xạ chân kết nối ngoại vi phần cứng trên ESP32-S3")

    add_p(doc, "Tính toán mạch driver điều khiển motor rung:")
    add_p(doc, "Motor rung ERM hoạt động ở điện áp Vcc = 5 V, có dòng điện định mức I_motor ≈ 120 mA, dòng khởi động đạt đỉnh I_peak ≈ 180 mA. Nhóm sử dụng MOSFET kênh N AOD4184 có điện áp đánh thủng Vds = 40 V, dòng liên tục tối đa Id = 50 A, nội trở dẫn Rds(on) = 8.5 mΩ. Khi chân GPIO 6 xuất mức logic HIGH (3.3 V), điện áp Vgs = 3.3 V đủ để mở bão hòa kênh dẫn. Tổn hao công suất dẫn trên MOSFET là cực kỳ nhỏ:")
    add_p(doc, "    P_loss = I_motor² × Rds(on) = (0.18 A)² × 0.0085 Ω ≈ 0.27 mW", style='Caption', align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(doc, "Do công suất tổn hao dưới 1 mW, MOSFET hoàn toàn mát và không cần gắn thêm tản nhiệt nhôm. Một điện trở xả R_pulldown = 10 kΩ được mắc giữa cực Gate và Source (GND) để đảm bảo MOSFET luôn khóa hoàn toàn khi ESP32-S3 đang khởi động lại hoặc khi chân GPIO ở trạng thái trở kháng cao.")

    # 3.4 Thiết kế 3D cơ khí
    add_heading2(doc, "Thiết kế cơ khí và vỏ bảo vệ gậy thông minh (Mô hình 3D):")
    add_p(doc, "Thiết kế cơ khí của cây gậy đóng vai trò quyết định đến độ bền, độ an toàn và sự thoải mái của người sử dụng. Dựa trên các nguyên lý công thái học (Ergonomics), nhóm nghiên cứu đã thiết kế mô hình 3D hoàn chỉnh cho cây gậy thông minh như minh họa trên Hình 3.3:")

    # Chèn hình 3.3 (ảnh smart_cane_3d_design.jpg có sẵn trong DH)
    add_fig(doc, os.path.join(DH_DIR, 'smart_cane_3d_design.jpg'), "Hình 3.3 Bản vẽ thiết kế 3D công thái học thân gậy và bố trí khoang cảm biến", width=Inches(4.8))

    add_p(doc, "Các điểm nhấn nổi bật trong thiết kế cơ khí của gậy:")
    add_p(doc, "1. Tay cầm công thái học (Ergonomic Handle): Được tạo hình uốn lượn theo các rãnh ngón tay của bàn tay người, sử dụng vật liệu nhựa composite bọc cao su mềm chống trơn trượt khi tay bị đổ mồ hôi. Hình dáng tay cầm dạng móc gập chữ L giúp phân bổ đều trọng lượng cơ thể lên xương cẳng tay, giảm tải áp lực dồn lên các khớp ngón tay và khớp cổ tay của người cao tuổi.")
    add_p(doc, "2. Nút bấm khẩn cấp SOS tích hợp: Được bố trí ngay tại đỉnh đầu của tay cầm với màu đỏ nổi bật. Nút bấm có kích thước lớn, vừa vặn với ngón tay cái, giúp người già có thể dễ dàng nhấn giữ trong trường hợp khẩn cấp (như cảm thấy hoa mắt, tức ngực, chóng mặt cần trợ giúp) mà không cần phải nhìn vào điện thoại.")
    add_p(doc, "3. Khoang chứa cảm biến và mạch điện tử (Sensor Pod): Được gắn chắc chắn tại phần thân trên của gậy, ngay bên dưới tay cầm. Khoang chứa được thiết kế dạng module khép kín bằng nhựa ABS in 3D chống va đập, bảo vệ toàn bộ bo mạch ESP32-S3, cảm biến MPU6050, pin Li-ion và còi báo động bên trong. Phía mặt trước của khoang bố trí hai mắt phát/thu của cảm biến siêu âm HC-SR04 hướng hơi chếch xuống một góc 15 độ so với phương thẳng đứng để tập trung phát hiện các chướng ngại vật ở cự ly bước chân tiếp theo của người già.")
    add_p(doc, "4. Đèn LED rọi đường ban đêm: Được tích hợp ở phần dưới của khoang cảm biến, rọi một chùm ánh sáng vàng dịu xuống khoảng đất phía trước chân người đi, hỗ trợ tối đa việc đi lại an toàn trong bóng tối hoặc khi người già thức dậy đi vệ sinh ban đêm.")
    add_p(doc, "5. Đế cao su chống trượt đa hướng (Anti-slip Rubber Tip): Đáy gậy được trang bị đệm cao su tổng hợp chịu mài mòn cao với bề mặt hoa lốp khía rãnh sâu, giúp tăng diện tích tiếp xúc và độ ma sát bám dính chắc chắn trên các bề mặt trơn trượt như nền gạch hoa ướt nước hay đường dốc.")

    # 3.5 Lưu đồ giải thuật
    add_heading2(doc, "Thiết kế lưu đồ giải thuật hệ thống:")
    add_heading3(doc, "Lưu đồ thuật toán chính của Firmware điều khiển trên ESP32-S3:")
    add_p(doc, "Firmware trên vi điều khiển ESP32-S3 được tổ chức thành một vòng lặp máy trạng thái liên tục với chu kỳ quét 100 ms (10 lần/giây), phối hợp nhịp nhàng giữa tác vụ phát hiện ngã, tác vụ quét vật cản và quản lý kết nối BLE. Toàn bộ lưu đồ giải thuật được mô tả chi tiết trên Hình 3.4:")

    # Chèn hình 3.4
    add_fig(doc, os.path.join(FIG_DIR, 'f_flow_firmware.png'), "Hình 3.4 Lưu đồ thuật toán chính của Firmware điều khiển trên ESP32-S3", width=Inches(5.0))

    add_p(doc, "Diễn giải quy trình hoạt động của Firmware ESP32-S3:")
    add_p(doc, "• Bước 1 (Khởi động): Khi gậy được bật nguồn, chương trình thiết lập cấu hình các chân vào/ra (pinMode), kéo mức LOW cho Trig, Motor rung và Còi hú. Chân Echo được cài đặt chế độ INPUT_PULLDOWN chống trôi tín hiệu.")
    add_p(doc, "• Bước 2 (Self-Test): Bật còi hú và motor rung đồng thời trong 200 ms để tự kiểm tra chức năng phần cứng và phát tín hiệu cho người dùng biết gậy đã sẵn sàng hoạt động.")
    add_p(doc, "• Bước 3 (Khởi tạo cảm biến & BLE): Mở cổng giao tiếp I2C ở tần số cao, kiểm tra sự hiện diện của MPU6050 và cài đặt dải đo ±8g. Khởi tạo BLE Server với tên thiết bị 'SmartCane', tạo Service và Characteristic thông báo ngã, sau đó bắt đầu phát sóng quảng bá (Advertising).")
    add_p(doc, "• Bước 4 (Quản lý kết nối BLE): Trong vòng lặp loop(), hệ thống liên tục kiểm tra trạng thái cờ deviceConnected. Nếu điện thoại bị mất kết nối (người già đi xa hoặc tắt app), hệ thống sẽ tự động phát sóng quảng bá trở lại sau 500 ms.")
    add_p(doc, "• Bước 5 (Xử lý phát hiện ngã MPU6050): Đọc dữ liệu gia tốc 3 trục từ cảm biến MPU6050, tính toán vector gia tốc tổng hợp |a|. Nếu |a| > 25.0 m/s² và cờ báo động chưa bật:")
    add_p(doc, "  - Kích hoạt còi hú tần số 2000 Hz và bật motor rung liên tục.")
    add_p(doc, "  - Gửi giá trị '1' qua BLE Characteristic Notify để thông báo lập tức lên điện thoại.")
    add_p(doc, "  - Bắt đầu ghi nhận thời điểm kích hoạt alarmStartTime.")
    add_p(doc, "  - Sau 3 giây, tự động tắt còi và rung phần cứng, gửi lại giá trị '0' qua BLE để thiết lập lại trạng thái bình thường.")
    add_p(doc, "• Bước 6 (Xử lý cảm biến siêu âm phát hiện vật cản): Nếu hệ thống không trong trạng thái báo ngã, gọi hàm getDistanceCm() đọc khoảng cách vật cản. Nếu khoảng cách nằm trong dải cảnh báo an toàn (3.0 cm ≤ d < 80.0 cm), bật motor rung cảnh báo xúc giác; ngược lại nếu đường đi thông thoáng hoặc vật cản ở xa ngoài 80 cm, tắt motor rung.")

    add_heading3(doc, "Lưu đồ hoạt động của dịch vụ chạy ngầm trên máy Người Dùng Gậy:")
    add_p(doc, "Dịch vụ ngầm (Foreground Service) trên smartphone của người cao tuổi đóng vai trò là 'bộ não xử lý sự cố' trung gian. Lưu đồ giải thuật chi tiết được trình bày trên Hình 3.5:")

    # Chèn hình 3.5
    add_fig(doc, os.path.join(FIG_DIR, 'f_flow_elderly.png'), "Hình 3.5 Lưu đồ hoạt động của dịch vụ chạy ngầm trên máy Người Dùng Gậy", width=Inches(5.0))

    add_p(doc, "Cơ chế bảo vệ ngầm và cứu hộ 15 giây đa tầng:")
    add_p(doc, "1. Tự động kết nối lại (Auto-Reconnect): Khi khởi động, dịch vụ kiểm tra bộ nhớ SharedPreferences. Nếu đã từng ghép nối gậy trước đó, dịch vụ đọc mã MAC và trực tiếp gọi lệnh device.connect() theo chu kỳ 5 giây, không cần quét quảng bá tốn pin. Ngay khi kết nối thành công, tự động gọi discoverServices() và kích hoạt lắng nghe Characteristic Notify (UUID ...26a9).")
    add_p(doc, "2. Duy trì luồng GPS độ chính xác cao: Đăng ký lắng nghe getPositionStream() với độ phân giải khoảng cách 5 mét. Mỗi khi người già bước đi, tọa độ mới nhất và dấu thời gian ServerValue.timestamp được cập nhật lên nhánh /users/{uid} trên Firebase.")
    add_p(doc, "3. Tiếp nhận sự cố ngã và kích hoạt bộ đếm ngược 15 giây: Khi nhận được byte giá trị '1' từ BLE, dịch vụ lập tức kích hoạt cờ isFalling = true, ghi nhận thời điểm ngã cục bộ local_fall_timestamp và đồng bộ lên Firebase. Đồng thời, khởi động Timer 15 giây và hiển thị màn hình báo ngã khẩn cấp màu đỏ với nút 'Tôi ổn - Hủy báo động'.")
    add_p(doc, "4. Xử lý sau 15 giây (Hết giờ cứu nạn): Nếu người già không bấm nút hủy (do ngất xỉu, bất tỉnh hoặc chấn thương nặng), hàm callGuardian() sẽ được kích hoạt tự động:")
    add_p(doc, "  - Tạo đường link bản đồ: https://maps.google.com/?q=lat,lng")
    add_p(doc, "  - Gọi thư viện BackgroundSms.sendMessage() tự động gửi tin nhắn SMS ngầm: 'Nguoi gia bi nga! Vi tri: [Link Maps]' đến số điện thoại người giám hộ đã lưu trong hồ sơ (thử tuần tự khe SIM 1, SIM 2 và SIM mặc định).")
    add_p(doc, "  - Kích hoạt quay số điện thoại SOS trực tiếp đến số người giám hộ.")

    add_heading3(doc, "Lưu đồ hoạt động giám sát và cảnh báo trên máy Người Giám Hộ:")
    add_p(doc, "Ứng dụng phía người chăm sóc hoạt động với lưu đồ giải thuật như minh họa trên Hình 3.6:")

    # Chèn hình 3.6
    add_fig(doc, os.path.join(FIG_DIR, 'f_flow_guardian.png'), "Hình 3.6 Lưu đồ hoạt động giám sát và cảnh báo trên máy Người Giám Hộ", width=Inches(5.0))

    add_p(doc, "Quy trình giám sát thời gian thực phía Người Giám Hộ:")
    add_p(doc, "• Ứng dụng liên tục duy trì lắng nghe sự kiện onValue() từ Firebase Realtime Database.")
    add_p(doc, "• Nếu phát hiện cờ is_falling == true: Hệ thống kích hoạt dịch vụ chuông báo động thức tỉnh (sử dụng FlutterRingtonePlayer.playAlarm() với âm lượng tối đa, bất chấp điện thoại đang ở chế độ im lặng), đồng thời đẩy thông báo khẩn cấp toàn màn hình (Full Screen Intent) với mức ưu tiên tuyệt đối.")
    add_p(doc, "• Nếu phát hiện cờ is_online == false hoặc gps_enabled == false: Giao diện ngay lập tức hiển thị dải banner màu đỏ cảnh báo: 'Cảnh báo: Người già đã mất kết nối mạng (hoặc đã tắt GPS)'. Khi mạng được kết nối trở lại, hệ thống tự động ghi nhận thời gian hồi phục vào lịch sử sự cố.")
    add_p(doc, "• Người giám hộ có thể chạm vào nút 'Chỉ đường' để mở trực tiếp ứng dụng Google Maps điều hướng, hoặc bấm nút 'Tắt báo động' để tắt còi hú và cập nhật trạng thái đã xử lý lên cơ sở dữ liệu.")

    # 3.6 Giao diện phần mềm
    add_heading2(doc, "Thiết kế phần mềm ứng dụng di động Flutter:")
    add_heading3(doc, "Cấu trúc module và kiến trúc mã nguồn ứng dụng:")
    add_p(doc, "Mã nguồn ứng dụng Flutter Smart Cane được tổ chức một cách khoa học và module hóa cao theo cấu trúc thư mục chuẩn:")
    add_p(doc, "• lib/main.dart: Điểm khởi nhập (Entry Point) của ứng dụng, cấu hình khởi tạo Firebase, hệ thống dịch vụ ngầm Background Service, quản lý chuyển đổi Theme sáng/tối và điều hướng xác thực AuthWrapper.")
    add_p(doc, "• lib/theme/app_theme.dart: Định nghĩa bảng màu chuẩn (AppThemeColors) cho cả 2 chế độ Dark Mode (nền xám đen #121212 tinh tế, thẻ #1E1E1E, điểm nhấn xanh lá #00C853, đỏ cảnh báo #FF3D00, xanh lam #29B6F6) và Light Mode.")
    add_p(doc, "• lib/screens/: Chứa toàn bộ các màn hình chức năng độc lập của ứng dụng:")
    add_p(doc, "  - login_screen.dart & forgot_password_screen.dart: Màn hình đăng nhập, tạo tài khoản và khôi phục mật khẩu qua Email Firebase.")
    add_p(doc, "  - role_selection_screen.dart: Màn hình phòng chờ (Lobby) điều phối và ghép nối đúng 2 thiết bị vào cùng một tài khoản gia đình.")
    add_p(doc, "  - elderly_screen.dart: Màn hình giao diện tối giản, trực quan dành riêng cho người cao tuổi sử dụng gậy.")
    add_p(doc, "  - dashboard_screen.dart: Màn hình Dashboard trung tâm giám sát bản đồ thời gian thực dành cho người giám hộ.")
    add_p(doc, "  - alert_history_screen.dart: Màn hình xem nhật ký và chi tiết toàn bộ các sự cố cảnh báo.")
    add_p(doc, "  - profile_screen.dart: Màn hình quản lý thông tin cá nhân, số điện thoại khẩn cấp và đổi mật khẩu.")
    add_p(doc, "• lib/widgets/: Chứa các widget dùng chung như thanh ngăn kéo điều hướng app_drawer.dart và thẻ thông số info_card.dart.")

    add_heading3(doc, "Giao diện Đăng nhập và Ghép nối vai trò 2 thiết bị:")
    add_p(doc, "Hình 3.7 minh họa giao diện màn hình Đăng nhập và màn hình Ghép nối vai trò (Role Selection). Điểm đặc biệt trong kiến trúc của hệ thống là cơ chế 'Single Account - Dual Roles' (Một tài khoản - Hai vai trò): Cả gia đình chỉ cần đăng ký duy nhất một tài khoản Email/Password trên Firebase. Khi chiếc điện thoại thứ nhất đăng nhập và chọn vai trò 'Người Giám Hộ', hệ thống lưu deviceId của máy đó lên Firebase. Khi chiếc điện thoại thứ hai đăng nhập, ứng dụng tự động nhận diện vai trò 'Người Dùng Gậy' còn lại để hoàn tất ghép nối.")

    # Chèn hình 3.7
    add_fig(doc, os.path.join(FIG_DIR, 'f_ui_role.png'), "Hình 3.7 Giao diện màn hình Đăng nhập và Ghép nối vai trò thiết bị")

    add_heading3(doc, "Giao diện Người Dùng Gậy (Trạng thái bình thường và Báo ngã):")
    add_p(doc, "Giao diện dành cho người cao tuổi (Hình 3.8) được thiết kế theo triết lý tối giản hóa với các nút bấm kích thước lớn, độ tương phản màu sắc cao, dễ đọc đối với mắt người già. Ở trạng thái bình thường, màn hình hiển thị thanh trạng thái kết nối Bluetooth với gậy, luồng bản đồ và hai nút bấm lớn '🏠 VỀ NHÀ' và '📍 ĐIỂM HẸN'. Khi người già bấm vào nút 'Về nhà', ứng dụng sẽ tự động gọi Intent mở ứng dụng Google Maps ở chế độ đi bộ (mode=w) dẫn đường thẳng về nhà.")
    add_p(doc, "Khi có sự cố té ngã xảy ra, màn hình lập tức chuyển sang chế độ khẩn cấp với nền đỏ rực rỡ, đồng hồ đếm ngược 15 giây và nút bấm cực đại 'TÔI ỔN - HỦY BÁO ĐỘNG', giúp người già dễ dàng chạm tay hủy sự cố nếu chỉ là va chạm nhẹ.")

    # Chèn hình 3.8
    add_fig(doc, os.path.join(FIG_DIR, 'f_ui_elderly.png'), "Hình 3.8 Giao diện màn hình Người Dùng Gậy ở trạng thái bình thường và trạng thái té ngã")

    add_heading3(doc, "Giao diện Người Giám Hộ (Dashboard bản đồ và Lịch sử cảnh báo):")
    add_p(doc, "Màn hình Dashboard phía Người Giám Hộ (Hình 3.9) tích hợp bản đồ số Flutter Map (sử dụng nguồn dữ liệu gạch bản đồ OpenStreetMap mượt mà). Trên bản đồ hiển thị trực tiếp marker gậy thông minh của người già, marker địa chỉ nhà và marker điểm hẹn. Người giám hộ có thể chạm trực tiếp lên bất kỳ điểm nào trên bản đồ để cập nhật vị trí nhà mới hoặc điểm hẹn mới cho cha mẹ.")
    add_p(doc, "Màn hình Lịch sử cảnh báo (Alert History) lưu trữ chi tiết từng sự cố theo thời gian thực: thời điểm phát hiện ngã, tọa độ GPS, thời gian mất mạng Internet và thời điểm máy người già kết nối mạng trở lại thành công, kèm theo nút 'Chỉ đường' mở ngay vị trí tương ứng trên Google Maps.")

    # Chèn hình 3.9
    add_fig(doc, os.path.join(FIG_DIR, 'f_ui_guardian.png'), "Hình 3.9 Giao diện màn hình Dashboard giám sát bản đồ và Lịch sử sự cố của Giám hộ")

    # Bảng 3.2
    add_heading3(doc, "Cấu trúc dữ liệu JSON trên Firebase Realtime Database:")
    add_p(doc, "Cấu trúc dữ liệu cây JSON được thiết kế tối ưu, gọn nhẹ nhằm giảm thiểu tối đa lưu lượng dữ liệu truyền qua mạng di động, được mô tả chi tiết trong Bảng 3.2:")

    fb_data = [
        ("users/{uid}/is_falling", "Boolean", "true / false", "Cờ báo trạng thái té ngã khẩn cấp từ gậy"),
        ("users/{uid}/latitude", "Float (Double)", "10.827530", "Vĩ độ GPS thời gian thực của người dùng gậy"),
        ("users/{uid}/longitude", "Float (Double)", "106.678910", "Kinh độ GPS thời gian thực của người dùng gậy"),
        ("users/{uid}/ble_connected", "Boolean", "true / false", "Trạng thái kết nối Bluetooth giữa gậy và điện thoại"),
        ("users/{uid}/ble_enabled", "Boolean", "true / false", "Trạng thái Bật/Tắt công tắc Bluetooth trên điện thoại"),
        ("users/{uid}/gps_enabled", "Boolean", "true / false", "Trạng thái Bật/Tắt dịch vụ Vị trí (GPS) trên điện thoại"),
        ("users/{uid}/is_online", "Boolean", "true / false", "Trạng thái kết nối Internet (Presence System qua socket)"),
        ("users/{uid}/guardianPhone", "String", "0938xxxxxx", "Số điện thoại khẩn cấp của người giám hộ dùng gọi/SMS"),
        ("users/{uid}/local_fall_timestamp", "Integer (Epoch ms)", "1773562800000", "Thời điểm ngã cục bộ đo đếm độ trễ khi mất mạng"),
        ("users/{uid}/home_location", "Map {lat, lng}", "{lat: ..., lng: ...}", "Tọa độ địa chỉ nhà do người giám hộ thiết lập"),
        ("users/{uid}/alert_history/{id}", "Map Object", "{message, time, lat...}", "Nhật ký lịch sử từng sự kiện té ngã hoặc mất mạng")
    ]
    headers = ["Đường dẫn trường dữ liệu (Path)", "Kiểu dữ liệu", "Giá trị mẫu", "Ý nghĩa chức năng trong hệ thống"]
    col_w = [Inches(2.0), Inches(1.1), Inches(1.2), Inches(2.2)]
    add_table_data(doc, headers, fb_data, col_w, "Bảng 3.2 Cấu trúc dữ liệu JSON lưu trữ thời gian thực trên Firebase Realtime Database")

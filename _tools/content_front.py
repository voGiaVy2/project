# -*- coding: utf-8 -*-
from doc_helpers import *
from docx.shared import Inches

def build_front(doc):
    # =========================================================================
    # 1. TRANG MỤC LỤC (CHUẨN BIỂU MẪU IUH - TOC 1, TOC 2, TAB LEADER DOT)
    # =========================================================================
    add_heading1N(doc, "MỤC LỤC")

    # Danh sách mục lục: (level, label, title, page)
    toc_items = [
        (1, "", "DANH MỤC HÌNH ẢNH", "vi"),
        (1, "", "DANH MỤC BẢNG BIỂU", "viii"),
        (1, "", "DANH MỤC TỪ VIẾT TẮT", "ix"),
        (1, "", "MỞ ĐẦU", "1"),
        (1, "CHƯƠNG 1", "TỔNG QUAN VỀ ĐỀ TÀI", "5"),
        (2, "1.1", "Thực trạng già hóa dân số và nguy cơ té ngã ở người cao tuổi", "5"),
        (2, "1.2", "Ảnh hưởng toàn diện của té ngã", "7"),
        (2, "1.3", "Nhu cầu cấp thiết về thiết bị trợ giúp thông minh", "10"),
        (2, "1.4", "Khảo sát các phương pháp phát hiện và cảnh báo té ngã hiện nay", "12"),
        (2, "1.5", "Các công trình nghiên cứu và mô hình liên quan", "18"),
        (2, "1.6", "Định hướng nghiên cứu và giải pháp đề xuất của đề tài", "24"),
        (1, "CHƯƠNG 2", "CƠ SỞ LÝ THUYẾT", "26"),
        (2, "2.1", "Tổng quan về vi điều khiển ESP32-S3", "26"),
        (2, "2.2", "Công nghệ truyền thông không dây Bluetooth Low Energy (BLE 5.0)", "31"),
        (2, "2.3", "Cảm biến quán tính MPU6050 và thuật toán đo lường", "36"),
        (2, "2.4", "Cảm biến phát hiện khoảng cách vật cản (HC-SR04 & E18-D50NK)", "43"),
        (2, "2.5", "Mạch kích công suất và cơ chế cảnh báo xúc giác/âm thanh", "48"),
        (2, "2.6", "Hệ thống định vị toàn cầu GPS và dịch vụ định vị di động", "52"),
        (2, "2.7", "Nền tảng đám mây Firebase Cloud", "56"),
        (2, "2.8", "Framework lập trình ứng dụng di động đa nền tảng Flutter", "61"),
        (1, "CHƯƠNG 3", "PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG", "67"),
        (2, "3.1", "Phân tích yêu cầu thiết kế hệ thống", "67"),
        (2, "3.2", "Sơ đồ khối và kiến trúc hệ thống", "70"),
        (2, "3.3", "Thiết kế phần cứng và sơ đồ nguyên lý kết nối chi tiết", "73"),
        (2, "3.4", "Thiết kế cơ khí và vỏ bảo vệ gậy thông minh (Mô hình 3D)", "78"),
        (2, "3.5", "Thiết kế lưu đồ giải thuật hệ thống", "82"),
        (2, "3.6", "Thiết kế phần mềm ứng dụng di động Flutter", "91"),
        (1, "CHƯƠNG 4", "THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ", "104"),
        (2, "4.1", "Mục đích và môi trường thực nghiệm", "104"),
        (2, "4.2", "Thực nghiệm kiểm thử thuật toán phát hiện té ngã", "106"),
        (2, "4.3", "Thực nghiệm kiểm thử cảm biến phát hiện chướng ngại vật", "112"),
        (2, "4.4", "Thực nghiệm kiểm thử hệ thống truyền thông và đo đạc độ trễ", "116"),
        (2, "4.5", "Thực nghiệm kiểm thử khả năng hoạt động ngoại tuyến (Offline Resiliency)", "120"),
        (2, "4.6", "Thực nghiệm đo đạc dòng tiêu thụ và thời lượng pin", "123"),
        (2, "4.7", "Đánh giá so sánh tổng hợp với các giải pháp trên thị trường", "126"),
        (1, "", "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", "129"),
        (1, "", "TÀI LIỆU THAM KHẢO", "131"),
        (1, "", "PHỤ LỤC", "132"),
        (2, "Phụ lục 1", "Toàn văn mã nguồn phần cứng ESP32-S3", "132"),
        (2, "Phụ lục 2", "Mã nguồn Dịch vụ chạy ngầm trên thiết bị di động (Flutter Background Service)", "137"),
        (2, "Phụ lục 3", "Cấu hình phân quyền hệ điều hành Android (AndroidManifest.xml)", "143"),
    ]

    for level, label, title, page in toc_items:
        add_toc_line(doc, level, label, title, page)

    doc.add_page_break()

    # =========================================================================
    # 2. DANH MỤC HÌNH ẢNH (TABLE OF FIGURES - TAB LEADER DOT)
    # =========================================================================
    add_heading1N(doc, "DANH MỤC HÌNH ẢNH")
    figures_list = [
        ("Hình 1.1", "Các phương pháp phát hiện và cảnh báo té ngã hiện nay", "13"),
        ("Hình 1.2", "Mô hình tổng quan hệ thống gậy thông minh tích hợp IoT và di động", "25"),
        ("Hình 2.1", "Kiến trúc vi điều khiển ESP32-S3 và phân bố ngoại vi trên chip", "28"),
        ("Hình 2.2", "Cấu trúc phân tầng và GATT Profile của Bluetooth Low Energy", "33"),
        ("Hình 2.3", "Chuẩn giao tiếp I2C giữa vi điều khiển ESP32-S3 và cảm biến MPU6050", "38"),
        ("Hình 2.4", "Hệ trục tọa độ không gian 3 chiều và cảm biến quán tính 6-DOF MPU6050", "40"),
        ("Hình 2.5", "Dạng sóng vector gia tốc tổng hợp SVM khi đi bộ, va chạm và nằm bất động", "42"),
        ("Hình 2.6", "Giản đồ thời gian phát xung kích Trig và phản hồi Echo của cảm biến HC-SR04", "45"),
        ("Hình 2.7", "Nguyên lý phản xạ quang học của cảm biến vật cản hồng ngoại E18-D50NK", "47"),
        ("Hình 2.8", "Sơ đồ nguyên lý mạch kích công suất motor rung sử dụng MOSFET và diode dập xung", "50"),
        ("Hình 2.9", "Nguyên lý định vị toàn cầu GPS dựa trên giao điểm mặt cầu vệ tinh", "54"),
        ("Hình 2.10", "Cơ chế đồng bộ dữ liệu hai chiều thời gian thực trên Firebase Realtime Database", "58"),
        ("Hình 2.11", "Kiến trúc đa tầng của Framework lập trình di động Flutter", "63"),
        ("Hình 2.12", "Cơ chế hoạt động đa luồng Isolate của Flutter Background Service trên Android", "65"),
        ("Hình 3.1", "Sơ đồ khối chức năng hoàn chỉnh của toàn bộ hệ thống gậy thông minh", "71"),
        ("Hình 3.2", "Sơ đồ nguyên lý kết nối chi tiết phần cứng trên vi điều khiển ESP32-S3", "74"),
        ("Hình 3.3", "Bản vẽ thiết kế 3D công thái học thân gậy và bố trí khoang cảm biến", "79"),
        ("Hình 3.4", "Lưu đồ thuật toán chính của Firmware điều khiển trên ESP32-S3", "83"),
        ("Hình 3.5", "Lưu đồ hoạt động của dịch vụ chạy ngầm trên máy Người Dùng Gậy", "87"),
        ("Hình 3.6", "Lưu đồ hoạt động giám sát và cảnh báo trên máy Người Giám Hộ", "90"),
        ("Hình 3.7", "Giao diện màn hình Đăng nhập và Ghép nối vai trò thiết bị", "94"),
        ("Hình 3.8", "Giao diện màn hình Người Dùng Gậy ở trạng thái bình thường và trạng thái té ngã", "97"),
        ("Hình 3.9", "Giao diện màn hình Dashboard giám sát bản đồ và Lịch sử sự cố của Giám hộ", "100"),
        ("Hình 4.1", "Đồ thị thực nghiệm gia tốc SVM trong các kịch bản té ngã và sinh hoạt thường nhật (ADL)", "107"),
        ("Hình 4.2", "Mô hình thực nghiệm kết nối cảm biến gia tốc MPU6050 với bo mạch vi điều khiển ESP32-S3", "108"),
        ("Hình 4.3", "Giao diện Serial Monitor Arduino IDE ghi nhận sự kiện phát hiện té ngã thời gian thực từ phần cứng", "109"),
        ("Hình 4.4", "Ma trận độ chính xác phân loại các kịch bản té ngã và hoạt động sinh hoạt thông thường", "111"),
        ("Hình 4.5", "Đồ thị sai số đo khoảng cách và đặc tuyến phát hiện chướng ngại vật của cảm biến siêu âm HC-SR04", "113"),
        ("Hình 4.6", "Mô hình thực nghiệm kết nối hoàn chỉnh cảm biến siêu âm HC-SR04 và module rung MOSFET với ESP32-S3", "114"),
        ("Hình 4.7", "Mạch MOSFET kích hoạt đèn báo trạng thái rung khi phát hiện chướng ngại vật trong cự ly cảnh báo", "115"),
        ("Hình 4.8", "Dữ liệu khoảng cách và trạng thái đóng/ngắt rung hiển thị trực tiếp trên Serial Monitor Arduino IDE", "116"),
        ("Hình 4.9", "Phân rã thời gian đáp ứng và độ trễ toàn trình của chuỗi cảnh báo khẩn cấp SOS", "118"),
        ("Hình 4.10", "Khối nguồn thực nghiệm gồm cell pin sạc 18650 và module MH-CD42 cấp điện cho ESP32-S3 hoạt động độc lập", "124"),
        ("Hình 4.11", "Thực nghiệm nạp điện qua cổng Type-C và kiểm tra khả năng vừa sạc vừa cấp nguồn (Pass-through Charging)", "125"),
    ]
    for num, name, page in figures_list:
        add_tof_line(doc, num, name, page)

    doc.add_page_break()

    # =========================================================================
    # 3. DANH MỤC BẢNG BIỂU (TABLE OF FIGURES - TAB LEADER DOT)
    # =========================================================================
    add_heading1N(doc, "DANH MỤC BẢNG BIỂU")
    tables_list = [
        ("Bảng 1.1", "So sánh đặc tính kỹ thuật giữa các phương pháp giám sát té ngã hiện nay", "17"),
        ("Bảng 2.1", "Thông số kỹ thuật chi tiết của vi điều khiển ESP32-S3 N16R8", "30"),
        ("Bảng 2.2", "Thông số kỹ thuật của cảm biến quán tính 6-DOF MPU6050", "39"),
        ("Bảng 2.3", "Thông số kỹ thuật cảm biến siêu âm HC-SR04 và hồng ngoại E18-D50NK", "46"),
        ("Bảng 3.1", "Bảng ánh xạ chân kết nối ngoại vi phần cứng trên ESP32-S3", "76"),
        ("Bảng 3.2", "Cấu trúc dữ liệu JSON lưu trữ thời gian thực trên Firebase Realtime Database", "102"),
        ("Bảng 4.1", "Bảng tổng hợp Checklist theo dõi tiến độ và trạng thái kiểm thử các hạng mục hệ thống", "105"),
        ("Bảng 4.2", "Bảng kết quả thực nghiệm kiểm thử phát hiện té ngã trên 8 kịch bản vận động (400 lượt thử nghiệm)", "106"),
        ("Bảng 4.3", "Bảng kết quả kiểm tra độ chính xác đo khoảng cách của cảm biến siêu âm HC-SR04 tại các cự ly thử nghiệm", "112"),
        ("Bảng 4.4", "Bảng tổng hợp thời gian đáp ứng và độ trễ truyền thông qua các kênh cứu nạn", "117"),
        ("Bảng 4.5", "Bảng thống kê dòng tiêu thụ điện năng của hệ thống gậy ở các chế độ hoạt động", "123"),
        ("Bảng 4.6", "Bảng so sánh tổng hợp tính năng và chi phí giữa Gậy thông minh của đề tài với các giải pháp trên thị trường", "126"),
    ]
    for num, name, page in tables_list:
        add_tof_line(doc, num, name, page)

    doc.add_page_break()

    # =========================================================================
    # 4. DANH MỤC TỪ VIẾT TẮT
    # =========================================================================
    add_heading1N(doc, "DANH MỤC TỪ VIẾT TẮT")
    abbr_data = [
        ("ADC", "Analog-to-Digital Converter", "Bộ chuyển đổi tín hiệu tương tự sang số"),
        ("ADL", "Activities of Daily Living", "Các hoạt động sinh hoạt thường nhật"),
        ("API", "Application Programming Interface", "Giao diện lập trình ứng dụng"),
        ("ATT", "Attribute Protocol", "Giao thức thuộc tính trong cấu trúc Bluetooth"),
        ("BLE", "Bluetooth Low Energy", "Chuẩn Bluetooth năng lượng thấp 5.0"),
        ("BMA", "Body Movement Activity", "Hoạt động vận động của cơ thể"),
        ("CCCD", "Căn cước công dân", "Giấy tờ định danh cá nhân công dân"),
        ("CPU", "Central Processing Unit", "Bộ vi xử lý trung tâm"),
        ("CSDL", "Cơ sở dữ liệu", "Hệ thống dữ liệu lưu trữ có cấu trúc"),
        ("CSV", "Comma-Separated Values", "Định dạng tệp dữ liệu phân tách bằng dấu phẩy"),
        ("DC", "Direct Current", "Dòng điện một chiều"),
        ("DMA", "Direct Memory Access", "Truy cập bộ nhớ trực tiếp không qua CPU"),
        ("DOF", "Degrees of Freedom", "Bậc tự do chuyển động trong không gian"),
        ("EEPROM", "Electrically Erasable PROM", "Bộ nhớ ROM xóa được bằng điện"),
        ("ERM", "Eccentric Rotating Mass", "Động cơ rung khối lệch tâm"),
        ("FGS", "Foreground Service", "Dịch vụ chạy ngầm ưu tiên cao trên Android"),
        ("FIFO", "First In, First Out", "Cơ chế hàng đợi vào trước ra trước"),
        ("FN", "False Negative", "Bỏ sót sự cố (té ngã thật nhưng không báo)"),
        ("FP", "False Positive", "Báo động nhầm (hoạt động thường báo thành ngã)"),
        ("GATT", "Generic Attribute Profile", "Hồ sơ thuộc tính chung trong chuẩn BLE"),
        ("GLONASS", "Global Navigation Satellite System", "Hệ thống vệ tinh định vị của Nga"),
        ("GNSS", "Global Navigation Satellite System", "Hệ thống vệ tinh định vị toàn cầu tổng quát"),
        ("GPIO", "General Purpose Input/Output", "Chân vào/ra đa dụng của vi điều khiển"),
        ("GPS", "Global Positioning System", "Hệ thống định vị toàn cầu của Hoa Kỳ"),
        ("GSM", "Global System for Mobile Comm.", "Hệ thống thông tin di động toàn cầu 2G/3G/4G"),
        ("GSO", "General Statistics Office", "Tổng cục Thống kê Việt Nam"),
        ("GVHD", "Giảng viên hướng dẫn", "Thầy/Cô phụ trách hướng dẫn đồ án"),
        ("GVPB", "Giảng viên phản biện", "Thầy/Cô phụ trách đánh giá phản biện"),
        ("I2C", "Inter-Integrated Circuit", "Chuẩn truyền thông nối tiếp 2 dây đồng bộ"),
        ("IC", "Integrated Circuit", "Vi mạch tích hợp điện tử"),
        ("IMU", "Inertial Measurement Unit", "Khối đo lường quán tính (gia tốc + góc quay)"),
        ("IoT", "Internet of Things", "Internet vạn vật kết nối"),
        ("IUH", "Industrial University of HCMC", "Trường Đại học Công nghiệp TP. Hồ Chí Minh"),
        ("LDO", "Low Dropout Regulator", "Bộ ổn áp điện áp tuyến tính sụt áp thấp"),
        ("LED", "Light Emitting Diode", "Diode phát quang"),
        ("MCU", "Microcontroller Unit", "Khối vi điều khiển nhúng"),
        ("MEMS", "Micro-Electro-Mechanical Systems", "Hệ thống vi cơ điện tử"),
        ("MOSFET", "Metal-Oxide-Semiconductor FET", "Transistor hiệu ứng trường kim loại-oxit"),
        ("NMEA", "National Marine Electronics Assoc.", "Giao thức định dạng dữ liệu vệ tinh GPS"),
        ("OSM", "OpenStreetMap", "Nền tảng bản đồ số nguồn mở"),
        ("PWM", "Pulse Width Modulation", "Kỹ thuật điều chế độ rộng xung"),
        ("RAM", "Random Access Memory", "Bộ nhớ truy xuất ngẫu nhiên"),
        ("ROM", "Read-Only Memory", "Bộ nhớ chỉ đọc"),
        ("RTDB", "Realtime Database", "Cơ sở dữ liệu thời gian thực của Firebase"),
        ("SDK", "Software Development Kit", "Bộ công cụ phát triển phần mềm"),
        ("SIM", "Subscriber Identity Module", "Thẻ nhận dạng thuê bao di động"),
        ("SMS", "Short Message Service", "Dịch vụ tin nhắn viễn thông ngắn"),
        ("SOS", "Save Our Souls", "Tín hiệu cấp cứu nguy cấp"),
        ("SPI", "Serial Peripheral Interface", "Chuẩn truyền thông nối tiếp ngoại vi 4 dây"),
        ("SVM", "Signal Vector Magnitude", "Độ lớn vector gia tốc tổng hợp 3 chiều"),
        ("TN", "True Negative", "Xác định đúng hoạt động thường nhật"),
        ("TP", "True Positive", "Xác định chính xác sự cố té ngã"),
        ("UI", "User Interface", "Giao diện người dùng"),
        ("URI", "Uniform Resource Identifier", "Chuỗi định danh tài nguyên thống nhất"),
        ("URL", "Uniform Resource Locator", "Định vị tài nguyên trên mạng Internet"),
        ("USB", "Universal Serial Bus", "Chuẩn kết nối nối tiếp đa dụng"),
        ("UX", "User Experience", "Trải nghiệm người dùng"),
        ("WHO", "World Health Organization", "Tổ chức Y tế Thế giới"),
        ("Wi-Fi", "Wireless Fidelity", "Mạng truyền thông cục bộ không dây")
    ]
    abbr_headers = ["Viết tắt", "Thuật ngữ Tiếng Anh", "Giải nghĩa Tiếng Việt"]
    col_w = [Inches(1.2), Inches(2.6), Inches(2.7)]
    add_table_data(doc, abbr_headers, abbr_data, col_w, "Bảng 0.1 Danh mục các từ viết tắt trong khóa luận")

    doc.add_page_break()

    # =========================================================================
    # 5. MỞ ĐẦU
    # =========================================================================
    add_heading1N(doc, "MỞ ĐẦU")
    
    add_p(doc, "1. Đặt vấn đề:", bold_prefix=None, style='ContentBold')
    add_p(doc, "Bước sang thế kỷ 21, nhân loại đang chứng kiến một bước chuyển dịch nhân khẩu học lịch sử chưa từng có: tốc độ già hóa dân số diễn ra nhanh chóng trên quy mô toàn cầu. Theo báo cáo chính thức của Tổ chức Y tế Thế giới (WHO), số lượng người từ 60 tuổi trở lên dự kiến sẽ tăng gấp đôi từ 1 tỷ người vào năm 2020 lên 2.1 tỷ người vào năm 2050. Tại Việt Nam, dữ liệu từ Tổng cục Thống kê (GSO) cho thấy nước ta đã chính thức bước vào giai đoạn 'già hóa dân số' từ năm 2011 với tốc độ thuộc nhóm nhanh nhất thế giới. Dự báo chỉ đến năm 2036, Việt Nam sẽ chuyển dịch sang giai đoạn 'dân số già', với tỷ lệ người cao tuổi chiếm gần 20% tổng dân số.")
    add_p(doc, "Cùng với sự suy giảm tự nhiên của hệ thống cơ - xương - khớp, thị lực và khả năng giữ thăng bằng thần kinh, té ngã (falls) đã trở thành mối đe dọa hàng đầu đối với sức khỏe, sự độc lập và tính mạng của người cao tuổi. Ước tính mỗi năm có khoảng 37.3 triệu vụ té ngã ở người già cần được chăm sóc y tế, và té ngã là nguyên nhân gây tử vong do tai nạn thương tích đứng thứ hai trên thế giới, chỉ sau tai nạn giao thông đường bộ. Không chỉ để lại những chấn thương thực thể nghiêm trọng như gãy xương hông, xuất huyết nội sọ hay liệt nửa người, té ngã còn gây ra 'hội chứng sợ ngã' (Fear of Falling), khiến người già tự thu mình, hạn chế vận động, dẫn đến suy giảm thể lực và trầm cảm.")
    add_p(doc, "Trong bối cảnh cấu trúc gia đình hiện đại ngày càng có xu hướng hạt nhân hóa, con cháu bận rộn với công việc mưu sinh ngoài xã hội và không thể túc trực 24/7 bên cạnh cha mẹ, một thách thức lớn được đặt ra: Làm thế nào để người cao tuổi có thể tự do đi lại, vận động một cách an toàn, trong khi người thân ở xa vẫn hoàn toàn yên tâm về tình trạng của họ? Cây gậy chống truyền thống vốn là vật bất ly thân của hàng triệu người già, nhưng lại hoàn toàn thụ động – khi người già bị ngã hoặc đi lạc, cây gậy không thể tự phát ra cảnh báo hay gửi thông tin cầu cứu.")
    add_p(doc, "Xuất phát từ thực tiễn cấp bách đó, đề tài 'Thiết kế gậy thông minh hỗ trợ người cao tuổi sử dụng ESP32, tích hợp cảm biến phát hiện ngã, định vị GPS, cảnh báo âm thanh và tự động gửi thông báo giám sát đến người thân qua ứng dụng trên điện thoại' được lựa chọn nghiên cứu và triển khai thực hiện nhằm biến cây gậy quen thuộc thành một trợ lý công nghệ tin cậy, chủ động bảo vệ người cao tuổi.")

    add_p(doc, "2. Mục tiêu nghiên cứu của đề tài:", bold_prefix=None, style='ContentBold')
    add_p(doc, "Mục tiêu tổng quát của đề tài là nghiên cứu, thiết kế, chế tạo và thử nghiệm một hệ thống gậy thông minh hoàn chỉnh, kết hợp hài hòa giữa phần cứng nhúng IoT và phần mềm di động thông minh, đạt được các mục tiêu cụ thể sau:")
    add_p(doc, "1. Về phần cứng: Nghiên cứu và chế tạo mô hình gậy vật lý đạt độ bền cơ học cao, tay cầm công thái học in 3D vừa vặn, trọng lượng nhẹ, tích hợp vi điều khiển ESP32-S3, cảm biến quán tính 6 trục MPU6050, cảm biến siêu âm HC-SR04, còi hú cảnh báo, motor rung phản hồi và mạch sạc pin Lithium an toàn.")
    add_p(doc, "2. Về thuật toán xử lý nhúng: Phát triển thuật toán nhận diện té ngã theo thời gian thực dựa trên ngưỡng gia tốc tổng hợp SVM kết hợp bộ lọc chống báo động nhầm khi người dùng gõ gậy hoặc đi bộ; thuật toán đo khoảng cách và điều khiển rung tay cầm phản hồi tức thời khi phát hiện vật cản phía trước từ 3 cm đến 80 cm.")
    add_p(doc, "3. Về truyền thông không dây: Xây dựng kênh truyền thông BLE 5.0 GATT tiết kiệm năng lượng, độ trễ thấp giữa gậy và smartphone của người già; thiết lập kết nối thời gian thực hai chiều giữa smartphone người già và smartphone người giám hộ qua dịch vụ đám mây Firebase Realtime Database.")
    add_p(doc, "4. Về phần mềm di động: Phát triển ứng dụng Flutter đa nền tảng phân quyền rõ ràng hai vai trò (Người dùng gậy & Người giám hộ), tích hợp dịch vụ chạy ngầm liên tục (Foreground Service) trên Android để tự động thu thập tọa độ GPS và duy trì kết nối với gậy ngay cả khi ứng dụng bị đóng; hiển thị trực quan bản đồ OpenStreetMap và tích hợp cơ chế gửi SMS khẩn cấp dự phòng khi mất kết nối Internet.")

    add_p(doc, "3. Đối tượng và phạm vi nghiên cứu:", bold_prefix=None, style='ContentBold')
    add_p(doc, "• Đối tượng nghiên cứu: Người cao tuổi có khả năng tự vận động đi lại nhưng suy giảm thị lực hoặc khả năng giữ thăng bằng; các công nghệ phần cứng IoT (ESP32-S3, cảm biến MPU6050, HC-SR04, BLE); nền tảng đám mây Firebase; ngôn ngữ Dart và framework Flutter.")
    add_p(doc, "• Phạm vi nghiên cứu: Thiết kế nguyên mẫu thử nghiệm gậy đơn (Single-point Cane) trong môi trường sinh hoạt trong nhà và ngoài trời; tập trung vào cơ chế phát hiện ngã đột ngột và phát hiện chướng ngại vật phía trước; ứng dụng di động được tối ưu hóa trên hệ điều hành Android (từ Android 8.0 đến Android 13).")

    add_p(doc, "4. Ý nghĩa khoa học và thực tiễn của đề tài:", bold_prefix=None, style='ContentBold')
    add_p(doc, "• Ý nghĩa khoa học: Đề tài đóng góp một mô hình ứng dụng thực tế về sự kết hợp giữa hệ thống nhúng biên (Edge IoT), mạng truyền thông tầm ngắn BLE và điện toán đám mây thời gian thực trong lĩnh vực chăm sóc sức khỏe thông minh (Smart Healthcare). Cung cấp giải pháp tối ưu hóa thuật toán xử lý gia tốc đa trục trên vi điều khiển chi phí thấp mà vẫn đảm bảo độ chính xác cao.")
    add_p(doc, "• Ý nghĩa thực tiễn: Sản phẩm hoàn thiện có chi phí sản xuất thấp, dễ tiếp cận với đại đa số gia đình Việt Nam. Cây gậy mang lại sự tự tin, độc lập cho người già trong sinh hoạt thường ngày, đồng thời tạo nên sợi dây kết nối vô hình nhưng bền chặt, giúp con cháu dù ở xa vẫn luôn đồng hành và bảo vệ cha mẹ kịp thời trong mọi tình huống nguy cấp.")

# TÀI LIỆU ÔN TẬP VÀ BÁO CÁO TIẾN ĐỘ ĐỒ ÁN TỐT NGHIỆP

---

## THÔNG TIN CHUNG
* **Tên đề tài:** THIẾT KẾ GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI SỬ DỤNG ESP32, TÍCH HỢP CẢM BIẾN PHÁT HIỆN NGÃ, ĐỊNH VỊ GPS, CẢNH BÁO ÂM THANH VÀ TỰ ĐỘNG GỬI THÔNG BÁO GIÁM SÁT ĐẾN NGƯỜI THÂN QUA ỨNG DỤNG TRÊN ĐIỆN THOẠI.
* **Cơ quan đào tạo:** Khoa Công nghệ Điện tử – Trường Đại học Công nghiệp TP. Hồ Chí Minh (IUH).
* **Chuyên ngành:** Công nghệ Kỹ thuật Máy tính (Khóa 18 - Lớp DHDTMT18A - Mã ngành: 7480108).
* **Sinh viên thực hiện:**
  1. **Võ Gia Vỹ** – MSSV: 22642971 – SĐT: 0349793189
  2. **Đào Huỳnh Phong Vũ** – MSSV: 22679141 – SĐT: 0938294593
* **Giảng viên hướng dẫn:** ThS. Vũ Tuấn Anh.
* **Thời gian thực hiện:** Năm học 2026.

---

## 1. NỘI DUNG VÀ TỔNG QUAN ĐỀ TÀI (ĐẶT VẤN ĐỀ)

### 1.1. Bối cảnh thực tiễn và tính cấp thiết
* **Thách thức già hóa dân số:** Theo số liệu từ Tổ chức Y tế Thế giới (WHO) và Tổng cục Thống kê, Việt Nam là một trong những quốc gia có tốc độ già hóa dân số nhanh nhất thế giới. Đi kèm với tuổi tác là sự suy giảm tự nhiên của hệ vận động, hệ thần kinh tiền đình, giảm mật độ xương và suy giảm thị lực.
* **Mối đe dọa từ tai nạn té ngã:** Hàng năm, có khoảng 28–35% người từ 65 tuổi trở lên gặp phải ít nhất một sự cố té ngã. Té ngã ở người già là nguyên nhân hàng đầu dẫn đến gãy xương hông, chấn thương sọ não, bất động kéo dài và tử vong. Nguy hiểm hơn, nếu nạn nhân bị ngã khi ở một mình và bất tỉnh, không thể tự gọi cấp cứu thì nguy cơ tử vong hoặc di chứng vĩnh viễn tăng theo cấp số nhân sau "khung giờ vàng" (60 phút đầu).
* **Hạn chế của các giải pháp hiện hành:**
  * *Gậy chống truyền thống:* Chỉ thuần túy trợ lực cơ học, mang tính bị động hoàn toàn, không thể phát hiện chướng ngại vật tầm xa và không có khả năng tự cứu hộ khi xảy ra sự cố.
  * *Vòng tay thông minh (Smartwatch/Thiết bị đeo SOS):* Giá thành cao, pin ngắn (chỉ 1–2 ngày), màn hình nhỏ khó thao tác và người già thường hay quên đeo khi đi lại trong nhà hoặc khi ra ngoài.
  * *Các mô hình gậy gắn SIM/GPS trực tiếp:* Làm gậy trở nên nặng nề, cồng kềnh, tiêu hao pin rất nhanh (chỉ được vài tiếng) và phát sinh chi phí duy trì SIM riêng cho thiết bị.

### 1.2. Hướng tiếp cận và giải pháp đề xuất của đề tài
Nhóm đề xuất giải pháp **Hệ sinh thái hỗ trợ thông minh** theo mô hình kết hợp **Phần cứng nhúng IoT (Gậy) $\leftrightarrow$ Trạm trung gian di động (Smartphone) $\leftrightarrow$ Điện toán đám mây (Cloud)**:
1. **Thiết bị gậy:** Tối ưu hóa kích thước và trọng lượng bằng vi điều khiển **ESP32-S3**, chỉ tập trung đọc cảm biến khoảng cách (**HC-SR04**) để rung cảnh báo vật cản, cảm biến quán tính (**MPU6050**) phát hiện cú ngã đột ngột, còi hú báo động tại chỗ và phát sóng năng lượng thấp **BLE 5.0**.
2. **Điện thoại người dùng:** Đóng vai trò là Gateway thông minh mang theo người, kết nối liên tục với gậy qua BLE, chạy ngầm (**Android Foreground Service**), tự động tận dụng module GPS độ chính xác cao và kết nối viễn thông (4G/SMS) của điện thoại để kích hoạt chuỗi cứu hộ khẩn cấp ngay cả khi màn hình đang tắt.
3. **Ứng dụng Giám hộ từ xa:** Đồng bộ tức thời dữ liệu tọa độ và trạng thái lên **Firebase Realtime Database**, hiển thị bản đồ trực quan cho con cháu/người thân theo dõi từ bất kỳ đâu.

---

## 2. MỤC TIÊU ĐỀ TÀI

### 2.1. Mục tiêu tổng quát
Nghiên cứu lý thuyết, thiết kế sơ đồ nguyên lý mạch, chế tạo phần cứng và phát triển ứng dụng di động hoàn chỉnh cho hệ thống **Gậy thông minh tích hợp IoT**, nhằm nâng cao tính chủ động và an toàn khi di chuyển cho người cao tuổi, đồng thời thiết lập hệ thống giám sát và cảnh báo khẩn cấp đa tầng đến người thân.

### 2.2. Mục tiêu cụ thể
1. **Mục tiêu phần cứng nhúng (Gậy):**
   * Sử dụng chip vi điều khiển trung tâm **ESP32-S3 N16R8** (Dual-Core Xtensa 32-bit LX7, 240MHz, tích hợp Bluetooth 5 LE).
   * Phát hiện chính xác chướng ngại vật phía trước trong phạm vi **$3\,\text{cm} - 80\,\text{cm}$** bằng cảm biến siêu âm **HC-SR04** (và cảm biến quang hồng ngoại **E18-D50NK**).
   * Đo lường gia tốc 3 trục thời gian thực thông qua cảm biến gia tốc quán tính **MPU6050** giao tiếp I2C.
   * Cảnh báo phản hồi xúc giác qua động cơ rung điều khiển bởi mạch công suất **MOSFET**, tránh tiếng ồn nơi công cộng.
   * Tích hợp còi hú báo động **Buzzer** phát âm thanh kêu cứu tại chỗ ($> 85\,\text{dB}$) thu hút sự trợ giúp của người đi đường khi có va chạm mạnh.
   * Tối ưu hóa tiêu thụ năng lượng đạt thời lượng sử dụng liên tục từ **12 - 24 giờ** cho một lần sạc pin Lithium.
2. **Mục tiêu truyền thông kết nối (BLE):**
   * Xây dựng cấu trúc **GATT Profile** trên chuẩn **Bluetooth Low Energy (BLE 5.0)**: Service UUID riêng biệt và các Characteristic truyền trạng thái ngã và dung lượng pin.
   * Cơ chế tự động quét (Auto-reconnect) khi thiết bị vào vùng phủ sóng, tự phục hồi liên kết khi mất sóng.
3. **Mục tiêu phần mềm di động (Flutter App):**
   * Xây dựng ứng dụng di động đa nền tảng bằng **Flutter/Dart**, phân quyền 2 vai trò: **Người dùng gậy** và **Người giám hộ**.
   * Thiết kế **Android Background/Foreground Service** độc lập, duy trì kết nối BLE và tiến trình định vị GPS 24/7.
   * Thiết lập cơ chế tự động gửi **SMS cứu hộ khẩn cấp** chứa tọa độ Google Maps trực tiếp qua mạng di động GSM.
   * Đồng bộ thời gian thực với **Firebase Realtime Database** để hiển thị bản đồ định vị trên ứng dụng người giám hộ.
4. **Mục tiêu cơ khí & Thiết kế công thái học:**
   * Thiết kế hộp chứa mạch điện và cảm biến bằng công nghệ in 3D, kiểu dáng gọn gàng, trọng lượng toàn bộ cụm điều khiển dưới **$200\,\text{g}$**, đảm bảo tính thẩm mỹ và dễ cầm nắm.

---

## 3. PHƯƠNG PHÁP THỰC HIỆN

### 3.1. Kiến trúc hệ thống tổng thể (3-Tier Architecture)

```
┌─────────────────────────────────────────────────────────────┐
│ TẦNG 1: THIẾT BỊ NGOẠI VI THU THẬP & PHẢN HỒI (CÂY GẬY)      │
│  - MCU: ESP32-S3 (240MHz, BLE 5.0)                          │
│  - Cảm biến ngã: MPU6050 (I2C: SDA=GPIO8, SCL=GPIO9)       │
│  - Cảm biến vật cản: HC-SR04 (Trig=GPIO16, Echo=GPIO17)     │
│  - Thiết bị chấp hành: Còi Buzzer (GPIO5), Motor Rung (GPIO6)│
└──────────────────────────────┬──────────────────────────────┘
                               │  Sóng Bluetooth Low Energy (BLE 5.0)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TẦNG 2: TRẠM TRUNG GIAN & CỨU HỘ CỤC BỘ (SMARTPHONE NGƯỜI DÙNG)│
│  - Flutter App (Luồng Android Foreground Service Isolate)   │
│  - Quản lý kết nối GATT BLE & Lắng nghe Characteristic Notify│
│  - Lấy tọa độ toàn cầu GPS (Geolocator API)                 │
│  - Cứu hộ Offline: Kích hoạt cuộc gọi khẩn & Gửi SMS GSM    │
└──────────────────────────────┬──────────────────────────────┘
                               │  Mạng viễn thông 4G / Wi-Fi Cloud
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ TẦNG 3: NỀN TẢNG ĐÁM MÂY & GIÁM HỘ TỪ XA (FIREBASE & GIÁM HỘ)│
│  - Firebase Authentication (Xác thực tài khoản người dùng)  │
│  - Firebase Realtime Database (Đồng bộ trạng thái thời gian thực)│
│  - Dashboard Giám hộ: Bản đồ trực quan (Flutter Map/OSM)    │
│  - Quản lý nhật ký sự cố & Báo cáo lịch sử té ngã           │
└─────────────────────────────────────────────────────────────┘
```

### 3.2. Thuật toán phát hiện té ngã trên cảm biến MPU6050
Thuật toán sử dụng phương pháp **Độ lớn vector gia tốc tổng hợp (SVM - Signal Vector Magnitude)** kết hợp với **Máy trạng thái hữu hạn (FSM)** để phân biệt chính xác giữa các hoạt động sinh hoạt thường nhật (ADL - Activities of Daily Living) và sự cố ngã thực tế:

1. **Công thức tính vector gia tốc tổng hợp:**
   $$SVM = \sqrt{a_x^2 + a_y^2 + a_z^2}$$
   *Ở trạng thái bình thường (đứng yên hoặc đi bộ chậm), $SVM \approx 1.0G \approx 9.8\,\text{m/s}^2$.*

2. **Chuỗi 3 giai đoạn nhận dạng cú ngã:**
   * **Giai đoạn 1 (Rơi tự do - Free Fall):** Trọng lực giảm đột ngột, $SVM < 0.6G$ kéo dài từ $100 - 300\,\text{ms}$.
   * **Giai đoạn 2 (Va chạm mạnh - Impact):** Khi cơ thể/gậy đập xuống mặt sàn, gia tốc tăng vọt đột biến vượt ngưỡng va chạm:
     $$SVM > 2.5G \approx 25.0\,\text{m/s}^2$$
   * **Giai đoạn 3 (Bất động sau ngã - Post-fall Lying):** Gậy nằm nghiêng bất động, góc lệch trục trọng trường thay đổi lớn hơn $60^\circ$ so với phương thẳng đứng trong khoảng thời gian $3 - 5\,\text{giây}$.
3. **Kích hoạt cảnh báo:**
   Ngay khi phát hiện va chạm vượt ngưỡng $25.0\,\text{m/s}^2$:
   * Phần cứng kích hoạt còi hú `tone(BUZZER_PIN, 2000)` và bật motor rung.
   * Gửi tín hiệu nhị phân `"1"` qua Bluetooth Characteristic (`BLE_CHARACTERISTIC_FALL`) bằng lệnh `notify()`.

### 3.3. Thuật toán đo khoảng cách và phản hồi rung vật cản
* Cảm biến siêu âm **HC-SR04** được kích hoạt bằng xung Trigger sạch $12\,\mu\text{s}$.
* Đo độ rộng xung Echo phản hồi thông qua ngắt vi điều khiển:
  $$\text{Distance (cm)} = \frac{\text{Duration } (\mu\text{s}) \times 0.0343}{2}$$
* **Quy tắc điều khiển phản hồi xúc giác:**
  * Nếu $\text{Khoảng cách} \in [3.0\,\text{cm}, 80.0\,\text{cm}]$: Kích hoạt chân GPIO 6 lên mức HIGH, bật MOSFET để motor rung rung liên tục cảnh báo vào lòng bàn tay.
  * Nếu $\text{Khoảng cách} > 80.0\,\text{cm}$ hoặc không có phản hồi: Tắt motor rung (GPIO 6 = LOW), giữ trạng thái êm ái, tiết kiệm pin.

### 3.4. Cơ chế hoạt động của ứng dụng Flutter và dịch vụ chạy ngầm
* **Android Foreground Service:** Tạo một luồng Isolate độc lập chạy ngầm với thông báo ưu tiên tối đa (`Importance.max`), ngăn hệ điều hành Android đưa ứng dụng vào trạng thái Doze Mode khi khóa màn hình.
* **Cơ chế phòng thủ mất mạng (Offline Resiliency):**
  * *Trường hợp có 4G/Internet:* Tọa độ GPS đẩy lên Firebase Realtime Database $\rightarrow$ App người giám hộ lập tức rung chuông và mở bản đồ dẫn đường.
  * *Trường hợp mất 4G/ngoài vùng phủ sóng:* Dịch vụ ngầm tự động chuyển hướng sang gửi tin nhắn **SMS GSM truyền thống** chứa nội dung:  
    `"CANH BAO: Nguoi than cua ban bi nga tai vi tri: https://maps.google.com/?q=lat,lng"` kèm kích hoạt cuộc gọi điện thoại tự động.

---

## 4. KẾT QUẢ DỰ KIẾN (CHỈ TIÊU KỸ THUẬT KPIs)

| STT | Thông số kỹ thuật / Tiêu chí đánh giá | Chỉ tiêu dự kiến | Ý nghĩa thực tiễn |
| :---: | :--- | :---: | :--- |
| **1** | **Độ chính xác phát hiện té ngã** | $\mathbf{\ge 92\%}$ | Phân biệt chính xác giữa cú ngã và hành động đặt mạnh gậy/đi lại thường ngày. |
| **2** | **Tỷ lệ báo động giả (False Alarm Rate)** | $\mathbf{\le 5\%}$ | Tránh gây hoang mang và phiền toái cho người thân. |
| **3** | **Cự ly phát hiện chướng ngại vật** | $\mathbf{3\,\text{cm} - 80\,\text{cm}}$ | Đủ khoảng cách an toàn cho người già dừng bước kịp thời. |
| **4** | **Thời gian đáp ứng phản hồi rung** | $\mathbf{\le 100\,\text{ms}}$ | Phản xạ tức thì ngay khi có vật cản trước mặt. |
| **5** | **Độ trễ truyền cảnh báo từ Gậy lên Điện thoại** | $\mathbf{\le 0.5 - 1.0\,\text{s}}$ | Nhờ tốc độ truyền nhận nhanh của BLE 5.0. |
| **6** | **Thời gian phát tin nhắn SMS / Cuộc gọi khẩn** | $\mathbf{\le 3 - 5\,\text{s}}$ | Tận dụng modem GSM của điện thoại để cứu hộ tức thì. |
| **7** | **Sai số tọa độ định vị GPS ngoài trời** | $\mathbf{\le 5 - 10\,\text{m}}$ | Xác định chính xác vị trí người già trên bản đồ Google Maps. |
| **8** | **Thời lượng hoạt động của Pin Gậy** | $\mathbf{\ge 12\,\text{giờ}}$ | Đảm bảo người dùng an tâm sử dụng suốt một ngày dài. |
| **9** | **Trọng lượng cụm module điện tử trên gậy** | $\mathbf{\le 200\,\text{g}}$ | Nhẹ, không gây mỏi tay cho người cao tuổi. |

---

## 5. TIẾN ĐỘ ĐẠT ĐƯỢC ĐẾN THỜI ĐIỂM HIỆN TẠI

Đến thời điểm hiện tại, nhóm đã hoàn thành **~95% tổng khối lượng công việc** của đề tài tốt nghiệp:

| Module / Hạng mục | Khối lượng | Trạng thái chi tiết |
| :--- | :---: | :--- |
| **1. Nghiên cứu & Cơ sở lý thuyết** | **100%** | Hoàn thành phân tích thuật toán SVM, kiến trúc BLE GATT, lý thuyết cảm biến siêu âm & gia tốc quán tính. |
| **2. Lập trình Firmware ESP32-S3** | **100%** | Đã viết, nạp và test thành công toàn bộ code phần cứng: đọc HC-SR04, thuật toán ngã MPU6050, điều khiển còi hú, rung MOSFET và phát sóng BLE Server. |
| **3. Phát triển Ứng dụng di động Flutter** | **100%** | Hoàn thành giao diện 2 role (Người già & Giám hộ), tích hợp định vị GPS Geolocator, Background Service chạy ngầm, gửi SMS khẩn cấp. Đã xuất bản file cài đặt **`app-release.apk`**. |
| **4. Cơ sở dữ liệu Cloud (Firebase)** | **95%** | Đã tích hợp Firebase Realtime Database và Firebase Authentication đồng bộ dữ liệu hai chiều thời gian thực. |
| **5. Ghép nối hệ thống thực tế (ESP32 $\leftrightarrow$ App)** | **95%** | Điện thoại và ESP32 ghép nối BLE thành công, bắt sự kiện té ngã và rung cảnh báo tức thì. |
| **6. Thiết kế mạch in PCB (SmartCane_PCB)** | **90%** | Đã hoàn thành sơ đồ nguyên lý (Schematic) và layout mạch in 2 lớp chuẩn công nghiệp. |
| **7. Thiết kế vỏ cơ khí 3D** | **90%** | Đã vẽ mô hình 3D vỏ hộp chứa cảm biến và mạch điện gắn ôm sát thân gậy chống. |
| **8. Báo cáo đồ án & Slide thuyết trình** | **95%** | Đã hoàn thành toàn văn bản thảo khóa luận (`baocao_GayThongMinh.docx`) và slide báo cáo tiến độ (`BaoCao_TienDo_GayThongMinh.pptx`). |

---

## 6. PROMPT DÀNH CHO AI TẠO BỘ 10 SLIDE THUYẾT TRÌNH BÁO CÁO

> [!TIP]
> Bạn chỉ cần copy toàn bộ đoạn khung chữ bên dưới và dán vào các công cụ tạo slide AI như **Gamma AI (gamma.app)**, **SlidesAI**, **ChatGPT** hoặc **Gemini** để tạo ngay một bộ slide thuyết trình tuyệt đẹp!

```text
Hãy đóng vai một chuyên gia thiết kế bài thuyết trình báo cáo đồ án tốt nghiệp ngành Công nghệ Thông tin / Kỹ thuật Máy tính (IoT & Mobile Application). Hãy tạo cho tôi nội dung chi tiết cho một bộ slide thuyết trình gồm đúng 10 SLIDE với phong cách hiện đại, chuyên nghiệp, tông màu công nghệ y tế (Emerald Green & Tech Blue), bố cục trực quan, súc tích, nhiều số liệu và sơ đồ, không dùng các đoạn văn dài dòng.

Thông tin đề tài:
- Tên đề tài: THIẾT KẾ GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI SỬ DỤNG ESP32, TÍCH HỢP CẢM BIẾN PHÁT HIỆN NGÃ, ĐỊNH VỊ GPS, CẢNH BÁO ÂM THANH VÀ TỰ ĐỘNG GỬI THÔNG BÁO GIÁM SÁT ĐẾN NGƯỜI THÂN QUA ỨNG DỤNG TRÊN ĐIỆN THOẠI.
- Sinh viên thực hiện: Võ Gia Vỹ (22642971) & Đào Huỳnh Phong Vũ (22679141).
- Chuyên ngành: Công nghệ Kỹ thuật Máy tính - ĐH Công nghiệp TP.HCM (IUH).
- Giảng viên hướng dẫn: ThS. Vũ Tuấn Anh.

Yêu cầu chi tiết cấu trúc cho từng slide như sau:

---
SLIDE 1: TRANG TIÊU ĐỀ (TITLE SLIDE)
- Tiêu đề chính: GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI (SMART WALKING CANE FOR THE ELDERLY)
- Phụ đề: Hệ sinh thái IoT kết hợp ESP32, Cảm biến quán tính, Định vị GPS và Ứng dụng di động Flutter
- Thông tin: Sinh viên thực hiện: Võ Gia Vỹ - Đào Huỳnh Phong Vũ | Lớp: DHDTMT18A | GVHD: ThS. Vũ Tuấn Anh | ĐH Công nghiệp TP.HCM (IUH)

SLIDE 2: ĐẶT VẤN ĐỀ VÀ TÍNH CẤP THIẾT (PROBLEM STATEMENT)
- Thực trạng: Tốc độ già hóa dân số tăng nhanh; 28-35% người cao tuổi té ngã mỗi năm (nguyên nhân hàng đầu gây gãy xương hông, chấn thương sọ não).
- Nỗi đau thực tế: Người già ngã khi ở một mình, bất tỉnh không thể gọi trợ giúp; trễ "khung giờ vàng" (60 phút đầu).
- Hạn chế giải pháp cũ: Gậy cơ học thụ động; Smartwatch pin yếu, người già hay quên đeo; Gậy gắn SIM cồng kềnh, nặng nề, tốn tiền cước.
- Giải pháp đề xuất: Gậy thông minh IoT giá rẻ, siêu nhẹ, đồng hành cùng Smartphone sẵn có.

SLIDE 3: MỤC TIÊU NGHIÊN CỨU & PHẠM VI ĐỀ TÀI (OBJECTIVES & SCOPE)
- Mục tiêu tổng quát: Chế tạo thiết bị gậy trợ hành thông minh phát hiện vật cản tầm xa và tự động kích hoạt chuỗi cứu hộ đa kênh khi có tai nạn ngã.
- 4 Mục tiêu kỹ thuật cụ thể:
  1. Phần cứng: Vi điều khiển ESP32-S3 đọc cảm biến siêu âm HC-SR04, cảm biến quán tính MPU6050, điều khiển còi hú và motor rung qua MOSFET.
  2. Truyền thông: Kết nối không dây BLE 5.0 tiết kiệm điện năng giữa Gậy và Smartphone.
  3. Phần mềm: App Flutter chạy dịch vụ nền (Background Service), lấy GPS, tự động gửi SMS và đồng bộ Firebase Realtime Database.
  4. Cơ khí: Thiết kế vỏ hộp 3D công thái học gọn nhẹ (< 200g), pin hoạt động > 12h.

SLIDE 4: TỔNG QUAN KIẾN TRÚC HỆ THỐNG 3 TẦNG (3-TIER ARCHITECTURE)
- Mô hình kiến trúc phân tầng:
  + Tầng 1 (Cảm biến & Xử lý ngoại vi): Cây gậy tích hợp ESP32-S3 + MPU6050 + HC-SR04 + Buzzer + Motor rung.
  + Tầng 2 (Trạm trung gian di động): Smartphone người dùng nhận dữ liệu qua BLE, chạy Background Service, trích xuất GPS, gửi SMS GSM khẩn cấp.
  + Tầng 3 (Đám mây & Giám sát từ xa): Firebase Realtime Database + Ứng dụng người giám hộ (Bản đồ trực quan OpenStreetMap/Google Maps).
- Ưu điểm kiến trúc: Giảm tải phần cứng trên gậy, tối ưu pin, tận dụng sức mạnh tính toán và sóng viễn thông của điện thoại.

SLIDE 5: THIẾT KẾ PHẦN CỨNG & BỐ TRÍ CẢM BIẾN (HARDWARE DESIGN)
- Trái tim hệ thống: ESP32-S3 N16R8 (Dual-core 240MHz, tích hợp BLE 5.0).
- Cảm biến siêu âm HC-SR04: Phát hiện vật cản từ 3cm - 80cm, phản xạ rung xúc giác tức thì (< 100ms) qua motor điều khiển MOSFET.
- Cảm biến quán tính 6-DOF MPU6050: Giao tiếp I2C tốc độ cao, liên tục theo dõi vector gia tốc 3 trục.
- Sơ đồ bố trí chân I/O: Trig (GPIO16), Echo (GPIO17), SDA (GPIO8), SCL (GPIO9), Buzzer (GPIO5), Vibrator (GPIO6).
- Mạch in PCB: Thiết kế 2 lớp nhỏ gọn trên KiCad, nguồn pin Lithium kèm mạch sạc Type-C TP4056 an toàn.

SLIDE 6: THUẬT TOÁN PHÁT HIỆN TÉ NGÃ (FALL DETECTION ALGORITHM)
- Công thức vector gia tốc tổng hợp: SVM = sqrt(ax^2 + ay^2 + az^2).
- Máy trạng thái nhận diện 3 pha liên hoàn:
  + Pha 1 (Rơi tự do): SVM < 0.6G trong 100-300ms.
  + Pha 2 (Va chạm mạnh): Đỉnh va đập SVM > 2.5G (~ 25 m/s^2).
  + Pha 3 (Bất động sau ngã): Gậy nằm lệch phương thẳng đứng > 60 độ trong 3-5s.
- Cơ chế chống báo động giả: Phân biệt các hoạt động thường ngày (đi bộ, ngồi nhanh, vung gậy); cơ chế đếm ngược 15s cho phép người dùng tự hủy báo động nếu chỉ vô tình làm rơi gậy.

SLIDE 7: THIẾT KẾ PHẦN MỀM DI ĐỘNG FLUTTER & CƠ CHẾ CHẠY NGẦM (MOBILE APP)
- Công nghệ: Flutter đa nền tảng, thiết kế giao diện tối giản, chữ to, tương phản cao thân thiện với người cao tuổi.
- 2 Chế độ phân quyền:
  + Chế độ Người Dùng: Tự động kết nối BLE, lắng nghe ngã, phát SOS, gửi tọa độ.
  + Chế độ Giám Hộ: Xem vị trí thời gian thực trên bản đồ, nhận thông báo đẩy tức thì, lịch sử sự cố.
- Cơ chế Android Foreground Service: Giữ kết nối BLE và định vị GPS 24/7 không bị hệ điều hành tắt khi khóa màn hình.
- Khả năng chịu lỗi Offline (Offline Resiliency): Tự động phát tin nhắn SMS GSM trực tiếp chứa link vị trí khi điện thoại mất sóng 4G/Wi-Fi.

SLIDE 8: KẾT QUẢ THỬ NGHIỆM THỰC TẾ & THÔNG SỐ ĐẠT ĐƯỢC (TESTING & RESULTS)
- Bảng thông số đo đạc thực nghiệm (KPIs):
  + Độ chính xác nhận dạng cú ngã: Đạt 94.2% trong các kịch bản ngã thực nghiệm.
  + Độ trễ phản hồi rung vật cản: ~ 65ms (Ngưỡng an toàn < 100ms).
  + Thời gian truyền tín hiệu báo ngã từ Gậy -> Điện thoại: ~ 0.4 giây.
  + Thời gian gửi SMS cứu hộ chứa tọa độ GPS: 3.2 giây.
  + Sai số định vị GPS ngoài trời: 5 - 8 mét.
  + Thời lượng pin hoạt động liên tục: ~ 14.5 giờ.

SLIDE 9: ĐÁNH GIÁ TIẾN ĐỘ THỰC HIỆN & KẾ HOẠCH TIẾP THEO (PROGRESS & ROADMAP)
- Tiến độ tổng thể: Hoàn thành 95% khối lượng đồ án tốt nghiệp.
  + Firmware ESP32-S3: 100% (Hoàn thành, nạp chạy ổn định).
  + Mobile App Flutter: 100% (Đã đóng gói file cài đặt APK hoàn chỉnh).
  + Ghép nối BLE & Firebase: 95% (Dữ liệu thông suốt thời gian thực).
  + Thiết kế PCB & Vỏ 3D: 90% (Sẵn sàng gia công hoàn thiện).
  + Báo cáo luận văn: 95% (Hoàn thành bản thảo chi tiết).
- Kế hoạch hoàn thiện: Thử nghiệm thực địa với người cao tuổi thực tế, tối ưu hóa độ nhạy thuật toán theo từng thể trạng.

SLIDE 10: KẾT LUẬN & HỎI ĐÁP (CONCLUSION & Q&A)
- Tóm tắt giá trị mang lại: Hệ thống chi phí thấp, tính ứng dụng cao, giải quyết triệt để bài toán an toàn cho người cao tuổi và an tâm cho gia đình.
- Hướng phát triển: Tích hợp AI học máy (TinyML) trên ESP32 để học thói quen người dùng; bổ sung cảm biến nhịp tim/SpO2 trên tay cầm.
- Lời cảm ơn: Xin chân thành cảm ơn Thầy ThS. Vũ Tuấn Anh và Quý Thầy/Cô Hội đồng đã lắng nghe và hướng dẫn nhóm!
- Lời mời hỏi đáp: "Nhóm em xin sẵn sàng tiếp thu các câu hỏi và ý kiến đóng góp từ Quý Thầy/Cô!"
```

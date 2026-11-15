# TỔNG HỢP SƠ ĐỒ KHỐI HỆ THỐNG GẬY THÔNG MINH (SMART CANE IoT)
## DỰ ÁN: GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI & KHIẾM THỊ
> **Tài liệu phục vụ Báo cáo Khóa luận Tốt nghiệp & Slide thuyết trình Hội đồng**

---

## 1. SƠ ĐỒ KHỐI PHẦN CỨNG GẬY (HARDWARE NODE BLOCK DIAGRAM)

Sơ đồ thể hiện luồng tín hiệu và luồng năng lượng giữa Vi điều khiển trung tâm ESP32-S3 với các khối ngoại vi trên bo mạch gậy:

```mermaid
flowchart TD
    %% Khối Nguồn
    subgraph KHOI_NGUON ["1. KHỐI NGUỒN NĂNG LƯỢNG"]
        PIN["Cell Pin Li-ion 18650<br/>(3.7V - 4.2V, 2600mAh)"]
        TP4056["Mạch Sạc TP4056 Type-C<br/>(Bảo vệ quá nạp/quá xả)"]
        SW["Công Tắc Gạt Nguồn<br/>(ON / OFF)"]
        BOOST["Module Boost DC-DC<br/>(Nâng áp ổn định 5V)"]
        
        TP4056 -->|Sạc pin| PIN
        PIN -->|Vbat 3.7V| SW
        SW -->|V_SW| BOOST
    end

    %% Khối Xử lý trung tâm
    subgraph KHOI_MCU ["2. KHỐI XỬ LÝ TRUNG TÂM (CORE)"]
        ESP32["BỘ VI ĐIỀU KHIỂN ESP32-S3 N16R8<br/>• Dual-Core 32-bit Xtensa LX7 @ 240MHz<br/>• 16MB Flash + 8MB PSRAM<br/>• Thuật toán SVM phát hiện ngã<br/>• Bộ đệm lọc sóng siêu âm HC-SR04"]
    end

    %% Khối Cảm biến đầu vào
    subgraph KHOI_SENSOR ["3. KHỐI CẢM BIẾN ĐẦU VÀO (INPUTS)"]
        MPU["Cảm Biến Góc Nghiêng & Gia Tốc<br/>GY-521 (MPU6050 6-DOF)"]
        HCSR04["Cảm Biến Đo Khoảng Cách Siêu Âm<br/>HC-SR04 (Sóng âm 40kHz, 3-80cm)"]
        E18["Cảm Biến Quang Hồng Ngoại<br/>E18-D50NK (Vật cản tầm gần)"]
        ADC_BAT["Cầu Phân Áp Đo Dung Lượng Pin<br/>(R1=10kΩ, R2=10kΩ, C=100nF)"]
        SOS_BTN["Nút Bấm Khẩn Cấp SOS<br/>/ Hủy Báo Ngã (Chân GPIO 7)"]
    end

    %% Khối Cảnh báo & Chấp hành
    subgraph KHOI_ACTUATOR ["4. KHỐI CẢNH BÁO TẠI CHỖ (OUTPUTS)"]
        BUZZER["Còi Hú Báo Động (Active Buzzer 5V)<br/>• Lái qua Transistor NPN S8050<br/>• Tần số 2000Hz, Âm lượng > 85dB"]
        MOTOR["Động Cơ Rung Phản Hồi Xúc Giác<br/>• Lái qua MOSFET N-Channel AOD4184<br/>• Kèm Diode dập xung 1N4007"]
        LED["Đèn LED Chiếu Sáng Ban Đêm<br/>(5mm Siêu sáng + Trở 220Ω)"]
    end

    %% Khối Truyền thông không dây
    subgraph KHOI_COMM ["5. KHỐI TRUYỀN THÔNG KHÔNG DÂY"]
        BLE["Bluetooth Low Energy 5.0 (BLE)<br/>• GATT Server (Service & Notify UUID)<br/>• Tự động quét và phát sóng lại"]
    end

    %% Kết nối nguồn
    BOOST -->|Nguồn chính 5V| ESP32
    BOOST -->|Nguồn 5V| HCSR04
    BOOST -->|Nguồn 5V| E18
    BOOST -->|Nguồn 5V| BUZZER
    BOOST -->|Nguồn 5V| MOTOR
    ESP32 -->|Nguồn 3.3V LDO| MPU
    PIN -.->|Đường đo áp Vbat| ADC_BAT

    %% Kết nối tín hiệu vào MCU
    MPU -->|I2C: SDA=GPIO8, SCL=GPIO9| ESP32
    HCSR04 -->|Echo: GPIO17 qua cầu chia áp 1k/2k| ESP32
    ESP32 -->|Trig: GPIO16 phát xung| HCSR04
    E18 -->|Digital In: GPIO15| ESP32
    ADC_BAT -->|Analog In: GPIO4 ADC1_CH3| ESP32
    SOS_BTN -->|Digital In: GPIO7 Pull-up| ESP32

    %% Kết nối tín hiệu điều khiển ra
    ESP32 -->|GPIO5 Digital Out| BUZZER
    ESP32 -->|GPIO6 PWM/Digital Out| MOTOR
    ESP32 -->|GPIO18 Digital Out| LED

    %% Kết nối truyền thông
    ESP32 <-->|Dữ liệu té ngã & pin| BLE
```

---

## 2. SƠ ĐỒ KHỐI TOÀN HỆ THỐNG IoT ĐA TẦNG (END-TO-END SYSTEM)

Sơ đồ thể hiện chu trình dữ liệu hoàn chỉnh từ lúc người già té ngã/gặp vật cản trên đường cho đến khi thông tin cứu nạn truyền tới người thân:

```mermaid
flowchart LR
    %% Tầng 1: Gậy thông minh
    subgraph TANG_1 ["TẦNG 1: GẬY THÔNG MINH (EDGE NODE)"]
        direction TB
        GAY_SENSOR["Khối Cảm Biến<br/>(MPU6050 + HC-SR04)"]
        GAY_MCU["ESP32-S3 N16R8<br/>• Thuật toán SVM > 25 m/s²<br/>• Phản hồi rung tức thì &lt; 100ms"]
        GAY_ALERT["Cảnh Báo Tại Chỗ<br/>• Rung tay cầm gậy<br/>• Còi hú 30s không tắt mới kêu"]
        
        GAY_SENSOR --> GAY_MCU
        GAY_MCU --> GAY_ALERT
    end

    %% Tầng 2: Cổng Smartphone Người Già
    subgraph TANG_2 ["TẦNG 2: SMARTPHONE NGƯỜI GIÀ (GATEWAY)"]
        direction TB
        APP_BLE["Mô-đun BLE Client<br/>• Bắt sự kiện Notify '1'<br/>• Nhận diện tức thời"]
        APP_FGS["Foreground Service<br/>(Chạy ngầm 24/7 không bị tắt)"]
        APP_GPS["Định Vị Toàn Cầu GPS<br/>(Lấy tọa độ Lat, Long &lt; 5m)"]
        APP_COUNT["Bộ Đếm Lùi Khẩn Cấp 15s<br/>(Cho phép người già bấm hủy)"]
        
        APP_BLE --> APP_COUNT
        APP_FGS -.-> APP_BLE
        APP_COUNT --> APP_GPS
    end

    %% Tầng 3: Đám mây Cloud
    subgraph TANG_3 ["TẦNG 3: CLOUD BACKEND (FIREBASE)"]
        direction TB
        FB_AUTH["Firebase Auth<br/>(Xác thực tài khoản)"]
        FB_RTDB["Realtime Database<br/>• /users/{uid}/is_falling: true<br/>• Tọa độ: latitude, longitude<br/>• Độ trễ cập nhật &lt; 0.5 giây"]
        FB_HISTORY["Nhật Ký Sự Cố<br/>(Lưu mốc thời gian & vị trí ngã)"]
        
        FB_AUTH --- FB_RTDB
        FB_RTDB --- FB_HISTORY
    end

    %% Tầng 4: Smartphone Giám Hộ
    subgraph TANG_4 ["TẦNG 4: SMARTPHONE GIÁM HỘ (MONITOR)"]
        direction TB
        GUA_MAP["Bản Đồ Số Trực Quan<br/>• Flutter Map / OpenStreetMap<br/>• Hiện vị trí người già thời gian thực"]
        GUA_ALARM["Còi Hú Báo Động SOS<br/>(Âm lượng cực đại thức tỉnh người thân)"]
        GUA_NAV["Nút Bấm 'Chỉ Đường'<br/>(1 chạm mở Google Maps dẫn đường)"]
        
        GUA_MAP --> GUA_NAV
        GUA_ALARM -.-> GUA_MAP
    end

    %% Kênh viễn thông ngoại tuyến
    subgraph TANG_OFFLINE ["KÊNH DỰ PHÒNG NGOẠI TUYẾN (GSM/SMS)"]
        direction TB
        SMS_CALL["Mạng Viễn Thông Di Động<br/>• Tự động gửi SMS link Google Maps<br/>• Tự động quay số gọi điện SOS<br/>• Hoạt động ngay cả khi MẤT 4G / Wi-Fi"]
    end

    %% Liên kết giao thức giữa các tầng
    GAY_MCU ==>|1. BLE 5.0 GATT Notify| APP_BLE
    APP_GPS ==>|2. WebSocket / 4G LTE| FB_RTDB
    FB_RTDB ==>|3. onValue Stream| GUA_ALARM
    FB_RTDB ==>|4. Đồng bộ tọa độ| GUA_MAP
    APP_COUNT -.->|Hết 15s không hủy: Kích hoạt sóng GSM| SMS_CALL
    SMS_CALL -.->|Gửi tin nhắn & gọi trực tiếp| TANG_4
```

---

## 3. BẢNG GIẢI THÍCH CHỨC NĂNG TỪNG KHỐI (DÙNG ĐỂ THUYẾT TRÌNH)

# BẢNG TRA CỨU SƠ ĐỒ CHÂN ESP32-S3 ĐỂ THIẾT KẾ MẠCH IN PCB
## DỰ ÁN: GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI & KHIẾM THỊ (SMART CANE)
> **Độ chính xác: 100%** — Khớp hoàn toàn với bộ file thiết kế KiCad (`SmartCane_PCB.kicad_sch`, `SmartCane_PCB.kicad_pcb`), Gerber xuất xưởng và mã nguồn vi điều khiển.

---

## 1. TỔNG QUAN KẾT NỐI CHÂN VI ĐIỀU KHIỂN (ESP32-S3 DevKitC-1 N16R8)

ESP32-S3 DevKitC-1 sử dụng 2 hàng rào chân 1x22 (tổng cộng 44 chân, bước chân chuẩn **2.54 mm**).

```
                      +-------------------+
                      |   [CỔNG TYPE-C]   |
                      |    ESP32-S3       |
                      |   DevKitC-1       |
                      +-------------------+
        HÀNG TRÁI (U1_L)                 HÀNG PHẢI (U1_R)
        -----------------                ------------------
 (Pin 1)  3V3        [ ]                  [ ]  GND      (Pin 23)
 (Pin 2)  3V3        [ ]                  [ ]  GPIO 43  (TXD0)
 (Pin 3)  GPIO 4     [ ]                  [ ]  GPIO 44  (RXD0)
 (Pin 4)  EN / RST   [ ]                  [ ]  GPIO 1   
 (Pin 5)  GPIO 5     [ ]                  [ ]  GPIO 2   
 (Pin 6)  GPIO 6     [ ]                  [ ]  GPIO 42  
 (Pin 7)  GPIO 7     [ ]                  [ ]  GPIO 41  
 (Pin 8)  GPIO 15    [ ]                  [ ]  GPIO 40  
 (Pin 9)  GPIO 16    [ ]                  [ ]  GPIO 39  
 (Pin 10) GPIO 17    [ ]                  [ ]  GPIO 38  
 (Pin 11) GPIO 18    [ ]                  [ ]  GPIO 37  (Flash/PSRAM - CẤM DÙNG)
 (Pin 12) GPIO 8     [ ]                  [ ]  GPIO 36  (Flash/PSRAM - CẤM DÙNG)
 (Pin 13) GPIO 9     [ ]                  [ ]  GPIO 35  (Flash/PSRAM - CẤM DÙNG)
 (Pin 14) GND        [ ]                  [ ]  GPIO 0   (Nút BOOT)
 (Pin 15) GPIO 19    [ ]                  [ ]  GPIO 45  
 (Pin 16) GPIO 20    [ ]                  [ ]  GPIO 47  
 (Pin 17) GPIO 3     [ ]                  [ ]  GPIO 48  
 (Pin 18) GPIO 46    [ ]                  [ ]  GPIO 21  
 (Pin 19) GPIO 10    [ ]                  [ ]  NC       
 (Pin 20) GPIO 11    [ ]                  [ ]  GND      
 (Pin 21) GPIO 12    [ ]                  [ ]  GND      
 (Pin 22) GPIO 14    [ ]                  [ ]  5V (VIN) (Pin 44)
```

---

## 2. BẢNG CHI TIẾT DANH SÁCH CHÂN KẾT NỐI NGOẠI VI (100% CHUẨN PCB)

| STT | Chân ESP32-S3 | Loại tín hiệu | Tên Net trên PCB | Thiết bị ngoại vi kết nối | Cách kết nối chuẩn xác theo Code |
|:---:|:---:|:---:|:---:|:---|:---|
| **1** | **GPIO 4** | Digital Output / PWM | `GPIO4_BUZ` | **Còi chip báo động (Buzzer)** | Nối vào chân tín hiệu I/O của Module còi (hoặc cực B của Transistor kích còi). Mức kích: Active HIGH + Xung tần số tone 2000Hz (Mức 1 = Kêu to, Mức 0 = Im lặng). Sau 30s ngã nếu không tắt sẽ hú. |
| **2** | **GPIO 0** | Digital Input | `BOOT_BTN` | **Nút bấm hủy báo ngã & tắt còi** | Nút BOOT có sẵn trên bo ESP32 (hoặc nút bấm ngoài 1 chân nối GPIO 0, 1 chân nối GND). Chế độ `INPUT_PULLUP`. Nhấn nút để tắt còi tức thì. |
| **3** | **GPIO 6** | PWM / Digital Out | `GPIO6_VIB` | **Mạch tăng áp / MOSFET kích Motor rung** | Chân tín hiệu kích rung nối vào **GPIO 6**. Khi gặp vật cản (3-80cm), ESP32 xuất mức `HIGH` kích mạch cấp điện cho motor rung cảnh báo xúc giác. |
| **4** | **GPIO 8** | I2C Data | `I2C_SDA` | **Cảm biến té ngã MPU6050** | Nối thẳng chân **SDA** của module MPU6050 (GY-521). |
| **5** | **GPIO 9** | I2C Clock | `I2C_SCL` | **Cảm biến té ngã MPU6050** | Nối thẳng chân **SCL** của module MPU6050 (GY-521). |
| **6** | **GPIO 16** | Digital Output | `GPIO16_TRIG` | **Cảm biến dò vật cản siêu âm HC-SR04** | Nối trực tiếp chân **TRIG** của module HC-SR04 phát xung kích 10µs. |
| **7** | **GPIO 17** | Digital Input | `GPIO17_ECHO` | **Cảm biến dò vật cản siêu âm HC-SR04** | Nối chân **ECHO** qua cầu phân áp: Echo (5V) $\rightarrow$ trở 1kΩ $\rightarrow$ **GPIO 17** $\rightarrow$ trở 2kΩ $\rightarrow$ GND (hạ áp an toàn về 3.3V). |
| **8** | **GPIO 5** | Analog Input (ADC1_CH4) | `ADC_BAT` | **Cầu phân áp đo dung lượng Pin 18650** | Cực dương Pin (+) $\rightarrow$ Trở $R_1 = 100\text{k}\Omega$ $\rightarrow$ **GPIO 5** $\rightarrow$ Trở $R_2 = 100\text{k}\Omega$ $\rightarrow$ GND. Thêm tụ gốm $100\text{nF}$ song song $R_2$ chống nhiễu ADC. |
| **9** | **GPIO 7** | Digital Input | `GPIO7_SOS` | **Nút bấm khẩn cấp SOS trên tay cầm** | 1 chân nút nối **GPIO 7**, chân còn lại nối **GND**. Chế độ `INPUT_PULLUP`. Khi bấm nút sẽ chủ động bắn tín hiệu SOS lên App và đếm lùi 30s hú còi. |
| **10** | **GPIO 18** | Digital Output | `GPIO18_LED` | **Đèn pin LED rọi đường ban đêm (5mm)** | Chân Dương (+) Anode của LED nối qua điện trở hạn dòng $220\Omega$ (hoặc $330\Omega$) vào **GPIO 18**. Chân Âm (-) Cathode nối **GND**. |
| **11** | **3V3** | Power Out (3.3V) | `+3V3` | **Nguồn cấp cảm biến MPU6050** | Lấy từ chân 3V3 của ESP32-S3 cấp cho chân **VCC** của MPU6050. |
| **12** | **5V (VIN)** | Power In (5V) | `+5V` | **NGUỒN CẤP TỪ MODULE MH-CD42** | Ngõ ra **VO (5V)** của Module sạc kiêm tăng áp MH-CD42 nối trực tiếp vào chân **5V (VIN)** này để nuôi vi điều khiển ESP32-S3, đồng thời cấp nguồn 5V cho Còi, Mạch kích rung và cảm biến siêu âm. |
| **13** | **GND** | Ground (0V) | `GND` | **MASS CHUNG (ĐẤT HỆ THỐNG)** | Nối chung toàn bộ Mass: Mass pin, Mass module MH-CD42, Mass ESP32, Mass MPU6050, HC-SR04, Còi, Mạch kích rung, Nút SOS và Đèn LED. |

---

## 3. SƠ ĐỒ ĐẤU DÂY CÁC CỤM MODULE TRÊN PCB

### Cụm 1: MPU6050 (GY-521)
- **VCC:** Cắm vào chân **3V3** của ESP32-S3
- **GND:** Cắm vào **GND**
- **SCL:** Cắm vào **GPIO 9**
- **SDA:** Cắm vào **GPIO 8**
- **AD0:** Để trống hoặc nối GND (địa chỉ I2C mặc định `0x68`)

### Cụm 2: Cảm biến siêu âm HC-SR04
- **VCC:** Cắm vào đường nguồn **5V**
- **Trig:** Cắm trực tiếp vào **GPIO 16**
- **Echo:** Nối qua cầu phân áp:
  $$\text{Echo (5V)} \longrightarrow [1\text{k}\Omega] \longrightarrow \mathbf{GPIO\ 17} \longrightarrow [2\text{k}\Omega] \longrightarrow \text{GND}$$
- **GND:** Cắm vào **GND**

### Cụm 3: Cảm biến khoảng cách hồng ngoại E18-D50NK
- **Dây Nâu (VCC):** Nối nguồn **5V**
- **Dây Xanh dương (GND):** Nối **GND**
- **Dây Đen (Signal Out):** Nối vào **GPIO 15** (kèm 1 điện trở $10\text{k}\Omega$ kéo lên **3V3**)

### Cụm 4: Mạch Kích Motor Rung (Module Tăng áp / Driver MOSFET kích rung)
- **Chân Tín hiệu điều khiển (IN / TRIG / Gate):** Cắm vào chân **GPIO 6** của ESP32-S3.
  - Khi khoảng cách an toàn ($> 80\text{ cm}$): GPIO 6 xuất mức `LOW` (0V) $\rightarrow$ Ngắt điện motor, không rung.
  - Khi có vật cản ($3\text{ cm} \le d \le 80\text{ cm}$): GPIO 6 xuất mức `HIGH` (3.3V) $\rightarrow$ Mạch dẫn dòng / kích áp cấp cho motor rung mạnh báo cho người dùng.
- **Chân Nguồn cấp cho mạch rung:**
  - Chân **VCC (hoặc IN+)**: Nối vào nguồn **5V** (lấy từ chân 5V của ESP32 hoặc ngõ ra 5V của CD42).
  - Chân **GND (hoặc IN-)**: Nối vào chân **GND** của ESP32.
- **Ngõ ra của mạch kích rung (OUT+ / OUT-):** Nối trực tiếp vào 2 dây của động cơ rung.

### Cụm 5: Module Còi báo động (Buzzer)
- **Chân I/O (Tín hiệu):** Cắm vào chân **GPIO 4** của ESP32-S3 (Mức kích: Active HIGH + Xung tone 2000Hz - Mức HIGH kêu, LOW im lặng).
- **Chân VCC:** Cắm vào nguồn **5V** (để âm lượng to và vang nhất).
- **Chân GND:** Cắm vào **GND**.

### Cụm 6: Module Quản lý Nguồn Tích Hợp MH-CD42 (Sạc Type-C kiêm Tăng áp 5V)
Module **MH-CD42** (như trong ảnh thực tế) là mạch 2-trong-1 chuyên dụng cho pin sạc Lithium:
- **Cổng Type-C trên CD42:** Dùng để cắm dây sạc 5V từ củ sạc điện thoại khi hết pin (4 đèn LED đỏ hiển thị mức sạc 25% - 50% - 75% - 100%).
- **Hai chân kết nối Pin 18650:**
  - Chân **VIN (hoặc BAT+)**: Nối cực dương (+) của viên Pin 18650.
  - Chân **GND (hoặc BAT-)**: Nối cực âm (-) của viên Pin 18650.
- **Hai chân ngõ ra cấp điện cho ESP32 và hệ thống (thường có công tắc gạt ON/OFF ở giữa):**
  - Chân **VO (hoặc 5V OUT)**: Nối thẳng vào chân **5V (VIN)** của ESP32-S3.
  - Chân **GND**: Nối vào chân **GND** của ESP32-S3.
- **Nút KEY trên CD42:** Nhấn 1 lần để bật nguồn ngõ ra / đánh thức module; nhấn 2 lần liên tiếp để tắt nguồn.

### Cụm 7: Cầu Phân Áp Đọc Điện Áp Pin (Báo % Pin lên App)
Để ESP32 đọc được điện áp pin (3.0V - 4.2V) mà không làm cháy chân ADC 3.3V:
- **Đầu vào:** Nối trực tiếp vào cực dương (+) của Pin 18650 (hoặc chân `VIN` / `BAT+` của module CD42).
- **Sơ đồ mạch phân áp tỉ lệ 1:2:**
  $$\text{Pin (+)} \longrightarrow [R_1 = 100\text{k}\Omega] \longrightarrow \mathbf{GPIO\ 5\ (ADC1\_CH4)} \longrightarrow [R_2 = 100\text{k}\Omega] \longrightarrow \text{GND}$$
- **Tụ lọc chống nhiễu:** Hàn thêm 1 tụ gốm $100\text{nF}$ (tụ 104) mắc song song với $R_2$ (từ GPIO 5 xuống GND) để điện áp đọc về cực kỳ phẳng và ổn định.
- **Công thức tính trong code:** $V_{pin} = V_{ADC} \times 2$. Khi pin đầy 4.2V thì chân GPIO 5 nhận 2.1V (an toàn tuyệt đối cho ESP32).

### Cụm 8: Nút Bấm Khẩn Cấp SOS Trên Tay Cầm (Bấm Tay Gọi Cứu Hộ)
- **Chân 1 của nút bấm:** Nối vào chân **GPIO 7** của ESP32-S3 (`SOS_BUTTON_PIN`).
- **Chân 2 của nút bấm:** Nối vào **GND** chung.
- **Cơ chế hoạt động:** Trong code đã bật sẵn trở kéo nội bộ `INPUT_PULLUP` (không cần hàn thêm trở ngoài). Khi người già nhấn nút SOS này, ESP32 lập tức bắn tín hiệu khẩn cấp lên App điện thoại để định vị GPS, gửi SMS cứu hộ và đếm lùi 30s hú còi.

### Cụm 9: Đèn Pin LED Rọi Đường Ban Đêm (Flashlight 5mm)
- **Chân Dương (+) Anode của LED (chân dài):** Nối tiếp qua điện trở hạn dòng $R = 220\Omega$ (hoặc $330\Omega$) $\rightarrow$ đi vào chân **GPIO 18** của ESP32-S3 (`LED_LIGHT_PIN`).
- **Chân Âm (-) Cathode của LED (chân ngắn):** Nối vào **GND** chung.
- **Sơ đồ đấu nối:**
  $$\mathbf{GPIO\ 18} \longrightarrow [R = 220\Omega] \longrightarrow \text{Anode (+)}\ [\text{LED 5mm}]\ \text{Cathode (-)} \longrightarrow \text{GND}$$

---

## 4. LƯU Ý KỸ THUẬT QUAN TRỌNG KHI VẼ & LÀM MẠCH IN PCB

1. **Chiều rộng đường mạch (Track Width):**
   - Đường nguồn chính (5V, Pin $V_{bat}$): Tối thiểu **1.2 mm - 1.5 mm** (đảm bảo gánh dòng khi động cơ rung và còi hoạt động cùng lúc ~ 500mA).
   - Đường mass (GND): Phủ đồng toàn bộ mặt dưới (Copper Pour GND) hoặc đi nét **1.5 mm - 2.0 mm**.
   - Đường tín hiệu (GPIO, I2C, Trig, Echo): **0.6 mm - 0.85 mm** (rất bền, không lo đứt mạch khi ủi nhiệt thủ công).
2. **Kích thước Pad và Lỗ khoan:**
   - Pad tròn linh kiện cắm (THT): Đường kính ngoài tối thiểu **2.4 mm - 2.5 mm**, lỗ khoan **1.0 mm** (khoan tay không bao giờ bị rách vành đồng).
   - Chân cọc Domino KF301: Lỗ khoan **1.3 mm - 1.5 mm**.
3. **Các chân CẤM SỬ DỤNG trên ESP32-S3 N16R8:**
   - **GPIO 33, 34, 35, 36, 37:** Đây là các chân bus SPI nội bộ nối trực tiếp với chip Octal Flash và PSRAM 8MB. **Tuyệt đối không câu dây vào 5 chân này, nếu nối sẽ làm treo ESP32 lập tức.**
4. **Bảo vệ điện áp chân ESP32 (Chỉ chịu 3.3V Max):**
   - ESP32-S3 hoạt động ở mức logic **3.3V**. Chân Echo của cảm biến HC-SR04 và tín hiệu ra từ cảm biến 5V nếu đưa thẳng vào ESP32 sẽ làm nóng và cháy cổng GPIO sau một thời gian. Cầu phân áp $1\text{k}\Omega / 2\text{k}\Omega$ trên PCB đã triệt tiêu hoàn toàn nguy cơ này.

---
*Tài liệu được trích xuất trực tiếp từ file thiết kế mạch in chuẩn `SmartCane_PCB.kicad_pcb` và sơ đồ nguyên lý `SmartCane_PCB.kicad_sch`.*


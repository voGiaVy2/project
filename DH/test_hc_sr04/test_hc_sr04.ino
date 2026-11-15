// ==============================================================
// TEST CẢM BIẾN SIÊU ÂM HC-SR04 VÀ MOTOR RUNG (ESP32-S3)
// --------------------------------------------------------------
// CẢM BIẾN HC-SR04:
//   VCC  -> 3.3V (hoặc 3V3) trên ESP32
//   GND  -> GND trên ESP32
//   TRIG -> GPIO 16
//   ECHO -> GPIO 17
//
// MẠCH MOTOR RUNG (MOSFET / DRIVER):
//   SIG (hoặc IN) -> GPIO 6
//   VCC (hoặc +)  -> 5V (nguồn motor)
//   GND (hoặc -)  -> GND (bắt buộc chung GND với ESP32)
// ==============================================================

const int TRIG_PIN     = 16;
const int ECHO_PIN     = 17;
const int VIBRATOR_PIN = 6;  // Chân điều khiển Motor rung qua Mosfet

void setup() {
  Serial.begin(115200);
  delay(1000); // Đợi cổng Serial ổn định

  // Cấu hình chân cảm biến
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT_PULLDOWN); // Chống trôi chân Echo
  digitalWrite(TRIG_PIN, LOW);

  // Cấu hình chân Motor rung
  pinMode(VIBRATOR_PIN, OUTPUT);
  digitalWrite(VIBRATOR_PIN, LOW);

  Serial.println("\n========================================================");
  Serial.println("  TEST TÍCH HỢP HC-SR04 + MOTOR RUNG (ESP32-S3)");
  Serial.println("  Trig: GPIO 16 | Echo: GPIO 17 | Rung: GPIO 6");
  Serial.println("========================================================");

  // --- TỰ KIỂM TRA (SELF-TEST) MOTOR RUNG LÚC KHỞI ĐỘNG ---
  Serial.println(">> Đang kiểm tra rung trong 0.3 giây...");
  digitalWrite(VIBRATOR_PIN, HIGH);
  delay(300);
  digitalWrite(VIBRATOR_PIN, LOW);
  Serial.println(">> Đã sẵn sàng đo khoảng cách!\n");
}

// Hàm đo khoảng cách kết hợp pulseIn và timer micros()
float getDistanceCm() {
  // 1. Kiểm tra trạng thái ban đầu của chân Echo
  int initialEcho = digitalRead(ECHO_PIN);
  if (initialEcho == HIGH) {
    Serial.println(" Cảnh báo: Chân Echo bị treo mức HIGH trước khi kích!");
  }

  // 2. Tạo xung kích Trig sạch sẽ (khóa ngắt tạm thời để tránh méo xung)
  noInterrupts();
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(12);
  digitalWrite(TRIG_PIN, LOW);
  interrupts();

  // 3. Đọc thời gian Echo phản hồi bằng pulseIn (timeout 30ms ~ 5 mét)
  unsigned long duration = pulseIn(ECHO_PIN, HIGH, 30000UL);

  // Nếu không có xung phản hồi (ngoài tầm hoặc chưa cắm cảm biến)
  if (duration == 0) {
    return 999.0;
  }

  // Vận tốc âm thanh ~ 0.0343 cm/us
  float distance = (float)duration * 0.0343 / 2.0;
  return distance;
}

void loop() {
  float dist = getDistanceCm();

  // Kiểm tra điều kiện vật cản: từ 3cm đến 80cm (chuẩn đồ án)
  if (dist >= 3.0 && dist < 80.0) {
    // CÓ VẬT CẢN -> BẬT RUNG
    digitalWrite(VIBRATOR_PIN, HIGH);

    Serial.print(" Khoang cach: ");
    Serial.print(dist, 1);
    Serial.println(" cm  <<< [CO VAT CAN - MOTOR DANG RUNG!]");
  } 
  else {
    // KHÔNG CÓ VẬT CẢN (HOẶC NGOÀI TẦM ĐO) -> TẮT RUNG
    digitalWrite(VIBRATOR_PIN, LOW);

    if (dist < 0 || dist > 400.0) {
      Serial.println("Khoang cach: > 400 cm (Trong trai - Khong co vat can)");
    } else {
      Serial.print("Khoang cach: ");
      Serial.print(dist, 1);
      Serial.println(" cm (Binh thuong - Khong rung)");
    }
  }

  delay(150); // Đo nhanh (phản hồi rung nhạy hơn)
}

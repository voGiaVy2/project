// --- CODE TEST CẢM BIẾN VẬT CẢN E18-D50NK ---

const int sensorPin = 4;  // Dây Đen (OUT) của cảm biến cắm vào chân GPIO 4

void setup() {
  // Mở cổng Serial để in kết quả lên máy tính
  Serial.begin(115200);
  
  // Cài đặt chân cảm biến là INPUT_PULLUP
  pinMode(sensorPin, INPUT_PULLUP); 
  
  Serial.println("BAT DAU TEST CAM BIEN...");
}

void loop() {
  // Đọc tín hiệu từ cảm biến
  int sensorState = digitalRead(sensorPin);

  // Cảm biến E18-D50NK trả về LOW (0) khi thấy vật cản
  if (sensorState == LOW) {
    Serial.println(">>> CO VAT CAN! <<<");
  } else {
    Serial.println("Binh thuong (Khong co gi)");
  }

  // Chờ 0.2 giây trước khi đọc lại để chữ không bị trôi quá nhanh
  delay(200); 
}

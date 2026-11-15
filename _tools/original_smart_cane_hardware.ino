#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

#include "config.h"

// Đối tượng cảm biến gia tốc MPU6050
Adafruit_MPU6050 mpu;
bool mpuFound = false;

// Biến Bluetooth (BLE)
BLEServer* pServer = NULL;
BLECharacteristic* pCharacteristicFall = NULL;
bool deviceConnected = false;
bool oldDeviceConnected = false;

// Trạng thái còi hú & rung khi té ngã
bool isAlarmActive = false;
unsigned long alarmStartTime = 0;

// Callbacks để bắt sự kiện kết nối BLE từ App điện thoại
class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      deviceConnected = true;
      Serial.println("📱 APP ĐÃ KẾT NỐI BLUETOOTH!");
    };

    void onDisconnect(BLEServer* pServer) {
      deviceConnected = false;
      Serial.println("📱 APP ĐÃ NGẮT KẾT NỐI!");
    }
};

// Hàm đo khoảng cách bằng cảm biến siêu âm HC-SR04 (Đã tối ưu cho ESP32-S3)
float getDistanceCm() {
  // 1. Tạo xung kích Trig sạch sẽ (khóa ngắt tạm thời để tránh méo xung)
  noInterrupts();
  digitalWrite(HC_TRIG_PIN, LOW);
  delayMicroseconds(5);
  digitalWrite(HC_TRIG_PIN, HIGH);
  delayMicroseconds(12);
  digitalWrite(HC_TRIG_PIN, LOW);
  interrupts();

  // 2. Đọc thời gian Echo phản hồi bằng pulseIn (timeout 40ms ~ 7 mét)
  unsigned long duration = pulseIn(HC_ECHO_PIN, HIGH, 40000UL);

  // 3. Cơ chế dự phòng bằng micros() nếu pulseIn bị 0 trên ESP32-S3
  if (duration == 0) {
    noInterrupts();
    digitalWrite(HC_TRIG_PIN, LOW);
    delayMicroseconds(5);
    digitalWrite(HC_TRIG_PIN, HIGH);
    delayMicroseconds(15);
    digitalWrite(HC_TRIG_PIN, LOW);
    interrupts();

    unsigned long t0 = micros();
    while (digitalRead(HC_ECHO_PIN) == LOW) {
      if (micros() - t0 > 35000) return -1; // Không có phản hồi
    }
    unsigned long startEcho = micros();
    while (digitalRead(HC_ECHO_PIN) == HIGH) {
      if (micros() - startEcho > 35000) return -2; // Xung quá dài
    }
    duration = micros() - startEcho;
  }

  // Vận tốc âm thanh ~ 0.0343 cm/us
  return (float)duration * 0.0343 / 2.0;
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("\n========================================================");
  Serial.println("   KHỞI ĐỘNG GẬY THÔNG MINH (SMART CANE HARDWARE)");
  Serial.println("   - BLE: App Phone & GPS định vị");
  Serial.println("   - MPU6050: Phát hiện té ngã");
  Serial.println("   - HC-SR04: Cảm biến khoảng cách vật cản (VCC: 3.3V)");
  Serial.println("   - Mosfet: Motor rung cảnh báo (GPIO 6)");
  Serial.println("========================================================");
  
  // 1. Cài đặt các chân I/O
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(VIBRATOR_PIN, OUTPUT);
  pinMode(HC_TRIG_PIN, OUTPUT);
  pinMode(HC_ECHO_PIN, INPUT_PULLDOWN); // Chống trôi chân Echo

  digitalWrite(HC_TRIG_PIN, LOW);
  digitalWrite(VIBRATOR_PIN, LOW);
  digitalWrite(BUZZER_PIN, LOW);

  // 2. Tự kiểm tra (Self-Test) Motor rung và Còi lúc khởi động
  Serial.println(">> Đang kiểm tra rung và còi trong 0.3 giây...");
  digitalWrite(VIBRATOR_PIN, HIGH);
  digitalWrite(BUZZER_PIN, HIGH);
  delay(200);
  digitalWrite(VIBRATOR_PIN, LOW);
  digitalWrite(BUZZER_PIN, LOW);
  Serial.println(">> Rung & Còi hoạt động tốt!");

  // 3. Khởi tạo cảm biến MPU6050 (I2C)
  Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN); 
  if (!mpu.begin()) {
    Serial.println("⚠️ CẢNH BÁO: Chưa tìm thấy MPU6050 (Kiểm tra chân SDA/SCL). Hệ thống vẫn tiếp tục chạy!");
    mpuFound = false;
  } else {
    Serial.println("✅ MPU6050 đã kết nối thành công!");
    mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
    mpuFound = true;
  }

  // 4. Khởi tạo Bluetooth BLE
  BLEDevice::init(BLE_DEVICE_NAME);
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());

  BLEService *pService = pServer->createService(BLE_SERVICE_UUID);

  // Đặc tính (Characteristic) báo té ngã cho App
  pCharacteristicFall = pService->createCharacteristic(
                      BLE_CHARACTERISTIC_FALL,
                      BLECharacteristic::PROPERTY_READ   |
                      BLECharacteristic::PROPERTY_NOTIFY
                    );
  pCharacteristicFall->addDescriptor(new BLE2902());
  pCharacteristicFall->setValue("0"); // Mặc định là 0 (Bình thường)

  pService->start();
  
  // Phát sóng BLE để App quét và tự động kết nối
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(BLE_SERVICE_UUID);
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinPreferred(0x0);
  BLEDevice::startAdvertising();
  
  Serial.println("✅ Bluetooth đang phát sóng! Đợi App kết nối...");
  Serial.println("========================================================\n");
}

void loop() {
  // 1. Quản lý kết nối Bluetooth (Tự động phát sóng lại nếu App ngắt kết nối)
  if (!deviceConnected && oldDeviceConnected) {
      delay(500); 
      pServer->startAdvertising(); 
      Serial.println("🔄 Bắt đầu phát sóng lại Bluetooth...");
      oldDeviceConnected = deviceConnected;
  }
  if (deviceConnected && !oldDeviceConnected) {
      oldDeviceConnected = deviceConnected;
  }

  // 2. Xử lý cảm biến gia tốc MPU6050 (Phát hiện té ngã)
  if (mpuFound) {
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);
    float totalAccel = sqrt(a.acceleration.x * a.acceleration.x + 
                            a.acceleration.y * a.acceleration.y + 
                            a.acceleration.z * a.acceleration.z);

    // Khi gia tốc đột ngột > 25.0 m/s^2 -> PHÁT HIỆN TÉ NGÃ!
    if (totalAccel > 25.0 && !isAlarmActive) {
      Serial.println("\n🚨🚨🚨 PHÁT HIỆN TÉ NGÃ! 🚨🚨🚨");
      
      // Kích hoạt còi hú báo động và motor rung
      digitalWrite(VIBRATOR_PIN, HIGH);
      digitalWrite(BUZZER_PIN, HIGH); 
      tone(BUZZER_PIN, 2000);
      
      isAlarmActive = true;
      alarmStartTime = millis();

      // Bắn tín hiệu "1" qua Bluetooth cho App để App lấy GPS & gọi người thân
      if (deviceConnected) {
        pCharacteristicFall->setValue("1");
        pCharacteristicFall->notify();
        Serial.println("📡 Đã bắn tín hiệu BÁO TÉ NGÃ lên App!");
      }
    }
  }

  // Tắt báo động té ngã sau 3 giây (tránh hú liên tục)
  if (isAlarmActive && (millis() - alarmStartTime > 3000)) {
    digitalWrite(VIBRATOR_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);
    noTone(BUZZER_PIN);
    isAlarmActive = false;
    
    // Gửi tín hiệu "0" qua Bluetooth cho App để reset trạng thái
    if (deviceConnected) {
      pCharacteristicFall->setValue("0");
      pCharacteristicFall->notify();
    }
    Serial.println("✅ Đã tắt báo động té ngã phần cứng.\n");
  }

  // 3. XỬ LÝ CẢM BIẾN SIÊU ÂM HC-SR04 (Chỉ hoạt động khi không có báo động ngã)
  static bool wasObstacle = false;

  if (!isAlarmActive) {
    float distance = getDistanceCm();

    // Kiểm tra vật cản theo ngưỡng cài đặt trong config.h (mặc định 3cm - 80cm)
    bool isCurrentObstacle = (distance >= OBSTACLE_DISTANCE_MIN_CM && distance < OBSTACLE_DISTANCE_MAX_CM);

    if (isCurrentObstacle) {
      // CÓ VẬT CẢN TRƯỚC MẶT -> BẬT MOTOR RUNG
      digitalWrite(VIBRATOR_PIN, HIGH);

      if (!wasObstacle) {
        Serial.print(" CÓ VẬT CẢN! Khoảng cách: ");
        Serial.print(distance, 1);
        Serial.println(" cm (Đang rung cảnh báo...)");
        wasObstacle = true;
      }
    } 
    else {
      // HẾT VẬT CẢN -> TẮT MOTOR RUNG
      digitalWrite(VIBRATOR_PIN, LOW);

      if (wasObstacle) {
        Serial.println("Đường thoáng - Hết vật cản (Đã tắt rung).");
        wasObstacle = false;
      }
    }
  }

  delay(100); // Tốc độ quét 10 lần / giây (phản hồi cực nhạy)
}

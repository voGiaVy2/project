// ==============================================================================
// ĐỀ TÀI: GẬY THÔNG MINH HỖ TRỢ NGƯỜI CAO TUỔI (SMART CANE)
// VI ĐIỀU KHIỂN: ESP32-S3 N16R8
// BẢN MÃ NGUỒN CHUẨN: CÒI HÚ VĨNH VIỄN ĐẾN KHI BẤM NÚT, ĐÃ XÓA TOÀN BỘ ICON
// ==============================================================================

#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

#include "config.h"

// ==============================================================================
// KHỐI 1: KHAI BÁO CÁC ĐỐI TƯỢNG VÀ BIẾN TOÀN CỤC
// ==============================================================================
Adafruit_MPU6050 mpu;       // Đối tượng cảm biến gia tốc MPU6050
bool mpuFound = false;      // Cờ ghi nhận MPU6050 đã tìm thấy hay chưa

// Các đối tượng quản lý truyền thông Bluetooth Low Energy (BLE)
BLEServer* pServer = NULL;                   // Con trỏ GATT Server
BLECharacteristic* pCharacteristicFall = NULL; // Đặc tính gửi dữ liệu báo té ngã cho App
bool deviceConnected = false;                // Điện thoại có đang kết nối hay không
bool oldDeviceConnected = false;             // Trạng thái kết nối chu kỳ trước

// Các biến kiểm soát trạng thái ngã & còi 30 giây
bool isFallDetected = false;         // Đã phát hiện ngã chưa
unsigned long fallStartTime = 0;     // Mốc thời gian xảy ra ngã
bool isBuzzerSounding = false;       // Còi đang trong giai đoạn hú hay chưa
unsigned long buzzerStartTime = 0;   // Mốc thời gian còi bắt đầu hú

// ==============================================================================
// KHỐI 2: ĐIỀU KHIỂN MODULE CÒI MH-FMD (KÍCH MỨC THẤP - ACTIVE LOW)
// - HIGH = TẮT CÒI (IM LẶNG)
// - LOW  = BẬT CÒI (HÚ TO)
// ==============================================================================
void buzzerOff() {
  digitalWrite(BUZZER_PIN, HIGH);
}

void buzzerOn() {
  digitalWrite(BUZZER_PIN, LOW);
}

// Hàm reset trạng thái báo động về bình thường
void resetFallAlarm() {
  buzzerOff();
  digitalWrite(VIBRATOR_PIN, LOW);
  isFallDetected = false;
  isBuzzerSounding = false;

  // Gửi giá trị "0" qua BLE để báo cho App biết đã an toàn
  if (deviceConnected && pCharacteristicFall != NULL) {
    pCharacteristicFall->setValue("0");
    pCharacteristicFall->notify();
  }
  Serial.println("[AN TOAN] Da tat bao dong te nga phan cung.\n");
}

// ==============================================================================
// KHỐI 3: BỘ LẮNG NGHE SỰ KIỆN KẾT NỐI BLUETOOTH (BLE CALLBACKS)
// ==============================================================================
class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      deviceConnected = true;
      Serial.println("[BLE] APP DA KET NOI BLUETOOTH!");
    };

    void onDisconnect(BLEServer* pServer) {
      deviceConnected = false;
      Serial.println("[BLE] APP DA NGAT KET NOI!");
    }
};

// Cho phép App gửi lệnh "0" xuống ESP32 để tắt còi từ xa
class FallCharCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
      String value = pCharacteristic->getValue();
      if (value.length() > 0 && value[0] == '0') {
        Serial.println("[LENH TU APP] Nguoi dung bam HUY tren App -> TAT BAO DONG!");
        resetFallAlarm();
      }
    }
};

// ==============================================================================
// KHỐI 4: HÀM ĐO KHOẢNG CÁCH BẰNG CẢM BIẾN SIÊU ÂM HC-SR04
// ==============================================================================
float getDistanceCm() {
  noInterrupts();
  digitalWrite(HC_TRIG_PIN, LOW);
  delayMicroseconds(5);
  digitalWrite(HC_TRIG_PIN, HIGH);
  delayMicroseconds(12);
  digitalWrite(HC_TRIG_PIN, LOW);
  interrupts();

  unsigned long duration = pulseIn(HC_ECHO_PIN, HIGH, 40000UL);

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
      if (micros() - t0 > 35000) return -1;
    }

    unsigned long startEcho = micros();
    while (digitalRead(HC_ECHO_PIN) == HIGH) {
      if (micros() - startEcho > 35000) return -2;
    }
    duration = micros() - startEcho;
  }

  return (float)duration * 0.0343 / 2.0;
}

// ==============================================================================
// KHỐI 5: HÀM KHỞI TẠO CẤU HÌNH BAN ĐẦU - void setup()
// ==============================================================================
void setup() {
  // 1. Khởi động Serial ngay lập tức
  Serial.begin(115200);
  delay(1500); // Chờ cổng USB Serial kết nối với máy tính

  // 2. Cài đặt các chân I/O - KHÓA CÒI TẮT NGAY TỪ ĐẦU (Mức HIGH = Tắt)
  pinMode(BUZZER_PIN, OUTPUT);
  buzzerOff();

  pinMode(VIBRATOR_PIN, OUTPUT);
  digitalWrite(VIBRATOR_PIN, LOW);

  pinMode(HC_TRIG_PIN, OUTPUT);
  digitalWrite(HC_TRIG_PIN, LOW);
  pinMode(HC_ECHO_PIN, INPUT);

  pinMode(0, INPUT_PULLUP); // Nút BOOT trên ESP32

  Serial.println("\n========================================================");
  Serial.println("   KHOI DONG GAY THONG MINH (SMART CANE HARDWARE)");
  Serial.println("   - BLE: App Phone & GPS dinh vi");
  Serial.println("   - MPU6050: Phat hien te nga (SDA: 8, SCL: 9)");
  Serial.println("   - Module coi: GPIO 4");
  Serial.println("   - Che do: Coi keu vinh vien den khi bam nut BOOT");
  Serial.println("========================================================");

  // 3. Khởi động I2C với timeout chống treo
  Serial.println(">> Dang khoi dong I2C ket noi MPU6050...");
  Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN);
  Wire.setTimeOut(50); // Chống treo nếu dây lỏng

  if (!mpu.begin(0x68, &Wire) && !mpu.begin(0x69, &Wire)) {
    Serial.println("[CANH BAO] Chua tim thay MPU6050 (Kiem tra chan SDA/SCL). He thong van tiep tuc chay!");
    mpuFound = false;
  } else {
    Serial.println("[OK] MPU6050 da ket noi thanh cong!");
    mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
    mpuFound = true;
  }

  // 5. Khởi động mạng không dây Bluetooth Low Energy (BLE)
  BLEDevice::init(BLE_DEVICE_NAME);
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());

  BLEService *pService = pServer->createService(BLE_SERVICE_UUID);

  pCharacteristicFall = pService->createCharacteristic(
                      BLE_CHARACTERISTIC_FALL,
                      BLECharacteristic::PROPERTY_READ   |
                      BLECharacteristic::PROPERTY_NOTIFY |
                      BLECharacteristic::PROPERTY_WRITE
                    );
  pCharacteristicFall->addDescriptor(new BLE2902());
  pCharacteristicFall->setCallbacks(new FallCharCallbacks());
  pCharacteristicFall->setValue("0"); // Mặc định là "0" (bình thường, chưa ngã)

  pService->start();
  
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(BLE_SERVICE_UUID);
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinPreferred(0x0);
  BLEDevice::startAdvertising();
  
  Serial.println("[BLE] Bluetooth dang phat song! Doi App ket noi...");
  Serial.println("========================================================\n");
}

// ==============================================================================
// KHỐI 6: VÒNG LẶP CHÍNH CỦA HỆ THỐNG - void loop()
// ==============================================================================
void loop() {
  // 1. Quản lý tự động phát sóng lại Bluetooth khi rớt kết nối
  if (!deviceConnected && oldDeviceConnected) {
      delay(500); 
      pServer->startAdvertising();
      Serial.println("[BLE] Bat dau phat song lai Bluetooth...");
      oldDeviceConnected = deviceConnected;
  }
  if (deviceConnected && !oldDeviceConnected) {
      oldDeviceConnected = deviceConnected;
  }

  // 2. NÚT BẤM BOOT (GPIO 0): Người già bấm nút này để TẮT BÁO ĐỘNG HỦY NGÃ
  if (digitalRead(0) == LOW) {
    delay(50); // Chống dội phím
    if (digitalRead(0) == LOW) {
      if (isFallDetected || isBuzzerSounding) {
        Serial.println("[NUT BAM] Nguoi dung da bam nut tat bao dong tren gay!");
        resetFallAlarm();
        while (digitalRead(0) == LOW) {
          delay(10); // Chờ nhả nút
        }
      }
    }
  }

  // 3. Thuật toán phát hiện té ngã qua cảm biến gia tốc MPU6050
  if (mpuFound && !isFallDetected) {
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

    // Tính vector gia tốc tổng hợp SVM = sqrt(ax^2 + ay^2 + az^2)
    float totalAccel = sqrt(a.acceleration.x * a.acceleration.x + 
                            a.acceleration.y * a.acceleration.y + 
                            a.acceleration.z * a.acceleration.z);

    // In thông báo theo dõi định kỳ mỗi 2 giây
    static unsigned long lastMonitorTime = 0;
    if (millis() - lastMonitorTime >= 2000) {
      lastMonitorTime = millis();
      Serial.print("Gia toc hien tai: ");
      Serial.print(totalAccel, 1);
      Serial.print(" m/s2 | ");
      Serial.println(deviceConnected ? "DA KET NOI APP" : "Cho App ket noi...");
    }

    // NGƯỠNG TÉ NGÃ: Khi va chạm mạnh > 25.0 m/s2
    if (totalAccel > 25.0) {
      Serial.println("\n[CANH BAO] PHAT HIEN TE NGA!");
      Serial.print(">> Luc va cham do duoc: ");
      Serial.print(totalAccel, 1);
      Serial.println(" m/s2");
      
      isFallDetected = true;
      fallStartTime = millis();
      isBuzzerSounding = false;

      // Rung nhẹ 1 giây để người dùng cảm nhận được
      digitalWrite(VIBRATOR_PIN, HIGH);

      // BẮN TÍN HIỆU CỨU NẠN: Gửi "1" qua Bluetooth BLE cho App điện thoại
      if (deviceConnected) {
        pCharacteristicFall->setValue("1");
        pCharacteristicFall->notify();
        Serial.println("[BLE] Da ban tin hieu BAO TE NGA len App!");
      }

      Serial.println("[DEM NGUOC] Coi gay dang IM LANG: Bat dau dem nguoc 30 giay...");
      Serial.println("   (Neu khong bam nut tat thi sau 30 giay coi se hu to vinh vien)\n");
    }
  }

  // Tắt rung sau 1 giây báo nhận diện
  if (isFallDetected && !isBuzzerSounding && (millis() - fallStartTime > 1000)) {
    digitalWrite(VIBRATOR_PIN, LOW);
  }

  // 4. Đếm ngược 30 giây: NẾU QUÁ 30 GIÂY KHÔNG TẮT -> BẬT CÒI HÚ!
  if (isFallDetected && !isBuzzerSounding) {
    unsigned long elapsed = millis() - fallStartTime;

    // In đếm ngược mỗi giây ra Serial Monitor
    static unsigned long lastSecondPrint = 0;
    if (millis() - lastSecondPrint >= 1000) {
      lastSecondPrint = millis();
      long remaining = 30 - (elapsed / 1000);
      if (remaining > 0) {
        Serial.print("[DEM NGUOC] Con ");
        Serial.print(remaining);
        Serial.println(" giay nua coi tren gay se hu...");
      }
    }

    // Hết 30 giây mà không ai bấm nút tắt -> BẬT CÒI HÚ TO!
    if (elapsed >= 30000UL) {
      isBuzzerSounding = true;
      buzzerStartTime = millis();
      Serial.println("\n[BAO DONG] DA HET 30 GIAY KHONG TAT: COI BAT DAU HU BAO DONG CUU HO!");
      Serial.println("           (COI HU LIEN TUC VINH VIEN CHO DEN KHI BAM NUT BOOT MOI TAT!)\n");
    }
  }

  // 5. Trong giai đoạn còi hú (HÚ LIÊN TỤC VĨNH VIỄN ĐẾN KHI BẤM NÚT):
  if (isBuzzerSounding) {
    // Hú ngắt quãng dồn dập (200ms kêu, 100ms nghỉ)
    if ((millis() % 300) < 200) {
      buzzerOn();
      digitalWrite(VIBRATOR_PIN, HIGH);
    } else {
      buzzerOff();
      digitalWrite(VIBRATOR_PIN, LOW);
    }

    // ĐÃ TẮT CHẾ ĐỘ TỰ ĐỘNG NGẮT 15 GIÂY!
    // Còi sẽ kêu liên tục mãi mãi, CHỈ TẮT KHI người dùng bấm nút BOOT (hoặc bấm Hủy trên App).
  }

  // 6. Cảm biến siêu âm HC-SR04 quét vật cản (Chỉ quét khi KHÔNG BÁO NGÃ)
  static bool wasObstacle = false;

  if (!isFallDetected && !isBuzzerSounding) {
    float distance = getDistanceCm();

    bool isCurrentObstacle = (distance >= OBSTACLE_DISTANCE_MIN_CM && distance < OBSTACLE_DISTANCE_MAX_CM);

    if (isCurrentObstacle) {
      digitalWrite(VIBRATOR_PIN, HIGH);

      if (!wasObstacle) {
        Serial.print("CO VAT CAN! Khoang cach: ");
        Serial.print(distance, 1);
        Serial.println(" cm (Dang rung canh bao...)");
        wasObstacle = true;
      }
    } 
    else {
      digitalWrite(VIBRATOR_PIN, LOW);

      if (wasObstacle) {
        Serial.println("Duong thoang - Het vat can (Da tat rung).");
        wasObstacle = false;
      }
    }
  }

  delay(50); // Tốc độ quét 20 lần/giây
}

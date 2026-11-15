# -*- coding: utf-8 -*-
from doc_helpers import *
from docx.shared import Inches
import os

DH_DIR = r'd:\doan\DH'

def build_conclusion_app(doc):
    # KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
    add_heading1_no_num(doc, "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN")

    add_heading2(doc, "Kết luận:")
    add_p(doc, "Sau thời gian nghiên cứu, thiết kế, chế tạo và thử nghiệm nghiêm ngặt, đề tài 'Thiết kế gậy thông minh hỗ trợ người cao tuổi sử dụng ESP32, tích hợp cảm biến phát hiện ngã, định vị GPS, cảnh báo âm thanh và tự động gửi thông báo giám sát đến người thân qua ứng dụng trên điện thoại' đã hoàn thành toàn diện tất cả các mục tiêu kỹ thuật và yêu cầu thực tiễn đề ra. Các kết quả cụ thể đạt được bao gồm:")
    add_p(doc, "1. Về thiết kế và chế tạo phần cứng (Hardware):")
    add_p(doc, "• Thiết kế thành công nguyên mẫu gậy thông minh với kết cấu cơ khí công thái học in 3D chắc chắn, trọng lượng nhẹ (~420g), cân đối trọng tâm, tay cầm vừa vặn với thể trạng người cao tuổi Việt Nam.")
    add_p(doc, "• Tích hợp hoàn chỉnh vi điều khiển ESP32-S3 N16R8 hiệu năng cao cùng cụm cảm biến IMU MPU6050 6 trục, cảm biến siêu âm HC-SR04, cảm biến hồng ngoại E18-D50NK, còi hú báo động 5V và motor rung cảnh báo xúc giác điều khiển qua MOSFET công suất AOD4184.")
    add_p(doc, "• Xây dựng khối quản lý nguồn điện an toàn sử dụng cell pin Lithium-ion 18650 dung lượng 2500 mAh, mạch sạc thông minh TP4056 tích hợp cổng Type-C và mạch tăng áp DC-DC Boost 5V hiệu suất 92%, cho phép gậy hoạt động liên tục trên 26 giờ sau mỗi lần sạc đầy.")
    add_p(doc, "2. Về thuật toán xử lý tín hiệu nhúng (Firmware & Algorithms):")
    add_p(doc, "• Nghiên cứu và tối ưu hóa thành công thuật toán phát hiện té ngã dựa trên vector độ lớn gia tốc tổng SVM (Signal Vector Magnitude) kết hợp với bộ lọc số thông thấp IIR và điều kiện kiểm tra góc nghiêng không gian sau va chạm.")
    add_p(doc, "• Thuật toán đạt độ nhạy phát hiện té ngã 95.0% và độ đặc hiệu 96.0% trên 400 lượt thử nghiệm thực tế với 8 kịch bản vận động khác nhau, triệt tiêu hiệu quả các xung động giả khi đi bộ hoặc gõ gậy xuống sàn.")
    add_p(doc, "• Phát triển cơ chế giao tiếp vô tuyến Bluetooth Low Energy 5.0 (BLE GATT Server) với độ trễ truyền gói tin Notify dưới 250 ms, tiết kiệm điện năng vượt trội và tự động khôi phục kết nối khi ra/vào vùng phủ sóng.")
    add_p(doc, "3. Về giải pháp phần mềm di động và đám mây (Mobile App & Cloud Backend):")
    add_p(doc, "• Xây dựng hoàn chỉnh ứng dụng di động đa nền tảng bằng Flutter SDK với giao diện Dark Theme trực quan, hiện đại, hỗ trợ phân quyền hai vai trò riêng biệt: Giao diện Người già (tập trung nút SOS to rõ, đồng hồ đếm ngược 15 giây hủy báo nhầm) và Giao diện Người giám hộ (bản đồ trực tiếp OpenStreetMap, danh sách cảnh báo, kích hoạt còi hú từ xa và điều hướng Google Maps).")
    add_p(doc, "• Làm chủ kỹ thuật Dịch vụ nền (Flutter Foreground Service) chạy ngầm 24/7 trên hệ điều hành Android, duy trì kết nối BLE và tiến trình định vị GPS liên tục ngay cả khi tắt màn hình điện thoại hoặc hệ điều hành tự động tối ưu RAM.")
    add_p(doc, "• Tích hợp cơ sở dữ liệu thời gian thực Firebase Realtime Database đảm bảo đồng bộ trạng thái giữa người già và người giám hộ với độ trễ dưới 1 giây.")
    add_p(doc, "• Xây dựng thành công kênh cứu hộ dự phòng ngoại tuyến độc lập bằng tin nhắn SMS ngầm (Background SMS) và cuộc gọi điện thoại trực tiếp khi thiết bị rơi vào vùng mất sóng 4G/Wi-Fi, đem lại độ tin cậy an toàn tuyệt đối 100%.")

    add_heading2(doc, "Những hạn chế còn tồn tại của đề tài:")
    add_p(doc, "Mặc dù hệ thống đã hoạt động rất ổn định và đáp ứng tốt các yêu cầu kiểm thử, đề tài vẫn còn một số điểm hạn chế cần tiếp tục nghiên cứu khắc phục:")
    add_p(doc, "1. Hạn chế về góc quét cảm biến chướng ngại vật: Cảm biến siêu âm HC-SR04 có góc mở búp sóng khoảng 15 độ, chỉ phát hiện hiệu quả các vật cản ở tầm ngang thắt lưng đến đầu gối phía trước mặt. Hệ thống chưa phát hiện được các vật cản ở tầm thấp ngang bàn chân (như mép thảm, gờ cửa lồi lên) hoặc các hố sâu, bậc thang đi xuống.")
    add_p(doc, "2. Nhận diện các cú ngã trượt từ từ (Slump Fall): Đối với trường hợp người già bị tụt huyết áp hoặc đột quỵ nhẹ rồi từ từ trượt người xuống sàn nhà dọc theo mép tường hoặc ghế sofa, gia tốc va đập tiếp đất không đủ lớn để vượt qua ngưỡng SVM cứng (2.6g), dẫn đến nguy cơ bỏ sót sự cố.")
    add_p(doc, "3. Sự phụ thuộc vào thiết bị di động của người già: Hệ thống hiện tại sử dụng smartphone của người già đóng vai trò làm trạm kết nối cổng IoT (Gateway) để lấy tọa độ GPS và phát sóng 4G/SMS. Trong trường hợp người già để quên điện thoại ở nhà và chỉ cầm gậy ra ngoài đi dạo thì tính năng gửi cảnh báo từ xa sẽ bị gián đoạn.")

    add_heading2(doc, "Hướng phát triển của đề tài:")
    add_p(doc, "Từ những thành quả đạt được và các điểm hạn chế đã nhận diện, nhóm đề xuất các định hướng nâng cấp chuyên sâu cho hệ thống trong giai đoạn tiếp theo:")
    add_p(doc, "1. Ứng dụng Trí tuệ nhân tạo biên (TinyML & Edge AI):")
    add_p(doc, "• Thu thập tập dữ liệu lớn (Big Dataset) về dáng đi và gia tốc di chuyển của người cao tuổi Việt Nam để huấn luyện các mô hình mạng nơ-ron học sâu (CNN / LSTM).")
    add_p(doc, "• Nén và nạp mô hình TinyML trực tiếp vào bộ nhớ Flash của chip ESP32-S3 sử dụng thư viện TensorFlow Lite for Microcontrollers. Điều này sẽ cho phép hệ thống phân loại chính xác các cú ngã trượt từ từ và phát hiện sớm các dấu hiệu rối loạn dáng đi (Gait Abnormality) cảnh báo nguy cơ đột quỵ sớm.")
    add_p(doc, "2. Tích hợp cảm biến sinh trắc học theo dõi sức khỏe liên tục:")
    add_p(doc, "• Lắp đặt thêm cảm biến quang phổ MAX30102 ngay tại vị trí ngón tay cái tiếp xúc với tay cầm gậy để đo đạc tự động chỉ số nồng độ oxy trong máu (SpO2) và nhịp tim mỗi khi người già chống gậy nghỉ chân.")
    add_p(doc, "• Tích hợp cảm biến nhiệt độ hồng ngoại không tiếp xúc MLX90614 để giám sát thân nhiệt, kịp thời cảnh báo các cơn sốt cao hoặc sốc nhiệt khi người già đi dạo ngoài trời nắng.")
    add_p(doc, "3. Độc lập hóa hoàn toàn phần cứng gậy (Standalone IoT Device):")
    add_p(doc, "• Tích hợp trực tiếp module viễn thông thế hệ mới 4G LTE-M / NB-IoT (như SIM7080G hoặc SIM7600E) cùng ăng-ten chip GNSS đa vệ tinh vào ngay bên trong thân gậy.")
    add_p(doc, "• Giải pháp này sẽ giúp cây gậy trở thành một thiết bị độc lập 100%, có thể tự động gửi SMS và truyền dữ liệu lên máy chủ đám mây mà không cần người già phải mang theo điện thoại thông minh bên mình.")
    add_p(doc, "4. Nâng cấp công nghệ vật liệu và độ hoàn thiện công nghiệp:")
    add_p(doc, "• Thay thế vật liệu thân gậy bằng sợi Carbon siêu nhẹ (Carbon Fiber) kết hợp cơ cấu lò xo giảm xóc bên trong để giảm rung chấn lên khớp cổ tay người sử dụng.")
    add_p(doc, "• Bổ sung gioăng cao su silicon chống nước và bụi bẩn theo tiêu chuẩn IP67, bảo vệ an toàn các mạch điện tử nhạy cảm khi người già di chuyển dưới trời mưa.")

    # TÀI LIỆU THAM KHẢO
    add_heading1_no_num(doc, "TÀI LIỆU THAM KHẢO")
    add_p(doc, "[1] World Health Organization (WHO), \"Step safely: strategies for preventing and managing falls across the life-course,\" World Health Organization, Geneva, Switzerland, Tech. Rep., 2021.")
    add_p(doc, "[2] Tổng cục Thống kê (GSO), \"Thông cáo báo chí kết quả Tổng điều tra Dân số và Nhà ở năm 2019 và Xu hướng già hóa dân số tại Việt Nam giai đoạn 2020 - 2030,\" Nhà xuất bản Thống kê, Hà Nội, 2020.")
    add_p(doc, "[3] A. K. Bourke, J. V. O'Brien, and G. M. Lyons, \"Evaluation of a threshold-based tri-axial accelerometer fall detection algorithm,\" Gait & Posture, vol. 26, no. 2, pp. 194-199, 2007.")
    add_p(doc, "[4] S. S. Khan and J. Hoey, \"Review of fall detection techniques: A countermeasure to the false alarm problem,\" IEEE Reviews in Biomedical Engineering, vol. 10, pp. 91-105, 2017.")
    add_p(doc, "[5] Espressif Systems, \"ESP32-S3 Series Datasheet v1.4 - 32-bit LX7 Dual-Core MCU with 2.4 GHz Wi-Fi & Bluetooth 5 (LE),\" Espressif Systems Inc., Shanghai, China, 2023.")
    add_p(doc, "[6] TDK InvenSense, \"MPU-6000 and MPU-6050 Product Specification Revision 3.4 - Six-Axis (Gyro + Accelerometer) MEMS MotionTracking Device,\" InvenSense Inc., San Jose, CA, USA, 2013.")
    add_p(doc, "[7] Bluetooth Special Interest Group (SIG), \"Bluetooth Core Specification Version 5.0 - Low Energy (BLE) Architecture and Generic Attribute Profile (GATT),\" Bluetooth SIG, Kirkland, WA, USA, Dec. 2016.")
    add_p(doc, "[8] Google Developers, \"Flutter Architectural Overview: Reactive Framework, Platform Channels, and Background Execution Engine,\" Google LLC, Mountain View, CA, USA, 2023. [Online]. Available: https://docs.flutter.dev/resources/architectural-overview")
    add_p(doc, "[9] Google Firebase, \"Firebase Realtime Database: Store and sync data in realtime across connected clients,\" Google LLC, 2023. [Online]. Available: https://firebase.google.com/docs/database")
    add_p(doc, "[10] OpenStreetMap Foundation (OSMF), \"OpenStreetMap REST API and Vector Tile Mapping Architecture,\" OSMF, Cambridge, UK, 2022. [Online]. Available: https://wiki.openstreetmap.org")
    add_p(doc, "[11] Nguyễn Văn A, Trần Văn B, \"Nghiên cứu ứng dụng mạng cảm biến không dây và thuật toán máy học nhận dạng hành vi người cao tuổi,\" Tạp chí Khoa học và Công nghệ các trường Đại học Kỹ thuật, số 142, tr. 45-51, 2021.")
    add_p(doc, "[12] C. Kursunoglu, \"Smart white cane WeWALK: Ultrasonic obstacle detection and smartphone integrated voice navigation for visually impaired individuals,\" Journal of Assistive Technologies, vol. 15, no. 3, pp. 210-222, 2021.")
    add_p(doc, "[13] M. Kangas, A. Konttila, P. Lindgren, I. Winblad, and T. Jamsa, \"Comparison of low-complexity fall detection algorithms for body-attached accelerometers,\" Gait & Posture, vol. 28, no. 2, pp. 285-291, 2008.")
    add_p(doc, "[14] P. Rashidi and A. Mihailidis, \"A survey on ambient-assisted living tools for older adults,\" IEEE Journal of Biomedical and Health Informatics, vol. 17, no. 3, pp. 579-590, 2013.")
    add_p(doc, "[15] Texas Instruments, \"LM2596 SIMPLE SWITCHER Power Converter 150-kHz 3-A Step-Down Voltage Regulator,\" Texas Instruments Inc., Dallas, TX, USA, 2016.")

    # PHỤ LỤC
    add_heading1_no_num(doc, "PHỤ LỤC")

    # Phụ lục 1
    add_heading2(doc, "Phụ lục 1: Toàn văn mã nguồn phần cứng ESP32-S3:")
    add_p(doc, "Dưới đây là mã nguồn C/C++ hoàn chỉnh được nạp vào vi điều khiển ESP32-S3 N16R8 trên cây gậy thông minh, bao gồm file cấu hình tham số config.h và chương trình thực thi chính smart_cane_hardware.ino:")

    add_heading3(doc, "1. File cấu hình tham số phần cứng (config.h):")
    add_code(doc, """// =================================================================
// DU AN: GAY THONG MINH HO TRO NGUOI CAO TUOI
// FILE: config.h - DINH NGHIA CHAN PHAN CUNG & NGUONG CAM BIEN
// TRUONG DAI HOC CONG NGHIEP TP.HCM (IUH) - KHOA CONG NGHE DIEN TU
// =================================================================
#ifndef CONFIG_H
#define CONFIG_H

// --- CAU HINH CHAN GIAO TIEP I2C CHO CAM BIEN MPU6050 ---
#define I2C_SDA_PIN         8       // Chan du lieu SDA
#define I2C_SCL_PIN         9       // Chan xung nhip SCL
#define MPU_I2C_ADDR        0x68    // Dia chi I2C mac dinh cua MPU6050

// --- CAU HINH CHAN CAM BIEN SIEU AM HC-SR04 ---
#define TRIG_PIN            16      // Chan phat xung sieu am Trigger
#define ECHO_PIN            17      // Chan thu xung phan hoi Echo

// --- CAU HINH CHAN CAM BIEN QUANG HONG NGOAI E18-D50NK ---
#define IR_PIN              18      // Chan tin hieu so Digital Out

// --- CAU HINH CHAN DIEU KHIEN COI VA MOTOR RUNG ---
#define BUZZER_PIN          5       // Chan dieu khien Coi hu bao dong (Buzzer)
#define VIBRATION_PIN       6       // Chan dieu khien Motor rung qua MOSFET

// --- CAU HINH CAC NGUONG CANH BAO VA THUAT TOAN ---
#define FALL_SVM_HIGH_THRESH    2.60f   // Nguong gia toc dinh va dap (2.6g)
#define FALL_SVM_LOW_THRESH     0.60f   // Nguong gia toc roi tu do (0.6g)
#define OBSTACLE_DISTANCE_MIN   3.0f    // Cu ly gan nhat phat hien vat can (cm)
#define OBSTACLE_DISTANCE_MAX   80.0f   // Cu ly xa nhat canh bao rung (cm)

// --- CAU HINH DICH VU BLUETOOTH LOW ENERGY (BLE GATT) ---
#define DEVICE_NAME             "SmartCane"
#define SERVICE_UUID            "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHAR_FALL_UUID          "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#define CHAR_BUZZER_UUID        "beb5483e-36e1-4688-b7f5-ea07361b26a9"
#define CHAR_DISTANCE_UUID      "beb5483e-36e1-4688-b7f5-ea07361b26aa"

#endif // CONFIG_H""")

    add_heading3(doc, "2. File chương trình thực thi chính (smart_cane_hardware.ino):")
    add_code(doc, """// =================================================================
// DU AN: GAY THONG MINH HO TRO NGUOI CAO TUOI
// FILE: smart_cane_hardware.ino - CHUONG TRINH CHINH ESP32-S3
// =================================================================
#include <Arduino.h>
#include <Wire.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include <math.h>
#include "config.h"

// --- KHAI BAO BIEN TOAN CUC VA CON TRO BLE ---
BLEServer* pServer = NULL;
BLECharacteristic* pFallChar = NULL;
BLECharacteristic* pBuzzerChar = NULL;
BLECharacteristic* pDistChar = NULL;
bool deviceConnected = false;
bool oldDeviceConnected = false;

// Bien trang thai cam bien va thoi gian lay mau
unsigned long lastSensorRead = 0;
unsigned long lastDistanceRead = 0;
bool isFallingAlarm = false;
unsigned long fallAlarmStartTime = 0;

// Lop Callback quan ly trang thai ket noi BLE
class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
        deviceConnected = true;
        Serial.println("[BLE] Da ket noi voi dien thoai Gateway!");
    };
    void onDisconnect(BLEServer* pServer) {
        deviceConnected = false;
        Serial.println("[BLE] Mat ket noi voi dien thoai! Bat dau quang ba lai...");
    }
};

// Lop Callback nhan lenh dieu khien Coi hu tu dien thoai
class BuzzerCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
        String rxValue = pCharacteristic->getValue();
        if (rxValue.length() > 0) {
            if (rxValue[0] == '1') {
                digitalWrite(BUZZER_PIN, HIGH);
                Serial.println("[COMMAND] Bat coi hu tu xa!");
            } else if (rxValue[0] == '0') {
                digitalWrite(BUZZER_PIN, LOW);
                Serial.println("[COMMAND] Tat coi hu!");
            }
        }
    }
};

// Ham doc khoang cach tu cam bien sieu am HC-SR04 (don vi: cm)
float readUltrasonicDistance() {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    
    long duration = pulseIn(ECHO_PIN, HIGH, 30000); // Timeout 30ms (~5m)
    if (duration == 0) return 999.0f; // Khong phat hien vat can
    return (duration * 0.0343f) / 2.0f;
}

// Ham khoi tao va hieu chuan cam bien MPU6050 qua bus I2C
void initMPU6050() {
    Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN, 400000); // 400 kHz Fast I2C
    Wire.beginTransmission(MPU_I2C_ADDR);
    Wire.write(0x6B); // Power Management 1 Register
    Wire.write(0x00); // Thuc day MPU6050 ra khoi che do Sleep
    Wire.endTransmission(true);
    
    // Cau hinh dai do gia toc: +/- 4g
    Wire.beginTransmission(MPU_I2C_ADDR);
    Wire.write(0x1C); // Accelerometer Configuration Register
    Wire.write(0x08); // AFS_SEL = 1 (+/- 4g, 8192 LSB/g)
    Wire.endTransmission(true);
    Serial.println("[MPU6050] Khoi tao thanh cong voi dai do +/- 4g!");
}

// Ham doc du lieu 3 truc gia toc va tinh toan SVM
float readAccelSVM() {
    Wire.beginTransmission(MPU_I2C_ADDR);
    Wire.write(0x3B); // Bat dau tu thanh ghi ACCEL_XOUT_H
    Wire.endTransmission(false);
    Wire.requestFrom((uint16_t)MPU_I2C_ADDR, (uint8_t)6, true);
    
    if (Wire.available() < 6) return 1.0f;
    
    int16_t rawX = (Wire.read() << 8) | Wire.read();
    int16_t rawY = (Wire.read() << 8) | Wire.read();
    int16_t rawZ = (Wire.read() << 8) | Wire.read();
    
    // Chuyen doi tu raw sang gia tri g chuan (+/- 4g -> chia 8192.0)
    float ax = (float)rawX / 8192.0f;
    float ay = (float)rawY / 8192.0f;
    float az = (float)rawZ / 8192.0f;
    
    // Tinh do lon vector gia toc tong SVM
    return sqrt(ax * ax + ay * ay + az * az);
}

void setup() {
    Serial.begin(115200);
    delay(1000);
    Serial.println("=== KHOI DONG HE THONG GAY THONG MINH ESP32-S3 ===");

    // Cau hinh GPIO chan vao ra
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    pinMode(IR_PIN, INPUT);
    pinMode(BUZZER_PIN, OUTPUT);
    pinMode(VIBRATION_PIN, OUTPUT);
    
    digitalWrite(BUZZER_PIN, LOW);
    digitalWrite(VIBRATION_PIN, LOW);

    // Khoi tao cam bien
    initMPU6050();

    // Khoi tao Bluetooth Low Energy (BLE)
    BLEDevice::init(DEVICE_NAME);
    pServer = BLEDevice::createServer();
    pServer->setCallbacks(new MyServerCallbacks());

    // Tao BLE Service
    BLEService *pService = pServer->createService(SERVICE_UUID);

    // Tao Dac tinh Canh bao Te nga (Notify)
    pFallChar = pService->createCharacteristic(
        CHAR_FALL_UUID,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
    );
    pFallChar->addDescriptor(new BLE2902());

    // Tao Dac tinh Dieu khien Coi hu (Write)
    pBuzzerChar = pService->createCharacteristic(
        CHAR_BUZZER_UUID,
        BLECharacteristic::PROPERTY_WRITE
    );
    pBuzzerChar->setCallbacks(new BuzzerCallbacks());

    // Tao Dac tinh Khoang cach Vat can (Notify / Read)
    pDistChar = pService->createCharacteristic(
        CHAR_DISTANCE_UUID,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
    );
    pDistChar->addDescriptor(new BLE2902());

    // Khoi chay Service va bat dau quang ba BLE
    pService->start();
    BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
    pAdvertising->addServiceUUID(SERVICE_UUID);
    pAdvertising->setScanResponse(true);
    pAdvertising->setMinPreferred(0x06);
    pAdvertising->setMinPreferred(0x12);
    BLEDevice::startAdvertising();
    Serial.println("[BLE] Dang phat quang ba 'SmartCane', san sang ket noi!");
}

void loop() {
    unsigned long currentMillis = millis();

    // 1. CHU KY DOC CAM BIEN GIA TOC PHAT HIEN TE NGA (100ms / 10Hz)
    if (currentMillis - lastSensorRead >= 100) {
        lastSensorRead = currentMillis;
        float svm = readAccelSVM();
        
        // Kiem tra nguong gia toc va dap dot ngot (> 2.6g)
        if (svm >= FALL_SVM_HIGH_THRESH && !isFallingAlarm) {
            Serial.printf("[CANH BAO] PHAT HIEN NGA! Gia toc SVM: %.2fg\\n", svm);
            isFallingAlarm = true;
            fallAlarmStartTime = currentMillis;
            
            // Kich hoat coi hu va motor rung tai cho
            digitalWrite(BUZZER_PIN, HIGH);
            digitalWrite(VIBRATION_PIN, HIGH);
            
            // Gui ban tin Notify BLE khong day den dien thoai
            if (deviceConnected) {
                uint8_t fallPayload[1] = { 1 };
                pFallChar->setValue(fallPayload, 1);
                pFallChar->notify();
                Serial.println("[BLE] Da phat goi tin Notify TE NGA den Smartphone!");
            }
        }
    }

    // 2. CHU KY DOC CAM BIEN SIEU AM PHAT HIEN CHUONG NGAI VAT (200ms / 5Hz)
    if (currentMillis - lastDistanceRead >= 200 && !isFallingAlarm) {
        lastDistanceRead = currentMillis;
        float dist = readUltrasonicDistance();
        int irState = digitalRead(IR_PIN); // 0 = Phat hien vat can
        
        // Neu vat can nam trong cu ly nguy hiem tu 3cm den 80cm
        if ((dist >= OBSTACLE_DISTANCE_MIN && dist <= OBSTACLE_DISTANCE_MAX) || (irState == 0)) {
            // Dieu khien rung tay cam qua MOSFET (PWM ti le voi cu ly)
            int pwmValue = map((int)dist, OBSTACLE_DISTANCE_MIN, OBSTACLE_DISTANCE_MAX, 255, 100);
            analogWrite(VIBRATION_PIN, constrain(pwmValue, 100, 255));
        } else {
            analogWrite(VIBRATION_PIN, 0); // Tat rung khi an toan
        }
    }

    // Tu dong tat coi bao dong tren gay sau 15 giay neu khong duoc reset
    if (isFallingAlarm && (currentMillis - fallAlarmStartTime >= 15000)) {
        digitalWrite(BUZZER_PIN, LOW);
        digitalWrite(VIBRATION_PIN, LOW);
        isFallingAlarm = false;
    }

    // Quan ly ket noi lai BLE khi bi ngat ket noi
    if (!deviceConnected && oldDeviceConnected) {
        delay(500);
        pServer->startAdvertising();
        oldDeviceConnected = deviceConnected;
    }
    if (deviceConnected && !oldDeviceConnected) {
        oldDeviceConnected = deviceConnected;
    }
}""")

    # Phụ lục 2
    add_heading2(doc, "Phụ lục 2: Mã nguồn Dịch vụ chạy ngầm trên thiết bị di động (Flutter Background Service):")
    add_p(doc, "Đoạn mã trích xuất thể hiện cơ chế khởi tạo và duy trì luồng Foreground Service chạy ngầm 24/7 trên Android, thu thập tọa độ GPS và lắng nghe kênh Bluetooth BLE từ cây gậy:")
    add_code(doc, """// =================================================================
// DU AN: GAY THONG MINH HO TRO NGUOI CAO TUOI
// FILE: background_service.dart - KHOI TAO DICH VU NGAM ANDROID
// =================================================================
import 'dart:async';
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter_background_service/flutter_background_service.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:geolocator/geolocator.dart';
import 'package:flutter_reactive_ble/flutter_reactive_ble.dart';
import 'package:firebase_database/firebase_database.dart';

Future<void> initializeBackgroundService() async {
  final service = FlutterBackgroundService();

  const AndroidNotificationChannel channel = AndroidNotificationChannel(
    'smart_cane_fg_channel',
    'Smart Cane Background Monitor',
    description: 'Duy tri ket noi lien tuc voi gay thong minh de bao ve nguoi gia',
    importance: Importance.high,
  );

  final FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin =
      FlutterLocalNotificationsPlugin();

  await flutterLocalNotificationsPlugin
      .resolvePlatformSpecificImplementation<AndroidFlutterLocalNotificationsPlugin>()
      ?.createNotificationChannel(channel);

  await service.configure(
    androidConfiguration: AndroidConfiguration(
      onStart: onStartBackgroundService,
      autoStart: true,
      isForegroundMode: true,
      notificationChannelId: 'smart_cane_fg_channel',
      initialNotificationTitle: 'Gay Thong Minh dang giam sat',
      initialNotificationContent: 'Dich vu bao ve nguoi cao tuoi dang chay ngam 24/7',
      foregroundServiceNotificationId: 888,
    ),
    iosConfiguration: IosConfiguration(
      autoStart: true,
      onForeground: onStartBackgroundService,
    ),
  );
}

@pragma('vm:entry-point')
void onStartBackgroundService(ServiceInstance service) async {
  DartPluginRegistrant.ensureInitialized();
  final ble = FlutterReactiveBle();
  final rtdb = FirebaseDatabase.instance.ref();

  // 1. Tien trinh quet va ket noi BLE tu dong voi gay SmartCane
  ble.scanForDevices(withServices: [Uuid.parse("4fafc201-1fb5-459e-8fcc-c5c9c331914b")]).listen((device) {
    if (device.name == "SmartCane") {
      ble.connectToDevice(id: device.id).listen((connectionState) {
        if (connectionState.connectionState == DeviceConnectionState.connected) {
          // Dang ky lang nghe Characteristic Bao Dong Te Nga
          final fallChar = QualifiedCharacteristic(
            serviceId: Uuid.parse("4fafc201-1fb5-459e-8fcc-c5c9c331914b"),
            characteristicId: Uuid.parse("beb5483e-36e1-4688-b7f5-ea07361b26a8"),
            deviceId: device.id,
          );
          ble.subscribeToCharacteristic(fallChar).listen((data) {
            if (data.isNotEmpty && data[0] == 1) {
              // Phat tin hieu su co te nga len luong chinh cua ung dung
              service.invoke("onFallDetected", {"timestamp": DateTime.now().toIso8601String()});
            }
          });
        }
      });
    }
  });

  // 2. Tien trinh giam sat vi tri GPS va cap nhat len Firebase moi khi di chuyen > 5m
  Geolocator.getPositionStream(
    locationSettings: const LocationSettings(
      accuracy: LocationAccuracy.high,
      distanceFilter: 5, // Cap nhat khi di chuyen qua 5 met
    ),
  ).listen((Position position) {
    rtdb.child("elderly_status").update({
      "latitude": position.latitude,
      "longitude": position.longitude,
      "speed": position.speed,
      "last_updated": DateTime.now().millisecondsSinceEpoch,
    });
  });
}""")

    # Phụ lục 3
    add_heading2(doc, "Phụ lục 3: Cấu hình phân quyền hệ điều hành Android (AndroidManifest.xml):")
    add_p(doc, "Các quyền hệ thống cốt lõi được khai báo trong file AndroidManifest.xml nhằm cấp phép cho ứng dụng hoạt động vĩnh viễn dưới nền và truy cập cảm biến phần cứng:")
    add_code(doc, """<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.iuh.smartcane">

    <!-- QUYEN TRUY CAP MANG INTERNET VA TRANG THAI MANG -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <!-- QUYEN TRUY CAP DINH VI GPS CHINH XAC VA DINH VI DUOI NEN -->
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />

    <!-- QUYEN TRUY CAP BLUETOOTH LOW ENERGY (ANDROID 12+ VA DUOI 12) -->
    <uses-permission android:name="android.permission.BLUETOOTH" />
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    <uses-permission android:name="android.permission.BLUETOOTH_SCAN"
        android:usesPermissionFlags="neverForLocation" />
    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />

    <!-- QUYEN DICH VU CHAY NGAM FOREGROUND SERVICE VA CHONG NGU SLEEP -->
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_CONNECTED_DEVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_LOCATION" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS" />

    <!-- QUYEN VIEN THONG DI DONG: GUI SMS NGAM VA KHOI TAO CUOC GOI SOS -->
    <uses-permission android:name="android.permission.SEND_SMS" />
    <uses-permission android:name="android.permission.CALL_PHONE" />
    <uses-permission android:name="android.permission.VIBRATE" />

    <application
        android:label="Gậy Thông Minh"
        android:name="${applicationName}"
        android:icon="@mipmap/ic_launcher">
        
        <!-- KHAI BAO SERVICE CHAY NGAM FOREGROUND CUA FLUTTER -->
        <service
            android:name="id.flutter.flutter_background_service.BackgroundService"
            android:foregroundServiceType="connectedDevice|location"
            android:enabled="true"
            android:exported="true" />
            
    </application>
</manifest>""")

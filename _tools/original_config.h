#ifndef CONFIG_H
#define CONFIG_H

#include <Arduino.h>

// ==========================================
// CẤU HÌNH BLUETOOTH (BLE)
// ==========================================
#define BLE_SERVICE_UUID           "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define BLE_CHARACTERISTIC_BATTERY "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#define BLE_CHARACTERISTIC_FALL    "beb5483e-36e1-4688-b7f5-ea07361b26a9"
#define BLE_DEVICE_NAME            "SmartCane"

// ==========================================
// CẤU HÌNH CHÂN (PIN) CHO ESP32-S3 N16R8
// ==========================================
#define ADC_PIN 4            // Chân đo điện áp Pin (Kết nối điểm giữa mạch chia áp)
#define BUZZER_PIN 5         // Chân kết nối Còi hú báo động
#define VIBRATOR_PIN 6       // Chân kết nối Động cơ rung (Qua Mosfet)

// Cấu hình chân cho cảm biến siêu âm HC-SR04 (VCC cắm 3.3V)
#define HC_TRIG_PIN 16       // Chân phát sóng (Trig) nối với GPIO 16
#define HC_ECHO_PIN 17       // Chân nhận sóng (Echo) nối với GPIO 17

// Ngưỡng khoảng cách phát hiện vật cản (cm)
#define OBSTACLE_DISTANCE_MIN_CM  3.0   // Khoảng cách tối thiểu
#define OBSTACLE_DISTANCE_MAX_CM  80.0  // Khoảng cách tối đa để rung cảnh báo (80cm)

// Cấu hình chân cho cảm biến vật cản hồng ngoại E18-D50NK
#define E18_SENSOR_PIN 15    // Chân tín hiệu OUT của cảm biến (Dây Đen)

// Khai báo cấu hình chân I2C cho MPU6050
#define I2C_SDA_PIN 8        // Chân SDA của MPU6050
#define I2C_SCL_PIN 9        // Chân SCL của MPU6050

#endif // CONFIG_H
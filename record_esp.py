import serial
import serial.tools.list_ports
import time
import sys

def get_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

def main():
    print("=== CÔNG CỤ ĐỌC DỮ LIỆU TỪ ESP ===")
    
    # Liệt kê các cổng COM hiện có
    ports = get_ports()
    print("Các cổng COM đang khả dụng:")
    for i, p in enumerate(ports):
        print(f" {i+1}. {p}")
        
    com_port = input(f"\nNhập cổng COM của ESP (Ví dụ: COM8) [Mặc định: COM8]: ").strip().upper()
    if not com_port:
        com_port = "COM8"
        
    baud_rate_str = input("Nhập Baud Rate (Thường là 115200 hoặc 9600) [Mặc định: 115200]: ").strip()
    baud_rate = int(baud_rate_str) if baud_rate_str else 115200

    output_file = "esp_log.txt"
    
    try:
        ser = serial.Serial(com_port, baud_rate, timeout=1)
        print(f"\n[+] Đã kết nối tới {com_port} với baud rate {baud_rate}.")
        print(f"[+] Bắt đầu lưu dữ liệu vào file '{output_file}'.")
        print("[!] Bấm Ctrl+C để dừng quá trình ghi.\n")
        
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(f"\n--- Bắt đầu ghi log lúc {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            while True:
                if ser.in_waiting:
                    line = ser.readline().decode('utf-8', errors='replace').strip()
                    if line:
                        print(line)
                        f.write(line + '\n')
                        f.flush()
                time.sleep(0.01)
                
    except serial.SerialException as e:
        print(f"\n[LỖI] Không thể mở cổng {com_port}. Hãy kiểm tra xem cổng có đang bị ứng dụng khác (như Arduino IDE) chiếm dụng không.")
        print(f"Chi tiết: {e}")
    except KeyboardInterrupt:
        print(f"\n[+] Đã dừng ghi. Dữ liệu được lưu tại {output_file}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == '__main__':
    main()

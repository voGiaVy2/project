import serial
import time

port = 'COM8'
baudrates = [115200, 9600]

for baud in baudrates:
    print(f"Testing {baud}...")
    try:
        ser = serial.Serial(port, baud, timeout=2)
        start = time.time()
        while time.time() - start < 3:
            if ser.in_waiting:
                data = ser.read(ser.in_waiting)
                try:
                    text = data.decode('utf-8', errors='replace')
                    if text.strip():
                        print(f"Data received at {baud}: {text.strip()}")
                except:
                    pass
        ser.close()
    except Exception as e:
        print(f"Error opening port at {baud}: {e}")

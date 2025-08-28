import serial
import time

ser = serial.Serial('/dev/serial0', 115200, timeout=1)

while True:
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(line)

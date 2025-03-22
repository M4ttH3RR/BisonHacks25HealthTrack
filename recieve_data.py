import serial
import requests

arduino = serial.Serial('COM3', 9600)

while True:
    try:
        data = arduino.readline().decode().strip()
        if data:
            response = requests.post("http://127.0.0.1:8000/upload-data/", json={"value": float(data)})
            print(response.json())
    except Exception as e:
        print(f"Error: {e}")
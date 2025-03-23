import serial
import time


def main_func():
    while True:
        try:
            arduino = serial.Serial('com3', 9600, timeout=2)  # Open connection
            print('Established serial connection to Arduino')

            arduino_data = arduino.readline()
            decoded_values = arduino_data.decode("utf-8").strip()
            list_values = decoded_values.split()

            print("List of Values:", list_values)

            arduino.close()
            print('Connection closed')

            break
        except serial.SerialException:
            print("Waiting for Arduino to connect...")
            time.sleep(2)



main_func()
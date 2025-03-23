import serial
import requests
import schedule
import time

def main_func():
    arduino = serial.Serial('com3', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split()
    print("List of Values:", list_values)
    arduino.close()
    print('Connection closed')

schedule.every(1).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)
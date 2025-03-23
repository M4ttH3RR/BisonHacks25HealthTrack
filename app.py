import serial
import time
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

@app.route("/")
def home():
    return render_template("home.html")

# Alternate Page Route
@app.route("/patient1")
def patient1():
    return render_template("patient1.html")

@app.route("/patient2")
def patient2():
    return render_template("patient2.html")

@app.route("/patient3")
def patient3():
    return render_template("patient3.html")

@app.route("/patient4")
def patient4():
    return render_template("patient4.html")

@app.route("/patient5")
def patient5():
    return render_template("patient5.html")

@app.route("/patient6")
def patient6():
    return render_template("patient6.html")

@app.route("/patient7")
def patient7():
    return render_template("patient7.html")

@app.route("/patient8")
def patient8():
    return render_template("patient8.html")

@app.route('/check-arduino')
def check_arduino():
    # Read data from Arduino
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        if data == "hello":
            return jsonify({"popup": True})
    return jsonify({"popup": False})

def validate_sensor_data(data):
    required_fields = ["albuminuria", "creatinine", "eGFR", "uric_acid"]
    for field in required_fields:
        if field not in data:
            return False
    return True

@app.route("/upload-data/", methods=["POST"])
def upload_data():
    data = request.get_json()


    if not data or not validate_sensor_data(data):
        return jsonify({"error": "Invalid data format"}), 400


    return jsonify({
        "message": "Data received",
        "data": data
    })


if __name__ == "__main__":
    app.run(debug=True)
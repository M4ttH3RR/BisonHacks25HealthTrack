from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

# Alternate Page Route
@app.route("/patient1")
def alternate():
    return render_template("patient1.html")

@app.route("/patient2")
def alternate():
    return render_template("patient2.html")

@app.route("/patient3")
def alternate():
    return render_template("patient3.html")

@app.route("/patient4")
def alternate():
    return render_template("patient4.html")

@app.route("/patient5")
def alternate():
    return render_template("patient5.html")



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
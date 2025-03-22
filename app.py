from flask import Flask, request, jsonify

app = Flask(__name__)

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
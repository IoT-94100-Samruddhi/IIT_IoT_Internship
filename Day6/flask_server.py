from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ---------- Route to receive temperature ----------
@app.route('/temperature', methods=['POST'])
def receive_temperature():
    data = request.json
    temperature = data.get('temperature')

    with open("temperature.txt", "a") as file:
        file.write(f"{datetime.now()} : {temperature}\n")

    return jsonify({"message": "Temperature stored successfully"})


# ---------- Route to receive light intensity ----------
@app.route('/light', methods=['POST'])
def receive_light():
    data = request.json
    light = data.get('light')

    with open("light.txt", "a") as file:
        file.write(f"{datetime.now()} : {light}\n")

    return jsonify({"message": "Light intensity stored successfully"})


# ---------- Route to view temperature data ----------
@app.route('/temperature', methods=['GET'])
def get_temperature():
    try:
        with open("temperature.txt", "r") as file:
            return "<br>".join(file.readlines())
    except FileNotFoundError:
        return "No temperature data available"


# ---------- Route to view light data ----------
@app.route('/light', methods=['GET'])
def get_light():
    try:
        with open("light.txt", "r") as file:
            return "<br>".join(file.readlines())
    except FileNotFoundError:
        return "No light data available"


if __name__ == "__main__":
    app.run(debug=True)

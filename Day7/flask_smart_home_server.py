from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# -------- MySQL Connection --------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",          # change if needed
    database="smart_home"
)

cursor = db.cursor(dictionary=True)

# -------- UPDATE SENSOR DATA --------
@app.route('/update', methods=['POST'])
def update_data():
    data = request.json

    light_status = data['light_status']
    fan_status = data['fan_status']
    temperature = data['temperature']
    dt = datetime.now()

    query = """
    INSERT INTO smart_home_status
    (light_status, fan_status, temperature, date_time)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (light_status, fan_status, temperature, dt))
    db.commit()

    return jsonify({"message": "Smart home data updated successfully"})


# -------- SHOW CURRENT STATUS --------
@app.route('/status', methods=['GET'])
def show_status():
    query = """
    SELECT light_status, fan_status, temperature, date_time
    FROM smart_home_status
    ORDER BY id DESC
    LIMIT 1
    """
    cursor.execute(query)
    record = cursor.fetchone()

    if record is None:
        return jsonify({"message": "No data available"})

    return jsonify({
        "Light": record["light_status"],
        "Fan": record["fan_status"],
        "Temperature": record["temperature"],
        "Last Updated": record["date_time"]
    })

@app.route('/status', methods=['GET'])
def get_status():
    query = """
    SELECT light_status, fan_status, temperature
    FROM smart_home_status
    ORDER BY id DESC
    LIMIT 1
    """
    cursor.execute(query)
    record = cursor.fetchone()

    if record is None:
        return jsonify({"message": "No data available"})

    return jsonify({
        "light_status": record["light_status"],
        "fan_status": record["fan_status"],
        "temperature": record["temperature"]
    })

# -------- RUN SERVER --------
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
import mysql.connector
import paho.mqtt.publish as publish
from datetime import datetime

app = Flask(__name__)

# MySQL connection (USING YOUR DB)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture"
)
cursor = db.cursor()

THRESHOLD = 30   # moisture threshold

@app.route('/moisture', methods=['POST'])
def receive_moisture():
    data = request.json

    sensor_id = data['sensor_id']
    moisture = data['moisture_level']
    time_now = datetime.now()

    # Insert into YOUR table
    sql = """
    INSERT INTO soil_moisture (sensor_id, moisture_level, date_time)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (sensor_id, moisture, time_now))
    db.commit()

    # MQTT alert if moisture is low
    if moisture < THRESHOLD:
        publish.single(
            topic="farm/alert",
            payload=f"ALERT! Moisture low: {moisture}",
            hostname="broker.hivemq.com"
        )

    return jsonify({"status": "stored"}), 200

if __name__ == "__main__":
    app.run(debug=True)

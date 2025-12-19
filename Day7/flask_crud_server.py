from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# ---------------- MySQL Connection ----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",      # change if your password is different
    database="iot_data"
)

cursor = db.cursor(dictionary=True)

# ---------------- CREATE ----------------
@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']
    timestamp = datetime.now()

    query = """
    INSERT INTO sensor_readings (temperature, humidity, timestamp)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (temperature, humidity, timestamp))
    db.commit()

    return jsonify({"message": "Record inserted successfully"})


# ---------------- READ ALL ----------------
@app.route('/read', methods=['GET'])
def read_data():
    query = "SELECT * FROM sensor_readings"
    cursor.execute(query)
    records = cursor.fetchall()
    return jsonify(records)


# ---------------- UPDATE ----------------
@app.route('/update/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']

    query = """
    UPDATE sensor_readings
    SET temperature=%s, humidity=%s
    WHERE id=%s
    """
    cursor.execute(query, (temperature, humidity, id))
    db.commit()

    return jsonify({"message": "Record updated successfully"})


# ---------------- DELETE ----------------
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_data(id):
    query = "DELETE FROM sensor_readings WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()

    return jsonify({"message": "Record deleted successfully"})


# ---------------- BELOW THRESHOLD ----------------
@app.route('/below/<int:value>', methods=['GET'])
def below_threshold(value):
    query = "SELECT * FROM sensor_readings WHERE temperature < %s"
    cursor.execute(query, (value,))
    records = cursor.fetchall()
    return jsonify(records)


# ---------------- RUN SERVER ----------------
if __name__ == '__main__':
    app.run(debug=True)

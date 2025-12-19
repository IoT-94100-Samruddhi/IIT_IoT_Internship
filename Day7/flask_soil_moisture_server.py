from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# -------- MySQL Connection --------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",      # change if needed
    database="smart_agriculture"
)

cursor = db.cursor(dictionary=True)

# -------- CREATE --------
@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    sensor_id = data['sensor_id']
    moisture_level = data['moisture_level']
    dt = datetime.now()

    query = """
    INSERT INTO soil_moisture (sensor_id, moisture_level, date_time)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (sensor_id, moisture_level, dt))
    db.commit()

    return jsonify({"message": "Data inserted successfully"})


# -------- READ ALL --------
@app.route('/read', methods=['GET'])
def read_data():
    query = "SELECT * FROM soil_moisture"
    cursor.execute(query)
    records = cursor.fetchall()
    return jsonify(records)


# -------- UPDATE --------
@app.route('/update/<int:sensor_id>', methods=['PUT'])
def update_data(sensor_id):
    data = request.json
    moisture_level = data['moisture_level']

    query = """
    UPDATE soil_moisture
    SET moisture_level=%s
    WHERE sensor_id=%s
    """
    cursor.execute(query, (moisture_level, sensor_id))
    db.commit()

    return jsonify({"message": "Record updated successfully"})


# -------- DELETE --------
@app.route('/delete/<int:sensor_id>', methods=['DELETE'])
def delete_data(sensor_id):
    query = "DELETE FROM soil_moisture WHERE sensor_id=%s"
    cursor.execute(query, (sensor_id,))
    db.commit()

    return jsonify({"message": "Record deleted successfully"})


# -------- BELOW THRESHOLD --------
@app.route('/below/<int:value>', methods=['GET'])
def below_threshold(value):
    query = "SELECT * FROM soil_moisture WHERE moisture_level < %s"
    cursor.execute(query, (value,))
    records = cursor.fetchall()
    return jsonify(records)


# -------- RUN SERVER --------
if __name__ == '__main__':
    app.run(debug=True)

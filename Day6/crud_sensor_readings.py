import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)

cursor = conn.cursor()

# -------- CREATE (INSERT) --------
def insert_data(temp, hum):
    sql = """
    INSERT INTO sensor_readings (temperature, humidity, timestamp)
    VALUES (%s, %s, NOW())
    """
    cursor.execute(sql, (temp, hum))
    conn.commit()
    print("Record inserted")

# -------- READ (SELECT) --------
def read_data():
    cursor.execute("SELECT * FROM sensor_readings")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# -------- UPDATE --------
def update_data(id, temp):
    sql = "UPDATE sensor_readings SET temperature=%s WHERE id=%s"
    cursor.execute(sql, (temp, id))
    conn.commit()
    print("Record updated")

# -------- DELETE --------
def delete_data(id):
    sql = "DELETE FROM sensor_readings WHERE id=%s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Record deleted")

# -------- THRESHOLD QUERY --------
def below_threshold(value):
    sql = "SELECT * FROM sensor_readings WHERE temperature < %s"
    cursor.execute(sql, (value,))
    rows = cursor.fetchall()
    print("Below threshold records:")
    for row in rows:
        print(row)

# -------- TEST CALLS --------
insert_data(26.5, 60)
insert_data(23.0, 55)

read_data()
below_threshold(25)

cursor.close()
conn.close()

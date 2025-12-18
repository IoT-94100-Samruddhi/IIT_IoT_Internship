import mysql.connector

# -------- Database Connection --------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",        # change if needed
    database="smart_agriculture"
)

cursor = conn.cursor()

# -------- CREATE (INSERT) --------
def insert_data(sensor_id, moisture):
    sql = """
    INSERT INTO soil_moisture (sensor_id, moisture_level, date_time)
    VALUES (%s, %s, NOW())
    """
    cursor.execute(sql, (sensor_id, moisture))
    conn.commit()
    print("Record inserted")

# -------- READ (SELECT ALL) --------
def read_data():
    cursor.execute("SELECT * FROM soil_moisture")
    rows = cursor.fetchall()
    print("All Records:")
    for row in rows:
        print(row)

# -------- UPDATE --------
def update_data(sensor_id, moisture):
    sql = "UPDATE soil_moisture SET moisture_level=%s WHERE sensor_id=%s"
    cursor.execute(sql, (moisture, sensor_id))
    conn.commit()
    print("Record updated")

# -------- DELETE --------
def delete_data(sensor_id):
    sql = "DELETE FROM soil_moisture WHERE sensor_id=%s"
    cursor.execute(sql, (sensor_id,))
    conn.commit()
    print("Record deleted")

# -------- THRESHOLD QUERY --------
def below_threshold(value):
    sql = "SELECT * FROM soil_moisture WHERE moisture_level < %s"
    cursor.execute(sql, (value,))
    rows = cursor.fetchall()
    print("Below threshold records:")
    for row in rows:
        print(row)

# -------- TEST CALLS --------
insert_data(101, 45.5)
insert_data(102, 30.2)

read_data()
below_threshold(40)

cursor.close()
conn.close()

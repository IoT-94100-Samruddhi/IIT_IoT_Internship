import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # replace this
    database="iot_data"
)

if conn.is_connected():
    print("Connected to iot_data database successfully")

conn.close()

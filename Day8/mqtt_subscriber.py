import paho.mqtt.client as mqtt
import mysql.connector

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_mqtt"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    topic = msg.topic
    value = float(msg.payload.decode())

    if "ldr" in topic:
        sensor = "LDR"
    else:
        sensor = "LM35"

    sql = "INSERT INTO sensor_data (sensor_type, value) VALUES (%s, %s)"
    cursor.execute(sql, (sensor, value))
    db.commit()

    print(f"Stored → {sensor}: {value}")

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("sensor/#")
client.on_message = on_message

print("MQTT Subscriber started...")
client.loop_forever()

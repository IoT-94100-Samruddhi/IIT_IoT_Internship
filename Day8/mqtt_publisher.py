import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port)

while True:
    ldr_value = random.randint(200, 900)
    temp_value = random.randint(25, 35)

    client.publish("sensor/ldr", ldr_value)
    client.publish("sensor/lm35", temp_value)

    print("Published -> LDR:", ldr_value, "TEMP:", temp_value)

    time.sleep(2)

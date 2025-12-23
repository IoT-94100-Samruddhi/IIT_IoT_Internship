import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.payload.decode())

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)
client.subscribe("farm/alert")
client.on_message = on_message
client.loop_forever()

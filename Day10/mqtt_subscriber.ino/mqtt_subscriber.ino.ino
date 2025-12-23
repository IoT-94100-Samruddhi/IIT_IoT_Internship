#include <WiFi.h>
#include <WiFiClient.h>
#include <ArduinoMqttClient.h>

const char* ssid = "SUNBEAM";
const char* password = "1234567890";

const char* broker = "broker.hivemq.com";
const int port = 1883;
const char* topic = "vanshri/room/light";

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

void setup() {
  Serial.begin(115200);
  delay(1000);

  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());

  Serial.print("Connecting to MQTT Broker...");
  if (!mqttClient.connect(broker, port)) {
    Serial.println("Failed!");
    while (1);
  }

  Serial.println("Connected to Broker");

  mqttClient.subscribe(topic);
  Serial.println("Subscribed to topic: room/light");
}

void loop() {
  mqttClient.poll();

  int messageSize = mqttClient.parseMessage();
  if (messageSize) {
    String message = "";

    while (mqttClient.available()) {
      message += (char)mqttClient.read();
    }

    Serial.print("Message received: ");
    Serial.println(message);

    if (message == "ON") {
      digitalWrite(2, HIGH);
      Serial.println("LED ON");
    } 
    else if (message == "OFF") {
      digitalWrite(2, LOW);
      Serial.println("LED OFF");
    }
  }
}
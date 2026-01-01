#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

/* WiFi Credentials */
const char *ssid = "vivo Y29 5G";
const char *password = "vanee2823";

/* ThingsBoard */
const char *thingsboardServer = "http://demo.thingsboard.io";
const char *accessToken = "an81Cgu3zF2dCscKTGEM";

/* DHT Configuration */
#define DHTPIN 4        // GPIO pin connected to DHT11 DATA
#define DHTTYPE DHT11   // DHT11 sensor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  delay(1000);

  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("\nWiFi Connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {

  if (WiFi.status() == WL_CONNECTED) {

    float temperature = dht.readTemperature(); // Celsius

    if (isnan(temperature)) {
      Serial.println("Failed to read from DHT sensor!");
      delay(2000);
      return;
    }

    String payload = "{\"temperature\":" + String(temperature) + "}";

    HTTPClient http;
    String url = String(thingsboardServer) +
                 "/api/v1/" + accessToken + "/telemetry";

    http.begin(url);
    http.addHeader("Content-Type", "application/json");

    int httpResponseCode = http.POST(payload);

    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" °C");

    Serial.print("HTTP Response Code: ");
    Serial.println(httpResponseCode);

    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  delay(3000); // DHT11 needs delay
}

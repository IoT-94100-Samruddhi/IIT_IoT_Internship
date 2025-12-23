// ESP32 MQ2 Gas Sensor Example

#define MQ2_PIN 35   // ADC pin (GPIO 35)

void setup() {
  Serial.begin(9600);
  delay(1000);
  Serial.println("MQ2 Gas Sensor Reading Started");
}

void loop() {
  int gasValue = analogRead(MQ2_PIN);  // Read ADC value

  Serial.print("Gas Sensor Value: ");
  Serial.println(gasValue);

  delay(1000);
}

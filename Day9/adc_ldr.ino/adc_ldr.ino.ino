// ESP32 ADC - LDR Example

#define LDR_PIN 34   // ADC pin (GPIO 34)

void setup() {
  Serial.begin(9600);      // Start UART
  delay(1000);
  Serial.println("ESP32 ADC (LDR) Reading Started");
}

void loop() {
  int ldrValue = analogRead(LDR_PIN);   // Read ADC value

  Serial.print("LDR Value: ");
  Serial.println(ldrValue);             // Print ADC value

  delay(1000);   // Read every 1 second
}


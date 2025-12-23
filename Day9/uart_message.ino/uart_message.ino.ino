// ESP32 UART / Serial Communication Example

void setup() {
  Serial.begin(9600);   // Start UART at 9600 baud rate
  delay(1000);          // Small delay for stability
  Serial.println("ESP32 UART Communication Started");
}

void loop() {
  Serial.println("Hello from ESP32");
  delay(2000);          // Send message every 2 seconds
}

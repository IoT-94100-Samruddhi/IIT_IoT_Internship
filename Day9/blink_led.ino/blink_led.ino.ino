// ESP32 Blink Built-in LED

#define LED_PIN 2   // ESP32 built-in LED is usually GPIO 2

void setup() {
  pinMode(LED_PIN, OUTPUT);   // Set LED pin as output
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // LED ON
  delay(1000);                  // wait 1 second

  digitalWrite(LED_PIN, LOW);   // LED OFF
  delay(1000);                  // wait 1 second
}
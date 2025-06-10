void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String msg = Serial.readString();
    if (msg.indexOf("AUTHORIZED") >= 0) {
      digitalWrite(LED_BUILTIN, HIGH);  // Unlock
      delay(5000);
      digitalWrite(LED_BUILTIN, LOW);   // Lock back
    }
  }
}
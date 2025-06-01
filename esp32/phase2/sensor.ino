void setupSensor() {
  Wire.begin();
  while (!sht3x.begin()) {
    Serial.println("SHT3x not found!");
    delay(1000);
  }
}

float convertToF(float temperatureInC) {
  return (temperatureInC * 9.0 / 5.0) + 32;
}

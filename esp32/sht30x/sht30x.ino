#include <Wire.h>
#include "ArtronShop_SHT3x.h"

// This is a basic script for reading sensor output and printing to serial monitor

// 0x44 = The sensor's I²C address (factory default for SHT31).
// &Wire = Tells it to use the main I²C bus
ArtronShop_SHT3x sht3x(0x44, &Wire); 

void setup() {
  Serial.begin(115200);
  Serial.println("SHT3x sensor test");

  Wire.begin();
  while (!sht3x.begin()) {
    Serial.println("SHT3x not found !");
    delay(1000);
  }
}

void loop() {
  if (sht3x.measure()){
  float temperatureInC = sht3x.temperature();
  float humidity = sht3x.humidity();

  float temperature = convertToF(temperatureInC);

  Serial.print("Temperature: ");
  Serial.print(temperature, 1);

  Serial.print(" *F\tHumidity: ");
  Serial.print(humidity, 1);
  Serial.print("% RH");
  Serial.println();

  } else{
    Serial.println("SHT3x Read ERROR :/");
  }

  delay(2000);
}

float convertToF(float temperatureInC){
  return (temperatureInC * (9.0/5.0)) + 32;
}

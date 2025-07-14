#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include "ArtronShop_SHT3x.h"

#include "secrets.h"

// Sensor instance
ArtronShop_SHT3x sht3x(0x44, &Wire); 

// 'done' pin for TPL5110
int donePin = 13;

void setup() {
  Serial.begin(115200);
  setupSensor();
  bool connected = connectToWiFi();

  if (!connected){
    return;
  }

  Serial.println("waiting 1.25 seconds for the sensor to startup.");
  delay(1250);

  if (sht3x.measure()) {
    float tempC = sht3x.temperature();
    float hum = sht3x.humidity();
    float tempF = convertToF(tempC);

    Serial.printf("Temperature: %.1f°F, Humidity: %.1f%%\n", tempF, hum);

    sendSensorData(tempF, hum); // defined in post.ino
  } else {
    Serial.println("Sensor read failed.");
  }

  // set gpio pin 13 to active so TPL5110 receives 'done'
  pinMode(donePin, OUTPUT);
  digitalWrite(donePin, HIGH);

  // Sleep for 30 minutes = (30 * 60 * 1_000_000 microseconds)
  // Serial.println("Going to deep sleep for 1 hour...");
  // esp_sleep_enable_timer_wakeup(60 * 60 * 1000000ULL); 
  // esp_deep_sleep_start();  // Does not return
}

void loop() {

}

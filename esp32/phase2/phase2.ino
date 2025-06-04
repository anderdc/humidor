#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include "ArtronShop_SHT3x.h"

#include "secrets.h"

// Sensor instance
ArtronShop_SHT3x sht3x(0x44, &Wire); 

void setup() {
  Serial.begin(115200);
  connectToWiFi();
  setupSensor();

  Serial.println("waiting 3 seconds for the sensor to startup.");
  delay(3000);

  if (sht3x.measure()) {
    float tempC = sht3x.temperature();
    float hum = sht3x.humidity();
    float tempF = convertToF(tempC);

    Serial.printf("Temperature: %.1f°F, Humidity: %.1f%%\n", tempF, hum);

    sendSensorData(tempF, hum); // defined in post.ino
  } else {
    Serial.println("Sensor read failed.");
  }


  // Sleep for 30 minutes (30 * 60 * 1_000_000 microseconds)
  Serial.println("Going to deep sleep for 1 hour...");
  esp_sleep_enable_timer_wakeup(60 * 60 * 1000000ULL); // 30 min
  esp_deep_sleep_start();  // Does not return
}

void loop() {

}

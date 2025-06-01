void sendSensorData(float temperature, float humidity) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(endpoint); // your flask server's IP/port
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"temperature\": " + String(temperature, 1)
                       +
                     ", \"humidity\": " + String(humidity, 1) + "}";

    int httpResponseCode = http.POST(payload);
    
    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Response: " + response);
    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("WiFi not connected, cannot send POST");
  }
}

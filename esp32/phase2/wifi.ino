bool connectToWiFi() {
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  int max_retries = 20;
  int count = 0;

  while (WiFi.status() != WL_CONNECTED) {
    if (count >= max_retries){
      Serial.println("ERROR: could not connect to wifi. Exiting.");
      return false;
    }

    delay(1000);
    Serial.print(".");
    count++;
  }

  Serial.println("\nConnected to WiFi.");
  Serial.println(WiFi.localIP());
  return true;
}

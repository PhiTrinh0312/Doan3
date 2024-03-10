#include <ESP8266WiFi.h>
#include <DHT.h>
#define BLYNK_TEMPLATE_ID "TMPL6pVGNwziE"
#define BLYNK_TEMPLATE_NAME "Dht11"
#define BLYNK_AUTH_TOKEN "nZDcawzoshBi7OHGnqStPRxazRBnO_ZD"



const char* host = "script.google.com";
const int httpsPort = 443;

String GAS_ID = "AKfycbxIQi8enTrb1GK7gy6u438mKcv9wI86NkLaGLubUbny-fNNDDJ6xLzrbqEzuDpDvf-S";

const char* ssid = "NganLoc";
const char* password = "20022012";

#define DHTPIN D3  // Chân kết nối cảm biến DHT11 với ESP8266
#define DHTTYPE DHT11  // Loại cảm biến DHT11

DHT dht(DHTPIN, DHTTYPE);

WiFiClientSecure client;

void setup() {
  Serial.begin(9600);
  delay(500);

  WiFi.begin(ssid, password);
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(2000);
  }

  Serial.println("");
  Serial.print("Successfully connected to : ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  client.setInsecure();

  dht.begin();
}

void loop() {
  delay(2000);  // Đợi 2 giây để cảm biến ổn định
  
  float temperature = dht.readTemperature(); // Đọc nhiệt độ từ cảm biến
  float humidity = dht.readHumidity(); // Đọc độ ẩm từ cảm biến

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  sendata(temperature, humidity);
  delay(4000);
}

void sendata(float temp, float hum) {
  Serial.print("Connecting to ");
  Serial.println(host);

  if (!client.connect(host, httpsPort)) {
    Serial.println("Connection failed");
    return;
  }

  String url = "/macros/s/" + GAS_ID + "/exec?nhietdo=" + String(temp) + "&doam=" + String(hum);
  Serial.println(url);

  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" +
               "User-Agent: ESP8266\r\n" +
               "Connection: close\r\n\r\n");
  Serial.println("OK");
}
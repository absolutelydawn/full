#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Wire.h>

const char* ssid = "SWcamp01_2.4G"; // WiFi SSID
const char* password = "kibwa1945*"; // WiFi 비밀번호
const char* serverName = "http://54.180.129.179:8000"; // FastAPI 서버 주소(EC2의 퍼블릭 IP 주소)

const int sensorPin = A0;  // 조도센서 핀 설정
const int ledPin = 12;     // LED 핀 설정 (GPIO 12, D6)

int sensorValue = 0;       // 센서 값 저장 변수

const int MPU_addr = 0x68; // I2C 주소 MPU-6050 자이로 센서
int16_t AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ; // 자이로 센서 값 변수

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  pinMode(ledPin, OUTPUT); // LED 핀을 출력으로 설정

  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B); // PWR_MGMT_1 레지스터
  Wire.write(0); // 센서를 켬
  Wire.endTransmission(true);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    // 조도센서 값 읽기
    sensorValue = analogRead(sensorPin);
    Serial.print("Sensor Value: ");  // 조도센서 값 출력
    Serial.println(sensorValue);

    // 자이로 센서 값 읽기
    Wire.beginTransmission(MPU_addr);
    Wire.write(0x3B); // 시작 레지스터 0x3B(ACCEL_XOUT_H)
    Wire.endTransmission(false);
    Wire.requestFrom(MPU_addr, 14, true); // 총 14개의 레지스터 요청
    AcX = Wire.read() << 8 | Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
    AcY = Wire.read() << 8 | Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
    AcZ = Wire.read() << 8 | Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
    Tmp = Wire.read() << 8 | Wire.read(); // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
    GyX = Wire.read() << 8 | Wire.read(); // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
    GyY = Wire.read() << 8 | Wire.read(); // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
    GyZ = Wire.read() << 8 | Wire.read(); // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

    Serial.println(F("MPU-6050 Data"));
    Serial.print(F("accel x,y,z: "));
    Serial.print("AcX = "); Serial.print(AcX); // 가속도 X축 값
    Serial.print(" | AcY = "); Serial.print(AcY); // 가속도 Y축 값
    Serial.print(" | AcZ = "); Serial.print(AcZ); // 가속도 Z축 값
    Serial.print(F("  temperature: "));
    Serial.print(" | Tmp = "); Serial.print(Tmp / 340.00 + 36.53); // 온도 값
    Serial.print(F("  gyro x,y,z: "));
    Serial.print("GyX = "); Serial.print(GyX); // 자이로 X축 값
    Serial.print(" | GyY = "); Serial.print(GyY); // 자이로 Y축 값
    Serial.print(" | GyZ = "); Serial.print(GyZ); // 자이로 Z축 값
    Serial.println();

    WiFiClient client;
    HTTPClient http;

    // 조도 센서 값 전송
    http.begin(client, String(serverName) + "/update");
    http.addHeader("Content-Type", "application/json");

    String jsonPayload = "{\"value\":" + String(sensorValue) + "}";
    int httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.print("POST Response Code: ");
      Serial.println(httpResponseCode);
      Serial.println("Response: " + response);
    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }

    http.end();

    // 자이로 센서 값 전송
    http.begin(client, String(serverName) + "/gyro");
    http.addHeader("Content-Type", "application/json");

    jsonPayload = "{\"AcX\":" + String(AcX) + ", \"AcY\":" + String(AcY) + ", \"AcZ\":" + String(AcZ) +
                  ", \"Tmp\":" + String(Tmp / 340.00 + 36.53) + ", \"GyX\":" + String(GyX) +
                  ", \"GyY\":" + String(GyY) + ", \"GyZ\":" + String(GyZ) + "}";
    httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.print("POST Response Code: ");
      Serial.println(httpResponseCode);
      Serial.println("Response: " + response);
    } else {
      Serial.print("Error on sending POST: ");
      Serial.println(httpResponseCode);
    }

    http.end();

    // LED 상태 확인 및 제어
    http.begin(client, String(serverName) + "/status");
    httpResponseCode = http.GET();

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.print("GET Response Code: ");
      Serial.println(httpResponseCode);
      Serial.println("Response: " + response);

      if (response.indexOf("\"led_status\":\"on\"") > -1) {
        digitalWrite(ledPin, HIGH); // LED 켜기
        Serial.println("LED ON");
      } else {
        digitalWrite(ledPin, LOW); // LED 끄기
        Serial.println("LED OFF");
      }
    } else {
      Serial.print("Error on getting GET: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }

  delay(10000); // 10초 대기
}

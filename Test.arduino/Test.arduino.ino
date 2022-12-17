#include <FastLED.h>
#include <M5Atom.h>
#define RX_PIN 32
#define TX_PIN 26

int i = 0, s = 0;

void setup() {
    M5.begin();
    Serial.println("RS485 Unit test");
    Serial.begin(115200);
    Serial2.begin(
        115200, SERIAL_8N1, RX_PIN,
        TX_PIN);  

    delay(10);
    Serial2.read();
}

void loop() {
    Serial2.write("Hello\n");
    delay(100);
}

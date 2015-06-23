#include <SoftwareSerial.h>

const int rxpin = 2;
const int txpin = 3;
char k = 'A';
SoftwareSerial bluetooth(rxpin, txpin);

void setup()
{
  pinMode(7, OUTPUT);
  Serial.begin(9600);
  bluetooth.begin(9600);
  Serial.println("Serial ready");
  bluetooth.println("Bluetooth ready");
}

void loop()
{
  if(bluetooth.available()){
    k = bluetooth.read();
    Serial.println(k);
  }
  if( k == 'H' ){
    digitalWrite(7, HIGH);
  }
  else {
    digitalWrite(7, LOW);
  }
   delay(10);
}

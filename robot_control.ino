#include <Servo.h>

Servo armServo;  // Servo for arm movement
int ledPin = 13; // Built-in LED

void setup() {
  Serial.begin(9600);
  armServo.attach(9);  // Servo on pin 9
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == 'W') {  // Wave arm
      armServo.write(90);
      delay(500);
      armServo.write(0);
      delay(500);
    }
    else if (command == 'S') {  // Slow nod
      armServo.write(45);
      delay(1000);
      armServo.write(0);
    }
    else if (command == 'F') {  // Flash LED
      digitalWrite(ledPin, HIGH);
      delay(200);
      digitalWrite(ledPin, LOW);
      delay(200);
    }
  }
}
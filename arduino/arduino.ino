#include <Servo.h> // BIBLIOTECA PARA O FUNCIONAMENTO DO SERVO
 
Servo servo_Motor; //OBJETO DO TIPO SERVO
int redLed = 13;
int greenLed = 12;
int num = 48;
int door = 8;

void setup()
{
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(door, OUTPUT);
  Serial.begin(9600);
  servo_Motor.attach(11);
}

void loop()
{
  Write(num);
  if (Serial.available()) {
    num = Serial.read();
    Serial.println(num);
  }
  delay(10);
}

void Write(int num)
{
  if(num == 49)
  {
    digitalWrite(redLed, LOW);
    digitalWrite(greenLed, HIGH);
    digitalWrite(door, HIGH);
    servo_Motor.write(90);
  }
  if(num == 48)
  {
    digitalWrite(redLed, HIGH);
    digitalWrite(greenLed, LOW);
    digitalWrite(door, LOW);
    servo_Motor.write(0);
  }
}

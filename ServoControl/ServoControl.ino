#include <Servo.h>  
 
Servo s1; 
Servo s2;
 
int inputU = 2;
int inputD = 3;
int inputL = 4; 
int inputR = 5;  
int angleV;
int angleH;  
 
void setup() {
  s1.attach(9);
  s2.attach(10);
  pinMode(inputU,INPUT);
  pinMode(inputD,INPUT);  
  Serial.begin(9600);
  angleV = 0;
  angleH = 0;
}
 
void loop() {
  
  int up = digitalRead(inputU);
  Serial.print(up);
  if(up == 1)
  {
    angleV = 90;           
  }
  int down = digitalRead(inputD);
  Serial.print(down);
  if(down == 1)
  {
    angleV = 0;           
  }

  //angle2 = analogRead(input2);           
  //angle2 = map(angle2, 0, 1023, 0, 180);    
  
  
  s1.write(angleV);
  //s2.write(angleH);                    
  delay(5);                           
}

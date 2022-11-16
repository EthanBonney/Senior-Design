#include <Servo.h>  
 
Servo s1; 
Servo s2;
 
int angleV;
int angleH; 
#define inputH A0
#define inputV A2 
 
void setup() {
  s1.attach(9);
  s2.attach(10);
}
 
void loop() {
  
  angleV = analogRead(inputV);           
  angleV = map(angleV, 0, 1023, 0, 180); 
 
  angleH = analogRead(inputH);           
  angleH = map(angleH, 0, 1023, 0, 180);    
  
  
  s1.write(angleV);
  s2.write(angleH);                    
  delay(5);                           
}

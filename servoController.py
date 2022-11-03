import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(14, GPIO.IN)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:

    if GPIO.input(14):
        p.ChangeDutyCycle(5)
    else:
        p.ChangeDutyCycle(10)
    time.sleep(0.5)
   
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
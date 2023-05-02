import RPi.GPIO as GPIO
import time
from pyPS4Controller.controller import Controller


servoPINV = 17
servoPINH = 4
motorPinF = 27
motorPinR = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPINH, GPIO.OUT)
GPIO.setup(servoPINV, GPIO.OUT)
GPIO.setup(motorPinF, GPIO.OUT)
GPIO.setup(motorPinR, GPIO.OUT)


pV = GPIO.PWM(servoPINV, 50) # GPIO 17 for PWM with 50Hz
pV.start(2.5) # Initialization


pH = GPIO.PWM(servoPINH, 50) # GPIO 17 for PWM with 50Hz
pH.start(2.5) # Initialization

pF = GPIO.PWM(motorPinF, 100)
pF.start(100)

pR = GPIO.PWM(motorPinR, 100)
pR.start(100)

angleV = 0
angleH = 0

class MyController(Controller):
    

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        pF.ChangeDutyCycle(0)
    def on_x_release(self):
        pF.ChangeDutyCycle(100)
    def on_circle_press(self):
        pR.ChangeDutyCycle(0)
    def on_circle_release(self):
        pR.ChangeDutyCycle(100)
        
    def on_up_arrow_press(self):
        global angleV
        if angleV < 10:
            angleV = angleV + 1
            pV.ChangeDutyCycle(angleV)
    def on_down_arrow_press(self):
        global angleV
        if angleV > 0:
            angleV = angleV - 1
            pV.ChangeDutyCycle(angleV)
    def on_left_arrow_press(self):
        global angleH
        if angleH < 10:
            angleH = angleH + 1
            pH.ChangeDutyCycle(angleH)
    def on_right_arrow_press(self):
        global angleH
        if angleH > 0:
            angleH = angleH - 1
            pH.ChangeDutyCycle(angleH)
    

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
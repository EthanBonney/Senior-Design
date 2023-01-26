import RPi.GPIO as GPIO
import time
from pyPS4Controller.controller import Controller


servoPINV = 17
servoPINH = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPINH, GPIO.OUT)
GPIO.setup(servoPINV, GPIO.OUT)


pV = GPIO.PWM(servoPINV, 50) # GPIO 17 for PWM with 50Hz
pV.start(2.5) # Initialization


pH = GPIO.PWM(servoPINH, 50) # GPIO 17 for PWM with 50Hz
pH.start(2.5) # Initialization

angleV = 0
angleH = 0
vFlag = 0

class MyController(Controller):
    

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("stop")
    def on_x_release(self):
        vFlag = 0
        print("stop")
    def on_circle_press(self):
        vFlag = 2
    def on_circle_release(self):
        vFlag = 0
        
    def on_up_arrow_press(self):
        global angleV
        if angleV < 10:
            angleV = angleV + 5
            pV.ChangeDutyCycle(angleV)
    def on_up_arrow_release(self):
        print("stop")
    def on_down_arrow_press(self):
        global angleV
        if angleV > 0:
            angleV = angleV - 5
            pV.ChangeDutyCycle(angleV)
    def on_down_arrow_release(self):
        print("stop")

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)


    



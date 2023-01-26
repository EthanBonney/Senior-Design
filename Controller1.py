import RPi.GPIO as GPIO
import time
from pyPS4Controller.controller import Controller
import pigpio

servoPINV = 17
servoPINH = 4
motorPinF = 27
motorPinR = 22
GPIO.setmode(GPIO.BCM)

GPIO.setup(motorPinF, GPIO.OUT)
GPIO.setup(motorPinR, GPIO.OUT)


pV = pigpio.pi()
pV.set_mode(servoPINV, pigpio.OUTPUT)
pV.set_PWM_frequency( servoPINV, 50 )


pH = pigpio.pi()
pH.set_mode(servoPINH, pigpio.OUTPUT)
pH.set_PWM_frequency( servoPINH, 50 )

pF = GPIO.PWM(motorPinR, 100)
pF.start(0)
pR = GPIO.PWM(motorPinR, 100)
pR.start(0)

angleV = 0
angleH = 0

class MyController(Controller):
    

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        pR.ChangeDutyCycle(100)
    def on_x_release(self):
        pR.ChangeDutyCycle(0)
    def on_circle_press(self):
        pR.ChangeDutyCycle(100)
    def on_circle_release(self):
        pR.ChangeDutyCycle(0)
        
    def on_up_arrow_press(self):
        global angleV
        if angleV < 2500:
            angleV = angleV + 500
            pV.set_servo_pulsewidth( servoPINV,angleV)
    def on_down_arrow_press(self):
        global angleV
        if angleV > 0:
            angleV = angleV - 500
            pV.set_servo_pulsewidth( servoPINV,angleV)
    def on_left_arrow_press(self):
        global angleH
        if angleH < 2500:
            angleH = angleH + 500
            pH.set_servo_pulsewidth( servoPINH,angleH)
    def on_right_arrow_press(self):
        global angleH
        if angleH > 0:
            angleH = angleH - 500
            pH.set_servo_pulsewidth( servoPINH,angleH)
    

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)


    



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

pM = GPIO.PWM(motorPinF, 100)
pM.start(0)

angleV = 0
angleH = 0

class MyController(Controller):
    

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        pM.ChangeDutyCycle(100)
    def on_x_release(self):
        pM.ChangeDutyCycle(0)
    def on_circle_press(self):
        vFlag = 2
    def on_circle_release(self):
        vFlag = 0
        
    def on_up_arrow_press(self):
        global angleV
        if angleV < 2500:
            angleV = angleV + 50
            pV.set_servo_pulsewidth(angleV)
    def on_down_arrow_press(self):
        global angleV
        if angleV > 0:
            angleV = angleV - 50
            pV.set_servo_pulsewidth(angleV)
    def on_left_arrow_press(self):
        global angleH
        if angleH < 2500:
            angleH = angleH + 50
            pH.set_servo_pulsewidth(angleH)
    def on_right_arrow_press(self):
        global angleH
        if angleH > 0:
            angleH = angleH - 50
            pH.set_servo_pulsewidth(angleH)
    

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)


    



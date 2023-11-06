import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18, False)

while True:
    input1 = input()
    if(input1=="e"):
        GPIO.output(18,True)
    elif(input1 == "a"):
        GPIO.output(18, False)
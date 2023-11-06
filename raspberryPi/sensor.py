import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

while true:
    print(GPIO.input(18))
    time.sleep(0.5)
import RPi.GPIO as GPIO
import time
import keyboard

isActiceGreen = True
isActiceRed = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18, isActiceGreen)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17, isActiceRed)


keyboard.on_press(lambda event: changeLED())

keyboard.wait('esc')  # Beenden Sie das Programm, wenn die Escape-Taste gedrückt wird


while True:
    GPIO.output(18, isActiveGreen)
    GPIO.output(17, isActiveRed)

def changeLED():
    if (isActiceGreen == True):
        isActiceGreen = False
    elif(isActiceGreen == False):
        isActiceGreen = True

    if (isActiceRed == True):
        isActiceRed = False
    elif(isActiceRed == False):
        isActiceRed = True
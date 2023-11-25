import RPi.GPIO as GPIO
import time

# GPIO-Pin konfigurieren (zum Beispiel Pin 17)
gpio_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.OUT)

# PWM für den GPIO-Pin initialisieren
pwm = GPIO.PWM(gpio_pin, 50)  # 50 Hz Frequenz

# Servo auf Position 0 Grad setzen
pwm.start(7.5)  # 2.5% Duty Cycle entspricht 0 Grad
xPos = 200
duty = 7.5
pixel = 320

def changeAngle(angle):
    pixelNew = 320/7.5*angle
    return pixelNew

try:

    while True:
        if(xPos>320 and xPos>=pixel):
            duty+=0.1
            pixel = changeAngle(duty)
            print("duty ",duty)
            print("pixel ",pixel)
        elif(xPos<320 and xPos <= pixel):
            duty -= 0.1
            pixel = changeAngle(duty)
            print("duty " ,duty)
            print("pixel " ,pixel)

        pwm.ChangeDutyCycle(duty)
        time.sleep(0.1)


except KeyboardInterrupt:
    # Aufräumen
    pwm.stop()
    GPIO.cleanup()



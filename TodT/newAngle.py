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

def changeAngle(xPos):
    newDuty = 9.5/640 *xPos +2.5
    return newDuty




try:

    while True:
        if(xPos<320):
            if(xPos+30<320):
                duty = changeAngle(xPos)
                print("duty ",duty)
                pwm.ChangeDutyCycle(duty)
                time.sleep(0.1)
                pwm.ChangeDutyCycle(0)
        elif(xPos>320):
            if(xPos - 30 > 320):
                duty = changeAngle(xPos)
                print("duty ", duty)
                pwm.ChangeDutyCycle(duty)
                time.sleep(0.1)
                pwm.ChangeDutyCycle(0)



except KeyboardInterrupt:
    # Aufräumen
    pwm.stop()
    GPIO.cleanup()



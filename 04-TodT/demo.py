import RPi.GPIO as GPIO
import time

# GPIO-Pin konfigurieren (zum Beispiel Pin 17)
gpio_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.OUT)

# GPIO auf "high" setzen
while True:
    GPIO.output(gpio_pin, GPIO.HIGH)
    print("HIGH")
    time.sleep(2)  # Warten Sie eine Sekunde
    # GPIO auf "low" setzen
    GPIO.output(gpio_pin, GPIO.LOW)
    print("LOW")
    time.sleep(2)

# Aufräumen
GPIO.cleanup()
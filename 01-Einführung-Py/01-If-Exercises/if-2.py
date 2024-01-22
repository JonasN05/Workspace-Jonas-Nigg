import random

randomNumber = random.randrange(0,100)
randomNumber2 = random.randrange(0,100)
print(randomNumber)
print(randomNumber2)


if (randomNumber<randomNumber2 and randomNumber<50):
    print("Zahl 1 ist kleiner als Zahl 2 und Min")
if (randomNumber<30 or randomNumber2<30):
    print("Eine der beiden ist kleiner als 30")
if (randomNumber<50 or randomNumber2 != 30):
    print("Erste Zahl klein, zweite kein 50iger")
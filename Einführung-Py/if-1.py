import random

randomNumber = random.randrange(0,100)
print(randomNumber)


if (randomNumber<20):
    print("mini")
elif (randomNumber>20 and randomNumber<50):
    print("Medium")
elif (randomNumber>50):
    print("Large")
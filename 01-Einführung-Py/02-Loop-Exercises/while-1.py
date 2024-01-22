import random

number = 0

while True:
    randomNumber = random.randint(10, 30)
    print(randomNumber)
    if randomNumber==15 or randomNumber==25:
        break
    number += randomNumber

print(number)
import random

totalPlayer = 0
totalComputer = 0
k = 0

for i in range(0,6):
    totalComputer += random.randint(1,7)

while True:
    print("Press W to roll the dice")
    key = input()
    if key == 'W':
        randNum = random.randint(1,7)
        print("Your Number:")
        print(randNum)
        totalPlayer += randNum
        k += 1
    if k >= 5:
        break
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
        totalPlayer += int(randNum)
        k += 1
    if k >= 5:
        break

print("Your Total: ", totalPlayer)
print("Computer Total: ", totalComputer)

if totalComputer > totalPlayer:
    print("You lost")
elif totalComputer < totalPlayer:
    print("You Won")
else:
    print("Draw")
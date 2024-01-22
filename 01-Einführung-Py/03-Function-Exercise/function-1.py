def addNumbers(a,b):
    print(a+b)

addNumbers(4,9)


import random
def randomNumber():
    return random.randint(100,200)

print(randomNumber())


words = ["wort", "name", "haus", "lied", "mappe", "krone"]
def randomWordFromArray():
    randomN = random.randint(0,len(words)-1)
    print(words[randomN])

randomWordFromArray()
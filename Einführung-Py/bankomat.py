import random

konto = 0
while True:
    input1 = input()

    if int(input1) == 1:
        print("Einzahlen")
        inputMoney = input()
        konto += int(inputMoney)
    if int(input1) == 2:
        print("Auszahlen")
        inputMoneyMinus = input()
        konto -= int(inputMoneyMinus)
    if int(input1) == 3:
        print(konto)
    if int(input1) == 4:
        break
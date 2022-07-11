import random

rollNumber = input("$ python 01_dice.py\nWelcome to this dices game!\nEnter the number of dices you want to roll:")

def rollNumber1():
    result = 0
    randomNumber = random.randint(1, 6)
    result += randomNumber
    print(f"RESULT : {result}")

def rollNumber2n8():
    result = 0
    for i in range(1, int(rollNumber) + 1):
        randomNumber = random.randint(1, 6)
        print(f"Dice {i} : {randomNumber}")
        result += randomNumber
    print(f"==========")
    print(f"RESULT : {result}")
    print(f"=" * 10)

def rollNumberNot2n8():
    if int(rollNumber) == 1:
        rollNumber1()
    elif (int(rollNumber) >= 2) and (int(rollNumber) <= 8) :
        rollNumber2n8()

if rollNumber.isnumeric():
    if int(rollNumber) == 1:
        rollNumber1()
    elif (int(rollNumber) >= 2) and (int(rollNumber) <= 8) :
        rollNumber2n8()
    elif (int(rollNumber) <= 0) or (int(rollNumber) >= 9):
        while True:
            print("USAGE: The number must be between 1 and 8")
            rollNumber = input("Enter the number of dices you want to roll")
            if int(rollNumber) == 1:
                rollNumber1()
                break
            elif (int(rollNumber) >= 2) and (int(rollNumber) <= 8):
                rollNumber2n8()
                break
else:
    while True:
        print("USAGE: The number must be between 1 and 8")
        rollNumber = input("Enter the number of dices you want to roll")
        if rollNumber.isnumeric():
            if int(rollNumber) == 1:
                rollNumber1()
                break
            elif (int(rollNumber) >= 2) and (int(rollNumber) <= 8):
                rollNumber2n8()
                break
            elif (int(rollNumber) <= 0) or (int(rollNumber) >= 9):
                while True:
                    print("USAGE: The number must be between 1 and 8")
                    rollNumber = input("Enter the number of dices you want to roll")
                    if int(rollNumber) == 1:
                        rollNumber1()
                        break
                    elif (int(rollNumber) >= 2) and (int(rollNumber) <= 8):
                        rollNumber2n8()
                        break
                    break
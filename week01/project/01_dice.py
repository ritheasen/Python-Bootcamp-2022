import random

rollNumber = int(input("Welcome to this dices game!\nEnter the number of dices you want to roll:"))
randomDice = random.randint(1,6)

if rollNumber == " ":
    print("USAGE: The number must be between 1 and 8")
else:
    for i in range(1,rollNumber):
        print(f"Dice {i} : {randomDice}")

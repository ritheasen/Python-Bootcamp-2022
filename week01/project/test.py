import random

rollNumber = input("Welcome to this dices game!\nEnter the number of dices you want to roll:")
result = 0




if rollNumber == "":
    print("USAGE: The number must be between 1 and 8")

    rollNumberAgain = input("Enter the number of dices you want to roll")
    while True:
        if (int(rollNumberAgain) >= 1) and (int(rollNumberAgain) <= 8) :
            for i in range(1, int(rollNumberAgain) + 1):
                randomNumber = random.randint(1, 6)
                print(f"Dice {i} : {randomNumber}")
                result += randomNumber
            print(f"==========")
            print(f"RESULT : {result}")
            print(f"="*10)

            break
        else:
            print("USAGE: The number must be between 1 and 8")
            rollNumberAgain = input("Enter the number of dices you want to roll")
    else:
        for i in range(1,int(rollNumber)+1):
            print(f"Dice {i} : {random.randint(1,6)}")

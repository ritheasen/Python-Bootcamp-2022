

enterNumber = input("Input a number : ")

if enterNumber.isnumeric():
    if (int(enterNumber) % 2) == 0:
        print("The number you have entered is Even")
    else:
        print("The number you have entered is Odd")
else:
    print("Not a valid number")




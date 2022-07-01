

sum = 0

while True:
    enterNumber = input("Input a number ")
    if enterNumber == 'stop' :
        break
    elif enterNumber.isnumeric():
        sum += int(enterNumber)
    else:
        print("The input must be a valid number")

print(f"Sum is : {sum}")

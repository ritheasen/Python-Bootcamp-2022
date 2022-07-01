nNumber = input("Input a number")
sumEven = 0
sumOdd = 0

if nNumber.isnumeric():
    for i in range (0,int(nNumber)+1):
        if i % 2 == 0:
            sumEven += i
        else:
            sumOdd += i
    print(f"Sum even number : {sumEven}")
    print(f"Sum odd number : {sumOdd}")
else:
    print(f"Ivalid Input")
    print(f"Sum odd number = 0")
    print(f"Sum odd number = 0")



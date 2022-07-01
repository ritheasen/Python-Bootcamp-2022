
nNumber = input("Input a number")
nEven = 0
nOdd = 0
sumEven = 0
sumOdd = 0

if nNumber.isnumeric():
    for i in range (0,int(nNumber)+1):
        if i % 2 == 0:
            sumEven += i
            nEven += 1
        else:
            sumOdd += i
            nOdd += 1
    print(f"Average of even numbers : {sumEven/nEven}")
    print(f"Average of odd numbers : {sumOdd/nOdd}")
else:
    print(f"Ivalid Input")
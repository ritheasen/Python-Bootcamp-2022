inputString = input("Enter a string: ")
String1st = inputString[0:len(inputString)//2]
String2nd = inputString[len(inputString)//2:len(inputString)]
stringReverse = String1st[::-1]

if inputString == '':
    print('The string is empty.')
else:
    print(f"{stringReverse}{String2nd}")


inputString = input("Enter a string: ")
String1st = inputString[:len(inputString)//2]
String2nd = inputString[len(inputString)//2:]

if inputString == '':
    print('The string is empty.')
else:
    print(f"{String1st}{String2nd}")

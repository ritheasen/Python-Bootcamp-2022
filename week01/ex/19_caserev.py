inputString = str(input("Enter a string"))
newString = ""

if inputString == "" :
    print("The string is empty.")
else:
    for i in range (0,len(inputString)):
        if inputString[i].islower():
            newString += inputString[i].upper()
        else:
            newString += inputString[i].lower()

print(newString)


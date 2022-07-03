userEnter = int(input("Press 1 to encode \nPress 2 to decode"))

def encodeTodecode():

    inputString = str(input("Enter the string to encode"))
    newString = ""
    for i in inputString:
        B = ord(i) - 13
        S = ord(i) + 13
        if ord(i) > 77:
            newString += chr(B)
        else:
            newString += chr(S)
    print(f"The decoded text is: {newString}")

def decodeToencode():
    inputString = str(input("Enter the string to decode"))
    newString = ""
    for i in inputString:
        B = ord(i) - 13
        S = ord(i) + 13
        if ord(i) > 77:
            newString += chr(B)
        else:
            newString += chr(S)
    print(f"The decoded text is: {newString}")

def YN():
    userYN = input("Do you want to continue?[Y/N]")
    if  userYN == "Y":
        userEnter = int(input("Press 1 to encode \nPress 2 to decode"))
        if userEnter == 1:
            encodeTodecode()
        elif userEnter == 2:
            decodeToencode()
    elif userYN == "N":
        print("Thank you")

if userEnter == 1:
    encodeTodecode()
    YN()
if userEnter == 2:
    decodeToencode()
    YN()








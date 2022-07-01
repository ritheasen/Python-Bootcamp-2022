
userEnter = int(input("Press 1 to encode \nPress 2 to decode"))
newString = ""
if userEnter == 1:
    inputString = str(input("Enter the string to encode"))
    for i in inputString:
        print(f"{i} : {ord(i)}")
        if ord(i) > 77:
            ord(i)-13
            newString = ""
        else:
            ord(i)+13
            newString = ""

        #print(f"{chr(ord(i)+13)}")
#print(f"{chr(ord(i)+13)}",end="")
print(newString)
#elif userEnter == 2:


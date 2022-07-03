
userEnter = int(input("Press 1 to encode \nPress 2 to decode"))
#userYN = str(input("Do you want to continue?[Y/N]"))
newString = ""

if userEnter == 1:
    while True:
        inputString = str(input("Enter the string to encode"))
        for i in inputString:
            B = ord(i) - 13
            S = ord(i) + 13
            if ord(i) > 77:
                newString += chr(B)
            else:
                newString += chr(S)
        print(f"The decode text is :{newString}\nDo you want to continue?[Y/N]")

#print(userYN)


#     if userEnter == 'Y':
#         print("")
#
# if userEnter == 2:
#     inputString = str(input("Enter the string to decode"))
#     for i in inputString:
#         B = ord(i) - 13
#         S = ord(i) + 13
#         if ord(i) > 77:
#             newString += chr(B)
#         else:
#             newString += chr(S)
#     print(newString)
#         #print(f"{chr(ord(i)+13)}")
# #print(f"{chr(ord(i)+13)}",end="")
# print(newString)
# #elif userEnter == 2:


def binary_addition(decimal1,decimal2):

    binary1 = bin(int(decimal1)).replace("0b","")
    binary2 = bin(int(decimal2)).replace("0b","")

    decimal1 = str(decimal1)
    decimal2 = str(decimal2)
    answerInList =[]
    carry = "0"

    for i in range(len(binary1)-1,-1,-1):
        b1 = binary1[i]
        b2 = binary2[i]
        if b1 == "0" and b2 == "0" and carry == "0":
            answerInList.append("0")
            carry = "0"
        elif b1 == "1" and b2 == "1" and carry == "1":
            answerInList.append("1")
            carry = "1"
        elif (b1 == "1" and b2 == "0" and carry == "0") or (b1 == "0" and b2 == "1" and carry == "0") or (b1 == "0" and b2 == "0" and carry =="1"):
            answerInList.append("1")
            carry = "0"
        else:
            answerInList.append( "0")
            carry = "1"
    if carry == "1":
        answerInList.append("1")

    print(f"binary_addition({decimal1},{decimal2})")
    print("Num1 : ",binary1)
    print("Num2 : ",binary2)

    answerInString = "".join(answerInList[::-1])
    print(f"Sum(Binary) : {answerInString}")
    
    print(f"Sum(Decimal) : {int(answerInString,2)}")
    
binary_addition(60,50)

def binary_subtraction(decimal1,decimal2):

    binary1 = bin(int(decimal1)).replace("0b","")
    binary2 = bin(int(decimal2)).replace("0b","") 

    decimal1 = str(decimal1)
    decimal2 = str(decimal2)
    answerInList =[]
    carry = "0"

    inverseBinary1 = ""
    
    for j in binary1:
        if j == "0":
            inverseBinary1 += "1"
        else:
            inverseBinary1 += "0"

    answerInList1 =[]
    carry1 = "0"

    plus1 = "000001"
    for i in range(len(inverseBinary1)-1,-1,-1):
        ib1 = inverseBinary1[i]
        p1 = plus1[i]
        if ib1 == "0" and p1 == "0" and carry1 == "0":
            answerInList1.append("0")
            carry1 = "0"
        elif ib1 == "1" and p1 == "1" and carry1 == "1":
            answerInList1.append("1")
            carry1 = "1"
        elif (ib1 == "1" and p1 == "0" and carry1 == "0") or (ib1 == "0" and p1 == "1" and carry == "0") or (ib1 == "0" and p1 == "0" and carry1 =="1"):
            answerInList1.append("1")
            carry1 = "0"
        else:
            answerInList1.append( "0")
            carry1 = "1"
    if carry1 == "1":
        answerInList1.append("1")   
    answerInString1 = "".join(answerInList1[::-1]) 

    for x in range(len(binary2)-1,-1,-1):
        b2 = binary2[x]
        aib1 = answerInString1[x]
        if aib1 == "0" and b2 == "0" and carry == "0":
            answerInList.append("0")
            carry = "0"
        elif aib1 == "1" and b2 == "1" and carry == "1":
            answerInList.append("1")
            carry = "1"
        elif (aib1 == "1" and b2 == "0" and carry == "0") or (aib1 == "0" and b2 == "1" and carry == "0") or (aib1 == "0" and b2 == "0" and carry =="1"):
            answerInList.append("1")
            carry = "0"
        else:
            answerInList.append( "0")
            carry = "1"
    if carry == "1":
        answerInList.append("1")
    answerInString = "".join(answerInList[::-1])

    inverseBinaryAfterSum = ""

    for c in answerInString:
        if c == "0":
            inverseBinaryAfterSum += "1"
        else:
            inverseBinaryAfterSum += "0"

    answerInList2 =[]
    carry2 = "0"

    plusAnother1 = "000001"
    for v in range(len(inverseBinaryAfterSum)-1,-1,-1):
        ibas1 = inverseBinaryAfterSum[v]
        pa1 = plusAnother1[v]
        if ibas1 == "0" and pa1 == "0" and carry2 == "0":
            answerInList2.append("0")
            carry2 = "0"
        elif ibas1 == "1" and pa1 == "1" and carry2 == "1":
            answerInList2.append("1")
            carry2 = "1"
        elif (ibas1 == "1" and pa1 == "0" and carry2 == "0") or (ibas1 == "0" and pa1 == "1" and carry2 == "0") or (ibas1 == "0" and pa1 == "0" and carry2 =="1"):
            answerInList2.append("1")
            carry2 = "0"
        else:
            answerInList2.append( "0")
            carry2 = "1"
    if carry2 == "1":
        answerInList2.append("1")   
    answerInString2 = "".join(answerInList2[::-1]) 

    print(f"binary_subtraction({decimal1},{decimal2})")
    print("Num1 : ",binary1)
    print("Num2 : ",binary2)
    print(f"Difference(Binary) : {int(answerInString2)}")
    print(f"Difference(Decimal) : {int(answerInString2,2)}")
    
binary_subtraction(60,50)

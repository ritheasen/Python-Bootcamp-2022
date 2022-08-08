def and_operation(hex1,hex2):
    binary1 = bin(int(hex1,16)).replace("0b","")
    binary2 = bin(int(hex2,16)).replace("0b","")

    result = []

    for i in range (len(binary1)-1,-1,-1):
        scanBinary1 = binary1[i]
        scanBinary2 = binary2[i]
        
        if int(scanBinary1) == 1 & int(scanBinary2) == 1:
            result.append("1")
        else:
            result.append("0")    

    realResult = "".join(result[::-1])

    print(f'and_operation("{hex1}","{hex2}")\n\n{binary1}\n{binary2}\n\n{realResult}')

and_operation("33","3D")
def or_operation(hex1,hex2):
    binary1 = bin(int(hex1,16)).replace("0b","")
    binary2 = bin(int(hex2,16)).replace("0b","")

    result = []

    for i in range (len(binary1)-1,-1,-1):
        scanBinary1 = binary1[i]
        scanBinary2 = binary2[i]

        if int(scanBinary1) == 0 | int(scanBinary2) == 0:
            result.append("0")
        else:
            result.append("1")

    realResult = "".join(result[::-1])

    print(f'or_operation("{hex1}","{hex2}")\n\n{binary1}\n{binary2}\n\n{realResult}')

or_operation("33","3D")
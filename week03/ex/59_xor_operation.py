def xor_operation(hex1,hex2):

    binary1 = bin(int(hex1,16)).replace("0b","")
    binary2 = bin(int(hex2,16)).replace("0b","")
    xorBinary = bin(int(binary1,2) ^ int(binary2,2))

    print(f'xor_operation("{hex1}","{hex2}")\n\n{binary1}\n{binary2}\n\n{xorBinary.replace("0b","")}')

xor_operation("33","3D")
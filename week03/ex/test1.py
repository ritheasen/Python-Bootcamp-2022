def xor_operation(x, y):

    print(f"xor_operation({x, y})")

    hexnum1 = x

    hexnum2 = y

    decnum1 = int(hexnum1, 16)

    decnum2 = int(hexnum2, 16)

    binnum1 = bin(decnum1).replace("0b", "")

    binnum2 = bin(decnum2).replace("0b", "")

    binxor = bin(decnum1 ^ decnum2)

    print(f"{binnum1} \n{binnum2} \n\n{binxor.replace('0b','')}")

xor_operation("33", "3D")
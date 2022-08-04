

def oct_to_hex(octal):
    octal = str(octal)

    checkOctal = int(octal) % 10
    decimal = 0
    base = 1
    

    if checkOctal >= 0 and checkOctal <= 7:
        
        print(f"oct_to_dec({octal})")
        while (octal):
            remainder = int(octal) % 10 # 0 5 7
            #print(remainder)
            octal = int(octal) / 10 # 750 75 7
            #print(octal)
            decimal += remainder * base # 0+(5*8)40+(7*64)448
            #print(decimal)
            base = base * 8 # 8 64 512
            #print(base) 

        print(hex(decimal).replace("0x",""))
    else :
        print(f"oct_to_dec({octal})")
        print("This is not an octal number")
oct_to_hex(1271)



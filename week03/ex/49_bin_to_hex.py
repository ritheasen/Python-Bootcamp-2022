
def bin_to_hex(binary):

    setBinary = set(binary)
    setForBinary = {"0","1"}

    if setForBinary == setBinary or setBinary == {"0"} or setBinary == {"1"}:

        print(f"bin_to_oct({binary})")
        decimal = int(binary,2) #return integer(binary,base = 2)
        return hex(decimal).replace("0x","")   
        
    else:

            print(f"bin_to_oct({binary})")
            print("This is not binary number")

print(bin_to_hex("11001101"))


def bin_to_oct(binary):

    setBinary = set(binary)
    setForBinary = {"0","1"}

    if setForBinary == setBinary or setBinary == {"0"} or setBinary == {"1"}:

        print(f"bin_to_oct({binary})")
        decimal = int(binary,2) #return integer(binary,base = 2)
        return oct(decimal).replace("0o","")   
        
    else:

            print(f"bin_to_oct({binary})")
            print("This is not binary number")

print(bin_to_oct("11001101"))
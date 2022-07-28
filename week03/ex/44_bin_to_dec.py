
import numbers








def bin_to_dec(binary):

    setBinary = set(binary)
    setForBinary = {"0","1"}

    if setForBinary == setBinary or setBinary == {"0"} or setBinary == {"1"}:

        print(f"bin_to_dic({binary})")
        return int(binary,2) #return integer(binary,base = 2)    
        
    else:

            print(f"bin_to_dic({binary})")
            print("This is not binary number")

print(bin_to_dec("110011"))
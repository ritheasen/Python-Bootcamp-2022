







def bin_to_dec(binary):
    binary = str(binary)
    setBinary = set(binary)
    setForBinary = {'0','1'}

    if setForBinary == setBinary or setBinary == {'0'} or setBinary == {'1'}:

        print(f"bin_to_dic({binary})")
        print(int(binary,2)) #return integer(binary,base = 2)    
        
    else:

            print(f"bin_to_dic({binary})")
            print("This is not binary number")

bin_to_dec(110011)
# print(bin_to_dec(110011))
#bin_to_dec(110011)
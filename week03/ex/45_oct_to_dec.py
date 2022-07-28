numOctal = 750


remainder = numOctal % 10 # 0 5 7

def oct_to_dec(octal):
    
    decimal1 = 0
    base1 = 1

    while (octal):

        if remainder >= 0 and remainder <= 7 :
                 
            octal = int(octal / 10) # 750 75 7
            #print(octal)
            decimal1 += remainder * base1 # 0+(5*8)40+(7*64)448
            #print(decimal)
            base1 = base1 * 8 # 8 64 512
            #print(base1) 
            print(decimal1)
            
        else:
            
            print("asd")


oct_to_dec(numOctal)
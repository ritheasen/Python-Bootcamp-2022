


def oct_to_dec(octal):

    num = 750
    decimal = 0
    base = 1



    if (num % 10) >= 0 and (num % 10) <= 7:
        while (num):
            remainder = num % 10 # 0 5 7
            #print(remainder)
            num = int(num / 10) # 750 75 7
            #print(num)
            decimal += remainder * base # 0+(5*8)40+(7*64)448
            #print(decimal)
            base = base * 8 # 8 64 512
            #print(base) 

        print(decimal)
    else :
        print("asd")
oct_to_dec("123")
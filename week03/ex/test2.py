def checkHex(s):
   
    # Iterate over string
    for ch in s:
 
        # Check if the character
        # is invalid
        if ((ch < '0' or ch > '9') and
            (ch < 'A' or ch > 'F')and
            (ch < 'a' or ch > 'f')):

            print("yes")
        else:
            print("no")
                 
    #         print("No")
    #         return
    # print("Yes")

s = "baaaaa1"

checkHex(s)
 
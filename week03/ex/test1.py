def checkHex(s):
   
    # Iterate over string
    for ch in s:
 
        # Check if the character
        # is invalid
        if ((ch < '0' or ch > '9') and
            (ch < 'A' or ch > 'F')and
            (ch < 'a' or ch > 'f')):
                 
            print("No")
            return
         
    # Print true if all
    # characters are valid
    print("Yes")
 
# Driver Code
     
# Given string
s = "ba1"
  
# Function call
checkHex(s)
 
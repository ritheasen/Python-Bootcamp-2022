string = str(input("Enter"))
def fun_split(string):
    #string = str(input("Enter"))
    newList = list(string.split(" "))
    return  newList

#print("fun_split("  ,string ,")")
#print(f"fun_split("{string}")")
print(f'fun_split("{string}")')
print(fun_split(string))
#print(f'fun_split("{string}")')
#print(f"fun_split(" {string} ")")

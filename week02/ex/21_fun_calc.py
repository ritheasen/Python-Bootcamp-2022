num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
operator = input("Enter operator")
operatorText = { '*' : 'Product', '-' : 'Minus', '+' : 'Plus', '/' : 'Divide'}

def fun_calc(num1,num2,operator):

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
#print(fun_calc(int(input("Enter 1st number")),int(input("Enter 2nd number")),input("Enter operator")))
print(f"fun_calc({num1},{num2},'{operator}')"
      f"\n{operatorText[operator]} : {fun_calc(num1,num2,operator)}"
      f"\nProcess : {num1} {operator} {num2} = {fun_calc(num1,num2,operator)} ")

# print(f"\nfun_calc({num1},{num2},'*')"
#       f"\nProduct: {fun_calc(50,2,'*')}"
#       f"\nProcress: {num1} * {num2} = {fun_calc(50,2,'*')}")



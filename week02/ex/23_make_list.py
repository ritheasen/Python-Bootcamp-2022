
num1 = input("Enter 1st number")
text = input("Enter any word")
num2 = input("Enter 2nd number")

def make_list(num1,text,num2):

    newList = [num1,text,num2]
    return newList

#print(make_list(input("Enter 1st number"),input("Enter any word"),input("Enter 2nd number ")))
print(f'make_list({num1},"{text}",{num2})')
print(make_list(int(num1),text,int(num2)))
#print(make_list(21,"hello",45))

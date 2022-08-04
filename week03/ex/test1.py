

list=[]
def fill(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    len1 = len(num1)
    len2 = len(num2)
    if len1 != len2:
        if len1 > len2:
            list.append(num2)
            while len1 != len2:
                list.append('0')
        rejoin = ''.join(list[::-1])
    print(rejoin)

fill('1000001', '1')
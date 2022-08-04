def solve(num):
    num = str(num)
    for i in range (0,len(num)):
        a = num[i]
        print(a)
        if int(a) >= 0 and int(a) <= 7:
            print("asd")
            
        else:
            print("qwe")
#     sum = 0
#     while num:
#         sum += num % 10
#         print(f"asd {sum}")
#         num = num // 10
#         print(f"qwe {num}")
#     if sum % 7 == 0 :
#         print("1")
#     else:
#         print("0")
num = 61
print(solve(num))
def sum_of_list():
    listLength = int(input("Enter length of list"))
    newList = []
    sum = 0

    for i in range(0, listLength):
        insertList = int(input(f"Insert number into list"))
        newList.append(insertList)
        sum += insertList
    print(f"Sum_of_list({newList})")
    print(sum)
    return sum

sum_of_list()

# newList = [20,15,10,30]
# def sum_of_list():
#     sum = 0
#     for i in range(0,len(newList)):
#         sum += newList[i]
#     print(f"Sum_of_list({newList})")
#     print(sum)
#     return sum
# sum_of_list()
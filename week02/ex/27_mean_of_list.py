
# def mean_of_list():
#     listLength = int(input("Enter length of list"))
#     newList = []
#     sum = 0
#     for i in range(0, listLength):
#         insertList = int(input(f"Insert number into list"))
#         newList.append(insertList)
#         sum += insertList
#     print(f"mean_of_list{newList}")
#     mean = float(sum / listLength)
#     print(mean)
#     return mean
# mean_of_list()

def mean_of_list(newList):
    sum = 0
    for i in range(0,len(newList)):
        sum += newList[i]
    mean = sum / len(newList)
    print(f"mean_of_list([50,10,62,32])")
    print(mean)
    return mean

mean_of_list([50,10,62,32])
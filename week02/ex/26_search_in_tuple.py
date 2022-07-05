
def search_in_tuple(newTuple,searchNum):
    if searchNum in newTuple:
        print(f"Element found at Index:{newTuple.index(searchNum)}")
        return newTuple.index(searchNum)
    else:
        print("Element not found in the tuple")

print(f"search_in_tuple([20,15,10,30],10)")
search_in_tuple([20,15,10,30],10)
print(f"search_in_tuple([20,15,10,30],70)")
search_in_tuple([20,15,10,30],70)



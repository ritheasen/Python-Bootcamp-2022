


def make_dictionary(listInteger,tupleString):
    #listInteger = [50,10,62]
    #tupleString = ("Borey","Thirak","Dane")

    newDict = dict(zip(listInteger,tupleString))

    print(f'make_dictionary([50,10,62],("Borey","Thirak","Dane"))')
    print(newDict)
    return newDict
make_dictionary([50,10,62],("Borey","Thirak","Dane"))

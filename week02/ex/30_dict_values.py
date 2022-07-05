

def dict_values(dictionary):
    dictValue = dictionary.values()
    dictKey = dictionary.keys()
    dictItem = dictionary.items()

    for dictKey, dictValue in dictItem:
        print(f'{dictKey}:{dictValue}')
    #print(*[str(dictValue) + ':' + str(dictKey) for dictValue, dictKey in dictionary.items()])
        print(f"*****")

    # print(dictValue)
    # print(dictKey)
    # print(newDict)
    # print(dictItem)

dict_values(({120: ("Visal", "Borey", "Sovann"),
              130: ("Hout","Mouyleng","Pidor"),
              140: ("Nary","Misora", "Masaki") }))




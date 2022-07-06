

def dict_values(dictionary):
    dictItem = dictionary.items()
    for dictKey, dictValue in dictItem:
        print(dictKey, ":",*dictValue)
        print(f"*****")

dict_values(({120: ("Visal", "Borey", "Sovann"),
              130: ("Hout","Mouyleng","Pidor"),
              140: ("Nary","Misora", "Masaki") }))




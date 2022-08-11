from pathlib import Path

# path_to_file = "Hello.txt"
# path = Path(path_to_file)

# if path.is_file():

#     print(f'The file {path_to_file} exists')
# else:
#     print(f'The file {path_to_file} does not exist')



def read_file(string):

    path = Path(string)

    if path.is_file():
        f = open(string, "r")
        readTextInList = f.readlines()
        readTextInString = "".join(readTextInList)        
        print(f"{readTextInString}")
    else:
        print(f"Invalid FILENAME")




read_file("Hello.txt")
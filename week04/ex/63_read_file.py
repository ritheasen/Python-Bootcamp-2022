from pathlib import Path

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
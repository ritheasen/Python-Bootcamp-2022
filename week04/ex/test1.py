import os.path
from pathlib import Path

def read_file(string):
    f = open(string, "r")
    fileExist = Path(string)

    if fileExist.is_file():
        print("asd")
    else:
        print("qwe")


read_file("Hello1.txt")
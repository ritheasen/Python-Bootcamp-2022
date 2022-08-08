import os

def current_path():
    path = os.getcwd()
    pathList = []
    pathList.append(path)
    pathString = "".join(pathList)


    print(pathString)
    #print(f"{path}")

current_path()
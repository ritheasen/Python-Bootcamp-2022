

import os
import inspect
from pathlib import Path
import os.path
import datetime

class Filelib:

    def inspect(self):
        
        #inspect current file
        currentFileInspect = inspect.getfile(inspect.currentframe())
        #inspect current folder
        currenFolderInspect = os.getcwd()

        selfToCheck = inspect.getfile(inspect.currentframe())

        if os.path.isdir(selfToCheck):
            print("This is a folder.")
        elif os.path.isfile(selfToCheck):
            print("This is a file.")

    def current_path(self):

        path = os.getcwd()
        pathList = []
        pathList.append(path)
        pathString = "".join(pathList)
        print(pathString)

    def read(self, filename):

        path = Path(filename)

        if path.is_file():
            f = open(filename, "r")
            readTextInList = f.readlines()
            readTextInString = "".join(readTextInList)        
            print(f"{readTextInString}")
        else:
            print(f"Invalid FILENAME")

    def write(self, filename, content):

            f = open(filename, "w")
            f.write(content)
            print("New file successfully writed.")
    
    def append(self, filename, content):

        currentTime = datetime.datetime.now()
        currentTimeFormat = currentTime.strftime("[%d/%m/%Y %X]")
        
        while True:
            stringInput = input(f"$:")
            if stringInput == "EXIT":
                break
            else:
                f = open(filename, "a")
                f.write(f"\n{currentTimeFormat}{stringInput}")
                f.close()
                continue
    def remove(self, filename):

        if os.path.exists(filename):
            os.remove(filename)
            print("File successfully deleted.")
        else:
            print("The file name does not exist.")   

    def create_folder(self, folder_list ):

        pathCurrentDir = os.getcwd()

        for i in range (len(folder_list)) :

            if os.path.exists(folder_list[i]):

                print("The file already existed")
                return

            else:

                path = os.path.join(pathCurrentDir, folder_list[i])
                os.mkdir(path)
                print("The file successfully created")
                return
            
print(f"\nFilelib().inspect() \n")
Filelib().inspect()

print(f"\nFilelib().current_path() \n")
Filelib().current_path()

print(f'\nFilelib().read(<FILENAME>) \n')
Filelib().read("Hello.txt")

print(f'\nFilelib().write(<FILENAME>,<CONTENT>) \n')
Filelib().write("Hello123.txt","Hello world")

print(f'\nFilelib().append(<FILENAME>,<CONTENT>) \n')
Filelib().append("Hello1234.txt","Welcome")

print(f'\nFilelib().remove(<FILENAME>) \n')
Filelib().remove("HelloDelete.txt")

print(f'\nFilelib().creat_folder(<LIST OF FILENAME>) \n')
Filelib().create_folder(["aa","bb"])



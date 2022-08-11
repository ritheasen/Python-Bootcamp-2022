import os

def current_folder():
    

    listFileFolder = []
    #currentDirectory = os.listdir("C://Users//KIT//Desktop//New folder") #empty
    currentDirectory = os.listdir() #not empty

    for i in range (len(currentDirectory)):
        
        if os.path.isdir(currentDirectory[i]):
            listFileFolder.append((currentDirectory[i],"Folder"))
            
        elif os.path.isfile(currentDirectory[i]):
            listFileFolder.append((currentDirectory[i],"File"))
            
        else:
            return

    print(listFileFolder)

current_folder()
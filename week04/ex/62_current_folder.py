import os

def current_folder():
    

    listFileFolder = []
    
    currentDirectory = os.listdir() 

    for i in range (len(currentDirectory)):
        
        if os.path.isdir(currentDirectory[i]):
            listFileFolder.append((currentDirectory[i],"Folder"))
            
        elif os.path.isfile(currentDirectory[i]):
            listFileFolder.append((currentDirectory[i],"File"))
            
        else:
            return

    print(listFileFolder)

current_folder()
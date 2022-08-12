import os
import shutil

def auto_folder(foldername):

    pathCurrentDir = os.getcwd()

    for i in range (len(folderName)) :

        if os.path.exists(folderName[i]):
            
            while True:

                replaceAsk = input(f"Are you sure tou want to replace {foldername}?[Y/N]")

                if replaceAsk == "Y":

                    shutil.rmtree(folderName[i])
                    path = os.path.join(pathCurrentDir, folderName[i])
                    os.mkdir(path)
                    print("1")
                    break

                elif replaceAsk == "N":

                    print("0")
                    break

                else:

                    print("Invalid Option")
                    continue

        elif foldername == "":

            print("0")

        else:
            path = os.path.join(pathCurrentDir, folderName[i])
            os.mkdir(path)
            print("1")
    
folderName = ["aa","bb"]
auto_folder(folderName)
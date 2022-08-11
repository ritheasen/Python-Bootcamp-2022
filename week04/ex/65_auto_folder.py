import os
import shutil

def auto_folder(foldername):

    if os.path.exists(foldername):

        while True:
            replaceAsk = input(f"Are you sure tou want to replace {foldername}?[Y/N]")

            if replaceAsk == "Y":

                shutil.rmtree(foldername)
                parent_dir = os.getcwd()
                path = os.path.join(parent_dir, foldername)
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
        
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, foldername)
        os.mkdir(path)
        print("1")

auto_folder("a")
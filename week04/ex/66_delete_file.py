

import os.path


def delete_file(filename):



    if os.path.exists(filename):

        while True:
            
            replaceAsk = input(f"Are you sure tou want to delete {filename}?[Y/N]")

            if replaceAsk == "Y":

                os.remove(filename)
                print("1")
                break

            elif replaceAsk == "N":

                print("0")
                break

            else:

                print("Invalid Option")
                continue

    else:
        print("The file name does not exist")

delete_file("Hello1.txt")

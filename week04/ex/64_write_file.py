

import os.path


def write_file(filename, content):

    if os.path.exists(filename):

        while True:
            replaceAsk = input(f"Are you sure you want to replace {filename}?[Y/N]")

            if replaceAsk == "Y":
                f = open(filename, "w")
                f.write(content)
                print("1")
                break

            elif replaceAsk == "N":
                print("0")
                break

            else:
                print("Invalid Option")
                continue

    else:
        f = open(filename, "w")
        f.write(content)
        print("1")


write_file("Hello12.txt","Hello world")

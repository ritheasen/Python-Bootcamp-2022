import datetime
import os.path

def append_life(filename):

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



append_life("Hello2.txt")
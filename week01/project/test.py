paragraphString = str(input("Enter paragraph1"))
searchString = str(input("Enter search word"))
countingWord = paragraphString.count(searchString)
print(f"There are {countingWord} occurrences")
userYN = str(input("Do you want to replace the text[Y/N]"))

if userYN == 'N' and 'n':
    userYNagain = str(input("Oh! you don’t like to replace, Do you want to check again [Y/N]?"))
    while True:
        if userYNagain == 'Y' and 'y':
            paragraphString = str(input("Enter paragraph"))
            searchString = str(input("Enter search word"))
            countingWord = paragraphString.count(searchString)
            print(f"There are {countingWord} occurrences")
            userYN = str(input("Do you want to replace the text[Y/N]"))
            if userYN == 'Y' and 'y' :
                replaceString = str(input("Enter word to replace"))
                print(f"{countingWord} words has been replaced from the paragraph")
                print(paragraphString.replace(searchString, replaceString))
                break
        elif userYNagain == 'N' and 'n':
            break
elif userYN == 'Y' and 'y' :
    replaceString = str(input("Enter word to replace"))
    replacementString = int(input("How many occurrences do you want to replace?"))
    print(f"{replacementString} words has been replaced from the paragraph")
    print(paragraphString.replace(searchString, replaceString,replacementString))
else:
    print('"Please give a proper input"')
    userYN = str(input("Do you want to replace the text[Y/N]"))
    if userYN == 'N':
        userYNagain = str(input("Oh! you don’t like to replace, Do you want to check again [Y/N]?"))
        if userYNagain == 'Y':
            paragraphString = str(input("Enter paragraph"))
            searchString = str(input("Enter search word"))
            countingWord = paragraphString.count(searchString)
            print(f"There are {countingWord} occurrences")
            userYN = str(input("Do you want to replace the text[Y/N]"))
            if userYN == 'Y' and 'y' :
                replaceString = str(input("Enter word to replace"))
                replacementString = int(input("How many occurrences do you want to replace?"))
                print(f"{replacementString} words has been replaced from the paragraph")
                print(paragraphString.replace(searchString, replaceString, replacementString))
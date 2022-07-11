paragraphString = str(input("Please input a paragraph"))
searchString = str(input("Please input a search string"))
countingWord = paragraphString.count(searchString)
print(f"There are {countingWord} occurrences")
userYN = str(input("Do you want to replace the text[Y/N]"))

if userYN == 'N' and 'n':
    userYNAgain = str(input("Oh! you don’t like to replace, Do you want to check again [Y/N]?"))
    while True:
        if userYNAgain == 'Y' and 'y':
            paragraphString = str(input("Please input a paragraph"))
            searchString = str(input("Please input a search string"))
            countingWord = paragraphString.count(searchString)
            print(f"There are {countingWord} occurrences")
            userYN = str(input("Do you want to replace the text[Y/N]"))
            if userYN == 'Y' and 'y' :
                replaceString = str(input("Please input a replacement string"))
                replacementString = int(input("How many occurrences do you want to replace?"))
                print(f"{replacementString} words has been replaced from the paragraph")
                print(paragraphString.replace(searchString, replaceString, replacementString))
                break
            elif userYN == 'N' and 'n':
                break
        elif userYNAgain == 'N' and 'n':
            break
elif userYN == 'Y' and 'y' :
    replaceString = str(input("Please input a replacement string"))
    replacementString = int(input("How many occurrences do you want to replace?"))
    print(f"{replacementString} words has been replaced from the paragraph")
    print(paragraphString.replace(searchString, replaceString,replacementString))
else:
    while True:
        print('"Please give a proper input"')
        userYN = str(input("Do you want to replace the text[Y/N]"))
        if userYN == 'N' and 'n':
            userYNAgain = str(input("Oh! you don’t like to replace, Do you want to check again [Y/N]?"))
            if userYNAgain == 'Y' and 'y':
                paragraphString = str(input("Please input a paragraph"))
                searchString = str(input("Please input a search string"))
                countingWord = paragraphString.count(searchString)
                print(f"There are {countingWord} occurrences")
                userYN = str(input("Do you want to replace the text[Y/N]"))
                if userYN == 'Y' and 'y' :
                    replaceString = str(input("Please input a replacement string"))
                    replacementString = int(input("How many occurrences do you want to replace?"))
                    print(f"{replacementString} words has been replaced from the paragraph")
                    print(paragraphString.replace(searchString, replaceString, replacementString))
                    break
                elif userYN == 'N' and 'n':
                    break
            elif userYNAgain == 'N' and 'n':
                break
        elif userYN == 'Y' and 'y':
            replaceString = str(input("Please input a replacement string"))
            replacementString = int(input("How many occurrences do you want to replace?"))
            print(f"{replacementString} words has been replaced from the paragraph")
            print(paragraphString.replace(searchString, replaceString, replacementString))
            break



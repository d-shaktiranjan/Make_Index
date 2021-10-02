f = open("collect.txt", "w")
indexDict = {}

excludeList = []
with open('exclude-words.txt', 'r') as file:
    for line in file:
        for word in line.split():
            excludeList.append(word)


def listToString(userSet):
    final = ""
    for item in userSet:
        final += str(item) + ","
    return final


def checkNumeric(word):
    try:
        word = int(word)
    except:
        pass
    try:
        word = float(word)
    except:
        pass
    return isinstance(word, int) or isinstance(word, float)


def readWords(fName, pageNumber):
    with open(fName, 'r') as file:
        for line in file:
            for word in line.split():
                if word not in excludeList and not checkNumeric(word):
                    if word not in indexDict.keys():
                        indexDict[word] = {pageNumber}
                    else:
                        indexDict[word].add(pageNumber)


if __name__ == "__main__":
    readWords("Page1.txt", 1)
    readWords("Page2.txt", 2)
    readWords("Page3.txt", 3)
    f.write("Word : Page Numbers\n")
    f.write("-------------------\n")
    for key in indexDict.keys():
        lineValue = f"{key} : {indexDict[key] if isinstance(indexDict[key],int) else listToString(indexDict[key])}"
        f.write(lineValue + "\n")

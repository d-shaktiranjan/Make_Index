f = open("collect.txt", "a")
indexDict = {}


def readWords(fName, pageNumber):
    with open(fName, 'r') as file:
        for line in file:
            for word in line.split():
                if word not in indexDict.keys():
                    indexDict[word] = pageNumber
                else:
                    if indexDict[word] != pageNumber:
                        indexDict[word] = [indexDict[word], pageNumber]


def listToString(userList):
    final = ""
    for i in range(len(userList)):
        if i == 0:
            final += str(userList[i])
        else:
            final += ","+str(userList[i])
    return final


if __name__ == "__main__":
    readWords("demo.txt", 1)
    readWords("demo2.txt", 2)
    for key in indexDict.keys():
        lineValue = f"{key} : {indexDict[key] if isinstance(indexDict[key],int) else listToString(indexDict[key])}"
        print(lineValue)

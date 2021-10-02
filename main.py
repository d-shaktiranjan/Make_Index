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


if __name__ == "__main__":
    readWords("demo.txt", 1)
    readWords("demo2.txt", 2)
    for key in indexDict.keys():
        lineValue = f"{key} : {indexDict[key]}"
        print(lineValue)

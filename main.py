f = open("collect.txt", "a")
indexDict = {}


def readWords(fName, pageNumber):
    with open(fName, 'r') as file:
        for line in file:
            for word in line.split():
                indexDict[word] = pageNumber


if __name__ == "__main__":
    readWords("demo.txt", 1)
    for key in indexDict.keys():
        lineValue = f"{key} : {indexDict[key]}"
        print(lineValue)

def sortByKeys(userDict):
    myDict = {}
    sortedKeys = sorted(userDict.keys())
    for item in sortedKeys:
        myDict[item] = userDict[item]
    return myDict


myDict = {
    "Shakti": 79,
    "Abhi": 85,
    "Pra": 15
}
print(myDict)
myDict = sortByKeys(myDict)
print(myDict)

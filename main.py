f = open("collect.txt", "a")
indexDict = {}
with open('demo.txt', 'r') as file:
    for line in file:
        for word in line.split():
            # print(word)
            indexDict[word] = 1

# f.write(str(indexDict))
for key in indexDict.keys():
    lineValue = f"{key} : {indexDict[key]}"
    print(lineValue)

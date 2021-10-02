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


print(checkNumeric("5.5"))

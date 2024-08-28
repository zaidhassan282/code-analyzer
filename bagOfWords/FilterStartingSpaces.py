import re

def FilterStartingSpaces(charList=[]):
    # return param
    for char in charList:
        if re.match("^[ ]$", char):
            charList.pop(charList.index(char))
        else:
            return charList
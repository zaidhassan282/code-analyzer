from bagOfWords.FilterStartingSpaces import FilterStartingSpaces
import re


def WordsGenerator(charList):
    lineNumber = 1
    filteredList = FilterStartingSpaces(charList)
    BagOfWords = []
    wordBreaker = ['+', '-', '*','/', '%', '<', '>', '!']
    alone = ['?', ';', ':', '(', ')', '{', '}', ',', '[', ']']
    temp = ""
    iterator = 0
    while iterator < len(filteredList):
        # handling identifiers or keywords.
        if re.match("^[a-zA-Z0-9]$", filteredList[iterator]):
            if temp != "" and re.match("^[a-zA-Z0-9|_|.]$", temp[len(temp)-1]):
                temp = temp + filteredList[iterator]
            elif temp != "" and not re.match("^[a-zA-Z0-9|_]$", temp[len(temp)-1]):
                BagOfWords.append(temp)
                temp = filteredList[iterator]
            else:
                temp = filteredList[iterator]

# handling any of the character present in alone list.
        elif filteredList[iterator] in alone:
            BagOfWords.append(temp)
            temp = ""
            BagOfWords.append(filteredList[iterator])

# handling spaces and newline charracter.
        elif filteredList[iterator] == " " or filteredList[iterator] == '\n':
            BagOfWords.append(temp) if temp != "" else False
            temp = ""
            if filteredList[iterator] == '\n':
                lineNumber += 1
                BagOfWords.append(lineNumber)

# handling charcter.
        elif filteredList[iterator] == "\'":
            count = 0

            if temp != "":
                BagOfWords.append(temp)
                temp = ""

            a = 2

            while count <= a:
                if count == 1 and filteredList[iterator] == "\\":
                    a = 3

                temp += filteredList[iterator]
                count += 1
                iterator += 1

            BagOfWords.append(temp)
            temp = ""
            continue

# handling strings.
        elif filteredList[iterator] == '\"':
            if temp != "" and temp[0] == '\"':
                temp += '\"'
                BagOfWords.append(temp)
                temp = ""
            else:
                temp = '\"'
                iterator += 1
                while filteredList[iterator] != '\"' and temp[len(temp)-1] != '\\':
                    temp += filteredList[iterator]
                    iterator += 1
                continue

# handling word breakers.
        elif filteredList[iterator] in wordBreaker:
            PM = ['+', '-']
            if temp == "":
                temp = filteredList[iterator]
                if filteredList[iterator+1] == "=":
                    iterator += 1
                    temp += filteredList[iterator]
                    BagOfWords.append(temp)
                    temp = ""

                elif filteredList[iterator] in PM and filteredList[iterator+1] == 'o':
                    iterator += 1
                    temp += filteredList[iterator]
                    BagOfWords.append(temp)
                    temp = ""

                else:
                    BagOfWords.append(temp)
                    temp = ""
            else:
                BagOfWords.append(temp)
                temp = filteredList[iterator]
                if filteredList[iterator+1] == "=":
                    iterator += 1
                    temp += filteredList[iterator]
                    BagOfWords.append(temp)
                    temp = ""

                elif filteredList[iterator] in PM and filteredList[iterator+1] == 'o':
                    iterator += 1
                    temp += filteredList[iterator]
                    BagOfWords.append(temp)
                    temp = ""

                else:
                    BagOfWords.append(temp)
                    temp = ""

        elif filteredList[iterator] == '=':
            if temp == "=":
                temp += filteredList[iterator]
                BagOfWords.append(temp)
                temp = ""
            elif temp == '':
                temp += filteredList[iterator]
            else:
                BagOfWords.append(temp)
                temp = filteredList[iterator]

# handling dot(.)
        elif filteredList[iterator] == '.':
            if re.match('^[0-9]$', filteredList[iterator+1]):
                try:
                    if int(temp):
                        temp += filteredList[iterator]
                except:
                    BagOfWords.append(temp)
                    temp = filteredList[iterator]
            else:
                if temp != "":
                    BagOfWords.append(temp)
                    BagOfWords.append(filteredList[iterator])
                    temp = ""
                else:
                    BagOfWords.append(filteredList[iterator])

# handling comments
        elif filteredList[iterator] == "#":
            BagOfWords.append(temp)
            temp = ""
            if filteredList[iterator+1] == "~":
                iterator+=1
                while filteredList[iterator+1] != "~" and filteredList[iterator+2]!="#":
                    iterator += 1
                iterator+=2
            else:
                while filteredList[iterator] != '\n':
                    iterator += 1

        iterator += 1
    if temp != "":
        BagOfWords.append(temp)
    return BagOfWords

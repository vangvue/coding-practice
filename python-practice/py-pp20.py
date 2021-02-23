# Write a program that replaces "?" with a lowercase character

riddle = "asdc?????f"
import random

def replaceStr(s):
    lowerChars = "abcdefghijklmnopqrstuvwxyz"

    if "?" not in s:
        return s

    for char in s:
        if char in lowerChars:
            lowerChars = lowerChars.replace(char, "")

    sArr = list(s)
    for x in range(len(sArr)):
        randChar = random.choice(lowerChars)
        if sArr[x] == "?":
            sArr[x] = randChar
            lowerChars = lowerChars.replace(randChar, "")

    return "".join(sArr)

print(replaceStr(riddle))

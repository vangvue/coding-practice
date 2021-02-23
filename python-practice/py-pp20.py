# Write a program that replaces "?" with a lowercase character

riddle = "??????"
import random

def replaceStr(s):
    lowerChars = "abcdefghijklmnopqrstuvwxyz"

    if "?" not in s:
        return s

    for x in range(len(s)):
        charBef = s[x - 1] if x != 0 else None
        charAft = s[x + 1] if x != len(s) - 1 else None
        randChar = None
        while True:
            randChar = random.choice(lowerChars)
            if randChar != charBef and randChar != charAft:
                break
        if s[x] == "?":
            s = s.replace("?", randChar, 1)

    return s

print(replaceStr(riddle))

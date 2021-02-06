# https://leetcode.com/problems/reverse-only-letters/
# 917. Reverse Only Letters
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their positions.


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letterList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letterStr = ""
        result = ""
        for char in S:
            if char in letterList:
                letterStr += char

        letterIndex = len(letterStr) - 1 # Used to reverse the string

        for char in S:
            if char in letterList:
                result += letterStr[letterIndex]
                letterIndex -= 1
            else:
                result += char

        return result

# https://leetcode.com/problems/reverse-only-letters/
# 917. Reverse Only Letters
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their positions.


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letterStr = ""
        result = ""
        for char in S:
            if char.isalpha():
                letterStr += char

        letterIndex = len(letterStr) - 1 # Will use to find the last index and decrement to reverse str

        for char in S:
            if char.isalpha():
                result += letterStr[letterIndex]
                letterIndex -= 1
            else:
                result += char

        return result

# Optimized Version
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        
        left = 0
        right = len(S) - 1
        while left < right:
            while left < right and not S[left].isalpha():
                left += 1
            while left < right and not S[right].isalpha():
                right -= 1                
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1
            
        return "".join(S)
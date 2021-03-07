# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        emptyArr = []
        emptyStr = ""
        for word in arr:
            wordLen = len(word) - 1
            while wordLen >= 0:
                emptyStr += word[wordLen]
                wordLen -= 1
            emptyArr.append(emptyStr)
            emptyStr = ""
        return " ".join(emptyArr)
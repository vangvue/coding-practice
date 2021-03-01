# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# 1662. Check If Two String Arrays are Equivalent

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wordStr1 = ""
        wordStr2 = ""
        for word in word1:
            wordStr1 += word  
        for word in word2:
            wordStr2 += word
            
        return wordStr1 == wordStr2
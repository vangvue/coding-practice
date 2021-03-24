# https://leetcode.com/problems/word-pattern/
# 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapChar = {}
        mapWord = {}
        
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        
        for char, word in zip(pattern, words):
            if char not in mapChar:
                if word in mapWord:
                    return False
                else:
                    mapChar[char] = word
                    mapWord[word] = char
                
            else:
                if mapChar[char] != word:
                    return False
                
        return True
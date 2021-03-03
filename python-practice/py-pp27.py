# https://leetcode.com/problems/shortest-completing-word/
# 748. Shortest Completing Word

# Given a string licensePlate and an array of strings words, find the shortest completing word in words.

# A completing word is a word that contains all the letters in licensePlate. 
# Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. 
# If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. 
# Possible completing words are "abccdef", "caaacab", and "cbca".

# Return the shortest completing word in words. It is guaranteed an answer exists. 
# If there are multiple shortest completing words, return the first one that occurs in words.

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        strLow = licensePlate.lower()
        wordLen = {}
        newLicensePlate = removeNonAlph(strLow)
        for word in words:
            for char in word:
                if char in newLicensePlate:
                    newLicensePlate = newLicensePlate.replace(char, "", 1)
                
            if len(newLicensePlate) == 0:
                wordLen[word] = 1 + len(word)
                newLicensePlate = removeNonAlph(strLow)
            else:
                newLicensePlate = removeNonAlph(strLow)
        
        
        return min(wordLen, key = wordLen.get)
        
# Helper Function
def removeNonAlph(string):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        newString = ""
        for char in string:
            if char in alphabet:
                newString += char
        return newString
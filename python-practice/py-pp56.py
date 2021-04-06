# https://leetcode.com/problems/truncate-sentence/
# 1816. Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        newStr = []
        for i in range(k):
            newStr.append(s[i])
        
        return " ".join(newStr)
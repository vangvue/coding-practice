# https://leetcode.com/problems/maximum-number-of-balloons/
# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

#My solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        str = "balloon"
        count = 0
        i = 0
        while i < len(text):
            if text[i] in str:
                str = str.replace(text[i], "", 1)
                text = text.replace(text[i], "", 1)
                i = 0
            else:
                i += 1
                
            if len(str) == 0:
                str = "balloon"
                count += 1
                i = 0
            
        return count

#Optimized Solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        strs = ['b', 'a', 'l', 'o', 'n']
        counts = [0] * 5

        for i in range(5):
            counts[i] = text.count(strs[i])

        counts[2] = counts[2] // 2
        counts[3] = counts[3] // 2

        return min(counts)
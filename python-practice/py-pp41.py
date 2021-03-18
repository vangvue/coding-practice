# https://leetcode.com/problems/count-items-matching-a-rule/
# 1773. Count Items Matching a Rule

# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, 
# and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            rKey = 0
        elif ruleKey == "color":
            rKey = 1
        else:
            rKey = 2
        
        count = 0
        
        for arr in items:
            i = 0
            while i < len(arr):
                if i == rKey:
                    if arr[i] == ruleValue:
                        count += 1
                i += 1
            i = 0
            
        return count
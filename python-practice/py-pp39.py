# https://leetcode.com/problems/add-strings/
# 415. Add Strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        val = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        num1Result = 0
        num2Result = 0
        
        for num in num1:
            num1Result = 10 * num1Result + val[num]
            
        for num in num2:
            num2Result = 10 * num2Result + val[num]
        
        return str(num1Result + num2Result)
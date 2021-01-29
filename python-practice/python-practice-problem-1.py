# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# 1304. Find N Unique Integers Sum up to Zero
#
# Given an integer n,
# return any array containing n unique integers such that they add up to 0.

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for x in range(1, int(n / 2) + 1):
            result.append(x)
            result.append(-x)
        if n % 2 != 0:
            result.append(0)
        return result

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# 1295. Find Numbers with Even Number of Digits


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
                
        return count
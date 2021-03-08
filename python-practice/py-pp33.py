# https://leetcode.com/problems/missing-number/
# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = []
        for a in range(len(nums) + 1):
            arr.append(a)
            a += 1
        nums.sort()
        for num in arr:
            if num not in nums:
                return num


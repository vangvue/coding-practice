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

# Shorter version
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for a in range(len(nums) + 1):
            if a not in nums:
                return a


# Different way to solve
# Compare method
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        arr = list(range(len(nums) + 1))
        i = 0
        for a in nums:
            if a != arr[i]:
                return arr[i]
            else:
                arr.pop(i)
        return arr[0]
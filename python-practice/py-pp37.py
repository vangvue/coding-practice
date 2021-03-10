# https://leetcode.com/problems/majority-element/
# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majEle = len(nums) / 2
        result = 0
        obj = {}
        i = 0
        while i < len(nums):
            if nums[i] in obj:
                obj[nums[i]] += 1
            else:
                obj[nums[i]] = 1
            i += 1
            
        for key, val in obj.items():
            if val > majEle:
                result = key
                majEle = val
        
        return result

# Shorten code
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        obj = {}
        i = 0
        while i < len(nums):
            obj[nums[i]] = obj.get(nums[i], 0) + 1
            i += 1
        
        return max(obj, key = obj.get)

# Optimized version
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
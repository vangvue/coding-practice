# https://leetcode.com/problems/third-maximum-number/
# 414. Third Maximum Number

# Given integer array nums, return the third maximum number in this array. 
# If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        if len(nums) < 3:
            return max(nums)
        
        return nums[-3]
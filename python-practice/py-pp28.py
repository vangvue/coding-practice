# https://leetcode.com/problems/move-zeroes/
# 283. Move Zeroes

# Given an array nums, write a function to move all 0's to the end 
# of it while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
                
        count = 0
        i = 0
        while count != zeroCount:
            if nums[i] == 0:
                holder = nums.pop(nums.index(0))
                nums.append(holder)
                count += 1
            else:
                i += 1

# Optimized Version
# Left and Right checker
# Right checker looks for numbers to replace with 0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        while r < len(nums):
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r += 1
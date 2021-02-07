# https://leetcode.com/problems/move-zeroes/submissions/
# 283. Move Zeroes
#
# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        """
        Do not return anything, modify nums in-place instead.
        """

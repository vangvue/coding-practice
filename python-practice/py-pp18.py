# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
# 1460. Make Two Arrays Equal by Reversing Sub-arrays
#
# Given two integer arrays of equal length target and arr.
#
# In one step, you can select any non-empty sub-array of arr and reverse it.
# You are allowed to make any number of steps.
#
# Return True if you can make arr equal to target, or False otherwise.

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        i = 0
        for num in arr:
            if num == target[i]:
                pass
            else:
                return False
            i += 1

        return True
            

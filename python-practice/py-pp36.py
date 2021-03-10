# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# 1287. Element Appearing More Than 25% In Sorted Array

# Given an integer array sorted in non-decreasing order, 
# there is exactly one integer in the array that occurs more than 25% of the time.
# Return that integer.

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        fourth = len(arr) / 4
        obj = {}
        i = 0
        while i < len(arr):
            if arr[i] in obj:
                obj[arr[i]] += 1
            else:
                obj[arr[i]] = 1
            i += 1
            
        for key, val in obj.items():
            if val > fourth:
                return key
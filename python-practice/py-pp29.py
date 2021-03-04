# https://leetcode.com/problems/contains-duplicate/
# 217. Contains Duplicate

# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            count[num] = 0
        
        for num in nums:
            if num in count:
                count[num] += 1
                
        for key,val in count.items():
            if val > 1:
                return True
            
        return False

# Optimized Version
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count.keys():
                count[num] = 1
            else:
                count[num] += 1
                if count[num] > 1:
                    return True
                
        return False
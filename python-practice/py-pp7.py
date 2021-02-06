# https://leetcode.com/problems/single-number/submissions/
# 136. Single Number
#
# Given a non-empty array of integers nums,
# every element appears twice except for one. Find that single one.
#
# Follow up: Could you implement a solution with a linear runtime complexity
# and without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums) # stores into a dictionary, int: count
        sortCount = sorted(count.items(), key = lambda x: x[1]) # sort by the value
        return sortCount[0][0] # gives the key in the first index of the list

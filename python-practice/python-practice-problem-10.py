# https://leetcode.com/problems/height-checker/
# 1051. Height Checker
#
# Students are asked to stand in non-decreasing order of heights for an annual photo.
#
# Return the minimum number of students that must move in order
# for all students to be standing in non-decreasing order of height.
#
# Notice that when a group of students is selected they can reorder
# in any possible way between themselves and the non selected students remain on their seats.

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        sortList = heights[:] # Copies heights, makes sure it doesn't change heights List
        sortList.sort()
        i = 0
        while i < len(heights):
            if sortList[i] == heights[i]:
                i += 1
            else:
                counter += 1
                i += 1
        return counter

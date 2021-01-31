# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/submissions/
# 1450. Number of Students Doing Homework at a Given Time
#
# Given two integer arrays startTime and endTime and given an integer queryTime.
#
# The ith student started doing their homework at the time startTime[i]
# and finished it at time endTime[i].
#
# Return the number of students doing their homework at time queryTime.
# More formally, return the number of students where queryTime lays
# in the interval [startTime[i], endTime[i]] inclusive.

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0
        i = 0
        for start in startTime:
            if (start <= queryTime and queryTime <= endTime[i]):
                result += 1
                i += 1
            else:
                i += 1

        return result

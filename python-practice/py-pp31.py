# https://leetcode.com/problems/student-attendance-record-i/
# 551. Student Attendance Record I

# You are given a string representing an attendance record for a student. 
# The record only contains the following three characters:

# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.

# A student could be rewarded if his attendance record doesn't 
# contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

class Solution:
    def checkRecord(self, s: str) -> bool:
        lCount = 0
        aCount = 0
        
        for char in s:
            if char == "A":
                aCount += 1
            if lCount >= 3:
                return False
            if char == "L":
                lCount += 1
            else:
                lCount = 0
                
        if aCount > 1 or lCount >= 3:
            return False
        else:
            return True
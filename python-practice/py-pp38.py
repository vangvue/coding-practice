# https://leetcode.com/problems/rotate-string/
# 796. Rotate String

# We are given two strings, A and B.

# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. 
# Return True if and only if A can become B after some number of shifts on A.

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        count = 0
        bLen = len(B)
        
        if len(A) == 0 and len(B) == 0:
            return True
        
        while count != len(B):
            if A == B:
                return True
            else:
                holder = B[:1]
                B = B[1:] + holder
            count += 1
            
        return False
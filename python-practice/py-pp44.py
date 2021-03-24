https://leetcode.com/problems/power-of-two/
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        
        i = 1
        while i < n:
            i *= 2
            
        if i == n:
            return True
        else:
            return False
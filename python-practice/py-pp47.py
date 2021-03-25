# https://leetcode.com/problems/power-of-three/
# 326. Power of Three

# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        
        i = 1
        while i < n:
            i *= 3
        
        if i == n:
            return True
        else:
            return False

# Method above is similar to py-pp44.py
# Different Approach
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n % 10 in [1, 3, 9, 7]:
            while n % 3 == 0:
                n = n // 3
            return n == 1       
        else:
            return False
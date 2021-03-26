https://leetcode.com/problems/power-of-four/
342. Power of Four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 1
        while i < n:
            i *= 4
            
        if i == n:
            return True
        else:
            return False


https://leetcode.com/problems/fibonacci-number/
509. Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)


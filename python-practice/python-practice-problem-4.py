# https://leetcode.com/problems/add-to-array-form-of-integer/submissions/
# 989. Add to Array-Form of Integer
#
# For a non-negative integer X, the array-form of X is an array of its digits
# in left to right order.  For example, if X = 1231,
# then the array form is [1,2,3,1].
#
# Given the array-form A of a non-negative integer X,
# return the array-form of the integer X+K.

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        result = []
        intStr = ""

        i = 0
        while i < len(A):
            intStr += str(A[i])
            i += 1

        sumTotal = str(int(intStr) + K)

        for digits in sumTotal:
            result.append(digits)

        return result

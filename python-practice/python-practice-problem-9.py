# https://leetcode.com/problems/self-dividing-numbers/
# 728. Self Dividing Numbers
#
# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#
# Also, a self-dividing number is not allowed to contain the digit zero.
#
# Given a lower and upper number bound, output a list of every possible self dividing number,
# including the bounds if possible.

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        i = left
        selfDiv = 0

        while i <= right:
            if "0" in str(left):
                left += 1
                i += 1
            elif len(str(left)) > 1:
                for num in str(left):
                    if left % int(num) == 0:
                        selfDiv += 1
                if selfDiv == len(str(left)):
                    result.append(left)
                selfDiv = 0
                left += 1
                i += 1
            elif left % i == 0:
                result.append(left)
                left += 1
                i += 1
            else:
                left += 1
                i += 1
        return result

# https://leetcode.com/problems/relative-sort-array/submissions/
# 1122. Relative Sort Array
#
# Given two arrays arr1 and arr2, the elements of arr2 are distinct,
# and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the
# relative ordering of items in arr1 are the same as in arr2.
# Elements that don't appear in arr2 should be placed at the end of arr1
# in ascending order.


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        extraElements = []

        for num in arr2:
            for digit in arr1:
                if num == digit:
                    result.append(digit)

        for element in arr1:
            if element not in arr2:
                extraElements.append(element)

        extraElements.sort()
        result.extend(extraElements)

        return result

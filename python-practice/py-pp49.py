https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
1437. Check If All 1's Are at Least Length K Places Away

Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        
        for num in nums:
            if num == 1:
                if count < k:
                    return False

                count = 0
                
            else:
                count += 1
                
        return True
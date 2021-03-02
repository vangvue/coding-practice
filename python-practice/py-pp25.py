# https://leetcode.com/problems/last-stone-weight/
# 1046. Last Stone Weight

# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  
# Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, 
# and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  
# Return the weight of this stone (or 0 if there are no stones left.)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones) < 2:
                break
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if y - x == 0:
                pass
            else:
                stones.append(y - x)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
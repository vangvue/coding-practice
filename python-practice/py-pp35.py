https://leetcode.com/problems/assign-cookies/
455. Assign Cookies

Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; 
and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, 
and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        
        g.sort()
        s.sort()
        
        result = 0
        childIndex = 0 
        
        for cookie in s:
            if childIndex >= len(g):
                return result
            if cookie >= g[childIndex]:
                result += 1
                childIndex += 1
        
        return result
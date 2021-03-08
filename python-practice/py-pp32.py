# https://leetcode.com/problems/make-the-string-great/
# 1544. Make The String Great

# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter 
# but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad 
# and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. 
# The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.

class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        sLen = len(s)
        while i <= sLen - 2:
            a = s[i]
            b = s[i + 1]
            if a.islower() and a.upper() == b or a.isupper() and a.lower() == b:
                s = s[:i] + "" + s[i + 2:]
                i = 0
                sLen = len(s)
            else:
                i += 1
        return s
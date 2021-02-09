# https://leetcode.com/problems/length-of-last-word/
# 58. Length of Last Word
#
# Given a string s consists of some words separated by spaces,
# return the length of the last word in the string.
# If the last word does not exist, return 0.
#
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.split()) == 0:
            return 0
        return len(s.split()[-1])

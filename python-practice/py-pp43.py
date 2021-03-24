https://leetcode.com/problems/valid-palindrome/
125. Valid Palindrome

Given a string s, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[\W_]+', '', s).lower()
        
        return s == s[::-1]
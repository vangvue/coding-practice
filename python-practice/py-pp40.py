# https://leetcode.com/problems/maximum-repeating-substring/
# 1668. Maximum Repeating Substring

# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. 
# The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. 
# If word is not a substring of sequence, word's maximum k-repeating value is 0.

# Given strings sequence and word, return the maximum k-repeating value of word in sequence.

class Solution(object):
    def maxRepeating(self, sequence, word):
        count = 0
        resword = ''
        
        while True:
            resword = resword + word
            val = sequence.find(resword)
            
            if val== -1:
                break
                
            else:
                count+=1
                
        return count
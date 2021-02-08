# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
#
# Given a sentence that consists of some words separated by a single space, and a searchWord.
#
# You have to check if searchWord is a prefix of any word in sentence.
#
# Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).
#
# If searchWord is a prefix of more than one word, return the index of the first word (minimum index).
# If there is no such word return -1.
#
# A prefix of a string S is any leading contiguous substring of S.

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordsArr = sentence.split()
        i = 0
        for words in wordsArr:
            if searchWord in words:
                if searchWord[0] == words[0]:
                    i += 1
                    return i
                else: i += 1
            else: i += 1
        return -1

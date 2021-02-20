https://leetcode.com/problems/valid-anagram/
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

var isAnagram = function(s, t) {
    if (t.length > s.length) return false
    for (let i = 0; i < t.length; i++) {
        if (s.includes(t[i])) s = s.substring(0, s.indexOf(t[i])) + s.substring(s.indexOf(t[i]) + 1)
    }

    if (s.length === 0) return true
    else return false
};

// https://leetcode.com/problems/reverse-string/
// 344. Reverse String
// Write a function that reverses a string. The input string is given as an array of characters char[].

// Do not allocate extra space for another array, you must do this by modifying the 
// input array in-place with O(1) extra memory.

// You may assume all the characters consist of printable ascii characters.

var reverseString = function(s) {
    return reverseStringHelper(0, s.length - 1)

    function reverseStringHelper(l, r) {
        if (l >= r) return s
        let temp = s[r]
        s[r] = s[l]
        s[l] = temp

        return reverseStringHelper(l + 1, r - 1)
    }
};
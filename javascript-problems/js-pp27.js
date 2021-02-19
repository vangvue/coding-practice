// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
// 1160. Find Words That Can Be Formed by Characters
//
// You are given an array of strings words and a string chars.
//
// A string is good if it can be formed by characters from chars (each character can only be used once).
//
// Return the sum of lengths of all good strings in words.

var countCharacters = function(words, chars) {
    let copyChar = chars;
    let strSum = "";
    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words[i].length; j++) {
            if (copyChar.includes(words[i][j])) {
              // Removes the char at the specific index
              copyChar = copyChar.substring(0, copyChar.indexOf(words[i][j])) + copyChar.substring(copyChar.indexOf(words[i][j]) + 1);
            } else {
                continue;
            }
        }
        if ((chars.length - words[i].length) === copyChar.length) strSum += words[i];
        copyChar = chars;
    }

    return strSum.length;
};

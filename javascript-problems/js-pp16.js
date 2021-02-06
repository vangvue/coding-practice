// https://leetcode.com/problems/keyboard-row/submissions/
// 500. Keyboard Row
//
// Given an array of strings words, return the words that can be
// typed using letters of the alphabet on only one row of
// American keyboard like the image below.
//
// In the American keyboard:
//
// the first row consists of the characters "qwertyuiop",
// the second row consists of the characters "asdfghjkl", and
// the third row consists of the characters "zxcvbnm".

var findWords = function(words) {
    const firstRow = "qwertyuiop";
    const secondRow = "asdfghjkl";
    const thirdRow = "zxcvbnm";
    let result = [];
    let firstCount = 0;
    let secondCount = 0;
    let thirdCount = 0;

    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words[i].length; j++) {
            if (firstRow.includes(words[i][j].toLowerCase())) { firstCount += 1; }
            else if (secondRow.includes(words[i][j].toLowerCase())) { secondCount += 1; }
            else { thirdCount += 1; }
        }
        
        if (firstCount > 0 && secondCount === 0 && thirdCount === 0) { result.push(words[i]) }
        if (firstCount === 0 && secondCount > 0 && thirdCount === 0) { result.push(words[i]) }
        if (firstCount === 0 && secondCount === 0 && thirdCount > 0) { result.push(words[i]) }
        firstCount = 0;
        secondCount = 0;
        thirdCount = 0;
    }
    return result;
};

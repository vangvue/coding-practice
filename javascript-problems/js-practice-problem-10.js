// https://leetcode.com/problems/shortest-distance-to-a-character/
// 821. Shortest Distance to a Character
//
// Given a string S and a character C,
// return an array of integers representing the shortest distance
// from the character C in the string.

var shortestToChar = function(S, C) {
    let cIndex = [];
    let result = [];
    for (let i = 0; i < S.length; i++) { // finds C, indexes
        if(S[i] == C) {
            cIndex.push(i);
        }
    }
    let cCounter = 0;
    for (let i = 0; i < S.length; i++) {
        if (i - cIndex[cCounter] >= cIndex[cCounter + 1] - i) {
            cCounter++;
        }
        let counter = cIndex[cCounter];
        result.push(Math.abs(counter - i));
    }
    return result;
};

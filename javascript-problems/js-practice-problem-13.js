// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
// 1619. Mean of Array After Removing Some Elements
//
// Given an integer array arr, return the mean of the remaining
// integers after removing the smallest 5% and the largest 5% of the elements.
//
// Answers within 10-5 of the actual answer will be considered accepted.

var trimMean = function(arr) {
    arr.sort((a,b) => a-b);
    let total = 0;
    const cutOff = Math.round(arr.length * .05);
    for (let i = cutOff; i < arr.length - cutOff; i++) {
        total += arr[i];
    }
    return total / (arr.length - 2 * cutOff);
};

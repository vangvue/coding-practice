// https://leetcode.com/problems/unique-number-of-occurrences/
// 1207. Unique Number of Occurrences

// Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

var uniqueOccurrences = function(arr) {
    let obj = {};
    let len = arr.length;
    let newArr = [];

    for (let i = 0; i < len; i++) {
        if (arr[i] in obj) {
            obj[arr[i]] += 1;
        } else {
            obj[arr[i]] = 1;
        }
    }

    for (const [key, value] of Object.entries(obj)) {
        if (newArr.includes(`${value}`)) return false;
        else newArr.push(`${value}`);
    }

    return true;
};
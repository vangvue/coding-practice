// https://leetcode.com/problems/check-if-n-and-its-double-exist/submissions/
// 1346. Check If N and Its Double Exist

// Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

// More formally check if there exists two indices i and j such that :

// i != j
// 0 <= i, j < arr.length
// arr[i] == 2 * arr[j]

var checkIfExist = function(array) {
    while (array.length) {
        const n = array.pop();
        if (array.includes(n * 2) || array.includes(n / 2)) return true;
    }
    return false;
}
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/
// 1299. Replace Elements with Greatest Element on Right Side
//
// Given an array arr, replace every element
// in that array with the greatest element among the elements to its right,
// and replace the last element with -1.
//
// After doing so, return the array.

var replaceElements = function(arr) {
    let resultArr = [];
    if (arr.length === 1) {
        resultArr.push(-1)
    } else {
        for (let i = 0; i < arr.length; i++) {
            if (i === (arr.length - 1)) {
                resultArr.push(-1);
            } else {
                resultArr.push(Math.max.apply(Math, arr.slice(i + 1)));
            }
        }
    }
    return resultArr;
};

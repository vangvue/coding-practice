// https://leetcode.com/problems/third-maximum-number/
// 414. Third Maximum Number

// Given integer array nums, return the third maximum number in this array.
// If the third maximum does not exist, return the maximum number.

var thirdMax = function(nums) {
    let sortedArr = [...new Set(nums)]; // removes duplicates
    sortedArr = sortedArr.sort((a, b) => a - b).reverse(); // sorts max to min
    if (sortedArr.length >= 3) {
        return sortedArr[2];
    } else {
        return sortedArr[0];
    }
};

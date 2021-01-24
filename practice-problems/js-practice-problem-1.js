// https://leetcode.com/problems/running-sum-of-1d-array/
// 1480. Running Sum of 1d Array

// Given an array nums.
// We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
// Return the running sum of nums.

var runningSum = function(nums) {
    let sumCount = 0;
    let arr = [];

    for (let i = 0; i < nums.length; i++) {
        sumCount += nums[i];
        arr.push(sumCount)
    }

    return arr
};

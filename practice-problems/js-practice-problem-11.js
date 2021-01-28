// https://leetcode.com/problems/maximum-subarray/
// 53. Maximum Subarray
//
// Given an integer array nums, find the contiguous subarray
// (containing at least one number) which has the largest sum and return its sum.

var maxSubArray = function(nums) {
    let max = Math.max(...nums);
    let sum = 0;
    
    for (let i = 0; i < l.length; i++) {
        sum += nums[i];
        if (sum > max) {
            max = sum;
        }
        if (sum < 0) {
            sum  = 0;
        }
    }
    return max;
};

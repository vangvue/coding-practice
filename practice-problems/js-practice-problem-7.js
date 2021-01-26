// https://leetcode.com/problems/find-all-duplicates-in-an-array/
// 442. Find All Duplicates in an Array
//
// Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
// some elements appear twice and others appear once.
//
// Find all the elements that appear twice in this array.
//
// Could you do it without extra space and in O(n) runtime?

var findDuplicates = function(nums) {
    let arr1 = [];
    let arr2 = [];
    for (let i = 0; i < nums.length; i++) {
        if (!arr1.includes(nums[i])) {
            arr1.push(nums[i]);
        } else {
            arr2.push(nums[i]);
        }
    }
    return arr2
};

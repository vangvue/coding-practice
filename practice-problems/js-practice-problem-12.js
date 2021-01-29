// https://leetcode.com/problems/maximum-product-of-three-numbers/
// 628. Maximum Product of Three Numbers
//
// Given an integer array nums,
// find three numbers whose product is maximum and return the maximum product.


var maximumProduct = function(nums) {
    let max = nums.sort((a, b) => a - b);
    let prod1 = max[0] * max[1] * max[nums.length - 1]; // multiplies first 2 elements and last element
    let prod2 = max[nums.length - 1] * max[nums.length - 2] * max[nums.length - 3]; // multiplies last 3 elements
    return Math.max(product1, product2);
};

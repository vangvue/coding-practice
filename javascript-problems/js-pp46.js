// https://leetcode.com/problems/sign-of-the-product-of-an-array/
// // 1822. Sign of the Product of an Array

/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    let counter = 1;
    let len = nums.length

    for (let i = 0; i < len; i++) {
        counter *= nums[i];
    }
    if (counter > 0) return 1
    else if (counter < 0) return -1
    else return 0
};
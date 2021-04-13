// https://leetcode.com/problems/squares-of-a-sorted-array/
// 977. Squares of a Sorted Array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let squaresArr = [];
    let len = nums.length

    for (let i = 0; i < len; i++) {
        squaresArr.push(nums[i] * nums[i])
    }

    return squaresArr.sort(function(a, b) { return a - b })
};
// https://leetcode.com/problems/sort-array-by-parity-ii/
// 922. Sort Array By Parity II

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function(nums) {
    let len = nums.length
    let evenArr = [];
    let oddArr = [];
    let result = [];

    for (let i = 0; i < len; i++) {
        if (nums[i] % 2 === 0) evenArr.push(nums[i])
        else oddArr.push(nums[i])
    }

    while (result.length < len) {
        if (result.length === 0) {
            let evenNum = evenArr.pop()
            result.push(evenNum)
        } else if (result.length % 2 === 1) {
            let oddNum = oddArr.pop()
            result.push(oddNum)
        } else {
            let evenNum = evenArr.pop()
            result.push(evenNum)
        }
    }

    return result
};
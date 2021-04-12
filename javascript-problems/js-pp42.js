// https://leetcode.com/problems/sum-of-unique-elements/
// 1748. Sum of Unique Elements

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    let result = 0;
    let uniqueArr = {};
    let len = nums.length;

    for (let i = 0; i < len; i++) {
        if (nums[i] in uniqueArr) uniqueArr[nums[i]] += 1
        else uniqueArr[nums[i]] = 1
    }

    for (const [key, value] of Object.entries(uniqueArr)) {
        if (`${value}` < 2) result += `${key}` * 1;
    }

    return result
};
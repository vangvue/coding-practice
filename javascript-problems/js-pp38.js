// https://leetcode.com/problems/maximum-69-number/
// 1323. Maximum 69 Number

/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function(num) {
    let numStr = num.toString();

    return (numStr.replace("6", "9")) * 1

}
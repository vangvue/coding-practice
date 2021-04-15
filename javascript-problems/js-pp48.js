// https://leetcode.com/problems/calculate-money-in-leetcode-bank/
// // 1716. Calculate Money in Leetcode Bank

/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    let count = 0;
    let week = 1;
    let day = 0;

    for (let i = 1; i <= n; i++) {
        if (day === 7) {
            week++
            day = 0
        }
        count += day + week
        day++;
    }

    return count
};
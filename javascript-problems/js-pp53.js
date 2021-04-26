// https://leetcode.com/problems/maximum-ice-cream-bars/
// 1833. Maximum Ice Cream Bars

/**
 * @param {number[]} costs
 * @param {number} coins
 * @return {number}
 */
var maxIceCream = function(costs, coins) {
    let result = 0;
    costs = costs.sort(function(a, b) { return a - b });

    for (let cost of costs) {
        if (cost <= coins) {
            if (coins < 0) continue
            coins = coins - cost;
            result += 1
        }
    }
    return result
};
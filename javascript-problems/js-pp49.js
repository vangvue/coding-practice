// https://leetcode.com/problems/thousand-separator/
// 1556. Thousand Separator

/**
 * @param {number} n
 * @return {string}
 */
var thousandSeparator = function(n) {
    n = n.toLocaleString();

    for (let i = 0; i < n.length; i++) {
        if (n[i] === ",") n = n.replace(n[i], ".")
    }

    return n
};
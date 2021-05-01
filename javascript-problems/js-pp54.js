// https://leetcode.com/problems/find-the-winner-of-the-circular-game/
// 1823. Find the Winner of the Circular Game

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    let countArr = [];
    let count = 1;

    while (countArr.length !== n) {
        countArr.push(count);
        count++;
    }


    let i = 1;
    let j = 0;
    while (countArr.length > 1) {
        let len = countArr.length
        if (j >= len) {
            j = 0;
        }
        if (i >= k) {
            countArr.splice(j, 1);
            i = 1;
        } else {
            i++;
            j++;
        }
    }

    return countArr[0]
};
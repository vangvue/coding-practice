// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
// 1351. Count Negative Numbers in a Sorted Matrix

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    let negCount = 0
    let len = grid.length

    for (let i = 0; i < len; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] < 0) negCount += 1
        }
    }

    return negCount
};
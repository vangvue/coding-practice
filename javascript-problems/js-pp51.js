// https://leetcode.com/problems/matrix-diagonal-sum/
// 1572. Matrix Diagonal Sum

/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let result = 0;

    for (let i = 0; i < mat.length; i++) {
        for (let j = 0; j < mat[i].length; j++) {
            if (i === 0 || i === mat.length - 1) {
                if (j === 0 || j === mat[i].length - 1) result += mat[i][j]
            } else if (j === i || j === (mat[i].length - 1) - i) {
                result += mat[i][j]
            }
        }
    }
    return result
};
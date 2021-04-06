// https://leetcode.com/problems/determine-color-of-a-chessboard-square/
// 1812. Determine Color of a Chessboard Square

/**
 * @param {string} coordinates
 * @return {boolean}
 a, c, e, g --> black odd white even
 b, d, f, h --> black even white odd
 */
var squareIsWhite = function(coordinates) {
    if (coordinates[0] === "a" || coordinates[0] === "c" || coordinates[0] === "e" || coordinates[0] === "g") {
        if (coordinates[1] % 2 === 0) return true
        else return false
    } else {
        if (coordinates[1] % 2 === 0) return false
        else return true
    }
};
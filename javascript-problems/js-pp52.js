// https://leetcode.com/problems/destination-city/
// 1436. Destination City

/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    let nextDestination = paths[0][1];
    let len = paths.length;

    let i = 0;
    while (i < len) {
        if (paths[i][0] === nextDestination) {
            nextDestination = paths[i][1]
            i = 0
        }
        i++;
    }

    return nextDestination
};
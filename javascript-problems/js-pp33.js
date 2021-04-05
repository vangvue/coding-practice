https: //leetcode.com/problems/path-crossing/
    1496. Path Crossing

/**
 * @param {string} path
 * @return {boolean}
 */
var isPathCrossing = function(path) {
    let x = 0;
    let y = 0;
    let pathLen = path.length;
    let coordArr = [
        [x, y]
    ];
    let obj = {}

    for (let i = 0; i < pathLen; i++) {
        if (path[i] == "N") {
            x += 1;
            coordArr.push([x, y]);
        } else if (path[i] == "S") {
            x -= 1;
            coordArr.push([x, y]);
        } else if (path[i] == "E") {
            y += 1;
            coordArr.push([x, y]);
        } else {
            y -= 1
            coordArr.push([x, y]);
        }
    }

    for (let i = 0; i < coordArr.length; i++) {
        if (coordArr[i] in obj) {
            obj[coordArr[i]] += 1;
        } else {
            obj[coordArr[i]] = 1;
        }
    }

    for (const [key, value] of Object.entries(obj)) {
        if (value > 1) return true
    }

    return false
};
// https://leetcode.com/problems/flipping-an-image/
// 832. Flipping an Image

/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function(image) {
    let arr = []
    for (let i = 0; i < image.length; i++) {
        arr.push(image[i].reverse())
        for (let j = 0; j < arr[i].length; j++) {
            if (arr[i][j] == 0) arr[i][j] = 1
            else arr[i][j] = 0
        }
    }

    return arr
};
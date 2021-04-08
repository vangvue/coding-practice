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

// Faster runtime
// Runtime: 80 ms, faster than 91.88% of JavaScript online submissions for Flipping an Image.
// Memory Usage: 40.6 MB, less than 35.36% of JavaScript online submissions for Flipping an Image.
/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function(image) {
    for (let i = 0; i < image.length; i++) {
        image[i] = image[i].reverse()
        for (let j = 0; j < image[i].length; j++) {
            if (image[i][j] == 0) image[i][j] = 1
            else image[i][j] = 0
        }
    }
    return image
};
// https://leetcode.com/problems/peak-index-in-a-mountain-array/
// 852. Peak Index in a Mountain Array

/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    let count = 0;
    let len = arr.length
    for (let i = 1; i < len; i++) {
        if (arr[i] > arr[i - 1]) count += 1
    }

    return count
};
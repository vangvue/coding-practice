// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
// 1385. Find the Distance Value Between Two Arrays

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number} d
 * @return {number}
 */
var findTheDistanceValue = function(arr1, arr2, d) {
    let count = 0;
    let checker = 0;
    let lenArr1 = arr1.length;
    let lenArr2 = arr2.length;

    for (let i = 0; i < lenArr1; i++) {
        for (let j = 0; j < lenArr2; j++) {
            if (Math.abs(arr1[i] - arr2[j]) > d) checker += 1
        }
        if (checker === lenArr2) count += 1
        checker = 0;
    }

    return count
};
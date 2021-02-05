https://leetcode.com/problems/three-consecutive-odds/
1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false.

var threeConsecutiveOdds = function(arr) {
    let oddCount = 0;
    for (let i = 0; i < arr.length; i++) {
        if (oddCount === 3) {
            break;
        }
        if (Math.abs(arr[i] % 2) === 1) {
            oddCount += 1;
        } else {
            oddCount = 0;
        }
    }
    if (oddCount >= 3) { return true;}
    else { return false; }
};

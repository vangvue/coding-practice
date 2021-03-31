// https://leetcode.com/problems/defuse-the-bomb/
// 1652. Defuse the Bomb

// You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

// To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

// If k > 0, replace the ith number with the sum of the next k numbers.
// If k < 0, replace the ith number with the sum of the previous k numbers.
// If k == 0, replace the ith number with 0.
// As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

// Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

var decrypt = function(code, k) {
    let arr = [];
    let len = code.length;
    let result = 0;
    let j = 0;
    let count = 0;
    if (k == 0) {
        for (let j = 0; j < len; j++) {
            arr.push(0);
        }
        return arr;
    } else if (k > 0) {
        for (let i = 0; i < len; i++) {
            j = i + 1;
            result = 0;
            count = 0;
            if (i == len - 1) {
                j = 0;
            }
            while (count != k) {
                if (j == len - 1) {
                    count += 1;
                    result += code[j];
                    j = 0;
                } else {
                    count += 1;
                    result += code[j];
                    j += 1;
                }
            }
            arr.push(result);
        }
    } else {
        k = Math.abs(k)
        for (let i = 0; i < len; i++) {
            j = i - 1;
            result = 0;
            count = 0;
            if (i == 0) {
                j = len - 1;
            }
            while (count != k) {
                if (j == 0) {
                    count += 1;
                    result += code[j];
                    j = len - 1;
                } else {
                    count += 1;
                    result += code[j];
                    j -= 1;
                }
            }
            arr.push(result);
        }
    }

    return arr;
};
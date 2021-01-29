// https://leetcode.com/problems/reverse-integer/
// 7. Reverse Integer
//
// Given a signed 32-bit integer x, return x with its digits reversed.
// If reversing x causes the value to go outside the signed
// 32-bit integer range [-231, 231 - 1], then return 0.
//
// Assume the environment does not allow you to store
// 64-bit integers (signed or unsigned).

var reverse = function(x) {
    let emptyStr = "";
    x = x.toString();

    for(let i = x.length - 1; i >= 0; i--) {
        if(x[i] === "-") {
            emptyStr = x[i] + emptyStr;
        } else {
            emptyStr += x[i];
        };
    };
    emptyStr *= 1 // converts back to int
    if (emptyStr < Math.pow(-2, 31) || emptyStr > Math.pow(2, 31) - 1) {
        return 0;
      };
    return emptyStr;
};

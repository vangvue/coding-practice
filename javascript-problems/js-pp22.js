// https://leetcode.com/problems/reformat-phone-number/
// 1694. Reformat Phone Number
//
// You are given a phone number as a string number.
// number consists of digits, spaces ' ', and/or dashes '-'.
//
// You would like to reformat the phone number in a certain manner.
// Firstly, remove all spaces and dashes.
// Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
// The final digits are then grouped as follows:
//
// 2 digits: A single block of length 2.
// 3 digits: A single block of length 3.
// 4 digits: Two blocks of length 2 each.
// The blocks are then joined by dashes.
// Notice that the reformatting process should never produce any blocks of length
// 1 and produce at most two blocks of length 2.
//
// Return the phone number after formatting.

var reformatNumber = function(number) {
    number = number.replace(/-|\s/g,""); // removes spaces and hyphens
    result = ""
    numLen = number.length // Counter to find how many digits left, use to decrement
    if (number.length < 4) { // Test case to automatically return digits under length of 4
        return number;
    }
    else {
        for (let i = 0; i < number.length; i++) {
            if (numLen > 4) {
                result += number[i] + number[i + 1] + number[i + 2] + "-";
                numLen -= 3;
                i += 2;
            } else if (numLen === 4) {
                result += number[i] + number[i + 1] + "-" + number[i + 2] + number[i + 3];
                numLen -= 4;
                i += 3;
            } else {
                if (numLen === 3) {
                    result += number[i] + number[i + 1] + number[i + 2];
                    numLen -= 3;
                    i += 2;
                } else {
                    result += number[i] + number[i + 1]
                    numLen -= 2;
                    i += 1;
                }
            }
        }
    }
    return result;
};

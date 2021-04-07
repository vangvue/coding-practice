// Recursion Practice

// Question 1: Sum all numbers
// Write a function called sumRange. It will take a number and return the sum of all numbers
// from 1 up to the number passed in.
// Sample: sumRange(3) returns 6, since 1 + 2 + 3 = 6.
function sumRange(n) {
    if (n === 1) return 1;
    return n + sumRange(n - 1);
}
console.log(sumRange(10));


// Question 2: Power function
// Write a function called power which takes in a base and an exponent.
// If the exponent is 0, return 1.
function power(base, exponent) {
    if (exponent === 0) return 1;
    return base * power(base, exponent - 1);
}

console.log(power(2, 4));


// Question 3: Calculate factorial
// Write a function that returns the factorial of a number. As a quick refresher,
// a factorial of a number is the result of that number multiplied by the number before it,
// and the number before that number, and so on, until you reach 1. The factorial of 1 is just 1.
function factorial(n) {
    if (n === 1) return 1;
    return n * factorial(n - 1);
}

console.log(factorial(5));


// Question 5: Product of an array
// Write a function called productOfArray which takes in an array
// of numbers and returns the product of them all
function product(arr) {
    let result = arr.pop()
    if (arr.length === 1) return result * arr[0]
    return result * product(arr)
}

console.log(product([1, 2, 3, 10, 10]));

// Question 6: Search JS object
// Write a function called contains that searches for a value in a nested object.
// It returns true if the object contains that value.
function contains()

// https://leetcode.com/problems/range-sum-of-bst/
// 938. Range Sum of BST

// Given the root node of a binary search tree, return the sum of values 
// of all nodes with a value in the range [low, high].

const rangeSumBST = (root, low, high) => {
    let sum = 0;
    const traverse = node => {
        if (!node) return
        if (node.val >= low && node.val <= high) {
            sum += node.val
        }
        traverse(node.left)
        traverse(node.right)
    }
    traverse(root);
    return sum
};


// ruby recursion problem
// ruby practice
// def rotate_array(arr, num)
//   if num > 0
//     arrLast = arr.pop()
//     arr.unshift(arrLast)
//     return rotate_array(arr, num - 1)
//   else
//     return arr
//   end
// end

// print rotate_array([ "Matt", "Danny", "Mashu", "Matthias" ], 1) # => [ "Matthias", "Matt", "Danny", "Mashu" ]
// puts

// print rotate_array([ "a", "b", "c", "d" ], 2) # => [ "c", "d", "a", "b" ]
// puts

// Greatest common divisor
// The greatest common divisor (gcd) of two integers, 
// when at least one of them is not zero, is the largest positive integer 
// that divides the numbers without a remainder. 
// Recursively find the greatest common divisor of a sequnce of values.

function gcd(a, b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
};

console.log(gcd(1263262, 553443));
//11


// https://leetcode.com/problems/count-of-matches-in-tournament/
// 1688. Count of Matches in Tournament

function numberOfMatches(n, sum = 0) {
    if (n === 1) return sum;
    if (n % 2 === 0) {
        return numberOfMatches((n / 2), sum += n / 2);
    } else if (n % 2 === 1) {
        return numberOfMatches((((n - 1) / 2) + 1), sum += (n - 1) / 2);
    }
};

// Lucas Number problem practice
// Write a function, lucasNumber(n), that takes in a number.
// The function should return the n-th number of the Lucas Sequence.
// The 0-th number of the Lucas Sequence is 2.
// The 1-st number of the Lucas Sequence is 1
// To generate the next number of the sequence, we add up the previous two numbers.
function lucasNumber(n) {
    if (n === 0) return 2
    if (n === 1) return 1
    return lucasNumber(n - 1) + lucasNumber(n - 2)
}
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
// 961. N-Repeated Element in Size 2N Array
//
// In a array A of size 2N, there are N+1 unique elements,
// and exactly one of these elements is repeated N times.
//
// Return the element repeated N times.

var repeatedNTimes = function(A) {
    let currentCount = 0;
    let previousCount = 0;
    let repeatedElement = -Infinity; // catches all elements inside A
    for (let i = 0; i <= A.length; i++) {
        for (let j = 0; j <= A.length; j++) {
            if (A[i] === A[j]) {
                currentCount += 1;
                if (currentCount >= previousCount) {
                    repeatedElement = A[i];
                    previousCount = currentCount;
                };
            };
        };
        currentCount = 0;
    };
    return repeatedElement;
};

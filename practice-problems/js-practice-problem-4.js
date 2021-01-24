// https://leetcode.com/problems/calculate-money-in-leetcode-bank/
// 1716. Calculate Money in Leetcode Bank

// Hercy wants to save money for his first car.
// He puts money in the Leetcode bank every day.
//
// He starts by putting in $1 on Monday, the first day.
// Every day from Tuesday to Sunday, he will put in $1 more than the day before.
// On every subsequent Monday, he will put in $1 more than the previous Monday.
// Given n, return the total amount of money he will have in the
// Leetcode bank at the end of the nth day.

var totalMoney = function(n) {
    let dollarAdd = 1;
    let days = 7;
    let moneyCount = 0;
    let week = 1;
    for (let i = 0; i < n; i++) {
        if (days !== 0) {
            moneyCount += dollarAdd;
            dollarAdd++;
            days--;
        } else {
            week++;
            dollarAdd = week;
            days = 7;
            i--;
        }
    }
    return moneyCount;
};

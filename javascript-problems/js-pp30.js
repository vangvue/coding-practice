// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
// 1491. Average Salary Excluding the Minimum and Maximum Salary

// Given an array of unique integers salary where salary[i] is the salary of the employee i.

// Return the average salary of employees excluding the minimum and maximum salary.

var average = function(salary) {
    salary.sort(function(a, b) { return a > b ? 1 : -1 });
    salary.shift();
    salary.pop();
    let average = 0;
    salary.forEach(num => average += num);
    return average / salary.length
};
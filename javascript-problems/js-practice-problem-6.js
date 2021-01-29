// https://leetcode.com/problems/subrectangle-queries/
// 1476. Subrectangle Queries
//
// Implement the class SubrectangleQueries which receives a rows x cols rectangle
// as a matrix of integers in the constructor and supports two methods:
//
// 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
//
// Updates all values with newValue in the subrectangle whose upper left coordinate
// is (row1,col1) and bottom right coordinate is (row2,col2).
//
// 2. getValue(int row, int col)
//
// Returns the current value of the coordinate (row,col) from the rectangle.

class SubrectangleQueries {
    constructor(rectangle) {
        this.rectangle = rectangle;

        SubrectangleQueries.prototype.updateSubrectangle = function(row1, col1, row2, col2, newValue) {

            for (let i = row1; i <= row2; i++) { // row
                for (let j = col1; j <= col2; j++) { // col
                    this.rectangle[i][j] = newValue;
                };
            };
        };

        SubrectangleQueries.prototype.getValue = function(row, col) {
            return this.rectangle[row][col];
        };
    };
};

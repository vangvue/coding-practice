// https://leetcode.com/problems/water-bottles/submissions/
// 1518. Water Bottles
//
// Given numBottles full water bottles,
// you can exchange numExchange empty water bottles for one full water bottle.
//
// The operation of drinking a full water bottle turns it into an empty bottle.
//
// Return the maximum number of water bottles you can drink.

var numWaterBottles = function(numBottles, numExchange) {
    let result = 0;
    let emptyBottles = 0;
    let fullBottles = numBottles;
    let totalBottles = numBottles;
    let counter = false;

    while (!counter) {
        result += fullBottles;
        emptyBottles = totalBottles % numExchange;
        fullBottles = Math.floor(totalBottles / numExchange);
        totalBottles = emptyBottles + fullBottles;
        if (totalBottles < numExchange) {
            counter = true;
            result += fullBottles;
        }
    }
    return result;
};

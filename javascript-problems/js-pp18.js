// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/submissions/
// 1475. Final Prices With a Special Discount in a Shop
//
// Given the array prices where prices[i] is the price of the ith item in a shop.
// There is a special discount for items in the shop, if you buy the ith item,
// then you will receive a discount equivalent to prices[j]
// where j is the minimum index such that j > i and prices[j] <= prices[i],
// otherwise, you will not receive any discount at all.
//
// Return an array where the ith element is the final price you will pay
// for the ith item of the shop considering the special discount.

var finalPrices = function(prices) {
    for(let i = 0; i < prices.length; i++) {
        for(let j = i + 1; j < prices.length; j++) {
            if(prices[i] >= prices[j]) {
                prices[i] = prices[i] - prices[j];
                break;
            }
        }
    }
    return prices;
};

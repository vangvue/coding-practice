// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// 121. Best Time to Buy and Sell Stock
//
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
//
// You want to maximize your profit by choosing a single day to buy one stock and choosing
// a different day in the future to sell that stock.
//
// Return the maximum profit you can achieve from this transaction.
// If you cannot achieve any profit, return 0.

var maxProfit = function(prices) {
    let cheapPrice = Infinity;
    let priceArr = [];

    for (let i = 0; i < prices.length; i++) {
        if (cheapPrice > prices[i]) { cheapPrice = prices[i] }
        if (cheapPrice < prices[i]) { priceArr.push(prices[i] - cheapPrice) }
    }

    if (priceArr.length === 0) { return 0 }
    return Math.max(...priceArr);
};

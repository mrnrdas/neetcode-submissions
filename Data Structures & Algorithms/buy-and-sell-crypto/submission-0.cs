public class Solution {
    public int MaxProfit(int[] prices) {
        // Initialize max profit and min price
        int maxProfit = 0;
        int minPrice = prices[0];
        
        // Loop through the prices
        for (int i = 1; i < prices.Length; i++) {
            // The current price is at the index
            int currPrice = prices[i];
            // Find the min price from the minimum of the current price and min price
            minPrice = Math.Min(minPrice, currPrice);
            // Find the max profit and currprice - min price
            maxProfit = Math.Max(maxProfit, currPrice - minPrice);
        }
        // Return the max profit
        return maxProfit;
    }
}

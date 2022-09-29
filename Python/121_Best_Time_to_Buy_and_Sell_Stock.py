"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class Solution:
    def maxProfit(self, prices):
        """
        Runtime: 1709 ms, faster than 54.79 % of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 25 MB, less than 38.22 % of Python3 online submissions for Best Time to Buy and Sell Stock.
        """
        if len(prices) == 1:
            return 0

        earning = 0
        minValue = prices[0]
        for i in range(len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            else:
                diff = prices[i] - minValue
                if diff > earning:
                    earning = diff
        return earning


if __name__ == "__main__":
    Solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]

    result = Solution.maxProfit(prices)
    print(f"My ans is: {result}\n")
    
    prices = [7, 6, 4, 3, 1]

    result = Solution.maxProfit(prices)
    print(f"My ans is: {result}\n")

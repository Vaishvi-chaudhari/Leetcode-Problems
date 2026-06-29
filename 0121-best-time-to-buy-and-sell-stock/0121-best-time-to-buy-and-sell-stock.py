class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            # curr_price = prices[i]
            curr_profit = prices[i] - buy_price
            if curr_profit > profit:
                profit = curr_profit
            buy_price = min(prices[i], buy_price)

        return profit
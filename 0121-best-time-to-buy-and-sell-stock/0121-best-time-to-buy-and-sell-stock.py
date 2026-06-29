class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            curr_profit = prices[i] - min_price
            if curr_profit > profit:
                profit = curr_profit
            min_price = min(prices[i], min_price)

        return profit
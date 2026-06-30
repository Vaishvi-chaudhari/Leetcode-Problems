class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m = len(accounts)
        n = len(accounts[0])

        max_wealth = 0
        for i in range(m):
            curr_wealth = 0

            for j in range(n):
                curr_wealth += accounts[i][j]
        
            max_wealth = max(max_wealth, curr_wealth)

        return max_wealth
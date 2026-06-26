class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        dig_sum = 0
        dig_prod = 1
        while n > 0:
            dig = n % 10
            dig_sum += dig
            dig_prod *= dig
            n //= 10
        return dig_prod - dig_sum
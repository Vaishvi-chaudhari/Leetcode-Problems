class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # num1 = 0
        # num2 = 0

        # for i in range(1, n + 1):
        #     if i % m == 0:
        #         num2 += i
        #     else:
        #         num1 += i

        # return num1 - num2

        total = n * (n + 1) // 2
        k = n // m
        divisible_sum = m * (k * (k + 1) // 2)

        return total - 2 * divisible_sum
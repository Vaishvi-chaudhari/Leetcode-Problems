class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # for x in range(n+1):
        #     if n == 2 ** x:
        #         return True
        # return False
        if n == 1:
            return True
        if n == 0:
            return False

        while n%2 == 0:
            n = n // 2 # n //= 2
            if n == 1:
                return True
        return False


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # optimized -
        if n <= 0:
            return False
        while n!= 0 and n%2 == 0:
            n //= 2
        return n==1

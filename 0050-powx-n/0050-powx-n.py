class Solution(object):
    def findPow(self, x, n):
        if n == 0:
            return 1

        temp = self.findPow(x, n//2)
        if n % 2 == 0:
            return temp * temp
        return temp * temp * x

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n >= 0:
            return self.findPow(x, n)
        return 1/ self.findPow(x, n*(-1))

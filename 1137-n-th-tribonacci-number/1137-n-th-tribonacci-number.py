class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # using iterative way - 
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        t0, t1, t2 = 0, 1, 1

        for i in range(3, n+1):
            t3 = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = t3

        return t2
        

        # using recursion - 
        # if n == 0:
        #     return 0
        # if n == 1 or n == 2:
        #     return 1
        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
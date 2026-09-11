class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
            
        l, r = 1, x // 2
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2
            sq = mid * mid
            
            if sq == x:
                return mid
            elif sq < x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans


        # r = x
        # while r * r > x:
        #     r = (r + x // r) // 2
        # return r
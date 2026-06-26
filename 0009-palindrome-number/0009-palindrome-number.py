class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev = 0
        is_palindrome = False
        while temp > 0:
            dig = temp % 10
            rev = rev * 10 + dig 
            temp //= 10

        return rev == x

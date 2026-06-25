class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev = 0
        is_palindrome = False
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig 
            x //= 10
            
        return rev == temp
        
        # if (rev == temp):
        #     is_palindrome = True
        
        # return is_palindrome

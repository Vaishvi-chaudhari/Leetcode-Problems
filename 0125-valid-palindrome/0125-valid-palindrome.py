class Solution(object):
    def isAlphaNumeric(self, s):
        x = ord(s)
        if 97<=x<=122 or 65<=x<=90 or 48<=x<=57:
            return True
        return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if not self.isAlphaNumeric(s[l]):
                l+=1
            elif not self.isAlphaNumeric(s[r]):
                r-=1
            elif s[l] == s[r]:
                l+=1
                r-=1
            
            else:
                return False
        return True
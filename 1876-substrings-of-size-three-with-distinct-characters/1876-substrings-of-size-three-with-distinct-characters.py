class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        n = len(s)
        # We will take i, i-1 and i-2 so, i has to stop at (n-3) or n-2 included.
        for i in range(n-2):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i+2] != s[i]: # Good str found
                count += 1
        return count
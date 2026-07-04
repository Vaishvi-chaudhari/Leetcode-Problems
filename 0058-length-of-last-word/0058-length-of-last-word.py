class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = (s.strip()). split()
        s = len(s[-1])
        return s
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                if s[j] in temp:
                    break
                temp += s[j]
                if len(temp) > max_len:
                    max_len = len(temp)
        return max_len
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1] * 128
        left = 0
        ans = 0

        for right in range(len(s)):
            x = ord(s[right])
            if last[x] >= left:
                left = last[x] + 1
            last[x] = right
            ans = max(ans, right - left + 1)
            
        return ans

        # max_len = 0
        # for i in range(len(s)):
        #     temp = ""
        #     for j in range(i, len(s)):
        #         if s[j] in temp:
        #             break
        #         temp += s[j]
        #         if len(temp) > max_len:
        #             max_len = len(temp)
        # return max_len
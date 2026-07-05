class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for i in range(len(s)):
            if freq[ord(s[i]) - ord('a')] == 1:
                return i
        return -1

        # for i in range(len(s)):
        #     count = 0
        #     for j in range(len(s)):
        #         if s[i] == s[j]:
        #             count += 1
        #     if count == 1:
        #         return i
        # return -1

        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         return i
        # return -1
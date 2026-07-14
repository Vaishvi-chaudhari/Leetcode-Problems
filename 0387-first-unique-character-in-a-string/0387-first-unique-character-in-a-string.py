class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for i in range(len(s)):
        #     count = 0
        #     for j in range(len(s)):
        #         if s[i] == s[j]:
        #             count += 1
        #     if count == 1:
        #         return i
        # return -1

        # Optimal : Using Freq of each character -
        n = len(s)
        freq = {}

        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        for i in range(n):
            if freq[s[i]] == 1:
                return i
        return -1
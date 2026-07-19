class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1
        k = len(s1)

        for i in range(k):
            freq2[ord(s2[i]) - ord('a')] += 1
        if freq1 == freq2:
            return True

        for i in range(k, len(s2)):
            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i - k]) - ord('a')] -= 1
            if freq1 == freq2:
                return True

        return False
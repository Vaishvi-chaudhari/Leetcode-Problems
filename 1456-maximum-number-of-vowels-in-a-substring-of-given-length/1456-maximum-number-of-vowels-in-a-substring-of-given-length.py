class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        ans = 0

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if i >= k and s[i - k] in vowels:
                count -= 1
            ans = max(ans, count)

        return ans
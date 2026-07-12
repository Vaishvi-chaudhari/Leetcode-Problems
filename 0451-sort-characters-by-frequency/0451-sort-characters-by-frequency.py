class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = ""
        for ch, count in sorted_chars:
            ans += ch * count

        return ans
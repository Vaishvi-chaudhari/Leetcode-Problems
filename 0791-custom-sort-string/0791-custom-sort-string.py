class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        ans = []

        for ch in order:
            if ch in freq:
                ans.append(ch * freq[ch])
                del freq[ch]
        for ch, count in freq.items():
            ans.append(ch * count)

        return "".join(ans)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cuts = [i-1 for i in range(n+1)] 

        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                cuts[r+1] = min(cuts[r+1], cuts[l] + 1)
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                cuts[r+1] = min(cuts[r+1], cuts[l] + 1)
                l -= 1
                r += 1

        return cuts[n]
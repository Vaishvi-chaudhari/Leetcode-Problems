class Solution:
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        pos = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                pos.append(i)

        m = len(pos)
        if m % 2:
            return -1

        @lru_cache(None)
        def dfs(i, free):
            if i == m:
                return 0 if free == 0 else float('inf')

            ans = float('inf')
            if free:
                ans = min(ans, dfs(i + 1, 0))

            ans = min(ans, x + dfs(i + 1, 1))
            if i + 1 < m:
                ans = min(ans,
                          pos[i + 1] - pos[i] + dfs(i + 2, free))
            
            return ans
        return dfs(0, 0)
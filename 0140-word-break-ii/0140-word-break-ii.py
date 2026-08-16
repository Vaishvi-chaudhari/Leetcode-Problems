class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        words = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    for sub in dfs(end):
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            memo[start] = res
            return res
            
        return dfs(0)
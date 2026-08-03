class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                    
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return result
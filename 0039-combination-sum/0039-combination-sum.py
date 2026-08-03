class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(index, current, total):
            if total == target:
                result.append(current[:])
                return
            if index == len(candidates) or total > target:
                return

            current.append(candidates[index])
            backtrack(index, current, total + candidates[index])
            current.pop()
            backtrack(index + 1, current, total)

        backtrack(0, [], 0)
        return result
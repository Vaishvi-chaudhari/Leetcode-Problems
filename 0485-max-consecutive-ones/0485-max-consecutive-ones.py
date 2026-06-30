class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_ones = 0
        max_ones = 0

        for n in nums:
            if n == 1:
                curr_ones += 1
                max_ones = max(curr_ones, max_ones)
            else:
                curr_ones = 0
        return max_ones
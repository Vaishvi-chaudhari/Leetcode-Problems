class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 0
        max_len = 0
        first_occurrence = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 1:
                prefix += 1
            else:
                prefix -= 1
            if prefix in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix])
            else:
                first_occurrence[prefix] = i
        return max_len

        # n = len(nums)
        # max_len = 0
        # for i in range(n):
        #     zero = 0
        #     one = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             zero += 1
        #         else:
        #             one += 1
        #         if zero == one:
        #             max_len = max(max_len, j - i + 1)
        # return max_len
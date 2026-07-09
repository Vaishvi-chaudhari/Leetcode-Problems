class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = 0

        for i in range(n):
            total_sum += nums[i]

        left_sum = 0
        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

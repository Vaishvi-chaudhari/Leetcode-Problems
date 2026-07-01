class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        running_sum = 0
        prefix_sums = {0: 1} # sum=0 has occurred once before we start
        
        for num in nums:
            running_sum += num
            if running_sum - k in prefix_sums:
                count += prefix_sums[running_sum - k]
            prefix_sums[running_sum] = prefix_sums.get(running_sum, 0) + 1
        
        return count
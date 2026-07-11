class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        curr_min = nums[0]
        max_prod = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp = curr_max

            curr_max = max(num, num * curr_max, num * curr_min)
            curr_min = min(num, num * temp, num * curr_min)
            max_prod = max(max_prod, curr_max)

        return max_prod
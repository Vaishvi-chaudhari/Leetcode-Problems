class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        max_prod = [0] * n
        min_prod = [0] * n

        max_prod[0] = nums[0]
        min_prod[0] = nums[0]

        ans = nums[0]

        for i in range(1, n):

            max_prod[i] = max(
                nums[i],
                nums[i] * max_prod[i - 1],
                nums[i] * min_prod[i - 1]
            )

            min_prod[i] = min(
                nums[i],
                nums[i] * max_prod[i - 1],
                nums[i] * min_prod[i - 1]
            )

            ans = max(ans, max_prod[i])

        return ans
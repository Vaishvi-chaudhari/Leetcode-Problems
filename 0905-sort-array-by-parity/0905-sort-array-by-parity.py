class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        start = 0

        for i in range(n):
            if nums[i] %2 == 0:
                # Swap i and start
                temp = nums[start]
                nums[start] = nums[i]
                nums[i] = temp
                # move start to next element
                start += 1

        # return start-1
        return nums
        
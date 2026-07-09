class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        ans.append(nums[0])
        for i in range(1,len(nums)):
            prefixSum = ans[i-1] + nums[i]
            ans.append(prefixSum)
        return ans
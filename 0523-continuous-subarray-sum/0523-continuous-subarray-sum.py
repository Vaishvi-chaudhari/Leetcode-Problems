class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mp = {0: -1}
        prefixSum = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            remainder = prefixSum % k
            if remainder in mp:
                if i - mp[remainder] >= 2:
                    return True
            else:
                mp[remainder] = i

        return False
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            parts = 1
            curr = 0

            for num in nums:
                if curr + num > mid:
                    parts += 1
                    curr = 0
                curr += num

            if parts <= k:
                r = mid
            else:
                l = mid + 1
        return l
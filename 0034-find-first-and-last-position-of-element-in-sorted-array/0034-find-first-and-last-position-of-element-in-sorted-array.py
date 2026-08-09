class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def lower_bound(x):
            l, r = 0, len(nums)

            while l < r:
                mid = (l + r) // 2

                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l

        first = lower_bound(target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = lower_bound(target + 1) - 1
        return [first, last]
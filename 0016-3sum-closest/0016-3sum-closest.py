class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest
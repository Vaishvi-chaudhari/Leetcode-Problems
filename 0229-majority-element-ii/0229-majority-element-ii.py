class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        ans = []
        count = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if count > n // 3:
                    ans.append(nums[i - 1])
                count = 1

        # Check last element
        if count > n // 3:
            ans.append(nums[-1])

        return ans
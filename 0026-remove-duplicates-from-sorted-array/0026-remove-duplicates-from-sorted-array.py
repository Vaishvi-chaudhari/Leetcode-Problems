class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        n = len(nums)

        for i in range(1,n):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]
            
        return start+1
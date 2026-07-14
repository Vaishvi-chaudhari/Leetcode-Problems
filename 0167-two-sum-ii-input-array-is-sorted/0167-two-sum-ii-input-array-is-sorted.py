class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n-1

        while left < right:
            sum = numbers[left] + numbers[right]

            if target < sum:
                right -= 1
            elif target > sum:
                left += 1
            else:
                # target = sum
                return [left+1, right+1] # We have to use : 1 based indexing!
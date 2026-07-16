class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_len = {}
        max_len = 0

        for num in nums:
            if num in curr_len:
                continue

            left = curr_len.get(num - 1, 0)
            right = curr_len.get(num + 1, 0)

            total = left + right + 1

            curr_len[num] = total
            curr_len[num - left] = total
            curr_len[num + right] = total

            max_len = max(max_len, total)
        return max_len
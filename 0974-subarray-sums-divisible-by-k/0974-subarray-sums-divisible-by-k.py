class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {0: 1}
        prefixSum = 0
        ans = 0

        for num in nums:
            prefixSum += num
            remainder = prefixSum % k
            remainder = (remainder + k) % k

            if remainder in freq:
                ans += freq[remainder]
            freq[remainder] = freq.get(remainder, 0) + 1

        return ans
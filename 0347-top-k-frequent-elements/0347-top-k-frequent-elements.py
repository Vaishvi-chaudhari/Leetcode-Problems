class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for num, count in sorted_freq:
            ans.append(num)
            if len(ans) == k:
                break
        return ans
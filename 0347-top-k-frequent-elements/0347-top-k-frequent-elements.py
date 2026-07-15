class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 01 Using : Sorting By Freq
        # freq = Counter(nums)
        # sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # ans = []
        # for num, count in sorted_freq:
        #     ans.append(num)
        #     if len(ans) == k:
        #         break
        # return ans

        # 02 : Using Min Heap / Priority Queue
        # Priority Queue (Min Heap) : Elements leave based on priority, not insertion order.
        freq = Counter(nums)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans
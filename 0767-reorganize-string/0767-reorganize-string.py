class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        heap = []
        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))

        ans = []
        while len(heap) > 1:
            count1, ch1 = heapq.heappop(heap)
            count2, ch2 = heapq.heappop(heap)
            ans.append(ch1)
            ans.append(ch2)
            count1 += 1
            count2 += 1

            if count1 != 0:
                heapq.heappush(heap, (count1, ch1))
            if count2 != 0:
                heapq.heappush(heap, (count2, ch2))

        if heap:
            count, ch = heapq.heappop(heap)
            if count != -1:
                return ""
            ans.append(ch)

        return "".join(ans)
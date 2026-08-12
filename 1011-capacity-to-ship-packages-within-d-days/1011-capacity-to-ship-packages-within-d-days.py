class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            d = 1
            curr = 0

            for w in weights:
                if curr + w > mid:
                    d += 1
                    curr = 0
                curr += w
            if d <= days:
                r = mid
            else:
                l = mid + 1

        return l
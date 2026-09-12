class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix = []
        s = 0
        for weight in w:
            s += weight
            self.prefix.append(s)
        self.total = s

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.random() * self.total
        l, r = 0, len(self.prefix) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.prefix[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
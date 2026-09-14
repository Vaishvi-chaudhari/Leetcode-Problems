class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, [])
        if not arr:
            return ""
            
        l, r = 0, len(arr) - 1
        ans = ""

        while l <= r:
            mid = l + (r - l) // 2
            t, v = arr[mid]
            if t <= timestamp:
                ans = v
                l = mid + 1 
            else:
                r = mid - 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
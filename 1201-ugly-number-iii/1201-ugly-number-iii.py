class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y):
            return x * y // math.gcd(x, y)

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)

        def count(mid):
            return (mid // a + mid // b + mid // c 
                    - mid // ab - mid // bc - mid // ac 
                    + mid // abc)

        low, high = 1, 2 * 10**9
        while low < high:
            mid = low + (high - low) // 2
            if count(mid) < n:
                low = mid + 1
            else:
                high = mid
        
        return low
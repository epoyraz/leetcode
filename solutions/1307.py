class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)

        def count(x):
            return (x // a) + (x // b) + (x // c) \
                 - (x // ab) - (x // bc) - (x // ac) \
                 + (x // abc)

        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if count(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left

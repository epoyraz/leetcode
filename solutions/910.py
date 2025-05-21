class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        from fractions import gcd
        MOD = 10**9 + 7
        lcm = a * b // gcd(a, b)

        left, right = 1, n * min(a, b)
        while left < right:
            mid = (left + right) // 2
            count = mid // a + mid // b - mid // lcm
            if count < n:
                left = mid + 1
            else:
                right = mid
        return left % MOD

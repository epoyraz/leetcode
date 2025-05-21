class Solution:
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)

        def enough(x):
            a = x - x // divisor1
            b = x - x // divisor2
            both = x - x // lcm
            return a >= uniqueCnt1 and b >= uniqueCnt2 and both >= uniqueCnt1 + uniqueCnt2

        left, right = 1, 10**18
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left

import math

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # If you ever have at least two elements, there's always
        # a valid subarray of length 2 (since a*b = gcd(a,b)*lcm(a,b)).
        # So start with ans = 2.
        # (For completeness one could handle n<2, but constraints say n>=2.)
        ans = 2

        last = {}    # last[p] = most recent index in window where prime p appeared
        l = 0        # left end of our sliding window

        for r, val in enumerate(nums):
            # factor val into its distinct prime divisors
            x = val
            primes = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    primes.append(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                primes.append(x)

            # If any prime p reoccurs in our current window [l..r-1],
            # we must advance l past its last occurrence to keep
            # "no prime divides more than one element" for windows â¥3.
            for p in primes:
                if p in last and last[p] >= l:
                    l = last[p] + 1
                last[p] = r

            # Now [l..r] has no repeated primes.
            # If its length is â¥3, it's a valid âproduct-equivalentâ subarray.
            length = r - l + 1
            if length >= 3:
                ans = max(ans, length)

        return ans

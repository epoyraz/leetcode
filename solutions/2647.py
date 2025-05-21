import math

class Solution(object):
    def findValidSplit(self, nums):
        n = len(nums)
        if n < 2:
            return -1

        # 1) Find primes up to sqrt(max(nums))
        M = max(nums)
        limit = int(math.sqrt(M)) + 1
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        primes = []
        for i in range(2, limit + 1):
            if sieve[i]:
                primes.append(i)
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False

        # 2) Record first/last index for each prime factor
        first = {}
        last = {}
        for idx, v in enumerate(nums):
            x = v
            seen = set()
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    seen.add(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                seen.add(x)
            for p in seen:
                if p not in first:
                    first[p] = idx
                last[p] = idx

        # 3) Mark forbidden split-intervals via a difference array
        diff = [0] * (n + 1)
        for p in first:
            a, b = first[p], last[p]
            if a < b:
                diff[a] += 1
                diff[b] -= 1

        # 4) Prefix-sum and find smallest valid split i in [0..n-2]
        cover = 0
        for i in range(n - 1):
            cover += diff[i]
            if cover == 0:
                return i

        return -1

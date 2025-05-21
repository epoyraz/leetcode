from collections import defaultdict
import math

class Solution:
    def largestComponentSize(self, nums):
        parent = {}

        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        def get_factors(n):
            factors = set()
            i = 2
            while i * i <= n:
                if n % i == 0:
                    factors.add(i)
                    while n % i == 0:
                        n //= i
                i += 1
            if n > 1:
                factors.add(n)
            return factors

        for num in nums:
            factors = get_factors(num)
            for f in factors:
                union(num, f)

        count = defaultdict(int)
        for num in nums:
            root = find(num)
            count[root] += 1

        return max(count.values())

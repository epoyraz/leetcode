from collections import defaultdict
import math

class Solution:
    def canTraverseAllPairs(self, nums):
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False  # 1 has no prime factors and cannot connect to any other number

        n = len(nums)
        max_val = max(nums)
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for num in nums:
            parent[num] = num

        # Sieve for smallest prime factor
        spf = list(range(max_val + 1))
        for i in range(2, int(math.sqrt(max_val)) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_factors(x):
            factors = set()
            while x > 1:
                factors.add(spf[x])
                x //= spf[x]
            return factors

        factor_to_num = defaultdict(list)
        for num in nums:
            factors = get_factors(num)
            for f in factors:
                factor_to_num[f].append(num)

        for group in factor_to_num.values():
            for i in range(1, len(group)):
                union(group[0], group[i])

        root = find(nums[0])
        for num in nums:
            if find(num) != root:
                return False
        return True

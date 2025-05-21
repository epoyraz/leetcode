class Solution:
    def gcdSort(self, nums):
        import math
        from collections import defaultdict

        n = len(nums)
        A = max(nums)

        # 1) Build SPF (smallest prime factor) sieve up to A
        spf = list(range(A + 1))
        limit = int(A**0.5)
        for p in range(2, limit + 1):
            if spf[p] == p:
                step = p * p
                for multiple in range(step, A + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        # 2) Factorization using SPF
        def get_primes(x):
            s = set()
            while x > 1:
                p = spf[x]
                s.add(p)
                x //= p
            return s

        # 3) Union-Find on indices
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        prime_to_index = {}
        for i, v in enumerate(nums):
            for p in get_primes(v):
                if p in prime_to_index:
                    union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i

        # 4) Group indices by root
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        # 5) Compare multisets within each component
        sorted_nums = sorted(nums)
        for grp in groups.values():
            orig = sorted(nums[i] for i in grp)
            targ = sorted(sorted_nums[i] for i in grp)
            if orig != targ:
                return False

        return True

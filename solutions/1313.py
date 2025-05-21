from collections import defaultdict
import sys
sys.setrecursionlimit(1 << 20)

MOD = 10**9 + 7

class Solution:
    def waysToBuildRooms(self, prevRoom):
        n = len(prevRoom)
        tree = defaultdict(list)
        for child, parent in enumerate(prevRoom):
            if parent != -1:
                tree[parent].append(child)

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb_mod(n, k):
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        def dfs(node):
            total_size = 1
            total_ways = 1

            for child in tree[node]:
                size_c, ways_c = dfs(child)
                total_ways = total_ways * ways_c % MOD
                total_ways = total_ways * comb_mod(total_size + size_c - 1, size_c) % MOD
                total_size += size_c

            return total_size, total_ways

        return dfs(0)[1]

class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        
        # Build the 'powers' array: the list of 2^k for each set bit in n
        powers = []
        bit = 0
        temp = n
        while temp:
            if temp & 1:
                powers.append(1 << bit)
            bit += 1
            temp >>= 1
        
        # Build prefix products of powers
        m = len(powers)
        prefix = [0]*m
        prefix[0] = powers[0] % MOD
        for i in range(1, m):
            prefix[i] = prefix[i-1] * powers[i] % MOD
        
        # Precompute modular inverses of prefix[i]
        inv_prefix = [0]*m
        inv_prefix[-1] = pow(prefix[-1], MOD-2, MOD)
        # Then inv_prefix[i-1] = inv_prefix[i] * powers[i] % MOD
        for i in range(m-1, 0, -1):
            inv_prefix[i-1] = inv_prefix[i] * powers[i] % MOD
        
        # Answer queries
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                # prefix[r] / prefix[l-1]  mod = prefix[r] * inv_prefix[l-1]
                res = prefix[r] * inv_prefix[l-1] % MOD
                ans.append(res)
        
        return ans

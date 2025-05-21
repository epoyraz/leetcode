class Solution(object):
    def countKSubsequencesWithMaxBeauty(self, s, k):
        MOD = 10**9 + 7
        
        # 1) Compute frequencies of each letter
        from collections import Counter
        freq = list(Counter(s).values())   # up to 26 entries
        D = len(freq)
        if k > D:
            return 0
        
        # 2) Sort descending
        freq.sort(reverse=True)
        t = freq[k-1]                      # threshold frequency
        greater = sum(1 for x in freq if x > t)
        needed = k - greater
        totalT = sum(1 for x in freq if x == t)
        
        # 3) Product of all frequencies > t
        prod_higher = 1
        for x in freq:
            if x > t:
                prod_higher = prod_higher * x % MOD
        
        # 4) Precompute small factorials for combinations up to 26
        maxN = 26
        fact = [1] * (maxN + 1)
        inv = [1] * (maxN + 1)
        for i in range(1, maxN + 1):
            fact[i] = fact[i-1] * i % MOD
        inv[maxN] = pow(fact[maxN], MOD-2, MOD)
        for i in range(maxN, 0, -1):
            inv[i-1] = inv[i] * i % MOD
        
        # nCk function
        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv[r] % MOD * inv[n-r] % MOD
        
        # 5) Compute the final answer
        #    Choose which of the "t"-frequency letters: C(totalT, needed)
        #    Multiply by t^needed, and by product of higher freqs.
        ways = comb(totalT, needed)
        ways = ways * pow(t, needed, MOD) % MOD
        ans = prod_higher * ways % MOD
        
        return ans

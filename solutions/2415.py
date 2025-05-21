class Solution:
    def idealArrays(self, n, maxValue):
        MOD = 10**9 + 7
        
        # 1) Precompute divisors for each v in [1..maxValue]
        divisors = [[] for _ in range(maxValue+1)]
        for d in range(1, maxValue+1):
            for multiple in range(d, maxValue+1, d):
                divisors[multiple].append(d)
        
        # 2) Precompute factorials and inv factorials up to n
        fact = [1] * (n+1)
        inv_fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD
        
        def comb(a, b):
            # C(a, b) = 0 if b<0 or b>a
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a-b] % MOD
        
        # 3) DP over chain-length k
        # f_cur[v] = # of divisor-chains of length k ending at v
        f_cur = [1] * (maxValue+1)
        sum_chains = [0] * (n+1)
        sum_chains[1] = maxValue
        
        max_k = 1
        for k in range(2, n+1):
            f_next = [0] * (maxValue+1)
            total_k = 0
            for v in range(1, maxValue+1):
                s = 0
                for u in divisors[v]:
                    if u == v:
                        break
                    s += f_cur[u]
                if s:
                    s %= MOD
                    f_next[v] = s
                    total_k += s
            total_k %= MOD
            if total_k == 0:
                break
            sum_chains[k] = total_k
            max_k = k
            f_cur = f_next
        
        # 4) Combine chains with placements
        ans = 0
        for k in range(1, max_k+1):
            ans = (ans + sum_chains[k] * comb(n-1, k-1)) % MOD
        
        return ans

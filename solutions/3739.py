class Solution(object):
    def distanceSum(self, m, n, k):
        MOD = 10**9 + 7
        N = m * n
        
        # 1) Precompute factorials + inverse factorials up to N
        fac = [1] * (N + 1)
        for i in range(1, N + 1):
            fac[i] = fac[i - 1] * i % MOD
        
        invfac = [1] * (N + 1)
        invfac[N] = pow(fac[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            invfac[i - 1] = invfac[i] * i % MOD
        
        def comb(a, b):
            if b < 0 or b > a: 
                return 0
            return fac[a] * invfac[b] % MOD * invfac[a - b] % MOD
        
        # 2) How many arrangements include any fixed pair?  C(N-2, k-2)
        choose_pair = comb(N - 2, k - 2)
        
        # 3) Sum of |r1-r2| over all row-pairs and |c1-c2| over all column-pairs:
        #    sum_{i<j}(j-i) for L = L*(L-1)*(L+1)/6.
        inv6 = pow(6, MOD - 2, MOD)
        # row-contribution = n^2 * (m^3 - m) / 6
        row_term = (pow(m, 3, MOD) - m) % MOD
        sum_row = (n * n % MOD) * row_term % MOD * inv6 % MOD
        # col-contribution = m^2 * (n^3 - n) / 6
        col_term = (pow(n, 3, MOD) - n) % MOD
        sum_col = (m * m % MOD) * col_term % MOD * inv6 % MOD
        
        total_pair_dist = (sum_row + sum_col) % MOD
        
        # 4) Answer = choose_pair * total_pair_dist  (mod MOD)
        return choose_pair * total_pair_dist % MOD

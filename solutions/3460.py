class Solution(object):
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7
        
        # 1) Build C[L] = required inversions for prefix length L, or -1
        C = [-1] * (n+1)
        for endi, cnti in requirements:
            C[endi+1] = cnti
        
        # 2) Find max constraint M
        M = max(cnt for cnt in C if cnt >= 0)
        
        # 3) DP base: length 0 has exactly 0 inversions
        prev_dp = [1]        # dp[0][0] = 1
        prev_prefix = [1]    # prefix sums of prev_dp
        prevK = 0            # max k for L-1 = 0
        
        # 4) Build up to length n
        for L in range(1, n+1):
            # max inversions we care about at length L
            KL = min(L*(L-1)//2, M)
            dp = [0] * (KL + 1)
            
            # prefix sums of prev_dp up to prevK
            P = prev_prefix
            last_sum = P[-1]  # sum up to prevK
            
            # fill dp[L][k]
            for k in range(KL + 1):
                # total ways up to k in prev_dp
                if k <= prevK:
                    s1 = P[k]
                else:
                    s1 = last_sum
                # subtract ways above k-(L-1) to enforce i<=L-1
                if k >= L:
                    j = k - L
                    s2 = P[j] if j <= prevK else last_sum
                else:
                    s2 = 0
                dp[k] = (s1 - s2) % MOD
            
            # 5) enforce constraint if any
            c = C[L]
            if c >= 0:
                # if the required c > KL, impossible
                if c > KL:
                    return 0
                val = dp[c]
                # zero out everything except dp[c]
                dp = [0]*(KL+1)
                dp[c] = val
            
            # 6) build prefix sums for dp[L]
            prefix = [0] * (KL + 1)
            running = 0
            for k in range(KL + 1):
                running = (running + dp[k]) % MOD
                prefix[k] = running
            
            # move forward
            prev_dp = dp
            prev_prefix = prefix
            prevK = KL
        
        # 7) final answer is dp[n][C[n]] (there is always a constraint at L=n)
        return prev_dp[C[n]]

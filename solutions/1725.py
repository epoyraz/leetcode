class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        
        # dp_prev[i] will hold dp[j-1][i], initialized for j=0: dp[0][i] = 1
        dp_prev = [1] * n
        
        # prefix_prev[i] = sum(dp_prev[0..i]) mod MOD
        prefix_prev = [0] * n
        prefix_prev[0] = dp_prev[0]
        for i in range(1, n):
            prefix_prev[i] = (prefix_prev[i-1] + dp_prev[i]) % MOD
        
        # Build up from j=1 to j=k
        for _ in range(1, k+1):
            dp_cur = [0] * n
            # dp_cur[0] stays 0 for j>=1
            for i in range(1, n):
                # dp[j][i] = dp[j][i-1] + sum(dp[j-1][0..i-1])
                dp_cur[i] = dp_cur[i-1] + prefix_prev[i-1]
                if dp_cur[i] >= MOD:
                    dp_cur[i] %= MOD
            
            # Move current row into dp_prev and rebuild prefix
            dp_prev = dp_cur
            prefix_prev[0] = dp_prev[0]
            for i in range(1, n):
                prefix_prev[i] = (prefix_prev[i-1] + dp_prev[i]) % MOD
        
        # Answer is dp[k][n-1]
        return dp_prev[n-1]

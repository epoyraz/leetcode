class Solution(object):
    def numberOfWays(self, n, x, y):
        mod = 10**9 + 7
        k_max = min(n, x)
        
        # dp[j] = # ways to assign i performers to exactly j non-empty stages
        dp = [0] * (k_max + 1)
        dp[0] = 1  # with 0 performers, exactly 0 stages used
        
        for _ in range(1, n + 1):
            # process one more performer:
            # new_dp[j] = j * old_dp[j]               (assign to one of the j used stages)
            #           + (x - (j-1)) * old_dp[j-1]  (assign to one of the (x-(j-1)) unused stages)
            for j in range(k_max, 0, -1):
                dp[j] = (j * dp[j] + (x - j + 1) * dp[j-1]) % mod
            dp[0] = 0  # you can't have 0 used stages once at least one performer arrived
        
        # now dp[j] = # assignments with exactly j non-empty stages
        # each such assignment can be scored in y^j ways
        ans = 0
        pow_y = 1
        for j in range(1, k_max + 1):
            pow_y = pow_y * y % mod
            ans = (ans + dp[j] * pow_y) % mod
        
        return ans

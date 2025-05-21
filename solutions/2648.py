class Solution(object):
    def waysToReachTarget(self, target, types):
        MOD = 10**9 + 7
        # dp[s] = #ways to reach sum s using processed types
        dp = [0] * (target + 1)
        dp[0] = 1

        for count, val in types:
            new_dp = [0] * (target + 1)
            # for each achievable sum s so far...
            for s in xrange(target + 1):
                ways = dp[s]
                if ways:
                    # try taking k questions of this type, 0 <= k <= count
                    for k in xrange(count + 1):
                        t = s + k * val
                        if t > target:
                            break
                        new_dp[t] = (new_dp[t] + ways) % MOD
            dp = new_dp

        return dp[target]

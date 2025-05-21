class Solution(object):
    def sumOfPowers(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        # 1) build sorted unique list of all gaps
        D = []
        for i in range(n):
            for j in range(i+1, n):
                D.append(nums[j] - nums[i])
        D = sorted(set(D))
        m = len(D)
        
        # 2) Precompute, for each G = D[idx], how many k-subsequences
        #    have ALL adjacent diffs >= G.
        cnt_ge = [0] * (m + 1)  # we will leave cnt_ge[m] = 0
        import bisect
        
        for idx, G in enumerate(D):
            # dp[t][i]: ways to pick t elements ending at i
            dp = [[0]*n for _ in range(k+1)]
            # prefix sums of dp[t] for O(1) range sums
            prefix = [[0]*n for _ in range(k+1)]
            
            # base: t=1
            for i in range(n):
                dp[1][i] = 1
                prefix[1][i] = (prefix[1][i-1] + 1) if i>0 else 1
            
            # build up t = 2..k
            for t in range(2, k+1):
                for i in range(n):
                    # find largest j < i with nums[j] <= nums[i] - G
                    limit = nums[i] - G
                    j = bisect.bisect_right(nums, limit, 0, i) - 1
                    if j >= 0:
                        dp[t][i] = prefix[t-1][j]
                    # update prefix[t][i]
                    prefix[t][i] = (prefix[t][i-1] + dp[t][i]) if i>0 else dp[t][i]
            
            # total ways for t=k is sum dp[k][i]
            cnt = sum(dp[k][i] for i in range(n)) % MOD
            cnt_ge[idx] = cnt
        
        # 3) apply âdifferenceâ to get exact counts and sum up
        ans = 0
        for i in range(m):
            ways_exact = (cnt_ge[i] - cnt_ge[i+1]) % MOD
            ans = (ans + D[i] * ways_exact) % MOD
        
        return ans

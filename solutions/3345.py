class Solution(object):
    def sumOfPower(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # 1) DP[s][l] = #ways to pick subset of size l summing to s
        dp = [[0]*(k+1) for _ in range(k+1)]
        dp[0][0] = 1
        
        for x in nums:
            if x > k:
                continue
            # reverse to avoid reuse within same iteration
            for s in range(k, x-1, -1):
                for l in range(1, k+1):
                    dp[s][l] = (dp[s][l] + dp[s-x][l-1]) % MOD
        
        # 2) precompute powers of 2
        pow2 = [1]*(n+1)
        for i in range(1, n+1):
            pow2[i] = (pow2[i-1]*2) % MOD
        
        # 3) sum over all subsetâsizes l
        ans = 0
        for l in range(k+1):
            cnt = dp[k][l]
            if cnt:
                # each such subset T contributes 2^(n-l)
                ans = (ans + cnt * pow2[n-l]) % MOD
        
        return ans

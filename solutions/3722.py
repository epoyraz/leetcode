class Solution(object):
    def maxSum(self, nums, k, m):
        """
        :type nums: List[int]
        :type k: int
        :type m: int
        :rtype: int
        """
        n = len(nums)
        # prefix sums: prefix[i] = sum of nums[0..i-1]
        prefix = [0]*(n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        # dp[j][i]: maximum sum using j subarrays within first i elements
        # initialize with -inf for impossible states
        NEG_INF = -10**18
        dp = [[NEG_INF]*(n+1) for _ in range(k+1)]
        # zero subarrays gives sum 0
        for i in range(n+1):
            dp[0][i] = 0
        
        # fill dp
        for j in range(1, k+1):
            best_h = NEG_INF
            # for i < m, can't form j>=1 subarrays
            for i in range(1, n+1):
                # carry over: not ending a subarray at i
                dp[j][i] = dp[j][i-1]
                # update best_h when h = i-m
                if i-m >= 0:
                    # candidate h = i-m
                    val = dp[j-1][i-m] - prefix[i-m]
                    if val > best_h:
                        best_h = val
                # if we have a valid best_h, consider ending a subarray at i
                if best_h != NEG_INF:
                    candidate = prefix[i] + best_h
                    if candidate > dp[j][i]:
                        dp[j][i] = candidate
        
        return dp[k][n]

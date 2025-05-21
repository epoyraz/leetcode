class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        index = {x: i for i, x in enumerate(arr)}
        
        for i, x in enumerate(arr):
            dp[x] = 1
            for j in range(i):
                if x % arr[j] == 0 and (x // arr[j]) in dp:
                    dp[x] += dp[arr[j]] * dp[x // arr[j]]
        
        return sum(dp.values()) % MOD

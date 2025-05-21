class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        n = len(nums)
        # prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        # maxv[i][j] = max of nums[i..j]
        maxv = [[0]*n for _ in range(n)]
        for i in range(n):
            m = nums[i]
            maxv[i][i] = m
            for j in range(i+1, n):
                if nums[j] > m:
                    m = nums[j]
                maxv[i][j] = m

        def waste(i, j):
            length = j - i + 1
            return maxv[i][j] * length - (prefix[j+1] - prefix[i])

        max_seg = min(k+1, n)
        INF = 10**30
        dp = [[INF]*n for _ in range(max_seg+1)]
        # Base: one segment
        for i in range(n):
            dp[1][i] = waste(0, i)

        for seg in range(2, max_seg+1):
            for i in range(seg-1, n):
                best = INF
                for p in range(seg-2, i):
                    val = dp[seg-1][p] + waste(p+1, i)
                    if val < best:
                        best = val
                dp[seg][i] = best

        return dp[max_seg][n-1]

class Solution(object):
    def maxSizeSlices(self, slices):
        def maxSum(arr, k):
            n = len(arr)
            dp = [[0] * (k + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, k + 1):
                    # Either skip current slice or take it (must skip i-1)
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + arr[i - 1] if i >= 2 else arr[i - 1])
            return dp[n][k]

        k = len(slices) // 3
        # Case 1: exclude last slice
        case1 = maxSum(slices[:-1], k)
        # Case 2: exclude first slice
        case2 = maxSum(slices[1:], k)
        return max(case1, case2)

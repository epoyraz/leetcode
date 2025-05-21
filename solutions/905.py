class Solution(object):
    def lenLongestFibSubseq(self, arr):
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = {}
        max_len = 0

        for i in range(n):
            for j in range(i):
                k = index.get(arr[i] - arr[j], None)
                if k is not None and k < j:
                    dp[j, i] = dp.get((k, j), 2) + 1
                    max_len = max(max_len, dp[j, i])

        return max_len if max_len >= 3 else 0

class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [-1] * n  # dp[i] = max number of indices starting from i

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            best = 1  # can always stay at i
            # jump to the right
            for x in range(1, d+1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            # jump to the left
            for x in range(1, d+1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            dp[i] = best
            return best

        return max(dfs(i) for i in range(n))

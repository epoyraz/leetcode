class Solution(object):
    def longestPalindromicSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # Precompute minimal cost to pair s[i] and s[j]
        cost_pair = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                diff = abs(ord(s[i]) - ord(s[j]))
                cost_pair[i][j] = min(diff, 26 - diff)

        # dp[i][j][c] = max length of palindromic subsequence in s[i..j] with <= c operations
        # Initialize 3D DP array
        dp = [[[0] * (k+1) for _ in range(n)] for __ in range(n)]

        # Base case: single characters
        for i in range(n):
            for c in range(k+1):
                dp[i][i][c] = 1

        # Fill DP for substrings of increasing length
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                for c in range(k+1):
                    # Option 1: skip s[i]
                    dp[i][j][c] = dp[i+1][j][c]
                    # Option 2: skip s[j]
                    if dp[i][j-1][c] > dp[i][j][c]:
                        dp[i][j][c] = dp[i][j-1][c]
                    # Option 3: pair s[i] and s[j]
                    cost = cost_pair[i][j]
                    if c >= cost:
                        val = 2 + (dp[i+1][j-1][c-cost] if i+1 <= j-1 else 0)
                        if val > dp[i][j][c]:
                            dp[i][j][c] = val
        return dp[0][n-1][k]
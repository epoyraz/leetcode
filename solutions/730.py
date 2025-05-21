class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        # next_same[i]: the next index > i where s[i] occurs, or n if none
        # prev_same[i]: the previous index < i where s[i] occurs, or -1 if none
        next_same = [n] * n
        prev_same = [-1] * n
        last = {}
        # Build prev_same
        for i, ch in enumerate(s):
            if ch in last:
                prev_same[i] = last[ch]
            last[ch] = i
        last.clear()
        # Build next_same
        for i in range(n-1, -1, -1):
            ch = s[i]
            if ch in last:
                next_same[i] = last[ch]
            last[ch] = i
        
        # dp[i][j]: number of distinct non-empty palindromic subsequences in s[i..j]
        dp = [[0] * n for _ in range(n)]
        
        # Subsequences in a single letter
        for i in range(n):
            dp[i][i] = 1
        
        # Build up by lengths
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    # Exclude one end or the other, plus inclusion-exclusion
                    dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % MOD
                else:
                    # s[i] == s[j]
                    dp[i][j] = (dp[i+1][j-1] * 2) % MOD
                    L = next_same[i]
                    R = prev_same[j]
                    if L > R:
                        # No equal char inside
                        dp[i][j] = (dp[i][j] + 2) % MOD
                    elif L == R:
                        # One occurrence inside
                        dp[i][j] = (dp[i][j] + 1) % MOD
                    else:
                        # More than one inside: subtract the duplicates
                        dp[i][j] = (dp[i][j] - dp[L+1][R-1]) % MOD
        
        return dp[0][n-1] % MOD

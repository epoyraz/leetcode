class Solution(object):
    def strangePrinter(self, s):
        if not s:
            return 0
        
        # remove consecutive duplicate characters
        new_s = []
        for ch in s:
            if not new_s or new_s[-1] != ch:
                new_s.append(ch)
        s = ''.join(new_s)
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                dp[i][j] = dp[i+1][j] + 1
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
        
        return dp[0][n-1]

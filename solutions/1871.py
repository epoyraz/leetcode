class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        
        # Step 1: Precompute palindrome substrings
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        
        # Step 2: Try all split positions
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if dp[0][i - 1] and dp[i][j - 1] and dp[j][n - 1]:
                    return True
        return False

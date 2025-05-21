class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s = word1 + word2
        n = len(s)
        
        # Build DP for longest palindromic subsequence
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        res = 0
        len1 = len(word1)
        
        # Try matching characters between word1 and word2
        for i in range(len1):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    left = i
                    right = len1 + j
                    res = max(res, dp[left][right])
        
        return res

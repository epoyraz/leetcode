class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        # dp[i][j]: min ASCII delete sum to make s1[:i] and s2[:j] equal
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: delete all from one string to match empty other
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    cost1 = dp[i-1][j] + ord(s1[i-1])  # delete from s1
                    cost2 = dp[i][j-1] + ord(s2[j-1])  # delete from s2
                    dp[i][j] = min(cost1, cost2)
        
        return dp[m][n]

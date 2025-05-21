class Solution:
    def numMusicPlaylists(self, n, goal, k):
        MOD = 10**9 + 7
        
        # dp[i][j]: number of playlists of length i with j unique songs
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # Add a new unique song
                dp[i][j] += dp[i - 1][j - 1] * (n - (j - 1))
                dp[i][j] %= MOD
                # Replay an old song (but not one of the last k songs)
                if j > k:
                    dp[i][j] += dp[i - 1][j] * (j - k)
                    dp[i][j] %= MOD
        
        return dp[goal][n]

class Solution:
    def bestTeamScore(self, scores, ages):
        # Pair up and sort by age, then by score
        players = sorted(zip(ages, scores))
        n = len(players)
        
        # dp[i] = best score of a team ending with players[i]
        dp = [0] * n
        ans = 0
        
        for i in range(n):
            age_i, score_i = players[i]
            dp[i] = score_i
            # Try to extend any j < i whose score <= this player's score
            for j in range(i):
                _, score_j = players[j]
                if score_j <= score_i:
                    dp[i] = max(dp[i], dp[j] + score_i)
            ans = max(ans, dp[i])
        
        return ans

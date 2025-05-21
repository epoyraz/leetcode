class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        dp = [[(-1, 0) for _ in range(n)] for _ in range(n)]  # (max_score, path_count)
        dp[n - 1][n - 1] = (0, 1)  # Start at 'S'

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or dp[i][j][1] == 0:
                    continue

                for dx, dy in [(-1, 0), (0, -1), (-1, -1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != 'X':
                        val = 0 if board[ni][nj] in 'SE' else int(board[ni][nj])
                        current_score = dp[i][j][0] + val
                        if current_score > dp[ni][nj][0]:
                            dp[ni][nj] = (current_score, dp[i][j][1])
                        elif current_score == dp[ni][nj][0]:
                            dp[ni][nj] = (
                                dp[ni][nj][0],
                                (dp[ni][nj][1] + dp[i][j][1]) % MOD
                            )

        max_score, path_count = dp[0][0]
        return [0, 0] if path_count == 0 else [max_score, path_count]

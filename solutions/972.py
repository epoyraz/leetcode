class Solution:
    def knightDialer(self, n):
        MOD = 10**9 + 7

        # Knight move transitions for digits 0 through 9
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        dp = [1] * 10  # dp[i] = number of ways to end at digit i at step 1

        for _ in range(n - 1):
            next_dp = [0] * 10
            for i in range(10):
                for nei in moves[i]:
                    next_dp[nei] = (next_dp[nei] + dp[i]) % MOD
            dp = next_dp

        return sum(dp) % MOD

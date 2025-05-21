class Solution:
    def minimumDistance(self, word):
        # Precompute positions for 'A'-'Z'
        pos = [(i // 6, i % 6) for i in range(26)]
        # Add a dummy position for 'no finger' with zero move cost
        pos.append((-1, -1))  # index 26

        def dist(i, j):
            # If either finger is not placed yet, moving cost is 0
            if i == 26 or j == 26:
                return 0
            r1, c1 = pos[i]
            r2, c2 = pos[j]
            return abs(r1 - r2) + abs(c1 - c2)

        # Map characters in word to indices 0-25
        w = [ord(ch) - ord('A') for ch in word]

        # dp[a][b] = min cost with finger1 at a, finger2 at b
        INF = float('inf')
        dp = [[INF] * 27 for _ in range(27)]
        dp[26][26] = 0  # both fingers start unplaced

        for c in w:
            new_dp = [[INF] * 27 for _ in range(27)]
            for i in range(27):
                for j in range(27):
                    cost = dp[i][j]
                    if cost == INF:
                        continue
                    # Move finger1 to c
                    nc = cost + dist(i, c)
                    if nc < new_dp[c][j]:
                        new_dp[c][j] = nc
                    # Move finger2 to c
                    nc = cost + dist(j, c)
                    if nc < new_dp[i][c]:
                        new_dp[i][c] = nc
            dp = new_dp

        # result is minimum cost over all end states
        ans = min(dp[i][j] for i in range(27) for j in range(27))
        return ans

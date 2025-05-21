class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        NEG_INF = -10**18

        # Tables for suffixâmax, suffixâ2ndâmax, and "another max exists"
        m1 = [[0]*n for _ in range(m)]
        m2 = [[NEG_INF]*n for _ in range(m)]
        has_same = [[False]*n for _ in range(m)]

        # Build from bottomâright upward
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                v = grid[i][j]
                # Collect up to two top candidates from self, right, and down
                cand = [v]
                if j+1 < n:
                    cand.append(m1[i][j+1])
                    cand.append(m2[i][j+1])
                if i+1 < m:
                    cand.append(m1[i+1][j])
                    cand.append(m2[i+1][j])
                # Keep unique descending
                uniq = sorted(set(cand), reverse=True)
                m1[i][j] = uniq[0]
                m2[i][j] = uniq[1] if len(uniq) > 1 else NEG_INF

                # Mark if a child suffix also has m1 => another occurrence
                same = False
                if j+1 < n and m1[i][j+1] == m1[i][j]:
                    same = True
                if i+1 < m and m1[i+1][j] == m1[i][j]:
                    same = True
                has_same[i][j] = same

        # Now compute the best possible score over all valid starts
        ans = NEG_INF
        for i in range(m):
            for j in range(n):
                # must make at least one move
                if i == m-1 and j == n-1:
                    continue
                v = grid[i][j]
                if m1[i][j] > v:
                    score = m1[i][j] - v
                elif m1[i][j] == v and has_same[i][j]:
                    score = 0
                else:
                    score = m2[i][j] - v
                ans = max(ans, score)

        return ans

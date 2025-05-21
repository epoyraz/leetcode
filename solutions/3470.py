class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # U[j][i] = sum of grid[0..i-1][j]
        U = [[0]*(n+1) for _ in range(n)]
        for j in range(n):
            for i in range(1, n+1):
                U[j][i] = U[j][i-1] + grid[i-1][j]

        # dp_prev[p][c] = best score up through column j-1,
        # with r[j-2]=p and r[j-1]=c, where r[*]â[0..n]
        INF = -10**30
        dp_prev = [[INF]*(n+1) for _ in range(n+1)]
        # Base: column -1 has r[-1]=0, so for j=0 we only set dp_prev[0][c]=0
        for c in range(n+1):
            dp_prev[0][c] = 0

        # Transition for columns j=1..n-1
        for j in range(1, n):
            dp_curr = [[INF]*(n+1) for _ in range(n+1)]
            Ucol = U[j-1]  # prefix sums for column j-1

            # For each possible old âcurâ = r[j-1], build
            #   pm1[x] = max_{p â¤ x} dp_prev[p][cur]
            #   B2[p] = dp_prev[p][cur] + max(0, Ucol[p]-Ucol[cur])
            #   sm2[x] = max_{p â¥ x} B2[p]
            #
            # Then for each next r[j]=rn:
            #   delta1 = max(0, Ucol[rn]-Ucol[cur])
            #   best1 = pm1[rn] + delta1
            #   best2 = sm2[rn+1]
            #   dp_curr[cur][rn] = max(best1, best2)
            #
            for cur in range(n+1):
                # build pm1
                pm1 = [INF]*(n+1)
                m = INF
                for p in range(n+1):
                    if dp_prev[p][cur] > m:
                        m = dp_prev[p][cur]
                    pm1[p] = m
                # build B2 and its suffix max sm2
                B2 = [INF]*(n+1)
                for p in range(n+1):
                    delta = Ucol[p] - Ucol[cur]
                    if delta < 0:
                        delta = 0
                    B2[p] = dp_prev[p][cur] + delta
                sm2 = [INF]*(n+2)
                m2 = INF
                for p in range(n, -1, -1):
                    if B2[p] > m2:
                        m2 = B2[p]
                    sm2[p] = m2

                # fill dp_curr for this cur
                for rn in range(n+1):
                    # oneâcutâonly on prevâ¤rn
                    d1 = Ucol[rn] - Ucol[cur]
                    if d1 < 0:
                        d1 = 0
                    best1 = pm1[rn] + d1
                    # twoâcutâneeded region
                    best2 = sm2[rn+1]
                    dp_curr[cur][rn] = best1 if best1 > best2 else best2

            dp_prev = dp_curr

        # Finally, add contribution of the last column j = n-1,
        # where neighbor on the right is ânoneâ => r[n]=0
        Ulast = U[n-1]
        ans = 0
        for prev in range(n+1):
            for cur in range(n+1):
                base = dp_prev[prev][cur]
                if base < 0:
                    continue
                # M = max(prev, r[n]=0) = prev
                # add = max(0, Ulast[prev] - Ulast[cur])
                delta = Ulast[prev] - Ulast[cur]
                if delta > 0:
                    base += delta
                if base > ans:
                    ans = base

        return ans

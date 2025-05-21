class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]   # cost[i][j]: cost of edge (i in G1, j in G2)
        :rtype: int
        """
        m = len(cost)
        n = len(cost[0])
        full = (1 << n) - 1
        INF = 10**18

        # 1) Precompute cost_i[sub] = sum of cost[i][j] for j in bitmask sub
        cost_i = [ [0]*(1<<n) for _ in range(m) ]
        for i in range(m):
            for sub in range(1, 1<<n):
                lsb = sub & -sub
                j = (lsb.bit_length() - 1)
                cost_i[i][sub] = cost_i[i][sub ^ lsb] + cost[i][j]

        # 2) Precompute mincost_i[sub] = min(cost[i][j] for j in sub), â if sub==0
        mincost_i = [ [INF]*(1<<n) for _ in range(m) ]
        for i in range(m):
            mincost_i[i][0] = INF
            for sub in range(1, 1<<n):
                lsb = sub & -sub
                j = (lsb.bit_length() - 1)
                rest = sub ^ lsb
                mincost_i[i][sub] = min(cost[i][j], mincost_i[i][rest])

        # 3) DP over Group1 vertices
        dp_prev = [INF]*(1<<n)
        dp_prev[0] = 0

        for i in range(m):
            dp_new = [INF]*(1<<n)
            for prev_mask in range(1<<n):
                base = dp_prev[prev_mask]
                if base >= INF:
                    continue
                free = (~prev_mask) & full

                # (A) connect i to an already-covered j (if any),
                #     so mask stays prev_mask
                if prev_mask != 0:
                    dp_new[prev_mask] = min(
                        dp_new[prev_mask],
                        base + mincost_i[i][prev_mask]
                    )

                # (B) connect i to some non-empty subset of new nodes sub â free
                sub = free
                while sub:
                    newmask = prev_mask | sub
                    dp_new[newmask] = min(
                        dp_new[newmask],
                        base + cost_i[i][sub]
                    )
                    sub = (sub - 1) & free

            dp_prev = dp_new

        ans = dp_prev[full]
        return ans if ans < INF else -1

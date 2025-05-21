class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        INF = 10**18
        # adjacency list for quick iteration
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        # dp[node][time] = min cost to reach node in exactly 'time' minutes
        dp = [ [INF] * (maxTime + 1) for _ in range(n) ]
        dp[0][0] = passingFees[0]

        for t in range(maxTime + 1):
            for u in range(n):
                cost_u_t = dp[u][t]
                if cost_u_t == INF:
                    continue
                # try all outgoing roads
                for v, travel in adj[u]:
                    nt = t + travel
                    if nt <= maxTime:
                        c = cost_u_t + passingFees[v]
                        if c < dp[v][nt]:
                            dp[v][nt] = c

        # answer is min cost to reach city n-1 in any time <= maxTime
        res = min(dp[n-1])
        return res if res < INF else -1

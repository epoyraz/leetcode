class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency with weight w:
        # w = +1 if original edge u->v (reversal needed when rooting at v)
        # w = -1 if original edge v->u
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append((v, 1))
            adj[v].append((u, -1))
        
        # 1) Compute dp0: reversals needed when root = 0
        dp = [0]*n
        def dfs0(u, p):
            total = 0
            for v, w in adj[u]:
                if v == p:
                    continue
                # cost to orient edge for root=u is 1 if reverse needed, i.e. 
                # original direction is v->u, which gives w==-1
                total += (1 if w == -1 else 0)
                total += dfs0(v, u)
            return total
        
        dp[0] = dfs0(0, -1)
        
        # 2) Reroot DP
        def dfs1(u, p):
            for v, w in adj[u]:
                if v == p:
                    continue
                # dp[v] = dp[u] + w
                dp[v] = dp[u] + w
                dfs1(v, u)
        
        dfs1(0, -1)
        return dp

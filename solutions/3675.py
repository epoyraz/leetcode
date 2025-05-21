class Solution(object):
    def maximizeSumOfWeights(self, edges, k):
        """
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(10**7)

        n = len(edges) + 1
        # build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # dp[u] will be a pair (f0, f1):
        #   f0 = max total in subtree u if we DO NOT keep the edge up to u's parent
        #        â u may keep up to k edges to its children
        #   f1 = max total if we DO keep the edge up to its parent
        #        â u may keep up to (k-1) edges to its children
        def dfs(u, parent):
            base = 0
            gains = []
            # process children
            for v, w in adj[u]:
                if v == parent:
                    continue
                f0_v, f1_v = dfs(v, u)
                # if we cut uâv, we get f0_v
                base += f0_v
                # if we keep uâv, we get (f1_v + w) instead
                gains.append((f1_v + w) - f0_v)

            # sort descending by marginal gain of keeping that childâedge
            gains.sort(reverse=True)

            # helper to sum top t positive gains
            def top_sum(t):
                s = 0
                for i in range(min(t, len(gains))):
                    if gains[i] > 0:
                        s += gains[i]
                    else:
                        break
                return s

            # f0: no parentâedge kept â can keep up to k children
            f0 = base + top_sum(k)
            # f1: parentâedge is kept â can only keep up to k-1 children
            f1 = base + top_sum(k-1)

            return f0, f1

        # pick node 0 as root; we have no parentâedge, so the answer is f0(0)
        answer, _ = dfs(0, -1)
        return answer

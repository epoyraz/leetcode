class Solution(object):
    def maximumScoreAfterOperations(self, edges, values):
        n = len(values)
        # build adjacency
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # root at 0, build children lists via a BFS/DFS
        parent = [-1]*n
        parent[0] = 0
        order = [0]
        for u in order:
            for v in adj[u]:
                if parent[v] < 0:
                    parent[v] = u
                    order.append(v)

        children = [[] for _ in range(n)]
        for u in range(1, n):
            children[parent[u]].append(u)

        # dp0[u] = min total value of chosen R-nodes in subtree(u)
        #           so that every rootâleaf path in that subtree is hit,
        #           assuming no ancestor of u is in R.
        dp0 = [0]*n

        # process nodes in reverse BFS/DFS order (i.e. leaves first)
        for u in reversed(order):
            if not children[u]:
                # u is a leaf: must pick u
                dp0[u] = values[u]
            else:
                # Option1: pick u itself â cost = values[u]
                # Option2: don't pick u â sum costs of children
                cost_children = sum(dp0[v] for v in children[u])
                dp0[u] = min(values[u], cost_children)

        total = sum(values)
        # best score = total values - min cost of R
        return total - dp0[0]
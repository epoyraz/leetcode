import collections

class Solution:
    def collectTheCoins(self, coins, edges):
        """Return minimum number of edge-traversals needed to collect every coin
        (distance â¤ 2 collection) and come back to start.
        Greedy pruning described in LC 2603 editorial.
        Complexity O(n)."""
        n = len(coins)
        if sum(coins) == 0:
            return 0

        # Build adjacency list and degree array
        g = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            degree[u] += 1
            degree[v] += 1

        removed = [False] * n
        q = collections.deque()
        # 1) Prune all leaves having no coin (repeat until none left)
        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                removed[i] = True
                q.append(i)
        while q:
            u = q.popleft()
            for v in g[u]:
                if removed[v]:
                    continue
                degree[v] -= 1
                if degree[v] == 1 and coins[v] == 0:
                    removed[v] = True
                    q.append(v)

        # 2) Remove leaves twice (regardless of coin)
        for _ in range(2):
            leaves = [i for i in range(n) if not removed[i] and degree[i] == 1]
            for u in leaves:
                removed[u] = True
                for v in g[u]:
                    if not removed[v]:
                        degree[v] -= 1

        # 3) Count remaining edges; each traversed twice (out & back)
        remaining_edges = 0
        for u, v in edges:
            if not removed[u] and not removed[v]:
                remaining_edges += 1

        return remaining_edges * 2
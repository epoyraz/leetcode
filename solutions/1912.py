import heapq
from collections import defaultdict

class Solution(object):
    def countRestrictedPaths(self, n, edges):
        MOD = 10**9 + 7

        # Build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra from node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))

        # DFS + memoization to count restricted paths
        memo = [None] * (n + 1)
        def dfs(u):
            if u == n:
                return 1
            if memo[u] is not None:
                return memo[u]
            res = 0
            for v, _ in graph[u]:
                if dist[u] > dist[v]:
                    res = (res + dfs(v)) % MOD
            memo[u] = res
            return res

        return dfs(1)

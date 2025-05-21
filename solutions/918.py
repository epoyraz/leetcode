import heapq
from collections import defaultdict

class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]  # (distance, node)

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, cnt in graph[u]:
                nd = d + cnt + 1
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        reachable = sum(d <= maxMoves for d in dist)

        used = {}
        for u, v, cnt in edges:
            a = max(0, maxMoves - dist[u])
            b = max(0, maxMoves - dist[v])
            reachable += min(cnt, a + b)

        return reachable

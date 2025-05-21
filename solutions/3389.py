import heapq

class Solution(object):
    def minimumTime(self, n, edges, disappear):
        """
        :type n: int
        :type edges: List[List[int]]
        :type disappear: List[int]
        :rtype: List[int]
        """
        # Build adjacency list
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        INF = 10**30
        dist = [INF]*n
        dist[0] = 0
        
        # Min-heap of (time, node)
        pq = [(0, 0)]
        
        while pq:
            t, u = heapq.heappop(pq)
            # If this is stale or node already disappeared, skip
            if t > dist[u] or t >= disappear[u]:
                continue
            # Relax edges
            for v, w in g[u]:
                nt = t + w
                # Only if we can get to v *before* it disappears
                if nt < disappear[v] and nt < dist[v]:
                    dist[v] = nt
                    heapq.heappush(pq, (nt, v))
        
        # Build answer
        ans = []
        for i in range(n):
            if dist[i] < disappear[i]:
                ans.append(dist[i])
            else:
                ans.append(-1)
        return ans

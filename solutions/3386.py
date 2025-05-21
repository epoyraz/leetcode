import heapq

class Solution(object):
    def findAnswer(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[bool]
        """
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for idx, (u, v, w) in enumerate(edges):
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist
        
        # Distances from 0 and from n-1
        dist0 = dijkstra(0)
        distN = dijkstra(n-1)
        target = dist0[n-1]
        
        # If no path exists, none are on a shortest path
        if target == float('inf'):
            return [False] * len(edges)
        
        answer = []
        for u, v, w in edges:
            # Check either direction
            on_path = (
                dist0[u] + w + distN[v] == target or
                dist0[v] + w + distN[u] == target
            )
            answer.append(on_path)
        
        return answer

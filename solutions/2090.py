import heapq

class Solution(object):
    def countPaths(self, n, roads):
        mod = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)]  # (time, node)
        
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for nei, t in graph[node]:
                new_time = time + t
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (new_time, nei))
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % mod
        
        return ways[n - 1]

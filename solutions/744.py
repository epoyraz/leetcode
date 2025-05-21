import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        while heap:
            time, node = heapq.heappop(heap)
            for nei, wt in graph[node]:
                if time + wt < dist[nei]:
                    dist[nei] = time + wt
                    heapq.heappush(heap, (dist[nei], nei))
        
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1

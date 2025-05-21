import collections

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        dist = [float('inf')] * n
        dist[src] = 0
        queue = [(src, 0)]
        
        steps = 0
        while queue and steps <= k:
            next_dist = dist[:]
            for u, cost_u in queue:
                for v, price in graph[u]:
                    if cost_u + price < next_dist[v]:
                        next_dist[v] = cost_u + price
            dist = next_dist
            queue = [(i, dist[i]) for i in range(n) if dist[i] != float('inf')]
            steps += 1
        
        return -1 if dist[dst] == float('inf') else dist[dst]

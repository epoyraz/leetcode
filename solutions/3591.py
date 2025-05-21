import heapq

class Solution(object):
    def shiftDistance(self, s, t, nextCost, previousCost):
        # 1) build the cycle graph
        graph = [[] for _ in range(26)]
        for u in range(26):
            v1 = (u + 1) % 26
            graph[u].append((v1, nextCost[u]))
            v2 = (u - 1) % 26
            graph[u].append((v2, previousCost[u]))

        # 2) Dijkstra from each source u
        dist = [[float('inf')]*26 for _ in range(26)]
        for src in range(26):
            dist[src][src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[src][u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[src][v]:
                        dist[src][v] = nd
                        heapq.heappush(pq, (nd, v))

        # 3) sum up per-character minimum costs
        total = 0
        for cs, ct in zip(s, t):
            u = ord(cs) - ord('a')
            v = ord(ct) - ord('a')
            total += dist[u][v]
        return total

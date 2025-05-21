import heapq

class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        g  = [[] for _ in xrange(n)]   # forward graph
        rg = [[] for _ in xrange(n)]   # reversed graph (for paths *to* dest)
        for u, v, w in edges:
            g[u].append((v, w))
            rg[v].append((u, w))

        def dijkstra(start, graph):
            INF = 10 ** 20
            dist = [INF] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        INF = 10 ** 20
        d1 = dijkstra(src1, g)   # src1 -> *
        d2 = dijkstra(src2, g)   # src2 -> *
        dd = dijkstra(dest, rg)  # * -> dest  (by running on reversed graph)

        ans = INF
        for i in xrange(n):      # choose meeting node i
            if d1[i] < INF and d2[i] < INF and dd[i] < INF:
                ans = min(ans, d1[i] + d2[i] + dd[i])

        return -1 if ans == INF else ans

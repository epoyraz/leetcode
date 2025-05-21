import heapq

class Graph(object):
    def __init__(self, n, edges):
        """
        :param n: int, number of nodes 0..n-1
        :param edges: List[List[int]] initial edges [u,v,cost]
        """
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v, cost in edges:
            self.adj[u].append((v, cost))

    def addEdge(self, edge):
        """
        :param edge: List[int] [u, v, cost]
        """
        u, v, cost = edge
        self.adj[u].append((v, cost))

    def shortestPath(self, node1, node2):
        """
        :param node1: int
        :param node2: int
        :return: int shortest path cost or -1 if unreachable
        """
        n = self.n
        dist = [float('inf')] * n
        dist[node1] = 0
        heap = [(0, node1)]  # (cost, node)
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            if u == node2:
                return d
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        return -1
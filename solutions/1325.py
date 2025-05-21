import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        # Build graph
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        # Max-heap: store (-probability, node)
        heap = [(-1.0, start)]
        visited = [False] * n

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob

            if node == end:
                return prob

            if visited[node]:
                continue
            visited[node] = True

            for neighbor, edge_prob in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(heap, (-prob * edge_prob, neighbor))

        return 0.0

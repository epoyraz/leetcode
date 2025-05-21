from collections import deque

class Solution:
    def minMalwareSpread(self, graph, initial):
        def bfs(blocked):
            visited = set()
            q = deque()

            for node in initial:
                if node != blocked:
                    q.append(node)
                    visited.add(node)

            while q:
                u = q.popleft()
                for v in range(len(graph)):
                    if graph[u][v] == 1 and v not in visited and v != blocked:
                        visited.add(v)
                        q.append(v)
            return len(visited)

        initial.sort()
        min_infected = float('inf')
        result = initial[0]

        for node in initial:
            infected = bfs(node)
            if infected < min_infected:
                min_infected = infected
                result = node

        return result

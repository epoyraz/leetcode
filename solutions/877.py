from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        queue = deque()
        visited = set()

        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))  # (node, visited_mask, steps)
            visited.add((i, mask))

        target = (1 << n) - 1  # all nodes visited

        while queue:
            node, mask, steps = queue.popleft()
            if mask == target:
                return steps
            for nei in graph[node]:
                next_mask = mask | (1 << nei)
                if (nei, next_mask) not in visited:
                    visited.add((nei, next_mask))
                    queue.append((nei, next_mask, steps + 1))

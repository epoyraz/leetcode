from collections import deque, defaultdict

class Solution:
    def findShortestCycle(self, n, edges):
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        min_cycle = float('inf')

        for start in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = deque()
            dist[start] = 0
            q.append(start)

            while q:
                u = q.popleft()
                for v in g[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        # Found a cycle
                        cycle_len = dist[u] + dist[v] + 1
                        min_cycle = min(min_cycle, cycle_len)

        return min_cycle if min_cycle != float('inf') else -1

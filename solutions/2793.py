from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                q = deque([i])
                visited[i] = True
                nodes = [i]
                edge_set = set()

                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        edge = tuple(sorted((node, neighbor)))
                        edge_set.add(edge)
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            nodes.append(neighbor)
                            q.append(neighbor)

                v = len(nodes)
                e = len(edge_set)
                # Check if complete: there should be v*(v-1)//2 edges
                if e == v * (v - 1) // 2:
                    count += 1

        return count

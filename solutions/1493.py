class Solution(object):
    def frogPosition(self, n, edges, t, target):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)
        def dfs(node, time, prob):
            if time > t:
                return 0.0
            visited[node] = True
            unvisited_children = [nei for nei in graph[node] if not visited[nei]]
            if time == t or not unvisited_children:
                return prob if node == target else 0.0
            res = 0.0
            for nei in unvisited_children:
                res += dfs(nei, time + 1, prob / len(unvisited_children))
            return res

        return dfs(1, 0, 1.0)

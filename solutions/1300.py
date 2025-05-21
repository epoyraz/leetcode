class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n  # discovery times
        low = [-1] * n   # lowest reachable time
        res = []
        time = [0]

        def dfs(u, parent):
            disc[u] = low[u] = time[0]
            time[0] += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        res.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        dfs(0, -1)
        return res

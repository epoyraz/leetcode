from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        
        # Build the graph
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v
        
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0
            if x == y:
                return 1.0
            visited.add(x)
            for nei, val in graph[x].items():
                if nei not in visited:
                    res = dfs(nei, y, visited)
                    if res != -1.0:
                        return res * val
            return -1.0
        
        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        
        return results

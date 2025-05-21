class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        color = {}
        
        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            for nei in graph[node]:
                if not dfs(nei, 1 - c):
                    return False
            return True
        
        for i in range(n):
            if i not in color:
                if not dfs(i, 0):
                    return False
        return True

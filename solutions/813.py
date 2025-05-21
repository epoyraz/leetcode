class Solution(object):
    def allPathsSourceTarget(self, graph):
        res = []
        n = len(graph)
        
        def dfs(path, node):
            if node == n - 1:
                res.append(list(path))
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(path, nei)
                path.pop()
        
        dfs([0], 0)
        return res

class Solution(object):
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

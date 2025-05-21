class Solution:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        parent = list(range(n))

        # Union-Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Group nodes into connected components
        for i in range(n):
            for j in range(n):
                if graph[i][j]:
                    union(i, j)

        # Step 2: Count size of each component
        size = [0] * n
        for i in range(n):
            root = find(i)
            size[root] += 1

        # Step 3: Count malware in each component
        malware_count = [0] * n
        for node in initial:
            malware_count[find(node)] += 1

        # Step 4: Pick best node to remove
        result = None
        max_saved = -1
        for node in sorted(initial):
            root = find(node)
            if malware_count[root] == 1:
                if size[root] > max_saved:
                    max_saved = size[root]
                    result = node

        # If no node can reduce spread, return the one with smallest index
        return result if result is not None else min(initial)

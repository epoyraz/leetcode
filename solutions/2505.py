class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

class Solution:
    def numberOfGoodPaths(self, vals, edges):
        n = len(vals)
        # Group nodes by value
        val_nodes = {}
        for i, v in enumerate(vals):
            val_nodes.setdefault(v, []).append(i)
        # Sort unique values
        unique_vals = sorted(val_nodes.keys())
        # Prepare edges with weight = max(vals[u], vals[v])
        edges2 = []
        for u, v in edges:
            w = max(vals[u], vals[v])
            edges2.append((w, u, v))
        edges2.sort(key=lambda x: x[0])

        dsu = DSU(n)
        res = n  # each node itself is a good path
        ei = 0
        m = len(edges2)

        # Process values in ascending order
        for v in unique_vals:
            # Union all edges whose max-value <= current v
            while ei < m and edges2[ei][0] <= v:
                _, u, w = edges2[ei]
                dsu.union(u, w)
                ei += 1
            # Count nodes with value v in each component
            count = {}
            for node in val_nodes[v]:
                root = dsu.find(node)
                count[root] = count.get(root, 0) + 1
            # For each component, add combinations C(cnt, 2)
            for cnt in count.values():
                res += cnt * (cnt - 1) // 2

        return res

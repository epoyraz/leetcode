class Solution:
    def countPairs(self, n, edges):
        # Disjoint set union (union-find) with path compression and union by size
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # attach smaller tree to larger
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Build components
        for u, v in edges:
            union(u, v)

        # Gather component sizes by root
        comp_sizes = {}
        for i in range(n):
            r = find(i)
            comp_sizes[r] = comp_sizes.get(r, 0) + 1

        # For each component of size c, it has c*(n-c) unreachable pairs
        total = 0
        for c in comp_sizes.values():
            total += c * (n - c)

        # Each pair counted twice, so divide by 2
        return total // 2

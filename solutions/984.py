from collections import defaultdict

class Solution:
    def removeStones(self, stones):
        n = len(stones)
        parent = list(range(n))

        def find(x):
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        # Group stone indices by row and by column
        rows = defaultdict(list)
        cols = defaultdict(list)
        for i, (r, c) in enumerate(stones):
            rows[r].append(i)
            cols[c].append(i)

        # Union all stones in the same row
        for idxs in rows.values():
            first = idxs[0]
            for i in idxs[1:]:
                union(first, i)

        # Union all stones in the same column
        for idxs in cols.values():
            first = idxs[0]
            for i in idxs[1:]:
                union(first, i)

        # Count distinct connected components (unique roots)
        roots = {find(i) for i in range(n)}

        # We can remove all stones except one per component
        return n - len(roots)

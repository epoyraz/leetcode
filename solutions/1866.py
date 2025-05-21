class Solution(object):
    def restoreArray(self, adjacentPairs):
        from collections import defaultdict

        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Find an endpoint (only one neighbor)
        for num in adj:
            if len(adj[num]) == 1:
                start = num
                break

        # Step 3: Reconstruct the array of length n = len(adjacentPairs) + 1
        n = len(adjacentPairs) + 1
        res = [start]
        visited = set([start])

        while len(res) < n:
            last = res[-1]
            for neighbor in adj[last]:
                if neighbor not in visited:
                    res.append(neighbor)
                    visited.add(neighbor)
                    break

        return res

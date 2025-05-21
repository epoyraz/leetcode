class Solution:
    def isPossible(self, n, edges):
        # Build degree array and adjacency sets
        deg = [0] * (n + 1)
        adj = [set() for _ in range(n + 1)]
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            adj[u].add(v)
            adj[v].add(u)

        # Find nodes with odd degree
        odd = [i for i in range(1, n + 1) if deg[i] % 2]
        k = len(odd)

        # 0 odd: already all even
        if k == 0:
            return True
        # Only 2 or 4 odd nodes can be fixed with â¤2 edges
        if k not in (2, 4):
            return False

        # Case k == 2: try one edge or twoâedge workaround
        if k == 2:
            u, v = odd
            # If u and v not already connected, add (u,v)
            if v not in adj[u]:
                return True
            # Otherwise, look for a third node x unconnected to both
            forbidden = adj[u] | adj[v] | {u, v}
            return len(forbidden) < n

        # Case k == 4: try pairing the four odds in any way
        a, b, c, d = odd
        for x, y, p, q in [(a, b, c, d), (a, c, b, d), (a, d, b, c)]:
            if y not in adj[x] and q not in adj[p]:
                return True

        return False

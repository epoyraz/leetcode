class Solution(object):
    def constructGridLayout(self, n, edges):
        from collections import deque, defaultdict

        # build adjacency and degree
        adj = [[] for _ in range(n)]
        deg = [0]*n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # --- Case 1: it's a 1Ãn path if exactly two nodes have degree 1 ---
        if sum(1 for d in deg if d == 1) == 2:
            # find one endpoint
            start = next(i for i, d in enumerate(deg) if d == 1)
            path = [start]
            visited = {start}
            cur = start
            # walk the unique path
            while True:
                for nei in adj[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        path.append(nei)
                        cur = nei
                        break
                else:
                    break
            return [path]

        # --- Case 2: it's an rÃc rectangle ---
        # find the 4 corner-nodes (degree 2) and count degree-3 nodes
        corners = [i for i, d in enumerate(deg) if d == 2]
        k3 = sum(1 for d in deg if d == 3)

        # r + c = (k3 / 2) + 4, and r*c = n  â solve quadratic
        S = (k3 // 2) + 4
        D = S*S - 4*n
        sqrtD = int(D**0.5)
        # smaller root = r, larger = c
        r = (S - sqrtD)//2
        c = (S + sqrtD)//2

        # BFS from one corner u = (0,0)
        u = corners[0]
        du = [-1]*n
        q = deque([u]); du[u] = 0
        while q:
            v = q.popleft()
            for w in adj[v]:
                if du[w] < 0:
                    du[w] = du[v] + 1
                    q.append(w)

        # find the corner at distance c-1  â (0,c-1)
        corner_c = next((v for v in corners if v != u and du[v] == c-1), None)
        if corner_c is None:
            # maybe we guessed r,c swapped
            r, c = c, r
            corner_c = next(v for v in corners if v != u and du[v] == c-1)

        # BFS from corner_c
        d2 = [-1]*n
        q = deque([corner_c]); d2[corner_c] = 0
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d2[w] < 0:
                    d2[w] = d2[v] + 1
                    q.append(w)

        # assign each node to (y,x) in an rÃc grid
        grid = [[-1]*c for _ in range(r)]
        for v in range(n):
            # solve
            # du[v]   = x + y
            # d2[v]   = (c-1 - x) + y
            # â y = (du[v] + d2[v] - (c-1)) / 2
            y = (du[v] + d2[v] - (c - 1)) // 2
            x = du[v] - y
            grid[y][x] = v

        return grid

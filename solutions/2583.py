from collections import deque

class Solution(object):
    def magnificentSets(self, n, edges):
        # build adjacency list
        adj = [[] for _ in range(n+1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = [False] * (n+1)
        color = [0] * (n+1)
        ans = 0
        # process each connected component
        for u in range(1, n+1):
            if not visited[u]:
                # BFS to collect component and check bipartiteness
                comp = []
                q = deque([u])
                visited[u] = True
                color[u] = 0
                comp.append(u)
                while q:
                    x = q.popleft()
                    for y in adj[x]:
                        if not visited[y]:
                            visited[y] = True
                            color[y] = 1 - color[x]
                            q.append(y)
                            comp.append(y)
                        else:
                            if color[y] == color[x]:
                                return -1
                # compute diameter of this component
                diameter = 0
                for w in comp:
                    # BFS from w to get max distance
                    dist = {w: 0}
                    dq = deque([w])
                    while dq:
                        v = dq.popleft()
                        for nei in adj[v]:
                            if nei not in dist:
                                dist[nei] = dist[v] + 1
                                dq.append(nei)
                    diameter = max(diameter, max(dist.values()))
                # maximum groups from this component
                ans += diameter + 1
        return ans

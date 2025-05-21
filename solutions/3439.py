from collections import deque

class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        # Helper to compute (diameter, radius) of a tree given its edges
        def tree_diameter_and_radius(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            # BFS to find farthest node from `start`
            def bfs_farthest(start):
                dist = [-1]*n
                q = deque([start])
                dist[start] = 0
                far = start
                while q:
                    u = q.popleft()
                    for w in adj[u]:
                        if dist[w] == -1:
                            dist[w] = dist[u] + 1
                            q.append(w)
                            if dist[w] > dist[far]:
                                far = w
                return far, dist[far]
            
            # 1) from node 0 find some farthest node A
            A, _ = bfs_farthest(0)
            # 2) from A find farthest node B and its distance = diameter
            B, diameter = bfs_farthest(A)
            # radius = ceil(diameter / 2)
            radius = (diameter + 1) // 2
            return diameter, radius
        
        d1, r1 = tree_diameter_and_radius(edges1)
        d2, r2 = tree_diameter_and_radius(edges2)
        # best merged diameter
        return max(d1, d2, r1 + 1 + r2)

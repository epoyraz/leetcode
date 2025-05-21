class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True


class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        # Add original indices to edges
        for i in range(len(edges)):
            edges[i].append(i)
        
        # Sort by weight
        edges.sort(key=lambda x: x[2])

        # Kruskal's MST total weight
        def kruskal(n, edges, skip=-1, force=None):
            dsu = DSU(n)
            weight = 0
            if force:
                a, b, w, _ = force
                if dsu.union(a, b):
                    weight += w
            for i, (a, b, w, idx) in enumerate(edges):
                if i == skip:
                    continue
                if dsu.union(a, b):
                    weight += w
            # Check if all nodes are connected
            parent_set = set(dsu.find(x) for x in range(n))
            return weight if len(parent_set) == 1 else float('inf')

        base_weight = kruskal(n, edges)

        critical = []
        pseudo_critical = []

        for i, edge in enumerate(edges):
            # Check if it's critical (skip it â MST cost increases)
            if kruskal(n, edges, skip=i) > base_weight:
                critical.append(edge[3])
            # Check if it's pseudo-critical (force include â same MST)
            elif kruskal(n, edges, force=edge) == base_weight:
                pseudo_critical.append(edge[3])

        return [critical, pseudo_critical]

class Solution(object):
    def timeTaken(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        # 1) Build undirected adjacency
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # 2) Nodeâweights
        w = [1 if i % 2 else 2 for i in range(n)]
        
        # 3) Root at 0: extract parent/children with an explicit stack (preorder)
        parent = [-1]*n
        children = [[] for _ in range(n)]
        order = []  # preorder
        stack = [(0, -1)]
        while stack:
            v, p = stack.pop()
            parent[v] = p
            order.append(v)
            for u in adj[v]:
                if u == p: continue
                children[v].append(u)
                stack.append((u, v))
        
        # 4) Bottomâup: compute down[v], plus track top two childâcontributions
        down = [0]*n
        best1 = [0]*n   # largest (w[c]+down[c]) among children
        best2 = [0]*n   # second largest
        bestc = [-1]*n  # which child gives best1
        
        for v in reversed(order):
            b1 = b2 = 0
            bc = -1
            for c in children[v]:
                val = w[c] + down[c]
                if val > b1:
                    b2, b1, bc = b1, val, c
                elif val > b2:
                    b2 = val
            best1[v], best2[v], bestc[v] = b1, b2, bc
            down[v] = b1
        
        # 5) Topâdown: compute up[v]
        up = [0]*n
        for v in order:
            for c in children[v]:
                # best among siblings of c under parent v
                sib_best = best1[v] if bestc[v] != c else best2[v]
                up[c] = w[v] + max(up[v], sib_best)
        
        # 6) Answer = max(down, up) for each node
        return [max(down[i], up[i]) for i in range(n)]

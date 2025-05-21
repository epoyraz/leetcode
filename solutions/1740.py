class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1  # convert to 0-based
            v -= 1
            adj[u].append(v)
            adj[v].append(u)
        
        # Precompute all-pairs shortest path distances (BFS from each node)
        dist = [[0]*n for _ in range(n)]
        from collections import deque
        for src in range(n):
            dq = deque([src])
            seen = {src}
            d = 0
            # BFS layer by layer
            while dq:
                for _ in range(len(dq)):
                    u = dq.popleft()
                    dist[src][u] = d
                    for w in adj[u]:
                        if w not in seen:
                            seen.add(w)
                            dq.append(w)
                d += 1
        
        # Prepare answer array for diameters 1..n-1 (index 0..n-2)
        ans = [0] * (n-1)
        
        # Iterate over every non-empty subset of nodes via bitmask
        # We only care about subsets of size >= 2
        full = 1 << n
        for mask in range(full):
            # Quick skip if fewer than 2 bits set
            if mask & (mask - 1) == 0:
                # either 0 or 1 bit set
                continue
            
            # Extract nodes in this subset
            nodes = [i for i in range(n) if (mask >> i) & 1]
            
            # Check connectivity of the induced subgraph
            # BFS/DFS constrained to 'nodes'
            seen = {nodes[0]}
            stack = [nodes[0]]
            node_set = set(nodes)
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if w in node_set and w not in seen:
                        seen.add(w)
                        stack.append(w)
            if len(seen) != len(nodes):
                continue  # not connected
            
            # Compute diameter: max dist between any two in 'nodes'
            dmax = 0
            L = len(nodes)
            for i in range(L):
                u = nodes[i]
                for j in range(i+1, L):
                    v = nodes[j]
                    if dist[u][v] > dmax:
                        dmax = dist[u][v]
            
            # diameter dmax is between 1 and n-1
            if dmax > 0:
                ans[dmax-1] += 1
        
        return ans

class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        INF = 10**18
        # Build the base distance matrix (taking min over multiple edges)
        dist0 = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist0[i][i] = 0
        for u, v, w in roads:
            if w < dist0[u][v]:
                dist0[u][v] = w
                dist0[v][u] = w
        
        total = 0
        # Iterate over all subsets of nodes to close (bitmask of closed nodes)
        for mask in range(1<<n):
            # R = list of active nodes
            R = [i for i in range(n) if not (mask >> i & 1)]
            k = len(R)
            # If 0 or 1 active node, it's always valid
            if k <= 1:
                total += 1
                continue
            
            # Initialize distances in the induced subgraph to the precomputed values
            dist = [[INF]*n for _ in range(n)]
            for i in R:
                for j in R:
                    dist[i][j] = dist0[i][j]
            
            # FloydâWarshall on the active nodes only
            for kk in R:
                for i in R:
                    # early skip if dist[i][kk] already too large
                    dik = dist[i][kk]
                    if dik == INF: 
                        continue
                    for j in R:
                        newd = dik + dist[kk][j]
                        if newd < dist[i][j]:
                            dist[i][j] = newd
            
            # Check that every pair of active nodes is within maxDistance
            valid = True
            for i in R:
                for j in R:
                    if dist[i][j] > maxDistance:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                total += 1
        
        return total

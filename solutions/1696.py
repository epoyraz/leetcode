from collections import defaultdict, deque

class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        m, n = len(targetGrid), len(targetGrid[0])
        # find all colors
        colors = set()
        for row in targetGrid:
            for c in row:
                colors.add(c)
        
        # bounding box for each color: minr, maxr, minc, maxc
        INF = 10**9
        minr = {c: INF for c in colors}
        maxr = {c: -INF for c in colors}
        minc = {c: INF for c in colors}
        maxc = {c: -INF for c in colors}
        
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                if i < minr[c]: minr[c] = i
                if i > maxr[c]: maxr[c] = i
                if j < minc[c]: minc[c] = j
                if j > maxc[c]: maxc[c] = j
        
        # build graph: edge c -> d if c's rectangle covers a cell of color d!=c
        adj = defaultdict(set)
        indegree = {c: 0 for c in colors}
        
        for c in colors:
            for i in range(minr[c], maxr[c] + 1):
                for j in range(minc[c], maxc[c] + 1):
                    d = targetGrid[i][j]
                    if d != c and d not in adj[c]:
                        adj[c].add(d)
                        indegree[d] += 1
        
        # topological sort (Kahn's algorithm)
        q = deque([c for c in colors if indegree[c] == 0])
        processed = 0
        
        while q:
            u = q.popleft()
            processed += 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        # if all colors processed, no cycle
        return processed == len(colors)

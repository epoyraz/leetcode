import heapq

class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        """
        :type start: List[int]
        :type target: List[int]
        :type specialRoads: List[List[int]]
        :rtype: int
        """
        # Collect all key points: start, target, and both ends of each special road
        points = [tuple(start), tuple(target)]
        for x1, y1, x2, y2, c in specialRoads:
            points.append((x1, y1))
            points.append((x2, y2))
        # Deduplicate and index them
        pts = list(dict.fromkeys(points))
        idx = {p:i for i,p in enumerate(pts)}
        N = len(pts)
        
        # Build adjacency list
        adj = [[] for _ in range(N)]
        # 1) direct edges between every pair via Manhattan distance
        for i in range(N):
            x1,y1 = pts[i]
            for j in range(N):
                if i==j: continue
                x2,y2 = pts[j]
                cost = abs(x2-x1) + abs(y2-y1)
                adj[i].append((j, cost))
        # 2) override with special roads (directed)
        for x1,y1,x2,y2,c in specialRoads:
            u = idx[(x1,y1)]
            v = idx[(x2,y2)]
            adj[u].append((v, c))
        
        # Dijkstra from start to target
        src = idx[tuple(start)]
        dst = idx[tuple(target)]
        dist = [float('inf')] * N
        dist[src] = 0
        heap = [(0, src)]
        
        while heap:
            d,u = heapq.heappop(heap)
            if d>dist[u]: continue
            if u==dst:
                return d
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        return -1  # should never happen

# Example usage:
# sol = Solution()
# print(sol.minimumCost([1,1], [4,5], [[1,2,3,3,2],[3,4,4,5,1]]))  # 5

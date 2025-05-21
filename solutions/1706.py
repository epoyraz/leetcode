class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 1:
            return 0
        
        # Prim's algorithm in O(n^2) without explicitly building all edges
        in_mst = [False] * n
        # min_cost[i] = minimum cost to connect point i to the current MST
        min_cost = [float('inf')] * n
        min_cost[0] = 0  # start from point 0
        
        total_cost = 0
        
        for _ in range(n):
            # pick the next point u not in MST with smallest connection cost
            u = -1
            cheapest = float('inf')
            for i in range(n):
                if not in_mst[i] and min_cost[i] < cheapest:
                    cheapest = min_cost[i]
                    u = i
            
            # add u to MST
            in_mst[u] = True
            total_cost += cheapest
            
            # update the connection costs using u
            ux, uy = points[u]
            for v in range(n):
                if not in_mst[v]:
                    vx, vy = points[v]
                    cost = abs(ux - vx) + abs(uy - vy)
                    if cost < min_cost[v]:
                        min_cost[v] = cost
        
        return total_cost

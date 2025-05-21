import collections

class Solution:
    def minimumFuelCost(self, roads, seats):
        n = len(roads) + 1
        if n == 1:
            return 0
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS from root (0) to get parent and traversal order
        parent = [-1] * n
        order = []
        q = collections.deque([0])
        parent[0] = 0
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        
        # subtree_count[i] = number of representatives in the subtree rooted at i
        subtree_count = [1] * n
        fuel = 0
        
        # Process nodes in reverse BFS order (post-order)
        for u in reversed(order[1:]):  # skip the root at order[0]
            p = parent[u]
            cnt = subtree_count[u]
            # Number of car trips needed to move these cnt reps one edge up
            trips = (cnt + seats - 1) // seats
            fuel += trips
            # Add these reps to the parent's subtree count
            subtree_count[p] += cnt
        
        return fuel

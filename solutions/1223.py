class Solution:
    def areConnected(self, n, threshold, queries):
        # Disjoint Set Union (Union-Find) with path compression & union by rank
        parent = list(range(n+1))
        rank = [0] * (n+1)
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        
        # Connect all cities that share a divisor > threshold
        for z in range(threshold + 1, n + 1):
            # Union z with all its multiples > z
            multiple = 2*z
            while multiple <= n:
                union(z, multiple)
                multiple += z
        
        # Answer each query by checking if two cities have the same root
        ans = []
        for a, b in queries:
            ans.append(find(a) == find(b))
        return ans

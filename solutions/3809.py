class Solution(object):
    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(properties)
        # Convert each list to a set of distinct integers
        sets = [set(p) for p in properties]
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                # count intersection size
                if len(sets[i] & sets[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)
        
        # Count connected components via DFS
        seen = [False]*n
        def dfs(u):
            seen[u] = True
            for v in adj[u]:
                if not seen[v]:
                    dfs(v)
        
        components = 0
        for i in range(n):
            if not seen[i]:
                components += 1
                dfs(i)
        
        return components

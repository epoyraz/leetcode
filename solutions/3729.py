class Solution(object):
    def baseUnitConversions(self, conversions):
        """
        :type conversions: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        
        # There are n units, and conversions has length n-1
        n = len(conversions) + 1
        
        # Build adjacency list from source -> (target, factor)
        graph = [[] for _ in range(n)]
        for src, tgt, factor in conversions:
            graph[src].append((tgt, factor))
        
        # Prepare result array; ans[i] = # of unit i per 1 unit of type 0
        ans = [0] * n
        ans[0] = 1
        
        # DFS (or BFS) from 0, propagating the multiplicative factor
        stack = [0]
        while stack:
            u = stack.pop()
            for v, f in graph[u]:
                # A single unit of u equals ans[u] units of type-0;
                # so a single unit of v equals ans[u] * f units of type-0.
                ans[v] = ans[u] * f % MOD
                stack.append(v)
        
        return ans

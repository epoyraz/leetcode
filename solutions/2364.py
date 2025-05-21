class Solution:
    def longestPath(self, parent, s):
        n = len(parent)
        # Build children lists
        children = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p >= 0:
                children[p].append(i)
        
        # Get a postâorder of the tree via iterative DFS
        order = []
        stack = [(0, False)]
        while stack:
            u, visited = stack.pop()
            if visited:
                order.append(u)
            else:
                stack.append((u, True))
                for v in children[u]:
                    stack.append((v, False))
        
        dp = [1] * n   # dp[u] = longest downward path from u with adjacent chars â 
        ans = 1
        
        # Process nodes bottomâup
        for u in order:
            best1 = best2 = 0
            for v in children[u]:
                if s[v] != s[u]:
                    length = dp[v]
                    if length > best1:
                        best2 = best1
                        best1 = length
                    elif length > best2:
                        best2 = length
            # Combine two best childâpaths through u
            ans = max(ans, best1 + best2 + 1)
            # And store the best single chain from u upward
            dp[u] = best1 + 1
        
        return ans

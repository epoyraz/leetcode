class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        from collections import defaultdict, deque
        
        n = len(amount)
        # build tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # find parent of each node via BFS from root 0
        parent = [-1]*n
        q = deque([0])
        parent[0] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        
        # compute when Bob arrives at each node on his path to root
        INF = 10**18
        bobTime = [INF]*n
        t = 0
        u = bob
        while True:
            bobTime[u] = t
            if u == 0:
                break
            u = parent[u]
            t += 1
        
        # DFS from root to find best profit
        maxProfit = -10**30
        stack = [(0, -1, 0, 0)]  # node, parent, curSum, depth (time)
        
        while stack:
            u, p, curSum, depth = stack.pop()
            # determine Alice's gain at this node
            if bobTime[u] < depth:
                gain = 0
            elif bobTime[u] == depth:
                gain = amount[u] // 2
            else:
                gain = amount[u]
            
            curSum += gain
            
            # check if leaf
            is_leaf = (u != 0 and len(adj[u]) == 1)
            if is_leaf:
                maxProfit = max(maxProfit, curSum)
            else:
                for v in adj[u]:
                    if v == p:
                        continue
                    stack.append((v, u, curSum, depth+1))
        
        return maxProfit

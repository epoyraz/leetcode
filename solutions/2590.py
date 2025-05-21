class Solution(object):
    def maxStarSum(self, vals, edges, k):
        n = len(vals)
        # build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans = float('-inf')
        # for each node, pick up to k largest positive neighbor values
        for i in range(n):
            neigh_vals = [vals[j] for j in adj[i]]
            neigh_vals.sort(reverse=True)
            total = vals[i]
            for t in neigh_vals[:k]:
                if t > 0:
                    total += t
                else:
                    break
            ans = max(ans, total)
        return ans

class Solution:
    def maximumScore(self, scores, edges):
        n = len(scores)
        # Build undirected adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # For each node, keep its top k neighbors by score
        k = 3
        topn = [[] for _ in range(n)]
        for u in range(n):
            # sort neighbors of u descending by their scores
            nbrs = adj[u]
            nbrs.sort(key=lambda v: scores[v], reverse=True)
            # trim to top k
            topn[u] = nbrs[:k]
        
        best = -1
        
        # For each undirected edge, try both orientations as the central edge
        for u, v in edges:
            for b, c in ((u, v), (v, u)):
                # b is the second node, c is the third node
                for a in topn[b]:
                    if a == c:
                        continue
                    for d in topn[c]:
                        if d == b or d == a:
                            continue
                        total = scores[a] + scores[b] + scores[c] + scores[d]
                        if total > best:
                            best = total
        
        return best

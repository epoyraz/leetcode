class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        
        n = len(edges) + 1
        # build adjacency list: (neighbor, weight)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        res = [0] * n
        
        # for each server c, treat it as center:
        for c in range(n):
            branch_counts = []
            # explore each neighbor-subtree separately:
            for (nei, w0) in adj[c]:
                count = 0
                # stack holds (node, parent, dist_from_c)
                stack = [(nei, c, w0)]
                while stack:
                    u, p, dist = stack.pop()
                    # check divisibility
                    if dist % signalSpeed == 0:
                        count += 1
                    # go deeper
                    for v, w in adj[u]:
                        if v == p:
                            continue
                        stack.append((v, u, dist + w))
                branch_counts.append(count)
            
            # now sum up all unordered pairs between different branches
            total = 0
            prefix = 0
            for cnt in branch_counts:
                total += prefix * cnt
                prefix += cnt
            
            res[c] = total
        
        return res

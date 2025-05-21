from collections import deque

class Solution(object):
    def maxTargetNodes(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: List[int]
        """
        def build_adj(n, edges):
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def bfs_parities(adj):
            """
            Returns:
             - parity: list of 0/1 parities of depth from node 0
             - cnt0, cnt1: counts of nodes at parity 0 and 1
            """
            n = len(adj)
            parity = [-1]*n
            parity[0] = 0
            cnt0 = 1
            cnt1 = 0
            q = deque([0])
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if parity[w] == -1:
                        parity[w] = parity[u]^1
                        if parity[w] == 0:
                            cnt0 += 1
                        else:
                            cnt1 += 1
                        q.append(w)
            return parity, cnt0, cnt1

        # Build adjacency lists
        n = len(edges1) + 1
        m = len(edges2) + 1
        adj1 = build_adj(n, edges1)
        adj2 = build_adj(m, edges2)

        # BFS to get parities and counts
        p1, even1, odd1 = bfs_parities(adj1)
        p2, even2, odd2 = bfs_parities(adj2)

        # Precompute best possible contribution from tree2
        best2 = max(odd2, even2)

        # Now compute answer for each i in tree1
        ans = [0]*n
        diff1 = even1 - odd1
        for i in range(n):
            if p1[i] == 0:
                E1 = (n + diff1)//2
            else:
                E1 = (n - diff1)//2
            ans[i] = E1 + best2

        return ans

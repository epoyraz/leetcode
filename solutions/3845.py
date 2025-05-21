import sys
from collections import defaultdict

class Solution(object):
    def maxScore(self, n, edges):
        # Build adjacency
        G = [[] for _ in range(n)]
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)

        m = len(edges)
        is_cycle = (m == n)

        # 1) Extract the nodes in order:
        order = [0]*n
        if is_cycle:
            # pick node 0, then pick one neighbor to start
            start = 0
            nxt = G[start][0]
            order[0] = start
            order[1] = nxt
            for i in range(2, n):
                prev = order[i-2]
                cur  = order[i-1]
                # among neighbors of cur, pick the one that's not prev
                for w in G[cur]:
                    if w != prev:
                        order[i] = w
                        break
        else:
            # path: find a leaf (degree == 1)
            leaf = next(u for u in range(n) if len(G[u]) == 1)
            order[0] = leaf
            order[1] = G[leaf][0]
            for i in range(2, n):
                prev = order[i-2]
                cur  = order[i-1]
                # among neighbors, pick the one not prev
                for w in G[cur]:
                    if w != prev:
                        order[i] = w
                        break

        # 2) Build the optimal valueâassignment for path or cycle
        perm = [0]*n
        if not is_cycle:
            # path:  1,3,5,..., (odd ascending) then (even descending)
            k = (n + 1)//2  # number of odds
            for i in range(k):
                perm[i] = 2*i + 1
            for i in range(k, n):
                # i=k maps to the largest even: 2*(n-k)
                perm[i] = 2*(n - i)
        else:
            # cycle: [1] + [2,4,6,...,2*m] + [odd descending except 1]
            m_even = n//2
            perm[0] = 1
            # fill evens ascending
            for j in range(m_even):
                perm[1+j] = 2*(j+1)
            # build all odds, drop the '1', reverse, then fill
            odds = [2*i-1 for i in range(1, n-m_even+1)]  # this is [1,3,5,...]
            odds.pop(0)       # remove the leading 1
            odds.reverse()    # now descending [..,5,3]
            for j, val in enumerate(odds):
                perm[1 + m_even + j] = val

        # 3) Map back to nodes and sum edgeâproducts
        value = [0]*n
        for idx, node in enumerate(order):
            value[node] = perm[idx]

        total = 0
        for u, v in edges:
            total += value[u] * value[v]
        return total
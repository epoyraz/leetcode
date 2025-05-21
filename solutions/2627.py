from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

class Solution:
    def maxOutput(self, n, edges, price):
        # Build adjacency list
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        down1 = [0] * n       # best path sum starting at u going downward
        m1 = [0] * n          # largest child down1 value
        m2 = [0] * n          # second-largest child down1 value
        m1_child = [-1] * n   # which child gives m1

        # 1) Post-order DFS to compute down1, m1, m2, m1_child
        def dfs1(u, p):
            best1 = best2 = 0
            best_child = -1
            for v in g[u]:
                if v == p:
                    continue
                dfs1(v, u)
                val = down1[v]  # childâs best path from v
                if val > best1:
                    best2 = best1
                    best1 = val
                    best_child = v
                elif val > best2:
                    best2 = val
            m1[u], m2[u], m1_child[u] = best1, best2, best_child
            down1[u] = price[u] + best1

        dfs1(0, -1)

        up = [0] * n  # best path sum starting at u going upward (toward parent)
        up[0] = price[0]

        # 2) Pre-order DFS to compute up[v] using rerooting
        def dfs2(u, p):
            for v in g[u]:
                if v == p:
                    continue
                # best downward at u excluding subtree v
                if m1_child[u] == v:
                    best_down_excl = price[u] + m2[u]
                else:
                    best_down_excl = price[u] + m1[u]
                # best path from u that doesn't go into v
                best_from_u = max(up[u], best_down_excl)
                # up[v] = price[v] + best_from_u
                up[v] = price[v] + best_from_u
                dfs2(v, u)

        dfs2(0, -1)

        # 3) Compute answer: max over u of (max(down1[u], up[u]) - price[u])
        ans = 0
        for u in range(n):
            ecc = max(down1[u], up[u])
            ans = max(ans, ecc - price[u])
        return ans

from collections import defaultdict
import sys
sys.setrecursionlimit(10000)          # allow deep recursions (n â¤ 1000)

class Solution:
    def minimumScore(self, nums, edges):
        n = len(nums)

        # ------------- build adjacency -------------
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        subxor = nums[:]          # subtree xor
        tin    = [0] * n          # DFS entry time
        tout   = [0] * n          # DFS exit  time
        timer  = [0]              # mutable integer

        # -------- DFS: parent, subtree xor, Euler times --------
        def dfs(u, p):
            parent[u] = p
            tin[u] = timer[0]
            timer[0] += 1
            for v in g[u]:
                if v == p:
                    continue
                dfs(v, u)
                subxor[u] ^= subxor[v]
            tout[u] = timer[0]
            timer[0] += 1

        dfs(0, -1)
        total = subxor[0]

        def is_ancestor(a, b):
            """True if a lies on the path rootââ¦âb (a is ancestor of b)."""
            return tin[a] <= tin[b] and tout[b] <= tout[a]

        # Each edge is uniquely identified by its child node (parent[child] â  -1)
        children = [v for v in range(1, n)]    # node 0 has no parent edge

        best = float('inf')
        m = len(children)

        for i in range(m):
            u = children[i]        # first cut edge = (parent[u], u)
            Xu = subxor[u]

            for j in range(i + 1, m):
                v = children[j]    # second cut edge = (parent[v], v)
                Xv = subxor[v]

                if is_ancestor(u, v):          # u-subtree strictly contains v-subtree
                    comp1 = Xv
                    comp2 = Xu ^ Xv
                    comp3 = total ^ Xu
                elif is_ancestor(v, u):        # v-subtree strictly contains u-subtree
                    comp1 = Xu
                    comp2 = Xv ^ Xu
                    comp3 = total ^ Xv
                else:                          # two disjoint subtrees
                    comp1 = Xu
                    comp2 = Xv
                    comp3 = total ^ Xu ^ Xv

                diff = max(comp1, comp2, comp3) - min(comp1, comp2, comp3)
                best = min(best, diff)

        return best

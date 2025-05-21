class Solution(object):
    def treeQueries(self, root, queries):
        import sys
        sys.setrecursionlimit(10**7)

        # 1) Build children map and count nodes
        nodes = {}
        stack = [root]
        while stack:
            u = stack.pop()
            nodes[u.val] = u
            if u.left: stack.append(u.left)
            if u.right: stack.append(u.right)
        children = {v: [] for v in nodes}
        for v, u in nodes.items():
            if u.left:  children[v].append(u.left.val)
            if u.right: children[v].append(u.right.val)
        n = len(nodes)

        # 2) Euler tour + depths
        tin = [0]*(n+1)
        tout = [0]*(n+1)
        depth = [0]*(n+1)
        order = []
        t = [0]  # use list to allow mutation

        def dfs(u, d):
            tin[u] = t[0]
            order.append(u)
            depth[u] = d
            t[0] += 1
            for w in children[u]:
                dfs(w, d+1)
            tout[u] = t[0]-1

        dfs(root.val, 0)

        # 3) Segment tree for max depth over Euler positions
        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2*size)
        for i, u in enumerate(order):
            seg[size + i] = depth[u]
        for i in range(size-1, 0, -1):
            seg[i] = max(seg[2*i], seg[2*i+1])

        def query(l, r):
            if l > r:
                return 0
            res = 0
            l += size; r += size
            while l <= r:
                if l & 1:
                    res = max(res, seg[l])
                    l += 1
                if not (r & 1):
                    res = max(res, seg[r])
                    r -= 1
                l //= 2; r //= 2
            return res

        # 4) Answer queries by max outside the subtree interval
        ans = []
        for q in queries:
            L, R = tin[q], tout[q]
            m1 = query(0, L-1)
            m2 = query(R+1, n-1)
            ans.append(max(m1, m2))
        return ans

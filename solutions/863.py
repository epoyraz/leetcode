class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        from collections import defaultdict
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        res = [0] * n
        count = [1] * n

        def dfs(node, parent):
            for child in tree[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def dfs2(node, parent):
            for child in tree[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)
        return res

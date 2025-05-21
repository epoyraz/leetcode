from collections import deque

class Solution(object):
    def distanceK(self, root, target, k):
        parent = {}

        def dfs(node, par=None):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = deque([(target, 0)])  # <-- directly use target, NOT find it
        visited = set([target])
        res = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                res.append(node.val)
            if node:
                for nei in (node.left, node.right, parent.get(node)):
                    if nei and nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))

        return res

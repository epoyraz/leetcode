# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def canMerge(self, trees):
        # Map root value to tree root
        root_map = {t.val: t for t in trees}
        n = len(trees)

        # Compute indegree for each root based on child pointers
        indegree = {}
        for t in trees:
            for ch in (t.left, t.right):
                if ch and ch.val in root_map:
                    indegree[ch.val] = indegree.get(ch.val, 0) + 1

        # Identify the unique starting root (indegree 0)
        start = None
        for t in trees:
            if indegree.get(t.val, 0) == 0:
                if start is not None:
                    return None
                start = t
        if start is None:
            return None

        # Merge subtrees by attaching when encountering matching leaves
        used = set([start.val])
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                v = node.val
                if v in root_map and v not in used:
                    used.add(v)
                    sub = root_map[v]
                    node.left = sub.left
                    node.right = sub.right
            dfs(node.left)
            dfs(node.right)

        dfs(start)

        # All trees must be merged
        if len(used) != n:
            return None

        # Validate BST property and count nodes by inorder traversal
        prev = float("-inf")
        count = 0
        stack = []
        node = start
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= prev:
                return None
            prev = node.val
            count += 1
            node = node.right

        # Expected total nodes = sum of sizes minus (n-1) merges
        total_nodes = 0
        for t in trees:
            sz = 1
            if t.left: sz += 1
            if t.right: sz += 1
            total_nodes += sz
        total_nodes -= (n - 1)

        if count != total_nodes:
            return None

        return start

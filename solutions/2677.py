from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def replaceValueInTree(self, root):
        if not root:
            return None

        root.val = 0
        queue = deque([root])

        while queue:
            next_level = []
            child_sum = 0
            parent_map = {}

            for node in queue:
                if node.left:
                    next_level.append(node.left)
                    child_sum += node.left.val
                    parent_map[node.left] = node
                if node.right:
                    next_level.append(node.right)
                    child_sum += node.right.val
                    parent_map[node.right] = node

            sibling_sum = {}
            for child, parent in parent_map.items():
                if parent not in sibling_sum:
                    s = 0
                    if parent.left:
                        s += parent.left.val
                    if parent.right:
                        s += parent.right.val
                    sibling_sum[parent] = s

            for child in next_level:
                parent = parent_map[child]
                child.val = child_sum - sibling_sum[parent]

            queue = deque(next_level)

        return root
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root):
        node_map = defaultdict(list)
        queue = deque([(root, 0, 0)])  # (node, row, col)

        while queue:
            node, row, col = queue.popleft()
            node_map[col].append((row, node.val))
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        result = []
        for col in sorted(node_map.keys()):
            # Sort first by row, then by value
            col_nodes = sorted(node_map[col])
            result.append([val for row, val in col_nodes])
        return result

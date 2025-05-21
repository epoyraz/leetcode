from collections import deque

class Solution:
    def deepestLeavesSum(self, root):
        if not root:
            return 0

        queue = deque([root])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level_sum

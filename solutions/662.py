class Solution(object):
    def widthOfBinaryTree(self, root):
        from collections import deque
        max_width = 0
        queue = deque([(root, 0)])
        
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            for _ in range(level_length):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))
            if queue:
                max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            else:
                max_width = max(max_width, idx - first_index + 1)
        
        return max_width

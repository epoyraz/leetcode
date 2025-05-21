class Solution:
    def largestValues(self, root):
        if not root:
            return []
        
        from collections import deque
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            max_val = float('-inf')
            for _ in range(level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max_val)
        
        return result

class Solution(object):
    def averageOfLevels(self, root):
        from collections import deque
        res = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_sum * 1.0 / level_count)
        
        return res

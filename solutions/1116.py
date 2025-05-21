from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum = float('-inf')
        max_level = 1
        level = 1
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
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
        
        return max_level

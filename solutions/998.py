from collections import deque

class Solution:
    def isCompleteTree(self, root):
        queue = deque([root])
        end = False  # flag to indicate whether a null has been seen

        while queue:
            node = queue.popleft()
            if node is None:
                end = True
            else:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True

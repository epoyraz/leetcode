# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.val)

            # Push left first so that right is processed first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        # Reverse the result to get left -> right -> root
        return output[::-1]

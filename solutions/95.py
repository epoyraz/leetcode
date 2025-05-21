# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        def build_trees(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = build_trees(start, i - 1)
                right_trees = build_trees(i + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            return all_trees
        
        return build_trees(1, n)

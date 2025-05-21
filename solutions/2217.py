import sys
sys.setrecursionlimit(10**7)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getDirections(self, root, startValue, destValue):
        # Helper: return the path from root to target as a string of 'L'/'R'
        def getPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            # Try left
            path.append('L')
            if getPath(node.left, target, path):
                return True
            path.pop()
            # Try right
            path.append('R')
            if getPath(node.right, target, path):
                return True
            path.pop()
            return False
        
        path_s = []
        path_t = []
        # Fill path_s and path_t
        getPath(root, startValue, path_s)
        getPath(root, destValue, path_t)
        
        # Find common prefix length
        i = 0
        while i < len(path_s) and i < len(path_t) and path_s[i] == path_t[i]:
            i += 1
        
        # Steps up from start to LCA, then down to dest
        up_moves = 'U' * (len(path_s) - i)
        down_moves = ''.join(path_t[i:])
        return up_moves + down_moves

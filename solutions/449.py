# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def preorder(node):
            if not node:
                return []
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return ','.join(preorder(root))

    def deserialize(self, data):
        if not data:
            return None
        
        preorder = list(map(int, data.split(',')))
        self.i = 0
        
        def build(lower, upper):
            if self.i == len(preorder):
                return None
            val = preorder[self.i]
            if val < lower or val > upper:
                return None
            self.i += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node
        
        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
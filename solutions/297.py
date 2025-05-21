# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        tokens = []
        
        def dfs(node):
            if node is None:
                tokens.append('#')    # null marker
                return
            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(tokens)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        tokens = iter(data.split(','))
        
        def build():
            val = next(tokens)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        
        return build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree_str = ser.serialize(root)
# ans     = deser.deserialize(tree_str)
# return ans

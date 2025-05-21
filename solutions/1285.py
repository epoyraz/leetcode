class Solution(object):
    def balanceBST(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def build_balanced_tree(vals):
            if not vals:
                return None
            mid = len(vals) // 2
            node = TreeNode(vals[mid])
            node.left = build_balanced_tree(vals[:mid])
            node.right = build_balanced_tree(vals[mid+1:])
            return node

        sorted_vals = inorder(root)
        return build_balanced_tree(sorted_vals)

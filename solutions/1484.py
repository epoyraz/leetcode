class Solution(object):
    def isSubPath(self, head, root):
        def dfs_path_match(tree, list_node):
            if list_node is None:
                return True
            if tree is None or tree.val != list_node.val:
                return False
            return (dfs_path_match(tree.left, list_node.next) or 
                    dfs_path_match(tree.right, list_node.next))

        def dfs_search(tree):
            if tree is None:
                return False
            return (dfs_path_match(tree, head) or 
                    dfs_search(tree.left) or 
                    dfs_search(tree.right))

        return dfs_search(root)

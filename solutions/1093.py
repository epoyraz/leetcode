class Solution:
    def recoverFromPreorder(self, traversal):
        # Parse into list of (depth, value)
        nodes = []
        i = 0
        n = len(traversal)
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            nodes.append((depth, val))
        
        # Reconstruct tree
        root = TreeNode(nodes[0][1])
        stack = [root]
        for depth, val in nodes[1:]:
            # pop to parent depth
            while len(stack) > depth:
                stack.pop()
            node = TreeNode(val)
            parent = stack[-1]
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
            stack.append(node)
        
        return root

class Solution(object):
    def printTree(self, root):
        def getHeight(node):
            if not node:
                return -1
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        height = getHeight(root)
        m = height + 1
        n = (1 << (height + 1)) - 1
        res = [["" for _ in range(n)] for _ in range(m)]
        
        def dfs(node, r, c):
            if not node:
                return
            res[r][c] = str(node.val)
            if r < height:
                offset = 1 << (height - r - 1)
                dfs(node.left, r + 1, c - offset)
                dfs(node.right, r + 1, c + offset)
        
        dfs(root, 0, (n - 1) // 2)
        return res

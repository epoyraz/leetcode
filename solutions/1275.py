class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        parent = [0] * n

        # Step 1: Check for multiple parents
        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    if parent[child] == 1:
                        return False
                    parent[child] = 1

        # Step 2: Find root (node with no parent)
        roots = [i for i in range(n) if parent[i] == 0]
        if len(roots) != 1:
            return False
        root = roots[0]

        # Step 3: DFS to check for cycles and connectivity
        visited = set()

        def dfs(node):
            if node == -1:
                return True
            if node in visited:
                return False
            visited.add(node)
            return dfs(leftChild[node]) and dfs(rightChild[node])

        return dfs(root) and len(visited) == n

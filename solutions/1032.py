class Solution:
    def equationsPossible(self, equations):
        parent = [i for i in range(26)]  # Union-Find for 26 lowercase letters

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # First, process all "==" equations
        for eq in equations:
            if eq[1:3] == "==":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                union(x, y)

        # Then, process all "!=" equations and check for conflicts
        for eq in equations:
            if eq[1:3] == "!=":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if find(x) == find(y):
                    return False

        return True

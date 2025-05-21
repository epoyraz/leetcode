import sys
sys.setrecursionlimit(10**7)

class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        
        # Build original tree adjacency
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        # Initialize new_parent with original parent
        new_parent = parent[:]
        # Stacks to track the latest ancestor for each character
        stacks = [[] for _ in range(26)]

        # DFS to determine new_parent for each node
        def dfs(u):
            idx = ord(s[u]) - ord('a')
            # If an ancestor with same character exists, reattach
            if stacks[idx]:
                new_parent[u] = stacks[idx][-1]
            # Push current node onto its character's stack
            stacks[idx].append(u)
            # Recurse into children
            for v in children[u]:
                dfs(v)
            # Pop when backtracking
            stacks[idx].pop()

        # Run DFS from root (0)
        dfs(0)

        # Build final tree adjacency based on new_parent
        final_children = [[] for _ in range(n)]
        for i in range(1, n):
            p = new_parent[i]
            final_children[p].append(i)

        # Compute subtree sizes with iterative post-order traversal
        sizes = [0] * n
        stack = [(0, False)]  # (node, visited_flag)
        while stack:
            u, visited = stack.pop()
            if not visited:
                # Postpone processing until after children
                stack.append((u, True))
                for v in final_children[u]:
                    stack.append((v, False))
            else:
                # All children have been processed
                total = 1
                for v in final_children[u]:
                    total += sizes[v]
                sizes[u] = total

        return sizes

class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        n = len(nums)
        # Build children lists
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        # Find the node with genetic value 1 (if any)
        idx1 = -1
        for i, v in enumerate(nums):
            if v == 1:
                idx1 = i
                break

        # If there is no '1' in the entire tree, every subtree misses '1'
        if idx1 == -1:
            return [1] * n

        # Prepare answer (default = 1) and a seenâarray for marking values 1..n+1
        ans = [1] * n
        seen = [False] * (n + 2)
        mex = 1

        # Iterative DFS to mark an entire subtree rooted at u
        def dfs_mark(u):
            stack = [u]
            while stack:
                v = stack.pop()
                val = nums[v]
                if val <= n + 1 and not seen[val]:
                    seen[val] = True
                for w in children[v]:
                    stack.append(w)

        # Walk from idx1 up to the root, merging in each ancestor's subtree
        node = idx1
        came_from = None
        while node != -1:
            if came_from is None:
                # First step: mark the whole subtree of idx1
                dfs_mark(node)
            else:
                # Mark the ancestor's own value
                val = nums[node]
                if val <= n + 1 and not seen[val]:
                    seen[val] = True
                # Mark every siblingâsubtree of the pathâchild
                for c in children[node]:
                    if c != came_from:
                        dfs_mark(c)

            # Advance mex until we find the first unseen integer
            while mex <= n + 1 and seen[mex]:
                mex += 1
            ans[node] = mex

            came_from, node = node, parents[node]

        return ans

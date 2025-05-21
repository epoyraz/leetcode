from collections import deque

class Solution:
    def minimumOperations(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        q = deque([root])
        
        while q:
            level_size = len(q)
            level_vals = []
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # To sort this level by minimal swaps, find how many swaps
            # needed to transform level_vals into its sorted order.
            # This is the size minus number of cycles in the permutation.
            sorted_vals = sorted(level_vals)
            idx_map = {v: i for i, v in enumerate(level_vals)}
            visited = [False] * level_size
            for i in range(level_size):
                if visited[i] or level_vals[i] == sorted_vals[i]:
                    continue
                # traverse the cycle
                cycle_len = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    cycle_len += 1
                    # value that should be here:
                    correct_val = sorted_vals[j]
                    # find where that value currently is:
                    j = idx_map[correct_val]
                # to fix a cycle of length L, needs (L - 1) swaps
                ans += cycle_len - 1
            
            # update idx_map for next level?
            # Not needed, rebuilt each level
            
        return ans

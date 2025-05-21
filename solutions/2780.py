class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        Returns the minimum number of increments to equalize all root-to-leaf path sums.
        Perfect binary tree stored as 1-indexed: node i has children 2*i and 2*i+1.
        cost array is 0-indexed for nodes 1..n at cost[i-1].
        """
        # Use recursion with post-order traversal
        self.ans = 0
        # define dfs on 1-indexed node
        def dfs(i):
            # if leaf node
            left_idx = 2 * i
            if left_idx > n:
                # leaf: path sum from i down is cost[i-1]
                return cost[i-1]
            # internal node: compute children's max path sums
            right_idx = left_idx + 1
            left_sum = dfs(left_idx)
            right_sum = dfs(right_idx)
            # balance children by incrementing the smaller subtree
            if left_sum > right_sum:
                self.ans += left_sum - right_sum
            else:
                self.ans += right_sum - left_sum
            # return path sum from current node including the larger child's sum
            return cost[i-1] + max(left_sum, right_sum)

        dfs(1)
        return self.ans
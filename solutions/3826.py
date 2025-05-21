import collections

class Solution(object):
    def maxProfit(self, n, edges, score):
        """
        :type n: int
        :type edges: List[List[int]]
        :type score: List[int]
        :rtype: int
        """
        
        # predecessor_mask[i] will be a bitmask where the j-th bit is set 
        # if node j is a direct predecessor of node i.
        predecessor_mask = [0] * n
        for u, v_node in edges: # Renamed v to v_node for clarity
            predecessor_mask[v_node] |= (1 << u)
            
        # dp[mask] stores the maximum profit for the subset of nodes represented by 'mask'.
        # These nodes are arranged to fill the first popcount(mask) positions 
        # in a valid topological order.
        # Initialize with -1 to signify states not yet reached or not optimally reachable yet.
        # Since scores are positive (>=1), any valid profit will be non-negative.
        dp = [-1] * (1 << n)
        
        # Base case: for an empty set of nodes (mask 0), profit is 0.
        dp[0] = 0
        
        # Precompute popcounts for all masks.
        # popcounts[mask] stores the number of set bits (nodes) in 'mask'.
        popcounts = [0] * (1 << n)
        # For mask 0, popcount is 0 (already set by initialization).
        # For other masks:
        for i_mask_val in range(1, 1 << n):
            # The popcount of i_mask_val is popcount of (i_mask_val / 2) plus (i_mask_val % 2)
            # Using bitwise operations: popcounts[i_mask_val >> 1] + (i_mask_val & 1)
            popcounts[i_mask_val] = popcounts[i_mask_val >> 1] + (i_mask_val & 1)

        # Iterate through all masks. 'prev_mask' represents the set of nodes already processed.
        for prev_mask in range(1 << n):
            # If prev_mask is not a reachable state, skip.
            if dp[prev_mask] == -1:
                continue
            
            # The node to be added now will be placed at k_pos (1-based).
            # k_pos is the count of nodes in prev_mask + 1.
            k_pos = popcounts[prev_mask] + 1
            
            # Consider adding each node 'i_node' that is not already in prev_mask.
            for i_node in range(n):
                # Check if i_node is NOT in prev_mask using bitwise AND
                if not (prev_mask & (1 << i_node)):
                    # Check if all predecessors of i_node ARE in prev_mask.
                    # The condition (A | B) == B means A is a submask of B.
                    # Here, all bits set in predecessor_mask[i_node] must also be set in prev_mask.
                    if (predecessor_mask[i_node] | prev_mask) == prev_mask:
                        # If valid to add i_node:
                        # Form the new mask including i_node using bitwise OR.
                        current_mask = prev_mask | (1 << i_node)
                        # Calculate profit if i_node is added at k_pos.
                        profit_val = dp[prev_mask] + score[i_node] * k_pos
                        
                        # Update dp[current_mask] if this path yields higher profit.
                        if profit_val > dp[current_mask]:
                            dp[current_mask] = profit_val
                            
        # The final answer is the max profit for the set of all nodes.
        # This mask is (1 << n) - 1.
        return dp[(1 << n) - 1]
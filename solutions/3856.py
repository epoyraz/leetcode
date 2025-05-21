class Solution(object):
    def maxWeight(self, n, edges, k, t):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :type t: int
        :rtype: int
        """
        # Mask to keep bits [0..t-1]
        mask = (1 << t) - 1
        
        # dp_prev[u]: bitset of achievable sums at node u using exactly e edges
        dp_prev = [1] * n  # bit-0 = 1 => 0-sum reachable with 0 edges
        
        # If k=0, only sum=0 with zero edges; check if 0 < t
        if k == 0:
            return 0 if t > 0 else -1
        
        # Iterate edge-count from 1 to k
        for _ in range(1, k + 1):
            dp_cur = [0] * n
            for u, v, w in edges:
                # shift dp_prev[u] by w, clip to < t, OR into dp_cur[v]
                dp_cur[v] |= (dp_prev[u] << w) & mask
            dp_prev = dp_cur
        
        # Combine all endânode bitsets
        reachable = 0
        for bits in dp_prev:
            reachable |= bits
        
        # Remove bit-0 if no path at all? It's fine: if reachable==0, no sums.
        if reachable == 0:
            return -1
        
        # Highest set bit position is max achievable sum < t
        return reachable.bit_length() - 1

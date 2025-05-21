class Solution(object):
    def findPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Build cost matrix: cost[u][v] = |u - nums[v]|
        cost = [[0]*n for _ in range(n)]
        for u in range(n):
            for v in range(n):
                cost[u][v] = abs(u - nums[v])
        
        # We'll mask over vertices 1..n-1
        N = 1 << (n-1)
        INF = 10**12
        
        # dp[mask][u] = min cost of a path starting at u,
        # visiting all vertices in 'mask', then returning to 0.
        # mask runs 0..N-1, u runs 0..n-1, but dp[mask][u] only
        # valid when u not in mask (i.e. if u>=1 then bit u-1 of mask = 0).
        dp = [[INF]*n for _ in range(N)]
        
        # Base case: mask=0, no vertices to visit => just go u->0
        for u in range(n):
            dp[0][u] = cost[u][0]
        
        # Fill DP for all nonempty masks
        for mask in range(1, N):
            # Enumerate which vertices are still to visit (v in mask)
            m = mask
            verts = []
            while m:
                b = m & -m
                j = (b.bit_length() - 1)   # bit index in 0..n-2
                v = j + 1                  # actual vertex
                verts.append((b, v))
                m ^= b
            
            # Now for each "current" u not in mask, compute dp[mask][u]
            # u=0 is always allowed; for u>0 check bit u-1 of mask == 0.
            for u in range(n):
                if u > 0 and ((mask >> (u-1)) & 1):
                    continue
                best = INF
                # Try going u -> v, then finish mask\{v} from v
                for (b, v) in verts:
                    prev = dp[mask ^ b][v] + cost[u][v]
                    if prev < best:
                        best = prev
                dp[mask][u] = best
        
        full = N - 1
        # Minimum cycle cost starting & ending at 0:
        C = dp[full][0]
        
        # Reconstruct lexicographically smallest permutation
        perm = [0] * n
        perm[0] = 0
        curr = 0
        rem_cost = C
        mask = full
        
        for i in range(1, n):
            # Try next in ascending order
            for v in range(1, n):
                bit = 1 << (v-1)
                if mask & bit == 0:
                    continue
                # cost of edge curr->v plus optimal suffix from v
                c = cost[curr][v] + dp[mask ^ bit][v]
                if c == rem_cost:
                    # this is our lexicographically smallest choice
                    perm[i] = v
                    curr = v
                    mask ^= bit
                    rem_cost -= cost[perm[i-1]][v]
                    break
        
        return perm

import sys
sys.setrecursionlimit(10**7)

class Solution(object):
    def subtreeInversionSum(self, edges, nums, k):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # build tree
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        m = (k+1)*2  # number of DP states per node: d=0..k, p=0/1
        NEG_INF = -10**18
        
        def dfs(u, parent):
            # Initialize accumulators S0, S1 for children contributions:
            # S0[idx] = sum of best child contributions if we do NOT invert at u,
            # S1[idx] = sum if we DO invert at u.
            S0 = [0]*m
            S1 = [0]*m
            
            # process children
            for v in g[u]:
                if v == parent:
                    continue
                dp_child = dfs(v, u)  # length-m list
                # compute this child's contribution for every parent state (d,p)
                # we will add into S0 and S1
                f0 = [0]*m
                f1 = [0]*m
                for d in range(k+1):
                    for p in (0,1):
                        idx_par = d*2 + p
                        # if we do NOT invert at u: d_child = min(d+1, k), p_child = p
                        d0 = d+1 if d < k else k
                        idx0 = d0*2 + p
                        f0[idx_par] = dp_child[idx0]
                        # if we DO invert at u: allowed later; 
                        # for now compute d_child = 1, p_child = p^1
                        idx1 = 1*2 + (p^1)
                        f1[idx_par] = dp_child[idx1]
                # accumulate
                for i in range(m):
                    S0[i] += f0[i]
                    S1[i] += f1[i]
            
            # now build dp for u
            dp_u = [NEG_INF]*m
            for d in range(k+1):
                for p in (0,1):
                    idx = d*2 + p
                    # value at u itself under sel=0 or 1
                    val0 = nums[u]* (1 if p==0 else -1)
                    val1 = nums[u]* ( -1 if p==0 else 1)  # flip once
                    # sel = 0 (no inversion at u)
                    best = S0[idx] + val0
                    # sel = 1 (invert at u) only if d >= k
                    if d >= k:
                        best = max(best, S1[idx] + val1)
                    dp_u[idx] = best
            return dp_u
        
        # compute dp at root, starting with no inversion above => d=k, p=0
        dp0 = dfs(0, -1)
        return dp0[k*2 + 0]

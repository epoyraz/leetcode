class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        V = 300
        # best[val][d]: best length of subseq ending at value `val` with last diff = d
        best = [[0]*(V+1) for _ in range(V+1)]
        # best_max[val][d] = max(best[val][d], best[val][d+1], ..., best[val][V])
        best_max = [[0]*(V+1) for _ in range(V+1)]
        
        ans = 1  # a single element always gives length 1
        
        for a in nums:
            # Build updates for this a:
            upd = [0]*(V+1)
            # Try to transition from every possible previous value v=1..V
            for v in range(1, V+1):
                diff = abs(a - v)
                # best chain we can extend whose last diff >= diff
                prev_best = best_max[v][diff]
                # if prev_best==0, we start a new length-2 subseq (vâa)
                cand = prev_best + 1
                if cand > upd[diff]:
                    upd[diff] = cand
            
            # Merge the updates into best[a][*]
            for d in range(V+1):
                if upd[d] > best[a][d]:
                    best[a][d] = upd[d]
            
            # Recompute best_max[a][*] by scanning from high diffs downwards
            best_max[a][V] = best[a][V]
            for d in range(V-1, -1, -1):
                # either take best[a][d] itself or carry forward the max from d+1
                m = best[a][d]
                if best_max[a][d+1] > m:
                    m = best_max[a][d+1]
                best_max[a][d] = m
            
            # The best subsequence ending in `a` can be any diff >= 0
            if best_max[a][0] > ans:
                ans = best_max[a][0]
        
        return ans

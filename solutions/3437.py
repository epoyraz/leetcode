import bisect
from collections import Counter

class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        MOD = None  # not needed here, sums stay within Python int
        
        # 1) Build weight for each distinct damage value
        cnt = Counter(power)
        vals = sorted(cnt)
        m = len(vals)
        wt   = [v*cnt[v] for v in vals]
        
        # 2) DP array
        dp = [0]*m
        
        # Base case: either take the first value or not
        dp[0] = wt[0]
        
        for i in range(1, m):
            # Option A: skip vals[i]
            best = dp[i-1]
            
            # Option B: take vals[i]
            # find rightmost j < i with vals[j] <= vals[i]-3
            # bisect_right returns first index > (vals[i]-3), so minus one gives j
            threshold = vals[i] - 3
            j = bisect.bisect_right(vals, threshold, 0, i) - 1
            
            take = wt[i] + (dp[j] if j >= 0 else 0)
            dp[i] = max(best, take)
        
        return dp[-1]

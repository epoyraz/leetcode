class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # 1) Collect positions of '1'
        P = [i for i,ch in enumerate(s) if ch == '1']
        m = len(P)
        if m == 0:
            return 0
        
        ans = 0
        # 2) For each 1-indexed j=1..m, compute its gap_j
        #    and add j if gap_j > 0
        # gap_1 is zeros between P[0] and left boundary? No: it's between P[0] and nothing,
        # but we only use gaps to the right of each '1', so gap_j for j=1..m:
        #   gap_j is zeros to the right of the j-th one.
        for j in range(1, m+1):
            if j < m:
                gap = P[j] - P[j-1] - 1
            else:
                gap = (n - 1) - P[m-1]
            if gap > 0:
                ans += j
        
        return ans

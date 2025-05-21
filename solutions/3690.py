class Solution(object):
    def minLength(self, s, numOps):
        """
        :type s: str
        :type numOps: int
        :rtype: int
        """
        n = len(s)
        # Convert to ints 0/1 for speed
        arr = [1 if c=='1' else 0 for c in s]
        INF = 10**9

        # Check if it's possible to make all runs <= L with â¤ numOps flips
        def can(L):
            # dp0[r] = min flips to process up through i-1,
            # ending with a run of '0's of length r (1 â¤ r â¤ L)
            # dp1[r] similarly for '1'
            dp0 = [INF]*(L+1)
            dp1 = [INF]*(L+1)
            # Initialize at i=0:
            #   if we choose 0 at pos0: cost = (arr[0]!=0)
            dp0[1] = (arr[0] != 0)
            dp1[1] = (arr[0] != 1)

            for i in range(1, n):
                a = arr[i]
                new0 = [INF]*(L+1)
                new1 = [INF]*(L+1)
                # try placing '0' at i: cost_add = (a!=0)
                cost0 = (a != 0)
                for r in range(1, L+1):
                    c = dp0[r]
                    if c < INF:
                        # extend run of 0's to length r+1?
                        if r+1 <= L:
                            new0[r+1] = min(new0[r+1], c + cost0)
                    c = dp1[r]
                    if c < INF:
                        # switch from run of 1's to a new run of 0's of length 1
                        new0[1] = min(new0[1], c + cost0)

                # try placing '1' at i
                cost1 = (a != 1)
                for r in range(1, L+1):
                    c = dp1[r]
                    if c < INF:
                        if r+1 <= L:
                            new1[r+1] = min(new1[r+1], c + cost1)
                    c = dp0[r]
                    if c < INF:
                        new1[1] = min(new1[1], c + cost1)

                dp0, dp1 = new0, new1

            # At the end, if any dp0[r] or dp1[r] â¤ numOps, it's feasible
            best = min(min(dp0[1:]), min(dp1[1:]))
            return best <= numOps

        # Binary search for smallest L â [1..n] such that can(L) is True
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi)//2
            if can(mid):
                hi = mid
            else:
                lo = mid+1
        return lo

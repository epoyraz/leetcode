class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # dp0, dp1, dp2: # of records length i with 0 'A's ending in 0,1,2 consecutive 'L's
        dp0, dp1, dp2 = 1, 0, 0
        # ap0, ap1, ap2: # of records length i with 1 'A'  ending in 0,1,2 consecutive 'L's
        ap0, ap1, ap2 = 0, 0, 0

        for _ in range(n):
            # totals of previous states
            s0 = (dp0 + dp1 + dp2) % MOD
            s1 = (ap0 + ap1 + ap2) % MOD

            # extend the 0-A records by P or L (never A)
            ndp0 = s0            # append 'P' resets L-streak
            ndp1 = dp0           # append 'L' to a streak of 0 L's
            ndp2 = dp1           # append 'L' to a streak of 1 L

            # extend the 1-A records by P, L, or add the sole 'A' from a 0-A record
            nap0 = (s1 + s0) % MOD   # append 'P' to 1-A *or* append 'A' to 0-A
            nap1 = ap0              # append 'L' to a streak of 0 L's
            nap2 = ap1              # append 'L' to a streak of 1 L

            dp0, dp1, dp2 = ndp0, ndp1, ndp2
            ap0, ap1, ap2 = nap0, nap1, nap2

        # Sum all valid end-states
        return (dp0 + dp1 + dp2 + ap0 + ap1 + ap2) % MOD

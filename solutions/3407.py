class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9 + 7
        Z, O, L = zero, one, limit
        N = Z + O

        # We need counts of compositions of Z into k positive parts <=L
        # for k up to max zeroâblocks (=ceil(N/2)), and similarly for O.
        max_blocks = (N + 1) // 2  # worstâcase number of blocks of one type

        # Build dp0[b][s] = #ways to write sum=s with exactly b positive parts (each 1..L)
        # up to b=max_blocks and s up to Z.
        def build_dp(total):
            mb = max_blocks
            dp = [[0] * (total + 1) for _ in range(mb + 1)]
            dp[0][0] = 1
            for b in range(1, mb + 1):
                # prefix sums of dp[b-1] to get sliding window sums in O(1)
                pref = [0] * (total + 2)
                for s in range(total + 1):
                    pref[s+1] = (pref[s] + dp[b-1][s]) % MOD
                for s in range(total + 1):
                    # sum of dp[b-1][s - t] for t=1..L  â  pref[s] â pref[max(0, sâL)]
                    low = s - L
                    dp[b][s] = (pref[s] - (pref[low] if low >= 0 else 0)) % MOD
            return dp

        dp0 = build_dp(Z)
        dp1 = build_dp(O)

        ans = 0
        # Sum over start-bit s=0 or 1, and total blocks K=1..N
        for s in (0, 1):
            for K in range(1, N + 1):
                if s == 0:
                    zb = (K + 1) // 2
                    ob = K // 2
                else:
                    zb = K // 2
                    ob = (K + 1) // 2

                if zb <= max_blocks and ob <= max_blocks:
                    ans = (ans + dp0[zb][Z] * dp1[ob][O]) % MOD

        return ans

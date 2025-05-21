class Solution(object):
    def valueAfterKSeconds(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        total = (n - 1) + k
        r = k
        # Compute C(total, r) mod MOD in O(r log MOD)
        res = 1
        for i in range(1, r + 1):
            # multiply by (total - r + i) / i
            res = res * (total - r + i) % MOD
            res = res * pow(i, MOD - 2, MOD) % MOD
        return res

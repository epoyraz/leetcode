class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        # simple gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        m = len(coins)
        N = 1 << m

        # Precompute LCM for each nonempty subset
        lcm_mask = [1] * N
        for mask in range(1, N):
            lb = mask & -mask
            j = lb.bit_length() - 1
            prev = mask ^ lb
            l = lcm_mask[prev]
            c = coins[j]
            # lcm(l, c) = l // gcd(l,c) * c
            lcm_mask[mask] = l // gcd(l, c) * c

        # Count how many distinct multiples â¤ X via inclusion-exclusion
        def count_upto(X):
            total = 0
            for mask in range(1, N):
                l = lcm_mask[mask]
                if l <= X:
                    cnt = X // l
                    if bin(mask).count("1") & 1:
                        total += cnt
                    else:
                        total -= cnt
            return total

        # Binary search for the minimal X with count_upto(X) â¥ k
        lo, hi = 1, k * min(coins)
        while lo < hi:
            mid = (lo + hi) // 2
            if count_upto(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo

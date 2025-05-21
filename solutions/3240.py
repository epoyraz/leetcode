class Solution(object):
    def findMaximumNumber(self, k, x):
        """
        :type k: int
        :type x: int
        :rtype: int
        """
        # Accumulated price from 1..N
        def F(N):
            total = 0
            if N <= 0:
                return 0
            L = N.bit_length()
            # Sum over bitâpositions p = x, 2x, 3x, ... up to L
            p = x
            while p <= L:
                cycle = 1 << p          # 2^p
                half  = 1 << (p - 1)    # 2^(p-1)
                full  = (N + 1) // cycle
                rem   = (N + 1) % cycle
                # ones in full cycles plus any extra in the last (partial) cycle
                total += full * half + max(0, rem - half)
                p += x
            return total

        # 1) Find 'high' by doubling until F(high) > k
        low, high = 0, 1
        while F(high) <= k:
            low = high
            high <<= 1  # high *= 2

        # 2) Binaryâsearch the largest N in [0..high] with F(N) <= k
        while low < high:
            mid = (low + high + 1) // 2
            if F(mid) <= k:
                low = mid
            else:
                high = mid - 1

        return low

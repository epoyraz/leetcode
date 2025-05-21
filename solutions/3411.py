class Solution(object):
    def findProductsOfElements(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        # --------------------------------------------------------------------
        # 1) Helpers to compute, for a non-negative m, over all integers 1..m:
        #
        #    T(m) = sum_{i=1..m} popcount(i)
        #    B(m) = sum_{i=1..m} sum_{j: bit j in i} j
        #
        # We compute both by counting, for each bit position j separately,
        # how many numbers in [1..m] have that bit set.
        # --------------------------------------------------------------------
        def prefix_counts(m):
            """
            Returns (T, B), where
              T = total number of set bits in 1..m,
              B = total of bitâpositions (i.e. sum of j for each set bit j).
            If m=0, returns (0,0).
            """
            if m <= 0:
                return 0, 0

            T = 0
            B = 0
            # We'll go up to bit 60 (since m â¤ 10^15 < 2^50)
            bit = 0
            while (1 << bit) <= m:
                cycle = 1 << (bit + 1)
                full_cycles = (m + 1) // cycle
                rem = (m + 1) % cycle

                # In each full cycle, 2^bit ones in position `bit`.
                cnt = full_cycles * (1 << bit)
                # Plus the leftover in the partial cycle
                cnt += max(0, rem - (1 << bit))

                T += cnt
                B += cnt * bit
                bit += 1

            return T, B

        # --------------------------------------------------------------------
        # 2) Given N = number of entries of big_nums, 
        #    find sum of bitâpositions over big_nums[0..N-1].
        #
        # big_nums is formed by concatenating, for i=1,2,3,...,
        #    the list of powers-of-two (i.e. set bits) in i, in sorted order.
        #
        # Let T(m) = total count of bits in 1..m,
        #     B(m) = total of their bitâpositions.
        #
        # If we want the first N entries, we find the largest m so that
        #    T(m) â¤ N < T(m+1).
        # Those N entries consist of all bits from 1..m (contributing B(m)),
        # plus the first (N - T(m)) bits of (m+1), in ascending bit order.
        # --------------------------------------------------------------------
        def prefix_bitpos_sum(N):
            # sum of positions for big_nums[0..N-1]
            if N <= 0:
                return 0

            # Binary search m in [0..N], T(m) is monotonic increasing
            lo, hi = 0, N
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if prefix_counts(mid)[0] <= N:
                    lo = mid
                else:
                    hi = mid - 1
            m = lo
            Tm, Bm = prefix_counts(m)
            rem = N - Tm  # how many bits from (m+1)

            # collect the bitâpositions of (m+1):
            bits_of_next = []
            x = m + 1
            bit = 0
            while x:
                if x & 1:
                    bits_of_next.append(bit)
                bit += 1
                x >>= 1
            # they're naturally in ascending order of bit
            # take the first `rem` of them
            return Bm + sum(bits_of_next[:rem])

        # --------------------------------------------------------------------
        # 3) Now answer each query [L, R, mod]:
        #    product = â big_nums[L..R] mod mod.
        # But each big_nums entry is 2^j, so the product is
        #    2^(sum of bitâpositions over [L..R]),
        # and we do that power mod `mod`.
        # --------------------------------------------------------------------
        ans = []
        for L, R, m in queries:
            # prefix up to R+1 minus prefix up to L
            exp = prefix_bitpos_sum(R+1) - prefix_bitpos_sum(L)
            ans.append(pow(2, exp, m))
        return ans

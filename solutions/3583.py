class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        import bisect

        n = len(nums)
        M = max(nums)

        # 1) freq[x] = how many times x appears
        freq = [0] * (M + 1)
        for x in nums:
            freq[x] += 1

        # 2) c[d] = count of numbers divisible by d
        c = [0] * (M + 1)
        for d in range(1, M + 1):
            for m in range(d, M + 1, d):
                c[d] += freq[m]

        # 3) f[d] = total pairs (i<j) with both nums divisible by d
        f = [0] * (M + 1)
        for d in range(1, M + 1):
            if c[d] >= 2:
                f[d] = c[d] * (c[d] - 1) // 2

        # 4) g[d] = # pairs whose GCD is exactly d
        #    g[d] = f[d] - sum_{k>=2} g[k*d]
        g = [0] * (M + 1)
        for d in range(M, 0, -1):
            total = f[d]
            # subtract off multiples
            for k in range(2, (M // d) + 1):
                total -= g[d * k]
            g[d] = total

        # 5) build prefix sums of counts, so we can do order-statistic queries
        pref = [0] * (M + 1)
        running = 0
        for d in range(1, M + 1):
            running += g[d]
            pref[d] = running

        # 6) answer each query by binaryâsearching the smallest d with pref[d] > q
        ans = []
        for q in queries:
            # we want the first d so that pref[d] > q  (0-based indexing of sorted gcds)
            d = bisect.bisect_left(pref, q + 1, 1, M + 1)
            ans.append(d)

        return ans

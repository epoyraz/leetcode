class Solution(object):
    def maxValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        B = 1 << 7  # masks 0..127

        # forward DP: dpA[p][a] = set of OR-masks picking p from nums[0:a]
        dp_prev = [ {0} for _ in range(n+1) ]
        for p in range(1, k+1):
            dp_curr = [set() for _ in range(n+1)]
            dp_curr[0] = set()
            for a in range(1, n+1):
                # skip a-th
                dp_curr[a] = dp_curr[a-1].copy()
                # take a-th
                na = nums[a-1]
                for m in dp_prev[a-1]:
                    dp_curr[a].add(m | na)
            dp_prev = dp_curr
        dpA = dp_prev  # dpA[a] = all OR-masks for first half ending by index a

        # backward DP: dpB[p][a] = set of OR-masks picking p from nums[a-1:n]
        dp_prev = [ {0} for _ in range(n+2) ]
        for p in range(1, k+1):
            dp_curr = [set() for _ in range(n+2)]
            dp_curr[n+1] = set()
            for a in range(n, 0, -1):
                dp_curr[a] = dp_curr[a+1].copy()
                na = nums[a-1]
                for m in dp_prev[a+1]:
                    dp_curr[a].add(m | na)
            dp_prev = dp_curr
        dpB = dp_prev  # dpB[a] = all OR-masks for second half starting at index a

        # combine at every pivot t: pick k in [0..t-1] and k in [t..n-1]
        ans = 0
        for t in range(k, n - k + 1):
            A = dpA[t]
            Bset = dpB[t+1]
            # brute-force XOR over two small sets (â¤128 each)
            for m1 in A:
                for m2 in Bset:
                    v = m1 ^ m2
                    if v > ans:
                        ans = v
        return ans

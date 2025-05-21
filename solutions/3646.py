class Solution(object):
    def sumOfGoodSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        if not nums:
            return 0

        # Determine the maximum value in nums to size our DP arrays
        mx = max(nums)
        size = mx + 3  # +3 so we can safely access x+1

        # dp_count[v]: number of good subsequences ending with value v seen so far
        # dp_sum[v]: sum of all elements across those subsequences ending with v
        dp_count = [0] * size
        dp_sum   = [0] * size

        total = 0
        for x in nums:
            # Extend from x-1
            if x > 0:
                c1 = dp_count[x-1]
                s1 = dp_sum[x-1]
            else:
                c1 = 0
                s1 = 0

            # Extend from x+1
            c2 = dp_count[x+1]
            s2 = dp_sum[x+1]

            # Subsequences ending here:
            # 1) The singleton [x]
            # 2) Extend each subsequence ending in x-1 by appending x
            # 3) Extend each subsequence ending in x+1 by appending x
            new_count = (1 + c1 + c2) % MOD
            # The total sum contributed by those new subsequences:
            # - singleton: x
            # - from x-1: each existing sum s1, plus c1 copies of x
            # - from x+1: each existing sum s2, plus c2 copies of x
            new_sum = (
                x
                + (s1 + c1 * x) % MOD
                + (s2 + c2 * x) % MOD
            ) % MOD

            # Add to global total
            total = (total + new_sum) % MOD

            # Update our DP for future extensions
            dp_count[x] = (dp_count[x] + new_count) % MOD
            dp_sum[x]   = (dp_sum[x]   + new_sum)   % MOD

        return total

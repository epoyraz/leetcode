class Solution(object):
    def countOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # dp_prev[a] = # ways for arr1 up to i-1 ending with value a
        # initially at i=0: any a in [0..nums[0]] is allowed
        dp_prev = [1] * (nums[0] + 1)

        for i in range(1, n):
            M0 = nums[i-1]
            M1 = nums[i]
            # d = nums[i] - nums[i-1]
            # we need arr1[i] >= arr1[i-1] + d  AND arr1[i]>=arr1[i-1]
            # combined as arr1[i] >= arr1[i-1] + max(d,0)
            delta = max(nums[i] - nums[i-1], 0)

            # build prefix sums of dp_prev
            prefix = [0] * (M0 + 2)
            for a in range(M0 + 1):
                prefix[a+1] = (prefix[a] + dp_prev[a]) % MOD

            # now compute dp_cur[b] for b in [0..M1]
            dp_cur = [0] * (M1 + 1)
            for b in range(delta, M1 + 1):
                # we need a â¤ b - delta
                limit = min(M0, b - delta)
                if limit >= 0:
                    # sum dp_prev[0..limit] = prefix[limit+1]
                    dp_cur[b] = prefix[limit+1]
            dp_prev = dp_cur

        # answer = sum of dp_prev[b] over b in [0..nums[n-1]]
        return sum(dp_prev) % MOD

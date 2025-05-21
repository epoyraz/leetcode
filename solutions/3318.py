class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        # Only these three scores can appear on the very first removal from [0..n-1]
        candidates = {
            nums[0] + nums[1],      # remove first two
            nums[-2] + nums[-1],    # remove last two
            nums[0] + nums[-1],     # remove one from each end
        }

        best = 0
        for S in candidates:
            # dp2[i] = best #ops on subarray of length (L-2) starting at i
            dp2 = [0] * (n + 2)
            # dp1[i] = best #ops on subarray of length (L-1) starting at i
            dp1 = [0] * (n + 1)

            # Build for subarrayâlength L = 2..n
            for L in range(2, n + 1):
                size = n - L + 1
                dp0 = [0] * size
                for i in range(size):
                    j = i + L - 1
                    v = 0
                    # 1) first two
                    if nums[i] + nums[i+1] == S:
                        v = max(v, 1 + dp2[i+2])
                    # 2) last two
                    if nums[j-1] + nums[j] == S:
                        v = max(v, 1 + dp2[i])
                    # 3) one from each end
                    if nums[i] + nums[j] == S:
                        v = max(v, 1 + dp2[i+1])
                    dp0[i] = v

                # roll forward: next L+1 will use these
                dp2, dp1 = dp1, dp0

            # dp1[0] now holds the best #ops for the full array [0..n-1]
            best = max(best, dp1[0])

        return best

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp1 = length of longest non-decreasing subsequence seen so far ending with 1
        # dp2 = length of longest non-decreasing subsequence seen so far ending with 2
        # dp3 = length of longest non-decreasing subsequence seen so far ending with 3
        dp1 = dp2 = dp3 = 0

        for x in nums:
            if x == 1:
                # we can always append a 1 to a subsequence of 1s
                dp1 += 1
            elif x == 2:
                # to append a 2, we need a subsequence ending in 1 or 2
                dp2 = max(dp1, dp2) + 1
            else:  # x == 3
                # to append a 3, we need a subsequence ending in 1, 2, or 3
                dp3 = max(dp1, dp2, dp3) + 1

        # the longest non-decreasing subsequence has length max(dp1, dp2, dp3)
        longest = max(dp1, dp2, dp3)
        # we remove all other elements
        return len(nums) - longest

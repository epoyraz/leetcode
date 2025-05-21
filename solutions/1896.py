class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n, m = len(nums), len(multipliers)
        memo = {}

        def dp(i, left):
            if i == m:
                return 0
            if (i, left) in memo:
                return memo[(i, left)]

            right = n - 1 - (i - left)
            pick_left = multipliers[i] * nums[left] + dp(i + 1, left + 1)
            pick_right = multipliers[i] * nums[right] + dp(i + 1, left)
            memo[(i, left)] = max(pick_left, pick_right)
            return memo[(i, left)]

        return dp(0, 0)

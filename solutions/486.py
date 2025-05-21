class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dp(i, j):
            if i == j:
                return nums[i]
            pick_start = nums[i] - dp(i + 1, j)
            pick_end = nums[j] - dp(i, j - 1)
            return max(pick_start, pick_end)

        return dp(0, len(nums) - 1) >= 0

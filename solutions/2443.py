class Solution(object):
    def validPartition(self, nums):
        n = len(nums)
        dp = [True, False, nums[0] == nums[1], False]

        for i in range(2, n):
            two_equal = nums[i] == nums[i - 1]
            three_equal = nums[i] == nums[i - 1] == nums[i - 2]
            three_consec = nums[i] - 1 == nums[i - 1] and nums[i - 1] - 1 == nums[i - 2]

            valid = False
            if two_equal and dp[1]:
                valid = True
            if (three_equal or three_consec) and dp[0]:
                valid = True

            dp = [dp[1], dp[2], valid]

        return dp[2]

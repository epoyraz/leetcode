class Solution:
    def longestSquareStreak(self, nums):
        nums_set = set(nums)
        nums.sort()
        max_len = -1

        for num in nums:
            streak = 1
            val = num
            while val * val in nums_set:
                val *= val
                streak += 1
            if streak >= 2:
                max_len = max(max_len, streak)

        return max_len

import math

class Solution:
    def maxStrength(self, nums):
        positives = [x for x in nums if x > 0]
        negatives = sorted([x for x in nums if x < 0])
        zero_count = nums.count(0)

        result = 1
        used = False

        # Multiply all positive numbers
        for num in positives:
            result *= num
            used = True

        # Multiply pairs of negative numbers
        for i in range(0, len(negatives) - 1, 2):
            result *= negatives[i] * negatives[i + 1]
            used = True

        # Edge case: only one negative and no positives
        if not used:
            if zero_count > 0:
                return 0
            else:
                return max(nums)  # only one negative, no zero, return that

        return result

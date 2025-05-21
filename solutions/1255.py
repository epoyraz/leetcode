class Solution:
    def maxValueAfterReverse(self, nums):
        n = len(nums)
        # Base sum of adjacent differences
        base = sum(abs(nums[i] - nums[i+1]) for i in range(n-1))

        # 1) Best prefix reversal gain
        best_prefix = 0
        for i in range(n-1):
            gain = abs(nums[0] - nums[i+1]) - abs(nums[i] - nums[i+1])
            if gain > best_prefix:
                best_prefix = gain

        # 2) Best suffix reversal gain
        best_suffix = 0
        for i in range(1, n):
            gain = abs(nums[i-1] - nums[n-1]) - abs(nums[i-1] - nums[i])
            if gain > best_suffix:
                best_suffix = gain

        # 3) Best middle reversal gain
        # Track min of max(adjacent pair) and max of min(adjacent pair)
        min_of_max = float('inf')
        max_of_min = float('-inf')
        for i in range(n-1):
            a, b = nums[i], nums[i+1]
            mn, mx = min(a, b), max(a, b)
            if mx < min_of_max:
                min_of_max = mx
            if mn > max_of_min:
                max_of_min = mn
        best_middle = 2 * (max_of_min - min_of_max)

        best_gain = max(best_prefix, best_suffix, best_middle)
        return base + best_gain

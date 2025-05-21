class Solution:
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)

        def compute_sum(divisor):
            return sum((num + divisor - 1) // divisor for num in nums)

        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid

        return left

class Solution:
    def maximumOr(self, nums, k):
        n = len(nums)
        suffix_or = [0] * (n + 1)

        # Build suffix ORs
        for i in range(n - 1, -1, -1):
            suffix_or[i] = suffix_or[i + 1] | nums[i]

        prefix_or = 0
        max_or = 0

        for i in range(n):
            modified = nums[i] << k  # Multiply by 2^k
            total_or = prefix_or | modified | suffix_or[i + 1]
            max_or = max(max_or, total_or)
            prefix_or |= nums[i]

        return max_or

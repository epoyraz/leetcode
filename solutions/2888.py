class Solution:
    def minimumIndex(self, nums):
        from collections import Counter

        # Step 1: Find the global dominant element
        count = Counter(nums)
        n = len(nums)
        dominant = max(count, key=lambda x: count[x])
        total = count[dominant]

        # Step 2: Try all splits from left to right
        left_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left_count += 1
            left_len = i + 1
            right_len = n - left_len
            if (left_count * 2 > left_len) and ((total - left_count) * 2 > right_len):
                return i

        return -1

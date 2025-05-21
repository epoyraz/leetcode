class Solution:
    def alternatingSubarray(self, nums):
        n = len(nums)
        max_len = -1
        i = 0

        while i < n - 1:
            if nums[i + 1] - nums[i] == 1:
                length = 2
                j = i + 1
                expected = -1
                while j + 1 < n and nums[j + 1] - nums[j] == expected:
                    length += 1
                    j += 1
                    expected *= -1
                max_len = max(max_len, length)
                i = j  # skip to end of this valid window
            else:
                i += 1

        return max_len

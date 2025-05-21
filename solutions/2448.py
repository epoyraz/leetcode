class Solution(object):
    def countBadPairs(self, nums):
        from collections import defaultdict

        n = len(nums)
        good = 0
        freq = defaultdict(int)

        for i in range(n):
            key = nums[i] - i
            good += freq[key]
            freq[key] += 1

        total = n * (n - 1) // 2
        return total - good

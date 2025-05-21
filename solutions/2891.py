class Solution:
    def maximumBeauty(self, nums, k):
        from collections import defaultdict

        freq = defaultdict(int)
        for num in nums:
            freq[num - k] += 1
            freq[num + k + 1] -= 1

        max_beauty = curr = 0
        for key in sorted(freq):
            curr += freq[key]
            max_beauty = max(max_beauty, curr)

        return max_beauty

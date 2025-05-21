from collections import defaultdict

class Solution:
    def countGood(self, nums, k):
        n = len(nums)
        count = defaultdict(int)
        left = 0
        pairs = 0
        res = 0

        for right in range(n):
            # When adding nums[right], we add count[nums[right]] pairs
            pairs += count[nums[right]]
            count[nums[right]] += 1

            # Shrink left pointer while pair count >= k
            while pairs >= k:
                res += n - right  # all subarrays starting from `left` to `right` are good
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1

        return res

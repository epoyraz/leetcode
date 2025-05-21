from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums, goal):
        count = defaultdict(int)
        count[0] = 1  # prefix sum 0 appears once
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            res += count[prefix_sum - goal]
            count[prefix_sum] += 1

        return res

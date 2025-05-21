class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        total = prefix[-1]

        # Base case: count valid partitions with no changes
        count = 0
        for i in range(n-1):
            if prefix[i] * 2 == total:
                count += 1

        # Use maps to store prefix differences
        left = defaultdict(int)
        right = defaultdict(int)
        for i in range(n-1):
            diff = prefix[i] * 2 - total
            right[diff] += 1

        max_ways = count
        for i in range(n):
            delta = k - nums[i]
            # simulating changing nums[i] to k:
            # if we change nums[i] by delta, then total sum changes by delta
            new_ways = 0
            if i > 0:
                new_ways += left[delta]
            if i < n - 1:
                new_ways += right[-delta]
            max_ways = max(max_ways, new_ways)

            if i < n - 1:
                d = prefix[i] * 2 - total
                right[d] -= 1
                left[d] += 1

        return max_ways

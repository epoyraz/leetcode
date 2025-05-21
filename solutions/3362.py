class Solution(object):
    def medianOfUniquenessArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # total subarrays
        N = n * (n + 1) // 2
        # lowerâmedian index
        k = (N + 1) // 2

        # maximum possible distinct in any subarray
        max_distinct = len(set(nums))

        # helper to count subarrays with â¤ t distinct
        from collections import defaultdict
        def count_at_most(t):
            freq = defaultdict(int)
            left = 0
            distinct = 0
            total = 0
            for right, v in enumerate(nums):
                if freq[v] == 0:
                    distinct += 1
                freq[v] += 1
                while distinct > t:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                total += right - left + 1
            return total

        # binary search smallest t in [1..max_distinct] with F(t) >= k
        lo, hi = 1, max_distinct
        ans = max_distinct
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_at_most(mid) >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans

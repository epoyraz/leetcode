from bisect import bisect_left

class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        from itertools import combinations

        def get_all_sums(arr):
            sums = set([0])
            for num in arr:
                new_sums = set()
                for s in sums:
                    new_sums.add(s + num)
                sums.update(new_sums)
            return list(sums)

        n = len(nums)
        left = nums[:n // 2]
        right = nums[n // 2:]

        left_sums = get_all_sums(left)
        right_sums = sorted(get_all_sums(right))

        res = float('inf')
        for l in left_sums:
            target = goal - l
            idx = bisect_left(right_sums, target)

            if idx < len(right_sums):
                res = min(res, abs(l + right_sums[idx] - goal))
            if idx > 0:
                res = min(res, abs(l + right_sums[idx - 1] - goal))

        return res

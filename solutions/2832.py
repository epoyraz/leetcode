from collections import defaultdict

class Solution(object):
    def longestEqualSubarray(self, nums, k):
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)

        res = 0
        for pos in positions.values():
            left = 0
            for right in range(len(pos)):
                # elements to delete = total elements in range - equal elements
                while pos[right] - pos[left] - (right - left) > k:
                    left += 1
                res = max(res, right - left + 1)
        return res

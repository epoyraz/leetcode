class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        left, right = n, 0
        max_seen = float('-inf')
        for i in range(n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]
        min_seen = float('inf')
        for i in range(n-1, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]
        return right - left + 1 if right > left else 0

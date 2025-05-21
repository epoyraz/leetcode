class Solution:
    def canBeIncreasing(self, nums):
        def is_strictly_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i - 1] >= arr[i]:
                    return False
            return True

        for i in range(len(nums)):
            if is_strictly_increasing(nums[:i] + nums[i+1:]):
                return True
        return False

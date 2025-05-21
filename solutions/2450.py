class Solution(object):
    def minimumReplacement(self, nums):
        n = len(nums)
        ops = 0
        prev = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                parts = (nums[i] + prev - 1) // prev
                ops += parts - 1
                prev = nums[i] // parts

        return ops

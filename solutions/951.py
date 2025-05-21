class Solution:
    def partitionDisjoint(self, nums):
        n = len(nums)
        max_left = nums[0]
        curr_max = nums[0]
        partition_idx = 0

        for i in range(1, n):
            curr_max = max(curr_max, nums[i])
            if nums[i] < max_left:
                partition_idx = i
                max_left = curr_max

        return partition_idx + 1

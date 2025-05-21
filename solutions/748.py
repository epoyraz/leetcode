class Solution(object):
    def dominantIndex(self, nums):
        max_num = max(nums)
        index = nums.index(max_num)
        for num in nums:
            if num != max_num and max_num < 2 * num:
                return -1
        return index

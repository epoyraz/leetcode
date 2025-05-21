class Solution:
    def minSwaps(self, nums):
        total_ones = sum(nums)
        if total_ones <= 1:
            return 0
        
        n = len(nums)
        nums += nums  # extend array to handle circular nature
        max_ones_in_window = curr = sum(nums[:total_ones])
        for i in range(total_ones, len(nums)):
            curr += nums[i] - nums[i - total_ones]
            max_ones_in_window = max(max_ones_in_window, curr)

        return total_ones - max_ones_in_window

class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)
        
        # Standard Kadane's algorithm for max subarray sum
        max_sum = curr_max = nums[0]
        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

        # Kadaneâs algorithm for min subarray sum
        min_sum = curr_min = nums[0]
        for num in nums[1:]:
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        # If all numbers are negative, max_sum is the answer
        if max_sum < 0:
            return max_sum

        # Otherwise, maximum of standard max subarray or circular case
        return max(max_sum, total - min_sum)

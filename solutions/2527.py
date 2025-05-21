class Solution:
    def countSubarrays(self, nums, minK, maxK):
        last_invalid = -1
        last_min = -1
        last_max = -1
        ans = 0
        
        for i, x in enumerate(nums):
            # If x is outside [minK, maxK], this breaks any valid subarray
            if x < minK or x > maxK:
                last_invalid = i
            if x == minK:
                last_min = i
            if x == maxK:
                last_max = i
            # The number of valid subarrays ending at i is the count of starting
            # positions after last_invalid and at or before min(last_min,last_max)
            valid_start = min(last_min, last_max)
            if valid_start > last_invalid:
                ans += (valid_start - last_invalid)
        
        return ans

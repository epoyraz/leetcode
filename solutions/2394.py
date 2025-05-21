class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        left = 0
        curr_sum = 0
        ans = 0
        
        # Expand right endpoint r from 0 to n-1
        for r in range(n):
            curr_sum += nums[r]
            # Shrink left endpoint while score >= k
            while left <= r and curr_sum * (r - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
            # Now for this r, all subarrays [L..r] with L in [left..r]
            # have score < k, so there are (r-left+1) of them
            ans += (r - left + 1)
        
        return ans

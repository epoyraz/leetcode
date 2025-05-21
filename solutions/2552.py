class Solution(object):
    def maximumSubarraySum(self, nums, k):
        from collections import defaultdict
        
        freq = defaultdict(int)
        curr_sum = 0
        dup = 0
        ans = 0
        
        # Initialize first window
        for i in range(k):
            x = nums[i]
            curr_sum += x
            freq[x] += 1
            if freq[x] == 2:
                dup += 1
        
        if dup == 0:
            ans = curr_sum
        
        # Slide the window
        for i in range(k, len(nums)):
            # Remove outgoing
            out = nums[i-k]
            freq[out] -= 1
            if freq[out] == 1:
                dup -= 1
            curr_sum -= out
            
            # Add incoming
            inc = nums[i]
            curr_sum += inc
            freq[inc] += 1
            if freq[inc] == 2:
                dup += 1
            
            # If no duplicates, consider sum
            if dup == 0 and curr_sum > ans:
                ans = curr_sum
        
        return ans

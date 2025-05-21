class Solution:
    def longestSubarray(self, nums):
        # The maximum AND of any subarray is the maximum element.
        k = max(nums)
        max_len = 0
        curr = 0
        
        for x in nums:
            # Only elements that have all bits of k can form a subarray with AND == k
            if x & k == k:
                curr += 1
                max_len = max(max_len, curr)
            else:
                curr = 0
        
        return max_len

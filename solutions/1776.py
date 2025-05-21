class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x
        # If we need to remove all elements
        if target == 0:
            return len(nums)
        # If it's impossible
        if target < 0:
            return -1
        
        n = len(nums)
        left = 0
        curr = 0
        max_len = -1
        
        # Sliding window to find the longest subarray summing to target
        for right in range(n):
            curr += nums[right]
            # Shrink from left if we exceed target
            while curr > target and left <= right:
                curr -= nums[left]
                left += 1
            # Check match
            if curr == target:
                max_len = max(max_len, right - left + 1)
        
        # If we never found a suitable subarray
        if max_len == -1:
            return -1
        
        # We keep max_len elements in the middle, remove the rest
        return n - max_len

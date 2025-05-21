class Solution:
    def getAverages(self, nums, k):
        n = len(nums)
        w = 2 * k + 1
        res = [-1] * n
        
        # If window is larger than array, no valid averages
        if w > n:
            return res
        
        # Compute sum of the first window [0..w-1]
        window_sum = sum(nums[:w])
        # Center of that window is at index k
        res[k] = window_sum // w
        
        # Slide the window forward
        for i in range(k + 1, n - k):
            # Remove the element leaving the window, add the new entering one
            window_sum += nums[i + k] - nums[i - k - 1]
            res[i] = window_sum // w
        
        return res

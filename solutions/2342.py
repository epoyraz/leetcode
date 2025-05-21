class Solution:
    def minimumAverageDifference(self, nums):
        n = len(nums)
        total = sum(nums)
        prefix = 0
        best_diff = float('inf')
        best_i = 0
        
        for i, x in enumerate(nums):
            prefix += x
            left_avg = prefix // (i + 1)
            if i < n - 1:
                right_avg = (total - prefix) // (n - i - 1)
            else:
                right_avg = 0
            
            diff = abs(left_avg - right_avg)
            if diff < best_diff:
                best_diff = diff
                best_i = i
        
        return best_i

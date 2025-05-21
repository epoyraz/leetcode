class Solution:
    def sumOfBeauties(self, nums):
        n = len(nums)
        # prefix_max[i] = max of nums[0..i-1], for i from 0..n-1
        prefix_max = [0] * n
        curr_max = float('-inf')
        for i in range(n):
            prefix_max[i] = curr_max
            curr_max = max(curr_max, nums[i])
        
        # suffix_min[i] = min of nums[i+1..n-1], for i from 0..n-1
        suffix_min = [0] * n
        curr_min = float('inf')
        for i in range(n-1, -1, -1):
            suffix_min[i] = curr_min
            curr_min = min(curr_min, nums[i])
        
        beauty_sum = 0
        for i in range(1, n-1):
            val = nums[i]
            # beauty = 2?
            if val > prefix_max[i] and val < suffix_min[i]:
                beauty_sum += 2
            # beauty = 1?
            elif nums[i-1] < val < nums[i+1]:
                beauty_sum += 1
            # else +0
        return beauty_sum

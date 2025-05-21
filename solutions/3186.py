class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        INF = float('inf')
        
        # prefix_min[i]: minimum value in nums[0..i]
        prefix_min = [0] * n
        prefix_min[0] = nums[0]
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i-1], nums[i])
        
        # suffix_min[i]: minimum value in nums[i..n-1]
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
        
        ans = INF
        # consider each j as the mountain peak
        for j in range(1, n-1):
            left = prefix_min[j-1]
            right = suffix_min[j+1]
            if left < nums[j] and right < nums[j]:
                ans = min(ans, left + nums[j] + right)
        
        return ans if ans < INF else -1

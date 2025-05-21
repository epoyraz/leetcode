class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = float('inf')
        for j in range(1, n-1):
            # find smallest nums[i] for i<j with nums[i]<nums[j]
            best_i = float('inf')
            for i in range(j):
                if nums[i] < nums[j] and nums[i] < best_i:
                    best_i = nums[i]
            # find smallest nums[k] for k>j with nums[k]<nums[j]
            best_k = float('inf')
            for k in range(j+1, n):
                if nums[k] < nums[j] and nums[k] < best_k:
                    best_k = nums[k]
            if best_i < float('inf') and best_k < float('inf'):
                ans = min(ans, best_i + nums[j] + best_k)
        return ans if ans < float('inf') else -1

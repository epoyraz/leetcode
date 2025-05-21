class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # build prefix sums where pre[i] = sum of nums[0..i-1]
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        
        total = 0
        for i in range(n):
            # compute start index of this subarray
            start = max(0, i - nums[i])
            # subarray sum = pre[i+1] - pre[start]
            total += pre[i+1] - pre[start]
        
        return total

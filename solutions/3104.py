class Solution(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = 0
        
        # Case when we select 0 students
        if nums[0] > 0:
            res += 1
        
        # Try all splits between 1 to n-1
        for i in range(1, n):
            if nums[i-1] < i and nums[i] > i:
                res += 1
        
        # Case when we select all students
        if nums[-1] < n:
            res += 1
        
        return res

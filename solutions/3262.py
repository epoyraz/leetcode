class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = sum(nums)
        
        for i in range(len(nums) - 1, 1, -1):
            if total - nums[i] > nums[i]:
                return total
            total -= nums[i]
        
        return -1
